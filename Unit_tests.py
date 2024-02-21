import unittest
from unittest.mock import patch
from TextTest import convert_audio_to_text, convert_text_to_speech

class TestAudioProcessing(unittest.TestCase):
    @patch('TextTest.sr')
    def test_convert_audio_to_text(self, mock_sr):
        mock_recognizer = mock_sr.Recognizer.return_value
        mock_audio_file = mock_sr.AudioFile.return_value
        mock_audio_data = mock_recognizer.record.return_value
        mock_recognizer.recognize_google.return_value = "this is a test audio file."

        audio_file_path = "audio/Unit_test.wav"
        expected_text = "this is a test audio file."
        actual_text = convert_audio_to_text(audio_file_path)
        self.assertEqual(actual_text.strip().lower(), expected_text.strip().lower())

    @patch('TextTest.gTTS')
    def test_convert_text_to_speech(self, mock_gtts):
        mock_tts_instance = mock_gtts.return_value

        text = "This is a test."
        output_audio_path = "audio/output_audio_test.mp3"
        convert_text_to_speech(text, output_audio_path)
        mock_tts_instance.save.assert_called_once_with(output_audio_path)

if __name__ == "__main__":
    unittest.main()
