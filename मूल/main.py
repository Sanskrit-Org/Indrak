# Sanskrit-Org  [Github]
# This file is part of Sanskrit-Org > Indrak Project
# See License for more details.

import visitor as visitor
import indrak as indrak

indrak_source = visitor.FileReader("../परीक्षण/लघुअंश.लघु")

engine = indrak.IndrakParser(indrak_source, False)  # Debug Mode
engine.action()
