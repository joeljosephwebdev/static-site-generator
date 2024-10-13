class HTMLNode:
  def __init__(self, 
               tag : str = None, 
               value : str = None, 
               children : list = None, 
               props : dict = None
              ):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if not self.props: return ""
    
    formatted_props = [f'{key}="{value}"' for key, value in self.props.items()]
    return " ".join(formatted_props)


  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"