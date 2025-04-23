---
title: Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet
type: docs
weight: 100
url: /it/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di salvare il workbook nel formato *Strict Open XML Spreadsheet*. A tale scopo, fornisce la proprietà [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance). Se imposti il suo valore come [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT), il file Excel di output verrà salvato nel formato *Strict Open XML Spreadsheet*.

## **Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet**

Il seguente codice di esempio crea un workbook e imposta il valore della proprietà [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance) come [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT) e lo salva come [file Excel di output](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Se apri il file Excel di output in Microsoft Excel e apri la finestra di dialogo *Salva come...*, vedrai che il suo formato è *Strict Open XML Spreadsheet* come mostrato in questa schermata.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
{{< app/cells/assistant language="java" >}}
