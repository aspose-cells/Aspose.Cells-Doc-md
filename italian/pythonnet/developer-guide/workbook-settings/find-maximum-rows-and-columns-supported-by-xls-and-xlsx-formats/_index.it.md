---
title: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX
type: docs
weight: 20
url: /it/python-net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Possibili Scenari di Utilizzo**

Esistono un numero diverso di righe e colonne supportate dai formati di Excel. Per esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se desideri sapere quante righe e colonne sono supportate dal formato dato, puoi utilizzare le proprietà [**WorkbookSettings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) e [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column).

## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**

Il codice di esempio seguente crea prima un foglio di lavoro in formato XLS e poi in formato XLSX. Dopo la creazione, stampa i valori delle proprietà [**Workbook.settings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) e [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column). Consultare l'output della console del codice sottostante per il riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.py" >}}

## **Output della console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
