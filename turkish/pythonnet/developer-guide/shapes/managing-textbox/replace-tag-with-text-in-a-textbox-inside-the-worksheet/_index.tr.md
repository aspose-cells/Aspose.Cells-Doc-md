---
title: Python.NET ile Çalışma Sayfasındaki bir Metin Kutusuna etiket yerine metin koyma
linktitle: Çalışsayıdaki bir metin kutusundaki etiketi bir metinle değiştirin.
type: docs
weight: 1100
url: /tr/python-net/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Aspose.Cells for Python via .NET kullanarak Excel çalışma sayfalarındaki metin kutularına etiketlerin yerine metin nasıl eklenir, öğrenin.
---

## **Olası Kullanım Senaryoları**
Text boxes can have tags which can be replaced with some text at run time to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Örnek Kod**
Aşağıdaki örnek kod TAG_1 ve TAG_2 etiketlerini 'ys' ve '1' olarak değiştirir. Aşağıdaki bağlantıdan bu kod için test amaçlı örnek dosya indirilebilir:

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
