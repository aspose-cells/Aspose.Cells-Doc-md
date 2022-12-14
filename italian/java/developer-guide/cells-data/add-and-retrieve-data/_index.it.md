---
title: Aggiungere e recuperare dati
type: docs
weight: 20
url: /it/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 In[Accesso a Cells di un foglio di lavoro](/cells/it/java/accessing-cells-of-a-worksheet/)abbiamo discusso gli approcci di base per l'accesso alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}} 
## **Aggiunta di dati a Cells**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[valore impostato](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)proprietà. Utilizzando il[valore impostato](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)proprietà, è possibile aggiungere valori booleani, stringa, double, interi o data/ora, ecc. alla cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Miglioramento dell'efficienza**
{{% alert color="primary" %}} 

 Se usi il[valore impostato](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)proprietà per aggiungere una grande quantità di dati a un foglio di lavoro, è necessario aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle vostre applicazioni.

{{% /alert %}} 

Mentre lavorano sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi elementi di dati possono includere valori booleani, interi, a virgola mobile, testo o data/ora. È possibile ottenere i valori appropriati dalle celle in base ai relativi tipi di dati utilizzando Aspose.Cells.
## **Recupero dati da Cells**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Excel.[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)class fornisce diverse proprietà che consentono agli sviluppatori di recuperare i valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [Valore stringa](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), il valore della stringa della cella.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), restituisce il doppio valore della cella.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), il valore booleano della cella.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), il valore di data/ora della cella.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), il valore float della cella.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), il valore intero della cella.

 Inoltre, il tipo di dati contenuti in una cella può essere verificato anche utilizzando il file[Tipo](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) proprietà del[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe. Infatti il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[Tipo](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) proprietà su cui si basa[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)enumerazione i cui valori predefiniti sono elencati di seguito:

|**Cell Tipi di valore**|**Descrizione**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Specifica che il valore della cella è booleano.|
|[È_DATA_VOLTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Specifica che il valore della cella è data/ora.|
|[È_ERRORE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Indica che la cella contiene un valore di errore|
|[È ZERO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Rappresenta una cella vuota.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Specifica che il valore della cella è numerico.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Specifica che il valore della cella è una stringa.|
|[È SCONOSCIUTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Specifica che il valore della cella è sconosciuto.|
È inoltre possibile utilizzare i tipi di valori di cella predefiniti sopra per confrontare con il tipo di dati presenti in ciascuna cella.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
