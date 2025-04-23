---
title: Disabilitare CSS durante il salvataggio in HTML con Python.NET
linktitle: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/python-net/disable-css-while-saving-to-html/
description: Scopri come disattivare gli stili CSS durante il salvataggio di file Excel in formato HTML utilizzando l API Aspose.Cells per Python via .NET.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel come una pagina HTML singola, di solito gli elementi CSS saranno incorporati nel file HTML e situati nella sezione HEAD. Se alleghi questo file come contenuto/corpo di un'email, gli elementi CSS saranno rimossi dalla maggior parte dei client email, risultando in una visualizzazione non corretta. L'API Aspose.Cells per Python via .NET introduce un'opzione che permette di disabilitare opzionalmente il CSS, consentendo agli stili di essere applicati direttamente agli elementi HTML stessi. Se desideri impostare l'HTML come contenuto/corpo dell'email, utilizza la proprietà [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) e impostala su **True**.

## **Disabilita CSS durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **Codice di Esempio**

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
