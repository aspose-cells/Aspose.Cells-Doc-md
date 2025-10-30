---
title: Aggiungere e recuperare dati
type: docs
weight: 20
url: /it/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accesso alle celle di un foglio di lavoro](/cells/it/cpp/accessing-cells-of-a-worksheet/), abbiamo discusso degli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di quegli approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}} 
## **Aggiunta di dati alle celle**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione di [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento nella collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells consente ai programmatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) della classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells fornisce versioni sovraccaricate del metodo [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) che consentono ai programmatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate del metodo [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), è possibile aggiungere valori booleani, stringhe, double, integer o data/ora, ecc. alla cella.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Miglioramento dell'efficienza**
Se si utilizza il metodo [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) per inserire una grande quantità di dati in un foglio di lavoro, è necessario aggiungere i valori alle celle prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle applicazioni.
## **Recupero dei dati dalle celle**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento nella raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) fornisce diversi metodi che consentono ai programmatori di recuperare i valori dalle celle in base ai loro tipi di dati. Questi metodi includono:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), restituisce il valore stringa della cella.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), restituisce il valore double della cella.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), restituisce il valore booleano della cella.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), restituisce il valore data/ora della cella.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), restituisce il valore float della cella.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) o [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) generano un'eccezione.

Anche il tipo di dati contenuto in una cella può essere verificato utilizzando il metodo [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) della classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Infatti, il metodo [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) della classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) si basa sull'enumerazione [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|CellValueType_IsBool| Specifica che il valore della cella è Booleano.
|CellValueType_IsDateTime| Specifica che il valore della cella è data/ora.
|CellValueType_IsNull| Rappresenta una cella vuota.
|CellValueType_IsNumeric| Specifica che il valore della cella è numerico.
|CellValueType_IsString| Specifica che il valore della cella è una stringa.
|CellValueType_IsUnknown| Specifica che il valore della cella è sconosciuto. |
Puoi anche usare i tipi di valore predefiniti sopra indicati per confrontare il Tipo dei dati presenti in ogni cella.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
