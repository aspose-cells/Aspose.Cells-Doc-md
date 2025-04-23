---
title: Deaktivieren Sie CSS beim Speichern in HTML mit Python.NET
linktitle: Deaktivieren Sie CSS beim Speichern in HTML
type: docs
weight: 320
url: /de/python-net/disable-css-while-saving-to-html/
description: Erfahren Sie, wie Sie CSS Stile beim Speichern von Excel Dateien im HTML Format mit der Aspose.Cells for Python via .NET API deaktivieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als einzelnes HTML-Dokument speichern, werden die CSS-Elemente normalerweise in den HEAD-Bereich des HTML-Dokuments eingebettet. Wenn Sie diese Datei als Inhalt/Body einer E-Mail anhängen, entfernt die Mehrheit der E-Mail-Clients die CSS-Elemente, was zu fehlerhafter Darstellung führt. Die Aspose.Cells for Python via .NET API führt eine Option ein, die es ermöglicht, CSS optional zu deaktivieren und Stile direkt innerhalb der HTML-Elemente anzuwenden. Wenn Sie den HTML-Inhalt/Body der E-Mail festlegen möchten, verwenden Sie die [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/)-Eigenschaft und setzen Sie sie auf **True**.

## **CSS beim Speichern in HTML deaktivieren**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **Beispielcode**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
