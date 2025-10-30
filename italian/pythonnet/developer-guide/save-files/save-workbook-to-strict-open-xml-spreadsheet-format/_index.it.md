---
title: Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet
type: docs
weight: 150
url: /it/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET consente di salvare il workbook nel formato *Strict Open XML Spreadsheet*. A tal fine, fornisce la proprietà [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Se imposti il suo valore come [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance), allora il file Excel di output sarà salvato nel formato Strict Open XML Spreadsheet.

## **Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet**

Il seguente codice di esempio crea un workbook e imposta il valore della proprietà [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) come [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) e lo salva come [file Excel di output](67338272.xlsx). Se apri il file Excel di output in Microsoft Excel e apri la finestra di dialogo Salva come..., vedrai il suo formato come *Strict Open XML Spreadsheet* come mostrato in questa schermata.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}
