---
title: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML con Python.NET
linktitle: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/python-net/enable-css-custom-properties-while-saving-to-html/
description: Scopri come abilitare le proprietà personalizzate CSS quando si salvano file Excel in HTML utilizzando l API Aspose.Cells per Python via .NET.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel in HTML, per scenari in cui ci sono più occorrenze di un'immagine base64, l'uso delle proprietà CSS personalizzate consente di salvare i dati dell'immagine solo una volta. Questo migliora le prestazioni dell'HTML risultante. Utilizza l'attributo [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) e impostalo su **True** durante il salvataggio in HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML**

Il seguente esempio di codice dimostra l'uso dell'attributo [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/). Lo screenshot mostra l'effetto quando questa proprietà non è impostata su True. Scarica il [file Excel di esempio](50528260.xlsx) utilizzato in questo codice e l'[HTML di output](50528261.zip) generato come riferimento.

## **Codice di Esempio**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
