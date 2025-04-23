---
title: So drucken Sie Excel als angepasste Seiten breit und hoch mit Python.NET
linktitle: Wie drucke ich Excel auf zugeschnittenen Seiten breit und hoch
type: docs
weight: 200
url: /de/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Lernen Sie, die Eigenschaften fit_to_pages_wide und fit_to_pages_tall für den Excel Druck mit Aspose.Cells für Python via .NET API zu setzen.
keywords: Python Excel Druck, Python, Anpassen der Seitengröße, Python FitToPagesWide, Python FitToPagesTall, Python Arbeitsblatt als Eine Seite drucken, Python Alle Spalten auf einer Seite drucken
---

## **Einführung**

Die Einstellungen fit_to_pages_wide und fit_to_pages_tall steuern die Skalierung des Tabellenblatts beim Drucken. Diese Einstellungen stellen sicher, dass der gedruckte Ausgang innerhalb der angegebenen Seitengröße passt.

1. **fit_to_pages_wide**: Gibt die horizontale Seitenanzahl für den Druck an
1. **fit_to_pages_tall**: Gibt die vertikale Seitenanzahl für den Druck an

## **Warum FitToPagesWide und FitToPagesTall verwenden**
Wichtige Vorteile sind:
1. Präzise Drucklayoutsteuerung
1. Konsistente Mehrblattformatierung
1. Professionelle Dokumentenpräsentation

## **So drucken Sie eine Datei als angepasste Seiten breit und hoch in Excel**
Zur Konfiguration in Microsoft Excel:
1. Arbeitsmappe öffnen und Arbeitsblatt auswählen
1. Navigieren Sie zu **Seitenlayout** → **Seite einrichten** Dialog
1. Im **Seite**-Tab unter **Skalierung:**
   - Wählen Sie "Anpassen"
   - Seiten breit (horizontal) und hoch (vertikal) festlegen

<br>
<img src="2.png" width=60% />

## **So drucken Sie Excel als angepasste Seiten breit und hoch mit Aspose.Cells**
Zur Programmatischen Konfiguration:
1. Laden Sie [Beispiel Datei](input.xlsx)
1. Zugriff auf das [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)-Objekt des Arbeitsblatts
1. Setzen Sie die Eigenschaften [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) und [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

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

Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **So drucken Sie ein Arbeitsblatt als Eine Seite**
Um eine Einseiten-Ausgabe zu erzwingen:
1. Verwenden Sie [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Setzen Sie die [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)-Eigenschaft

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

Ausgabenergebnis:
<br>
<img src="3.png" width=60% />

## **Wie man alle Spalten auf einer Seite druckt**
Zur horizontalen Konsolidierung von Spalten:
1. Konfigurieren Sie [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Aktivieren Sie die [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)-Eigenschaft

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

Ausgabenergebnis:
<br>
<img src="4.png" width=60% />
