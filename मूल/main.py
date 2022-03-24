# Code of this file belongs to Indrak.Bol

import visitor as visitor
import indrak as indrak

indrak_source = visitor.FileReader("../परीक्षण/लघुअंश.लघु")

engine = indrak.IndrakParser(indrak_source)
engine.action()