---
title: Crea un intervallo denominato in una cartella di lavoro
type: docs
weight: 60
url: /it/cpp/create-named-range-in-a-workbook/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells supporta la creazione di un intervallo denominato. Esistono diversi modi per creare un intervallo denominato. Uno dei modi più semplici è creare prima[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) oggetto e quindi impostarne il nome utilizzando[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) metodo. Puoi vedere tutti gli intervalli denominati all'interno del tuo file excel tramite Microsoft Excel*Nome Responsabile*interfaccia.
## **Crea un intervallo denominato in una cartella di lavoro**
 Il codice di esempio seguente spiega come creare un file*Intervallo con nome* via Aspose.Cells. Una volta, il*Intervallo con nome* viene creato, è visibile all'interno del[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) collezione. Si prega di consultare il[file excel di output](23167006.xlsx) generato dal codice per un riferimento.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Uscita console**
 Il seguente output della console stampa i valori di[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) e `GetRefersTo` metodi del creato*Intervallo con nome*nel codice di cui sopra.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
