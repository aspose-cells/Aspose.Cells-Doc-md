---
title: Creare un intervallo nominato in un libro di lavoro
type: docs
weight: 60
url: /it/cpp/create-named-range-in-a-workbook/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells supporta la creazione di un intervallo nominato. Ci sono diversi modi per creare un intervallo nominato. Uno dei modi più semplici è creare prima un oggetto [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) e quindi impostarne il nome utilizzando il metodo [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). È possibile visualizzare tutti gli intervalli nominati all'interno del file Excel tramite l'interfaccia *Nome gestione* di Microsoft Excel.
## **Creare un intervallo nominato in un libro di lavoro**
Il seguente codice di esempio spiega come creare un *Intervallo nominato* tramite Aspose.Cells. Una volta creato l'*Intervallo nominato*, sarà visibile internamente alla collezione [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames). Si prega di consultare il [file Excel di output](23167006.xlsx) generato dal codice per un riferimento.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Output della console**
Il seguente output della console stampa i valori dei metodi [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) e [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) dell'*Intervallo nominato* creato nel codice precedente.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
