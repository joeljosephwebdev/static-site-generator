from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag : str, value : str, props : dict = None):
    super().__init__(tag, value, None, props)
    self._value = value

  @property 
  def value(self):
    return self._value
  
  @value.setter #validation for value
  def value(self, contents: str):
    if not contents:
        raise ValueError("leaf node must have a value")
    self._value = contents.lower()
  
  def to_html(self):
    if not self.tag:
      return self.value
    
    props = self.props_to_html()
    return f"<{self.tag}{props}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
  def __eq__(self, other):
    return (self.tag == other.tag 
            and self.value == other.value 
            and self.props == other.props)