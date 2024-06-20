---
title: Modifiche API pubbliche in Aspose.Cells 17.1.0
type: docs
weight: 20
url: /it/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.12.0 alla 17.1.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per i Named Ranges**
Aspose.Cells for C++ ora supporta la creazione e la manipolazione dei Named Ranges. Il seguente snippet di codice dimostra quanto sia semplice utilizzare l'API Aspose.Cells for C++ per [creare named ranges](/cells/it/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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

Oltre alla creazione di nuovi Named Ranges, le API Aspose.Cells for C++ supportano anche la manipolazione di Named Ranges esistenti. Il seguente snippet di codice utilizza l'API Aspose.Cells for C++ per [manipolare un named range esistente](/cells/it/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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
Il metodo LinkToXmlMap è stato aggiunto alla classe ICells ed è utile per collegare una mappa XML.
### **Aggiunto il metodo ICells::ImportCSV**
Il metodo ImportCSV è stato aggiunto alla classe ICells che è utile per l'importazione di un file CSV sulle celle di un foglio di lavoro.
### **Aggiunto Metodo ICells::ImportTwoDimensionArray**
Il metodo GetIProtectedRangeCollection è stato aggiunto alla classe ICells che è utile per l'importazione di un array bidimensionale di dati su un foglio di lavoro.
### **Aggiunto Metodo IWorksheet::GetIProtectedRangeCollection**
Il metodo GetIProtectedRangeCollection è stato aggiunto alla classe IWorksheet ed è utile per il recupero della collezione degli oggetti IProtectedRange.
### **Aggiunto Metodo IWorksheet::GetIProtectedRangeCollection**
Il metodo GetIProtectedRangeCollection è stato aggiunto alla classe IWorksheet ed è utile per il recupero della collezione di intervalli di modifica dal foglio di lavoro.
### **Aggiunto Metodo IWorkbookSettings::ClearPivottables**
Il metodo ClearPivottables è stato aggiunto alla classe IWorkbookSettings ed è utile per eliminare tutte le tabelle pivot da un foglio di calcolo specifico.
### **Aggiunto Metodo IWorksheetCollection::CreateIRange**
Il metodo CreateIRange è stato aggiunto alla classe IWorksheetCollection ed è utile per creare un oggetto di tipo IRange passando i riferimenti delle celle in formato stringa.
### **Aggiunto Metodo IExternalLink::IsVisible**
Il metodo IsVisible ottiene lo stato di visibilità di un collegamento esterno nell'applicazione Excel.
### **Aggiunti Metodi GetScaleCrop & SetScaleCrop**
Aspose.Cells for C++ 17.1.0 ha esposto i metodi GetScaleCrop & SetScaleCrop alla classe IBuiltInDocumentPropertyCollection. Questi metodi sono utili per ottenere o impostare la proprietà ScaleCrop che indica la modalità di visualizzazione dell'anteprima del documento.
### **Aggiunti Metodi GetLinksUpToDate & SetLinksUpToDate**
Aspose.Cells for C++ 17.1.0 ha esposto i metodi GetLinksUpToDate & SetLinksUpToDate alla classe IBuiltInDocumentPropertyCollection. Questi metodi sono utili per ottenere o impostare la proprietà LinkUpToDate che indica se i collegamenti ipertestuali in un documento sono aggiornati.
### **Aggiunti Metodi GetAbsolutePath & SetAbsolutePath**
Aspose.Cells for C++ 17.1.0 ha esposto i metodi GetAbsolutePath & SetAbsolutePath alla classe IWorkbook. Questi metodi sono utili per ottenere o impostare il percorso assoluto del file che può essere utilizzato solo per i collegamenti esterni.
### **Aggiunti Metodi GetFormula & SetFormula**
Questa release di Aspose.Cells for C++ ha esposto i metodi GetFormula & SetFormula per la classe IListColumn. Questi metodi sono utili per ottenere o impostare la formula di una colonna della lista.
### **Aggiunti i metodi GetCheckCompatibility & SetCheckCompatibility**
Questa release di Aspose.Cells for C++ ha esposto i metodi GetCheckCompatibility & GetCheckCompatibility per la classe IWorkbookSettings. Questi metodi sono utili per ottenere o impostare la proprietà di controllo della compatibilità che indica se l'API deve controllare la compatibilità durante il salvataggio del workbook. Il valore predefinito è true e può essere impostato su false se il requisito dell'applicazione non è controllare la compatibilità.
### **Aggiunti i metodi GetILightCellsDataHandler & SetILightCellsDataHandler**
Aspose.Cells for C++ ha ora esposto i metodi GetILightCellsDataHandler & SetILightCellsDataHandler per la classe ILoadOptions. Questi metodi indicano il gestore dati per elaborare i dati delle celle durante la lettura del file di modello.
### **Aggiunti i metodi GetCultureInfo & SetCultureInfo**
Aspose.Cells for C++ ha esposto i metodi GetCultureInfo & SetCultureInfo per la classe ILoadOptions. Questi metodi possono ottenere o impostare le informazioni culturali di sistema al momento del caricamento del file.
## **API rimosse**
### **Rimosso il metodo ICells::MaxDataRowInColumn**
Si consiglia di utilizzare il metodo ICells::GetLastDataRow al suo posto.
### **Rimosso il metodo ICell::GetConditionalIStyle**
Si consiglia di utilizzare il metodo ICell::GetIConditionalFormattingResult al suo posto.
### **Rimossi i metodi IPageSetup::GetDraft & SetDraft**
Si consiglia di utilizzare i metodi IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft al loro posto.

{{% alert color="primary" %}} 

Con il rilascio di Aspose.Cells for C++ 17.1.0, abbiamo rimosso alcuni metodi che non erano in uso e quindi ritenuti superflui. Ecco l'elenco di tutti questi metodi.

- Metodi IPaneCollection::GetAcitvePaneType & SetAcitvePaneType
- Metodo IRange::ToString
- Metodo IRow::Equals
- Metodo IWorkbook::SetISettings
- Metodo ICell::ToString
- Metodo ICell::Equals(ObjectPtr)
- Metodo ICell::GetHashCode
- Metodo IWorksheet::ToString

{{% /alert %}}
