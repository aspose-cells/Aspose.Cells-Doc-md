---
title: Crea un intervallo denominato in una cartella di lavoro
type: docs
weight: 60
url: /it/cpp/create-named-range-in-a-workbook/
---
##  **Possibili scenari di utilizzo**
 Aspose.Cells supporta la creazione di un intervallo denominato. Esistono diversi modi per creare un intervallo denominato. Uno dei modi più semplici è prima creare[Allineare](https://reference.aspose.com/cells/cpp/aspose.cells/range) oggetto e quindi impostarne il nome utilizzando[Intervallo.SetNome()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) metodo. Puoi vedere tutti gli intervalli denominati all'interno del tuo file Excel tramite Microsoft Excel*Nome Gestore*interfaccia.
##  **Crea un intervallo denominato in una cartella di lavoro**
 Il seguente codice di esempio spiega come creare un file*Intervallo denominato* tramite Aspose.Cells. Una volta, il*Intervallo denominato* viene creato, è visibile all'interno del file[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) collezione. Si prega di consultare il[file Excel di output](23167006.xlsx) generato dal codice per un riferimento.
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Uscita della console**
 Il seguente output della console stampa i valori di[Ottieni testo completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) E[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) metodi del creato*Intervallo denominato*nel codice sopra.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
