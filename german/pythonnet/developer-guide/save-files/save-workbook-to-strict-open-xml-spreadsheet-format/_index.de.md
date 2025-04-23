---
title: Arbeitsmappe im strengen Open XML Tabellenformat speichern
type: docs
weight: 150
url: /de/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells für Python via .NET ermöglicht das Speichern des Arbeitsbuchs im Format *Strict Open XML Spreadsheet*. Zu diesem Zweck bietet es die Eigenschaft [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Wenn Sie den Wert auf [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) setzen, wird die Ausgabedatei im Strict Open XML Spreadsheet-Format gespeichert.

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**

Der folgende Beispielcode erstellt eine Arbeitsmappe und setzt den Wert der [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) Eigenschaft auf [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) und speichert sie als [Ausgabe-Excel-Datei](67338272.xlsx). Wenn Sie die Ausgabe-Excel-Datei in Microsoft Excel öffnen und das Dialogfeld Speichern unter... öffnen, wird ihr Format als *Striktes Open-XML-Spreadsheet* angezeigt, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

