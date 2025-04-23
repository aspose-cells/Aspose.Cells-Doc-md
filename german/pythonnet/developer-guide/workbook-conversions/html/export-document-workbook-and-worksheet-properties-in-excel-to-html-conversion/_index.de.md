---
title: Dokumentarbeitsmappen und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren
type: docs
weight: 50
url: /de/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Mögliche Verwendungsszenarien**

Wenn eine Microsoft Excel-Datei mithilfe von Microsoft Excel oder Aspose.Cells in HTML exportiert wird, werden auch verschiedene Arten von Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften exportiert, wie im folgenden Screenshot gezeigt. Sie können verhindern, dass diese Eigenschaften exportiert werden, indem Sie die [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties), [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) und [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften in der exportierten HTML aussehen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML und exportiert die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften nicht in der [Ausgabe-HTML](61767779.zip).

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
