---
title: Modifiche all API pubblica in Aspose.Cells 8.7.0
type: docs
weight: 240
url: /it/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.3 alla 8.7.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per ottimizzazione PDF**
Aspose.Cells Le API già forniscono la funzionalità di convertire i fogli elettronici in PDF. Con questa versione dell'API, gli utenti possono ora [ottimizzare le dimensioni del PDF risultante](/cells/it/java/save-excel-into-pdf-with-standard-or-minimum-size/) Aspose.Cells for Java 8.7.0 ha esposto la proprietà PdfSaveOptions.OptimizationType insieme all'enumerazione PdfOptimizationType per facilitare gli utenti a scegliere l'algoritmo di ottimizzazione desiderato durante l'esportazione dei fogli elettronici nel formato PDF. Ci sono 2 valori possibili per la proprietà PdfSaveOptions.OptimizationType come dettagliato di seguito. 

1. PdfOptimizationType.MINIMUM_SIZE: La qualità è compromessa per la dimensione del file risultante.
1. PdfOptimizationType.STANDARD: La qualità non è compromessa, quindi le dimensioni del file risultante saranno grandi.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Rilevamento del progetto VBA firmato digitalmente**
La nuova proprietà VbaProject.isSigned può essere utilizzata per rilevare se il progetto VBA in un foglio di lavoro è firmato digitalmente.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Aggiunto il metodo Protection.verifyPassword**
Le API di Aspose.Cells hanno potenziato la classe Protection introducendo il metodo verifyPassword che consente di specificare una password come istanza di Stringa e verifica se la stessa password è stata utilizzata per proteggere il Foglio di lavoro. Il metodo Protection.verifyPassword restituisce true se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro dato, e false se la password specificata non corrisponde. Il seguente codice utilizza il metodo Protection.verifyPassword insieme al campo Protection.isProtectedWithPassword per rilevare la protezione con password e verifica la password.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Proprietà Protection.isProtectedWithPassword Aggiunta**
Questo rilascio di Aspose.Cells for Java ha anche esposto il campo Protection.isProtectedWithPassword che può essere utile nel rilevare se un Foglio di lavoro è protetto da password o meno.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Proprietà aggiunta ColorScale.Is3ColorScale**
Aspose.Cells for Java 8.7.0 ha esposto la proprietà ColorScale.Is3ColorScale che può essere utilizzata per [creare un formato condizionale a scala di colori a 2 colori](/cells/it/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). La suddetta proprietà è di tipo Boolean con un valore predefinito di true, il che significa che per impostazione predefinita il formato condizionale sarà a scala di colori a 3 colori. Tuttavia, passando la proprietà ColorScale.Is3ColorScale a false, verrà generato un formato condizionale a scala di colori a 2 colori.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Proprietà aggiunta TxtLoadOptions.HasFormula**
Aspose.Cells for Java 8.7.0 ha fornito supporto per [identificare e analizzare le formule durante il caricamento di file CSV/TXT contenenti dati delimitati](/cells/it/java/load-or-import-csv-file-with-formulas/). La nuova proprietà TxtLoadOptions.HasFormula, quando impostata su true, indica all'API di analizzare le formule dal file delimitato di input e impostarle nelle celle pertinenti senza richiedere alcun ulteriore processo.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Proprietà Added DataLabels.ResizeShapeToFitText aggiunta**
Un'altra funzionalità utile esposta da Aspose.Cells for Java 8.7.0 è la proprietà DataLabels.ResizeShapeToFitText che può abilitare la funzionalità [ridimensiona forma per adattare testo](/cells/it/java/resize-chart-s-data-label-shape-to-fit-text/) dell'applicazione Excel per le etichette dei dati del grafico.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **API rimosse**
### **Proprietà Workbook.SaveOptions rimossa**
La proprietà Workbook.SaveOptions è stata dichiarata obsoleta qualche tempo fa. Con questa versione, è stata completamente rimossa dall'API pubblica, quindi si consiglia di utilizzare il metodo Workbook.save(Stream, SaveOptions) o Workbook.save(string, SaveOptions) come alternativa.
{{< app/cells/assistant language="java" >}}
