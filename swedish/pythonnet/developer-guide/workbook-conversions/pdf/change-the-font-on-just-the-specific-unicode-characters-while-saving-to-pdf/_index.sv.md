---
title: Ändra teckensnitt för specifika Unicode tecken vid sparande till PDF med Python.NET
linktitle: Ändra teckensnitt för specifika Unicode tecken
type: docs
weight: 260
url: /sv/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lär dig hur du ändrar teckensnitt för specifika Unicode tecken under PDF konvertering med Aspose.Cells för Python via .NET. Säkerställ exakt textrendering med tecken för tecken teckensnittssubstitution.
---

{{% alert color="primary" %}}

Vissa Unicode-tecken är inte visningsbara med användarspecificerade teckensnitt. Ett sådant Unicode-tecken är **Non-breaking Hyphen** (U+2011) med Unicode-nummer 8209. Detta tecken kan inte visas med **Times New Roman** men kan visas med teckensnitt som **Arial Unicode MS**.

När sådana tecken visas i text formaterad med ett specifikt teckensnitt (t.ex. Times New Roman), ändrar Aspose.Cells teckensnitt för hela ordet/satsen till ett kompatibelt teckensnitt (t.ex. Arial Unicode MS) som standard. För användare som bara vill ändra teckensnittet för det ohärbara tecknet, ger vi granulär kontroll via egenskapen **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **Exempeljämförelse**

Nedanstående skärmbilder visar resultat med olika inställningar. Den första PDF visar fullständig teckensnittssubstitution, medan den andra PDF ändrar endast tecknet.

|**Fullständig textsubstitution**|**Teckennivåersättning**|
| :- | :- |
|![Fullt teckensnittbyte](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Selektivt teckensnittsbyte](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Implementationssteg**

För att aktivera tecken för tecken-teckensnittssubstitution:

1. Skapa ett [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)-objekt
2. Använd [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-egenskapen för att komma åt kalkylbladsceller
3. Sätt cellvärden som innehåller särskilda Unicode-tecken
4. Konfigurera [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) med:
   - `is_font_substitution_char_granularity = True`
5. Spara arbetsboken i PDF-format

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

## **Viktig konfiguration**

Använd dessa nödvändiga API-komponenter:

- [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)-klass för PDF-renderingsinställningar
- Egenskapen **is_font_substitution_char_granularity** för tecken för tecken-teckensnittssubstitution
- [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/)-metod för utgångsgenerering

{{% alert color="note" %}} 
**Skillnadsnotering för API**: I Python.NET använder booleska egenskaper snake_case (`is_font_substitution_char_granularity`) istället för PascalCase som används i .NET.
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
