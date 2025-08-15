from enum import Enum
from typing import Optional
from htmlnode import LeafNode

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
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")