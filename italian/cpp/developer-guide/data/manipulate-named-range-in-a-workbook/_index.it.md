---
title: Manipolare l'intervallo denominato in una cartella di lavoro
type: docs
weight: 90
url: /it/cpp/manipulate-named-range-in-a-workbook/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells supporta la manipolazione di intervalli denominati esistenti. È possibile accedere a tutti gli intervalli denominati esistenti[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) collezione. Una volta che si accede all'intervallo denominato, è possibile modificarne i vari metodi, ad es[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)e[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Manipolare l'intervallo denominato in una cartella di lavoro**
Il codice di esempio seguente legge il primo intervallo denominato all'interno di[file excel di origine](23167008.xlsx) e stampa il suo[Testo intero](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)e[Si riferisce a](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) proprietà sulla console. Successivamente, modifica la proprietà `RefersTo` e salva il file[file excel di output](23167009.xlsx).
## **Codice di esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Uscita console**
 Il seguente output della console stampa i valori di[Testo intero](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)e[Si riferisce a](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) membri dell'esistente*Intervallo con nome*nel codice di cui sopra.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
