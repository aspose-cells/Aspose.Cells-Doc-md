---
title: Manipolare l'intervallo denominato in una cartella di lavoro
type: docs
weight: 90
url: /it/cpp/manipulate-named-range-in-a-workbook/
---
##  **Possibili scenari di utilizzo**
 Aspose.Cells supporta la manipolazione di intervalli denominati esistenti. È possibile accedere a tutti gli intervalli denominati esistenti da[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) collezione. Una volta effettuato l'accesso all'intervallo denominato, è possibile modificare i suoi vari metodi, ad es[Ottieni testo completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)E[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Manipolare l'intervallo denominato in una cartella di lavoro**
 Il seguente codice di esempio legge il primo intervallo denominato all'interno di[file Excel di origine](23167008.xlsx) e lo stampa[Testo intero](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)E[Si riferisce a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) proprietà sulla console. Successivamente, modifica la proprietà `RefersTo` e salva il file[file Excel di output](23167009.xlsx).
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Uscita della console**
 Il seguente output della console stampa i valori di[Testo intero](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)E[Si riferisce a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) membri dell'esistente*Intervallo denominato*nel codice sopra.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
