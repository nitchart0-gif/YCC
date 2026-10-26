import os
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
import script_length  # noqa: E402


class ScriptLengthTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.input_path = self.root / "brief.yaml"
        self.out_dir = self.root / "out"

    def tearDown(self):
        self.temp.cleanup()

    def write_input(self, content):
        self.input_path.write_text(content, encoding="utf-8")

    def test_reads_nested_video_fields(self):
        self.write_input(
            "video:\n  target_minutes: 5\n  words_per_minute: 150\n"
        )
        result = script_length.run(str(self.input_path), str(self.out_dir))
        report = Path(result).read_text(encoding="utf-8")
        self.assertIn("- estimated_word_budget: 750", report)

    def test_supports_legacy_flat_fields(self):
        self.write_input("minutes: 4\nwords_per_minute: 125\n")
        result = script_length.run(str(self.input_path), str(self.out_dir))
        report = Path(result).read_text(encoding="utf-8")
        self.assertIn("- estimated_word_budget: 500", report)

    def test_rejects_unfilled_template_placeholder(self):
        self.write_input(
            "video:\n  target_minutes: <number>\n  words_per_minute: 150\n"
        )
        with self.assertRaisesRegex(ValueError, "template placeholder"):
            script_length.run(str(self.input_path), str(self.out_dir))

    def test_requires_words_per_minute(self):
        self.write_input("video:\n  target_minutes: 5\n")
        with self.assertRaisesRegex(ValueError, "missing words per minute"):
            script_length.run(str(self.input_path), str(self.out_dir))

    def test_rejects_non_positive_values(self):
        self.write_input("video:\n  target_minutes: 0\n  words_per_minute: 150\n")
        with self.assertRaisesRegex(ValueError, "greater than zero"):
            script_length.run(str(self.input_path), str(self.out_dir))

    def test_does_not_overwrite_without_explicit_flag(self):
        self.write_input("video:\n  target_minutes: 2\n  words_per_minute: 100\n")
        self.out_dir.mkdir()
        output = self.out_dir / "calculation.md"
        output.write_text("keep me", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            script_length.run(str(self.input_path), str(self.out_dir))
        self.assertEqual(output.read_text(encoding="utf-8"), "keep me")

    def test_overwrites_only_when_explicitly_requested(self):
        self.write_input("video:\n  target_minutes: 2\n  words_per_minute: 100\n")
        self.out_dir.mkdir()
        output = self.out_dir / "calculation.md"
        output.write_text("old report", encoding="utf-8")
        script_length.run(str(self.input_path), str(self.out_dir), overwrite=True)
        self.assertIn("estimated_word_budget: 200", output.read_text(encoding="utf-8"))

    def test_non_finite_values_are_rejected(self):
        self.write_input("video:\n  target_minutes: nan\n  words_per_minute: 150\n")
        with self.assertRaisesRegex(ValueError, "finite number"):
            script_length.run(str(self.input_path), str(self.out_dir))


if __name__ == "__main__":
    unittest.main()
