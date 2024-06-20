---
title: Quell Excel Datei ohne Diagramme laden
type: docs
weight: 750
url: /de/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells ermöglicht es Ihnen, Ihre Excel-Datei ohne Diagramme zu laden. Bitte verwenden Sie die Eigenschaft LoadOptions.LoadFilter zu diesem Zweck.

{{% /alert %}} 
## **Quell-Excel-Datei ohne Diagramme laden**
Der folgende Beispielcode lädt die Beispieldatei ohne Diagramme und speichert sie im Ausgabe-PDF-Format.





{{< highlight java >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






