---
title: Aggiungi e recupera dati
type: docs
weight: 20
url: /it/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 In[Accesso allo Cells di un foglio di lavoro](/cells/it/cpp/accessing-cells-of-a-worksheet/), abbiamo discusso gli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}} 
##  **Aggiunta Dati allo Cells**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. Ogni elemento in[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la raccolta rappresenta un oggetto del[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)classe.

 Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il file[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metodo. Aspose.Cells fornisce versioni sovraccaricate di[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) metodo che consente agli sviluppatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate di[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)metodo, è possibile aggiungere alla cella un valore booleano, stringa, double, intero o data/ora, ecc.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Migliorare l'efficienza**
 Se usi[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Per inserire una grande quantità di dati in un foglio di lavoro, è necessario aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle tue applicazioni.
##  **Recupero dati da Cells**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) raccolta che consente l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. Ogni elemento in[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la raccolta rappresenta un oggetto del[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)classe.

 IL[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)La classe fornisce diversi metodi che consentono agli sviluppatori di recuperare valori dalle celle in base ai tipi di dati. Questi metodi includono:

- [OttieniValoreStringa](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), restituisce il valore stringa della cella.
- [OttieniDoppioValore](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), restituisce il doppio valore della cella.
- [Ottieni valore bool](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), restituisce il valore booleano della cella.
- [OttieniDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), restituisce il valore data/ora della cella.
- [Ottieni Valore Float](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), restituisce il valore float della cella.
- [OttieniIntValore](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)restituisce il valore intero della cella.

 Quando un campo non è riempito, le celle con[OttieniDoppioValore](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) O[Ottieni Valore Float](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)genera un'eccezione.

 Il tipo di dati contenuti in una cella può essere verificato anche utilizzando il comando[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[OttieniTipo](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metodo. In effetti, il[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[OttieniTipo](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) il metodo si basa su[TipoValoreCella](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)enumerazione i cui valori predefiniti sono elencati di seguito:

|**Cell Tipi di valore**|**Descrizione**|
| :- | :- |
|CellValueType_IsBool|Specifica che il valore della cella è booleano.|
|CellValueType_IsDateTime|Specifica che il valore della cella è data/ora.|
|CellValueType_IsNull|Rappresenta una cella vuota.|
|CellValueType_IsNumeric|Specifica che il valore della cella è numerico.|
|CellValueType_IsString|Specifica che il valore della cella è una stringa.|
|CellValueType_IsUnknown|Specifica che il valore della cella è sconosciuto.|
È inoltre possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontarli con il Tipo di dati presenti in ciascuna cella.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
