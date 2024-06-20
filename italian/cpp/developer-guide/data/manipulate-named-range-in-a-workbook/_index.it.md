---
title: Manipolare Intervalli con Nome in un Workbook
type: docs
weight: 90
url: /it/cpp/manipulate-named-range-in-a-workbook/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells supporta la manipolazione degli intervalli con nome esistenti. Tutti gli intervalli con nome esistenti possono essere accessibili dalla collezione [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/). Una volta che si accede all'intervallo con nome, è possibile modificare i vari metodi come ad es. [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) e [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Manipolare l'intervallo di celle con nome in un documento di lavoro**
Il seguente codice di esempio legge il primo intervallo di celle con nome all'interno del [file Excel di origine](23167008.xlsx) e ne stampa le proprietà [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) e [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) sulla console. Successivamente modifica la proprietà `RefersTo` e salva il [file Excel di output](23167009.xlsx).
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Output della console**
Il seguente output della console stampa i valori dei membri [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) e [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) dell' *Intervallo di Celle con Nome* esistente nel codice precedente.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
