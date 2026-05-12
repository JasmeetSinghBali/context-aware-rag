import re


class Chunker:
    """
    Simple chunking strategy:
    - splits by paragraphs
    - removes empty lines
    """

    def chunk_text(self, text: str) -> list[str]:
        chunks = re.split(r"\n\s*\n", text)
        return [c.strip() for c in chunks if c.strip()]