---
title: Dokumentarbeitsmappen und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren
type: docs
weight: 50
url: /de/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Mögliche Verwendungsszenarien**

Wenn eine Microsoft Excel-Datei mithilfe von Microsoft Excel oder Aspose.Cells in HTML exportiert wird, werden auch verschiedene Arten von Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften exportiert, wie im folgenden Screenshot gezeigt. Sie können verhindern, dass diese Eigenschaften exportiert werden, indem Sie die [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) und [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften in der exportierten HTML aussehen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML und exportiert die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften nicht in der [Ausgabe-HTML](61767779.zip).

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
