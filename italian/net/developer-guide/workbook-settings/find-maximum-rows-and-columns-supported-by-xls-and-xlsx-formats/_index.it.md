---
title: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX
type: docs
weight: 20
url: /it/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Possibili scenari di utilizzo**

Esistono diversi numeri di righe e colonne supportati dai formati Excel. Ad esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se vuoi sapere quante righe e colonne sono supportate da un determinato formato, puoi utilizzare[**Cartella di lavoro.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) e[**Cartella di lavoro.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)proprietà.

## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**

Il codice di esempio seguente crea la cartella di lavoro prima in XLS e quindi in formato XLSX. Dopo la creazione, stampa i valori di[**Cartella di lavoro.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) e[**Cartella di lavoro.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)proprietà. Si prega di consultare l'output della console del codice fornito di seguito per riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
