---
title: Salva il workbook in formato Strict Open XML Spreadsheet con Golang tramite C++
linktitle: Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet
type: docs
weight: 150
url: /it/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Impara come salvare un workbook in formato Strict Open XML Spreadsheet usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells consente di salvare il workbook in formato *Strict Open XML Spreadsheet*. Per questo fornisce la proprietà [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/). Se imposti il suo valore a [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), il file Excel di output sarà salvato in formato Strict Open XML Spreadsheet.

## **Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet**

Il seguente esempio di codice crea un workbook, imposta il valore della proprietà [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) su [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) e lo salva come [file Excel di output](67338272.xlsx). Se apri il file Excel di output in Microsoft Excel e apri la finestra di dialogo Salva con nome..., vedrai il suo formato come *Strict Open XML Spreadsheet* come mostrato in questa schermata.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
