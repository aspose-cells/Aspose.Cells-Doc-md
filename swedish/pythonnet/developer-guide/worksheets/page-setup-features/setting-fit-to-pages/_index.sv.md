---
title: Hur man skriver ut Excel som anpassade sidor breda och höga med Python.NET
linktitle: Hur man skriver ut Excel som anpassade sidor breda och höga
type: docs
weight: 200
url: /sv/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Lär dig att ställa in fit_to_pages_wide och fit_to_pages_tall egenskaper för utskrift av Excel med Aspose.Cells för Python via .NET API.
keywords: Python Excel utskrift, Python Fit to Page inställningar, Python FitToPagesWide, Python FitToPagesTall, Python Skriva ut kalkylblad som en sida, Python skriva ut alla kolumner på en sida
---

## **Introduktion**

fit_to_pages_wide och fit_to_pages_tall-inställningarna styr skärmlayouten under utskrift. Dessa inställningar säkerställer att den utskrivna outputen passar inom angivna sidmått:

1. **fit_to_pages_wide**: Anger sidantal horisontellt för utskrift
1. **fit_to_pages_tall**: Anger sidantal vertikalt för utskrift

## **Varför använda FitToPagesWide och FitToPagesTall**
Nyckelfördelarna inkluderar:
1. Precist utskriftslayouterstyrning
1. Konsistent flera-blad formatering
1. Professionell dokumentpresentation

## **Hur man skriver ut filen som anpassade sidor breda och höga i Excel**
För att konfigurera i Microsoft Excel:
1. Öppna arbetsboken och välj kalkylblad
1. Navigera till **Sidlayout** → **Sidinställningar** dialogrutan
1. Under **Sida**-fliken, under **Skalning**:
   - Välj "Anpassa till"
   - Specificera sidor brett (horisontellt) och högt (vertikalt)

<br>
<img src="2.png" width=60% />

## **Hur man skriver ut Excel som anpassade sidor brett och högt med Aspose.Cells**
För att konfigurera programmatiskt:
1. Ladda [exempelfil](input.xlsx)
1. Åtkomst till kalkylbladets [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)-objekt
1. Sätt egenskaperna [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) och [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Resultat av utmatning:
<br>
<img src="1.png" width=60% />

## **Hur man skriver ut kalkylblad som en sida**
För att tvinga utskrift på en sida:
1. Använd [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Sätt egenskapen [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Resultat av utmatning:
<br>
<img src="3.png" width=60% />

## **Hur man skriver ut alla kolumner på en sida**
För att konsolidera kolumner horisontellt:
1. Konfigurera [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Aktivera egenskapen [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Resultat av utmatning:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
