def generate_notes(transcribed_text):
    """
    Generates notes from transcribed text.

    Parameters:
    - transcribed_text: list, the list of text lines to generate notes from.

    Returns:
    - list: a list of notes extracted from the text.
    """
    notes = []
    for line in transcribed_text:
        # Split each line into sentences
        notes.extend(line.split('.'))  # Split by sentences
    return [note.strip() for note in notes if note]  # Clean up notes
