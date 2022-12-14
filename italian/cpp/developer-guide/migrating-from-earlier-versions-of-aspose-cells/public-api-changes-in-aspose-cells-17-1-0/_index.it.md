---
title: Pubblico API Modifiche Aspose.Cells 17.1.0
type: docs
weight: 20
url: /it/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 16.12.0 alla 17.1.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per intervalli denominati**
 Aspose.Cells per C++ ora supporta la creazione e la manipolazione degli intervalli denominati. Il seguente frammento di codice dimostra quanto sia semplice utilizzare Aspose.Cells per C++ API per[creare intervalli denominati](/cells/it/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 Oltre a creare nuovi intervalli denominati, le API Aspose.Cells per C++ supportano anche la manipolazione degli intervalli denominati esistenti. Il seguente frammento di codice utilizza Aspose.Cells per C++ API per[manipolare un intervallo denominato esistente](/cells/it/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Aggiunto il metodo ICells::LinkToXmlMap**
Il metodo LinkToXmlMap è stato aggiunto alla classe ICells, utile per collegare una mappa XML.
### **Aggiunto metodo ICells::ImportCSV**
Alla classe ICells è stato aggiunto il metodo ImportCSV utile per importare un file CSV nelle celle di un foglio di lavoro.
### **Aggiunto il metodo ICells::ImportTwoDimensionArray**
Alla classe ICells è stato aggiunto il metodo GetIProtectedRangeCollection, utile per importare un array bidimensionale di dati in un foglio di lavoro.
### **Aggiunto il metodo IWorksheet::GetIProtectedRangeCollection**
Alla classe IWorksheet è stato aggiunto il metodo GetIProtectedRangeCollection utile per recuperare la collezione di oggetti IProtectedRange.
### **Aggiunto il metodo IWorksheet::GetIProtectedRangeCollection**
Il metodo GetIProtectedRangeCollection è stato aggiunto alla classe IWorksheet, utile per recuperare la raccolta dell'intervallo di modifica dal foglio di lavoro.
### **Aggiunto il metodo IWorkbookSettings::ClearPivottables**
Il metodo ClearPivottables è stato aggiunto alla classe IWorkbookSettings, utile per cancellare tutte le tabelle pivot da un determinato foglio di calcolo.
### **Aggiunto metodo IWorksheetCollection::CreateIRange**
Alla classe IWorksheetCollection è stato aggiunto il metodo CreateIRange che è utile per creare un oggetto dell'IRange passando i riferimenti di cella in formato stringa.
### **Aggiunto il metodo IExternalLink::IsVisible**
Il metodo IsVisible ottiene lo stato di visibilità di un collegamento esterno nell'applicazione Excel.
### **Aggiunti i metodi GetScaleCrop e SetScaleCrop**
Aspose.Cells per C++ 17.1.0 ha esposto i metodi GetScaleCrop e SetScaleCrop alla classe IBuiltInDocumentPropertyCollection. Questi metodi sono utili per ottenere o impostare la proprietà ScaleCrop che indica la modalità di visualizzazione della miniatura del documento.
### **Aggiunti i metodi GetLinksUpToDate e SetLinksUpToDate**
Aspose.Cells per C++ 17.1.0 ha esposto i metodi GetLinksUpToDate e SetLinksUpToDate alla classe IBuiltInDocumentPropertyCollection. Questi metodi sono utili per ottenere o impostare la proprietà LinkUpToDate che indica se i collegamenti ipertestuali in un documento sono aggiornati.
### **Aggiunti i metodi GetAbsolutePath e SetAbsolutePath**
Aspose.Cells per C++ 17.1.0 ha esposto i metodi GetAbsolutePath e SetAbsolutePath alla classe IWorkbook. Questi metodi sono utili per ottenere o impostare il percorso assoluto del file che può essere utilizzato solo per collegamenti esterni.
### **Aggiunti i metodi GetFormula e SetFormula**
Questa versione di Aspose.Cells per C++ ha esposto i metodi GetFormula e SetFormula per la classe IListColumn. Questi metodi sono utili per ottenere o impostare la formula di una colonna dell'elenco.
### **Aggiunti i metodi GetCheckCompatibility e SetCheckCompatibility**
Questa versione di Aspose.Cells per C++ ha esposto i metodi GetCheckCompatibility e GetCheckCompatibility per la classe IWorkbookSettings. Questi metodi sono utili per ottenere o impostare la proprietà di verifica della compatibilità che indica se API deve verificare la compatibilità durante il salvataggio della cartella di lavoro. Il valore predefinito è true e può essere impostato su false se il requisito dell'applicazione non è verificare la compatibilità.
### **Aggiunti i metodi GetILightCellsDataHandler e SetILightCellsDataHandler**
Aspose.Cells per C++ ha ora esposto i metodi GetILightCellsDataHandler e SetILightCellsDataHandler per la classe ILoadOptions. Questi metodi denotano il gestore dati per l'elaborazione dei dati delle celle durante la lettura del file modello.
### **Aggiunti i metodi GetCultureInfo e SetCultureInfo**
Aspose.Cells per C++ ha esposto i metodi GetCultureInfo e SetCultureInfo per la classe ILoadOptions. Questi metodi possono ottenere o impostare le informazioni sulla cultura del sistema al momento del caricamento del file.
## **API rimosse**
### **Metodo ICells::MaxDataRowInColumn rimosso**
Si consiglia invece di utilizzare il metodo ICells::GetLastDataRow.
### **Metodo ICell::GetConditionalIStyle rimosso**
Si consiglia invece di utilizzare il metodo ICell::GetIConditionalFormattingResult.
### **Rimossi i metodi IPageSetup::GetDraft e SetDraft**
Si consiglia invece di utilizzare i metodi IPageSetup::GetPrintDraft e IPageSetup::SetPrintDraft.

{{% alert color="primary" %}} 

Con il rilascio di Aspose.Cells per C++ 17.1.0, abbiamo rimosso alcuni metodi che non erano in uso e quindi ritenuti non necessari. Ecco l'elenco di tutti questi metodi.

- Metodi IPaneCollection::GetAcitvePaneType e SetAcitvePaneType
- Metodo IRange::ToString
- Metodo IRow::Equals
- Metodo IWorkbook::SetISettings
- Metodo ICell::ToString()
- Metodo ICell::Equals(ObjectPtr).
- Metodo ICell::GetHashCode
- Metodo IWorksheet::ToString

{{% /alert %}}
