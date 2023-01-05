---
title: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX
type: docs
weight: 60
url: /it/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Possibili scenari di utilizzo**
Esistono diversi numeri di righe e colonne supportati dai formati Excel. Ad esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se vuoi sapere quante righe e colonne sono supportate da un determinato formato, puoi utilizzare[Cartella di lavoro.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)e[Cartella di lavoro.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)proprietà.
## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**
Il codice di esempio seguente crea la cartella di lavoro prima nel formato XLS e quindi nel formato XLSX. Dopo la creazione, stampa i valori di[Cartella di lavoro.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)e[Cartella di lavoro.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)proprietà. Si prega di consultare l'output della console del codice fornito di seguito per riferimento.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Uscita console

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
