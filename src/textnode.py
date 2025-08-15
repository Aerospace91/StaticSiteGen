from enum import Enum
from typing import Optional

class TextType(Enum):
    """
    An enumeration that represents the type of text formatting.

    Attributes:
        TEXT: Plain text.
        BOLD: Bold formatting.
        ITALIC: Italic formatting.
        CODE: Code formatting.
        LINK: Hyperlink.
        IMAGE: Image reference.
    """
    
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    """
    Represents a node of text with formatting and optional URL.

    Attributes:
        text (str): The actual text content.
        text_type (TextType): Formatting type of the text.
        url (Optional[str]): URL associated with the text (for links/images).
    """
    
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        """
        Initializes a TextNode object.

        Args:
            text (str): The actual text content.
            text_type (TextType): Formatting type of the text.
            url (Optional[str], optional): URL for LINK or IMAGE types.
        """
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other: object) -> bool:
        """
        Checks equality of two TextNode objects.

        Args:
            other (object): Another TextNode to compare.

        Returns:
            bool: True if objects are equivalent, False otherwise.
        """
        if not isinstance(other, TextNode):
            return NotImplemented
        
        return (
        self.text == other.text and
        self.text_type == other.text_type and
        self.url == other.url
        )
    
    def __repr__(self):
        """
        Returns a string representation of the TextNode.

        Returns:
            str: The string representation.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"    