---
title: Come stampare Excel come pagine adattate in larghezza e altezza con Python.NET
linktitle: Come stampare Excel in pagine larghe e alte adattate
type: docs
weight: 200
url: /it/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Impara a impostare le proprietà fit_to_pages_wide e fit_to_pages_tall per la stampa di Excel usando le API Aspose.Cells per Python via .NET.
keywords: Stampa Python Excel, impostazioni Fit to Page in Python, FitToPagesWide in Python, FitToPagesTall in Python, stampa di un foglio come una pagina, stampa di tutte le colonne in una pagina in Python.
---

## **Introduzione**

Le impostazioni fit_to_pages_wide e fit_to_pages_tall controllano la scala del foglio di calcolo durante la stampa. Queste impostazioni assicurano che il risultato stampato si adatti alle dimensioni di pagina specificate:

1. **fit_to_pages_wide**: Specifica il numero di pagine orizzontali per la stampa
1. **fit_to_pages_tall**: Specifica il numero di pagine verticali per la stampa

## **Perché usare FitToPagesWide e FitToPagesTall**
I principali vantaggi includono:
1. Controllo preciso del layout di stampa
1. Formattazione coerente di più fogli
1. Presentazione professionale del documento

## **Come stampare il file come pagine adattate in larghezza e altezza in Excel**
Per configurare in Microsoft Excel:
1. Apri il libro di lavoro e seleziona il foglio di lavoro
1. Naviga a **Layout di pagina** → **Imposta pagina** di dialogo
1. Nella scheda **Pagina** sotto **Scala:**
   - Seleziona "Adatta a"
   - Specifica le pagine di larghezza (orizzontale) e altezza (verticale)

<br>
<img src="2.png" width=60% />

## **Come stampare Excel come pagine adattate in larghezza e altezza usando Aspose.Cells**
Per configurare programmaticamente:
1. Carica il [file di esempio](input.xlsx)
1. Accedi all'oggetto [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) del foglio di lavoro
1. Imposta le proprietà [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) e [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

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

Risultato in output:
<br>
<img src="1.png" width=60% />

## **Come stampare il foglio di lavoro come una sola pagina**
Per forzare l'output su una sola pagina:
1. Usa [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Imposta la proprietà [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

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

Risultato in output:
<br>
<img src="3.png" width=60% />

## **Come stampare tutte le colonne in una sola pagina**
Per consolidare le colonne orizzontalmente:
1. Configura [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Abilita la proprietà [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

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

Risultato in output:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
