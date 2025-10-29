---
title: Remplacer une balise par du texte dans une zone de texte à l’intérieur de la feuille avec Python.NET
linktitle: Remplacer une balise par un texte dans une zone de texte à l intérieur de la feuille de calcul
type: docs
weight: 1100
url: /fr/python-net/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Apprenez comment remplacer des balises par du texte dans les zones de texte des feuilles Excel à l’aide d’Aspose.Cells pour Python via .NET.
---

## **Scénarios d'utilisation possibles**
Text boxes can have tags which can be replaced with some text at run time to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Code d'exemple**
Le code d'exemple suivant remplace les balises TAG_1 et TAG_2 par un texte quelconque, disons 'ys' et '1'. Le fichier d'exemple pour tester le code ci-dessous peut être téléchargé depuis le lien suivant :

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleReplaceTagWithText.xlsx"))
tag = "TAG_2$TAG_1"
replace = "1$ys"

tags = tag.split('$')
replaces = replace.split('$')

for t, r in zip(tags, replaces):
    wb.replace(f"<{t}>", r)

opts = PdfSaveOptions()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb.save(os.path.join(output_dir, "outputReplaceTagWithText.pdf"), opts)
```

```python
from aspose.cells import Workbook
from aspose.cells.drawing import TextBox

def sheet_replace(workbook, s_find, s_replace):
    finding = s_find

    # Replace in cells and headers/footers
    for sheet in workbook.worksheets:
        sheet.replace(finding, s_replace)
        for j in range(3):
            header = sheet.page_setup.get_header(j)
            if header is not None:
                sheet.page_setup.set_header(j, header.replace(finding, s_replace))

            footer = sheet.page_setup.get_footer(j)
            if footer is not None:
                sheet.page_setup.set_footer(j, footer.replace(finding, s_replace))

    # Replace in textboxes with HTML entities
    for sheet in workbook.worksheets:
        s_find = s_find.replace("<", "&lt;")
        s_find = s_find.replace(">", "&gt;")
        for mytextbox in sheet.text_boxes:
            if mytextbox.html_text is not None and s_find in mytextbox.html_text:
                mytextbox.html_text = mytextbox.html_text.replace(s_find, s_replace)
```
{{< app/cells/assistant language="python-net" >}}
