---
title: Ändern Sie die Schriftart für bestimmte Unicode Zeichen beim Speichern als PDF mit Python.NET
linktitle: Ändern Sie die Schriftart für bestimmte Unicode Zeichen
type: docs
weight: 260
url: /de/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Erfahren Sie, wie Sie Schriftarten für spezifische Unicode Zeichen während der PDF Konvertierung mit Aspose.Cells für Python via .NET anpassen. Gewährleisten Sie eine präzise Textdarstellung durch Zeichen für Zeichen Schriftartenersetzung.
---

{{% alert color="primary" %}}

Einige Unicode-Zeichen sind mit benutzerdefinierten Schriftarten nicht darstellbar. Ein solches Zeichen ist das **Non-breaking Hyphen** (U+2011) mit Unicode-Nummer 8209. Dieses Zeichen kann mit **Times New Roman** nicht angezeigt werden, aber mit Schriftarten wie **Arial Unicode MS**.

Wenn solche Zeichen im Text erscheinen, der mit einer bestimmten Schriftart formatiert ist (z.B. Times New Roman), ändert Aspose.Cells standardmäßig die Schriftart des gesamten Wortes/Satzes in eine kompatible Schriftart (z.B. Arial Unicode MS). Für Nutzer, die nur die Schriftart des nicht darstellbaren Zeichens ändern möchten, bieten wir eine granulare Steuerung über die Eigenschaft **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **Beispielvergleich**

Die nachfolgenden Screenshots zeigen Ausgaben mit unterschiedlichen Einstellungen. Das erste PDF zeigt vollständige Text-Schriftartenersetzung, während das zweite nur die Schriftart des spezifischen Zeichens ändert.

|**Vollständige Textersetzung**|**Zeichen-Ebene-Ersetzung**|
| :- | :- |
|![Vollständige Schriftartenänderung](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Selektive Schriftartenänderung](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Implementierungsschritte**

Um eine Zeichenebene für Schriftartsubstitution zu aktivieren:

1. Erstelle ein [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)-Objekt
2. Greife auf Arbeitsblattzellen mit [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Eigenschaft zu
3. Setze Zellwerte, die spezielle Unicode-Zeichen enthalten
4. Konfiguriere [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) mit:
   - `is_font_substitution_char_granularity = True`
5. Speichere Arbeitsmappe im PDF-Format

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **Schlüsseleinstellungen**

Verwende diese essenziellen API-Komponenten:

- [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)-Klasse für PDF-Druckeinstellungen
- **is_font_substitution_char_granularity**-Eigenschaft für Zeichenebene-Schriftartsubstitution
- [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/)-Methode für die Ausgabenerstellung

{{% alert color="note" %}} 
**API-Unterschiedsnotiz**: In Python.NET verwenden boolesche Eigenschaften snake_case-Namensgebung (`is_font_substitution_char_granularity`) anstelle des in .NET verwendeten PascalCase.
{{% /alert %}}
