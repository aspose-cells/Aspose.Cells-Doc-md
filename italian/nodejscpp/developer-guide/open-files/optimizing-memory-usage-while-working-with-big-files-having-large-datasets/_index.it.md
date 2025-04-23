---  
title: Ottimizzazione dell uso della memoria durante il lavoro con file di grandi dimensioni e grandi dataset con Node.js tramite C++  
linktitle: Ottimizzazione dell uso della memoria durante il lavoro con grandi file contenenti grandi set di dati  
type: docs  
weight: 180  
url: /it/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

Quando si costruisce un workbook con grandi set di dati, o si legge un grande file Microsoft Excel, la quantità totale di RAM richiesta dal processo è sempre una preoccupazione. Esistono misure che possono essere adattate per affrontare questa sfida. Aspose.Cells for Node.js via C++ fornisce alcune opzioni e chiamate API rilevanti per ridurre, abbassare e ottimizzare l'uso della memoria. Inoltre, può aiutare il processo a lavorare più efficientemente e a eseguire più velocemente.  

Usa l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) per ottimizzare l'uso della memoria per i dati delle celle e diminuire il costo complessivo della memoria. Quando si costruisce un ampio set di dati per le celle, può risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Ottimizzazione della Memoria**  

### **Lettura di File Excel di Grandi Dimensioni**  

L'esempio seguente mostra come leggere un grande file Microsoft Excel in modalità ottimizzata.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Scrittura di file Excel di grandi dimensioni**  

L'esempio seguente mostra come scrivere un ampio dataset in un foglio di lavoro in modalità ottimizzata.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Attenzione**  

L'opzione predefinita, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), viene applicata a tutte le versioni. Per alcune situazioni, come la costruzione di un workbook con un grande set di dati per le celle, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) può ottimizzare l'uso della memoria e ridurre i costi di memoria per l'applicazione. Tuttavia, questa opzione può degradare le prestazioni in alcuni casi particolari come il seguente.  

1. **Accesso casuale e ripetuto alle celle**: La sequenza più efficiente per accedere alla collezione di celle è cella per cella in una riga, e poi riga per riga. Specialmente, se si accedono alle righe/celle tramite l'enumerator acquisito da [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection), e [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), le prestazioni saranno massimizzate con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Inserire e eliminare celle e righe**: Si prega di notare che se ci sono molte operazioni di inserimento/eliminazione per Celle/Righe, il decadimento delle prestazioni sarà notevole in modalità *MemoryPreference* rispetto alla modalità *Normale*.  
3. **Operare su diversi tipi di celle**: Se la maggior parte delle celle contiene valori stringa o formule, il costo di memoria sarà lo stesso della modalità *Normale*, ma se ci sono molte celle vuote, o i valori delle celle sono numerici, booleani e così via, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) offrirà prestazioni migliori.  

