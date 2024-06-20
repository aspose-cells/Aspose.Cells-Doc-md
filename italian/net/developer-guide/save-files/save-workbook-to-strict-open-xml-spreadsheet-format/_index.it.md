---
title: Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet
type: docs
weight: 150
url: /it/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells consente di salvare il workbook in formato *Strict Open XML Spreadsheet*. A tale scopo, fornisce la proprietà [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance). Se imposti il suo valore come [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance), il file Excel di output verrà salvato in formato Strict Open XML Spreadsheet.

## **Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet**

Il seguente codice di esempio crea un workbook e imposta il valore della proprietà [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) come [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance) e lo salva come [file Excel di output](67338272.xlsx). Se apri il file Excel di output in Microsoft Excel e apri la finestra di dialogo Salva come..., vedrai il suo formato come *Strict Open XML Spreadsheet* come mostrato in questa schermata.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
