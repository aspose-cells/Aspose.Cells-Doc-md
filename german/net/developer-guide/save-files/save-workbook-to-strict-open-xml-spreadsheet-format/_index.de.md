---
title: Arbeitsmappe im strengen Open XML Tabellenformat speichern
type: docs
weight: 150
url: /de/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Arbeitsmappe im Format *Striktes Open XML-Spreadsheet* zu speichern. Hierfür wird die [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) Eigenschaft bereitgestellt. Wenn Sie ihren Wert auf [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance) setzen, wird die Ausgabe-Excel-Datei im Format *Striktes Open XML-Spreadsheet* gespeichert.

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**

Der folgende Beispielcode erstellt eine Arbeitsmappe und setzt den Wert der [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) Eigenschaft auf [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance) und speichert sie als [Ausgabe-Excel-Datei](67338272.xlsx). Wenn Sie die Ausgabe-Excel-Datei in Microsoft Excel öffnen und das Dialogfeld Speichern unter... öffnen, wird ihr Format als *Striktes Open-XML-Spreadsheet* angezeigt, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
