---
title: Dokumentarbeitsmappen und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren
type: docs
weight: 50
url: /de/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Mögliche Verwendungsszenarien**

Beim Exportieren einer Microsoft Excel-Datei in HTML mithilfe von Microsoft Excel oder Aspose.Cells werden auch verschiedene Arten von Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften exportiert, wie im folgenden Screenshot gezeigt. Sie können vermeiden, diese Eigenschaften zu exportieren, indem Sie die [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) und [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften im exportierten HTML aussehen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren**

Der folgende Beispielcode lädt die [Beispiels-Excel-Datei](61767784.xlsx) und konvertiert sie in HTML, wobei die Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften nicht in der [ausgegebenen HTML](61767783.zip) exportiert werden.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
