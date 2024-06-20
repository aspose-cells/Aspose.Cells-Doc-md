---
title: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX
type: docs
weight: 20
url: /it/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Possibili Scenari di Utilizzo**

Esistono un numero diverso di righe e colonne supportate dai formati di Excel. Per esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se desideri sapere quante righe e colonne sono supportate dal formato dato, puoi utilizzare le proprietà [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) e [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn).

## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**

Il codice di esempio seguente crea prima un foglio di lavoro in formato XLS e poi in formato XLSX. Dopo la creazione, stampa i valori delle proprietà [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) e [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn). Consultare l'output della console del codice sottostante per il riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Output della console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
