---
title: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX
type: docs
weight: 60
url: /it/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Possibili Scenari di Utilizzo**
I formati Excel supportano un numero diverso di righe e colonne. Ad esempio, XLS supporta 65536 righe e 256 colonne, mentre XLSX supporta 1048576 righe e 16384 colonne. Se si desidera sapere quante righe e colonne sono supportate dal formato dato, è possibile utilizzare le proprietà [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) e [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn).
## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**
Il codice di esempio seguente crea prima un workbook in formato XLS e poi in formato XLSX. Dopo la creazione, stampa i valori delle proprietà [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) e [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn). Si prega di consultare l'output della console del codice riportato di seguito per il riferimento.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Output della console

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
