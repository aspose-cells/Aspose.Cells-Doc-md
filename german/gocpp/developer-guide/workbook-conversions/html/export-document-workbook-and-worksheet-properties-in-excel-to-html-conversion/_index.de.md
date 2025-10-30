---
title: Exportieren Sie Eigenschaften des Arbeitsbuchs und der Arbeitsblätter in der Excel zu HTML Konvertierung mit Golang über C++
linktitle: Exportieren von Dokument , Arbeitsbuch und Arbeitsblatt Eigenschaften in Excel in HTML Konvertierung
type: docs
weight: 50
url: /de/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Erfahren Sie, wie Sie Dokument , Arbeitsbuch und Arbeitsblatt Eigenschaften beim Konvertieren von Excel Dateien in HTML mit Aspose.Cells for C++ exportieren oder vermeiden können.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Microsoft Excel-Datei mit Microsoft Excel oder Aspose.Cells in HTML exportiert wird, werden auch verschiedene Arten von Dokument-, Arbeitsbuch- und Arbeitsblatt-Eigenschaften exportiert, wie im folgenden Screenshot gezeigt wird. Sie können das Exportieren dieser Eigenschaften vermeiden, indem Sie [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) und [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften im exportierten HTML aussehen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportieren von Dokument-, Arbeitsbuch- und Arbeitsblatt-Eigenschaften in Excel in HTML-Konvertierung**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML, ohne die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften im [Ausgabe-HTML](61767779.zip) zu exportieren.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
