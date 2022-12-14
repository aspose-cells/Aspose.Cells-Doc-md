---
title: Aggiungere e recuperare dati
type: docs
weight: 20
url: /it/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 In[Accesso a Cells di un foglio di lavoro](/cells/it/cpp/accessing-cells-of-a-worksheet/)abbiamo discusso gli approcci di base per l'accesso alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}} 
## **Aggiunta di dati a Cells**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce un[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Ogni elemento del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione rappresenta un oggetto della[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)classe.

 Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classe[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) metodo. Aspose.Cells fornisce versioni sovraccaricate di[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) metodo che consente agli sviluppatori di aggiungere diversi tipi di dati alle celle. L'utilizzo di queste versioni sovraccaricate di[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)metodo, è possibile aggiungere alla cella un valore booleano, stringa, double, intero o data/ora, ecc.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Miglioramento dell'efficienza**
 Se usi[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)metodo per inserire una grande quantità di dati in un foglio di lavoro, è necessario aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle vostre applicazioni.
## **Recupero dati da Cells**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) raccolta che consente l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce a[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Ogni elemento del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione rappresenta un oggetto della[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)classe.

 Il[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)class fornisce diversi metodi che consentono agli sviluppatori di recuperare i valori dalle celle in base ai loro tipi di dati. Questi metodi includono:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), restituisce il valore stringa della cella.
- [OttieniDoppioValore](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), restituisce il doppio valore della cella.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), restituisce il valore booleano della cella.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), restituisce il valore data/ora della cella.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), restituisce il valore float della cella.
- [OttieniIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), restituisce il valore intero della cella.

 Quando un campo non è riempito, le celle con[OttieniDoppioValore](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) o[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)genera un'eccezione.

Il tipo di dati contenuti in una cella può essere controllato anche utilizzando il[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classe[OttieniTipo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) metodo. Infatti il[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classe[OttieniTipo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) metodo si basa sul[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)enumerazione i cui valori predefiniti sono elencati di seguito:

|**Cell Tipi di valore**|**Descrizione**|
|:- |:- |
|CellValueType_IsBool|Specifica che il valore della cella è booleano.|
|CellValueType_IsDateTime|Specifica che il valore della cella è data/ora.|
|CellValueType_IsNull|Rappresenta una cella vuota.|
|CellValueType_IsNumeric|Specifica che il valore della cella è numerico.|
|CellValueType_IsString|Specifica che il valore della cella è una stringa.|
|CellValueType_IsUnknown|Specifica che il valore della cella è sconosciuto.|
È inoltre possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontare con il tipo dei dati presenti in ciascuna cella.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
