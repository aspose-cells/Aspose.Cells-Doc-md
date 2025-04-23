---
title: Personnalisation du XML de Ribbon avec Python via .NET
linktitle: Personnaliser le menu Excel
type: docs
weight: 1500
url: /fr/python-net/customizing-the-ribbon-xml/
description: Lire, écrire et gérer la personnalisation du XML du Ribbon Excel en utilisant Aspose.Cells pour Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office a remplacé les menus et barres d'outils par un ruban en haut de la fenêtre de l'application depuis Office 2007. Le ruban est personnalisable. 
Aspose.Cells vous permet de :

- Conserver le XML du Ribbon sans le parser
- Lire et écrire le XML du Ribbon sans le parser
- Obtenir et définir les données XML du Ribbon

Si vous souhaitez modifier le Ribbon XML, vous devez l'analyser avec un analyseur XML ou un autre outil Ribbon XML.

{{% /alert %}}

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

wb = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
xml_path = os.path.join(data_dir, "CustomUI.xml")

with open(xml_path, 'r') as sr:
    wb.ribbon_xml = sr.read()
```
