---
title: Arbeitsmappe im strengen Open XML Tabellenformat speichern
type: docs
weight: 100
url: /de/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Arbeitsmappe im *Strict Open XML Spreadsheet* Format zu speichern. Zu diesem Zweck bietet es die [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)-Eigenschaft. Wenn Sie ihren Wert als [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT) setzen, wird die Ausgabe-Excel-Datei im *Strict Open XML Spreadsheet*-Format gespeichert.

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**

Der folgende Beispielscode erstellt eine Arbeitsmappe und setzt den Wert der [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)-Eigenschaft als [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT) und speichert sie als [Ausgabe-Excel-Datei](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Wenn Sie die Ausgabe-Excel-Datei in Microsoft Excel öffnen und das *Speichern unter...* Dialogfeld öffnen, wird ihr Format als *Strict Open XML Spreadsheet*-Format angezeigt, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
{{< app/cells/assistant language="java" >}}
