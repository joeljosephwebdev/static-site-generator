from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag : str, children : list, props : dict = None):
    super().__init__(tag, None, children, props)
    self._children = children
    self._tag = tag

  @property 
  def tag(self):
    return self._tag
  
  @tag.setter #validation for tag
  def tag(self, value: list):
    if not value:
        raise ValueError("parent node must have a tag")
    self._tag = value

  @property 
  def children(self):
    return self._children
  
  @children.setter #validation for children
  def children(self, value: list):
    if not value:
        raise ValueError("parent node must have at least one child node")
    self._children = value

  
  def __repr__(self):
    return f"ParentNode({self.tag} {self.children} {self.props})"
  
  def to_html(self):
    html = ""
    if self.children:
      for child in self.children:
        html += child.to_html()
    
    return f"<{self.tag}>{html}</{self.tag}>"
  
  def __eq__(self, other):
    return (self.tag == other.tag 
            and self.children == other.children
            and self.props == other.props)