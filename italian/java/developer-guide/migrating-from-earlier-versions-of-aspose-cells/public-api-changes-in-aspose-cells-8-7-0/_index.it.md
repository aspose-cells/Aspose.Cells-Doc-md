---
title: Modifiche all'API pubblica in Aspose.Cells 8.7.0
type: docs
weight: 240
url: /it/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.3 alla 8.7.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per l'ottimizzazione PDF**
 Le API Aspose.Cells forniscono già la funzione di conversione dei fogli di calcolo in PDF. Con questa versione dell'API, gli utenti possono ora[ottimizzare la dimensione del PDF risultante](/cells/it/java/save-excel-into-pdf-with-standard-or-minimum-size/)anche. Aspose.Cells for Java 8.7.0 ha esposto la proprietà PdfSaveOptions.OptimizationType insieme all'enumerazione PdfOptimizationType per facilitare agli utenti la scelta dell'algoritmo di ottimizzazione desiderato durante l'esportazione dei fogli di calcolo in formato PDF. Esistono 2 valori possibili per la proprietà PdfSaveOptions.OptimizationType come descritto di seguito.

1. PdfOptimizationType.MINIMUM_SIZE: la qualità è compromessa per la dimensione del file risultante.
1. PdfOptimizationType.STANDARD: la qualità non è compromessa quindi la dimensione del file risultante sarà grande.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Rilevamento del progetto VBA con firma digitale**
 È possibile utilizzare la proprietà VbaProject.isSigned appena esposta[rilevare se il progetto VBA in una cartella di lavoro è firmato digitalmente](/cells/it/java/check-if-vba-code-is-signed/). La proprietà VbaProject.isSigned è di tipo Boolean, che restituisce true se il progetto VBA è firmato digitalmente e viceversa.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Metodo Protection.verifyPassword aggiunto**
Aspose.Cells Le API hanno potenziato la classe Protection introducendo il metodo verifyPassword che permette di specificare una password come istanza di String e[verifica se la stessa password è stata utilizzata per proteggere il foglio di lavoro](/cells/it/java/verify-password-used-to-protect-the-worksheet/). Il metodo Protection.verifyPassword restituisce true se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro specificato e false se la password specificata non corrisponde. La parte di codice seguente utilizza il metodo Protection.verifyPassword insieme al campo Protection.isProtectedWithPassword per rilevare la protezione tramite password e verifica la password.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Proprietà Protection.isProtectedWithPassword aggiunto**
 Questa versione di Aspose.Cells for Java ha anche esposto il campo Protection.isProtectedWithPassword che può essere utile in[rilevare se un foglio di lavoro è protetto da password o meno](/cells/it/java/detect-if-worksheet-is-password-protected/).

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Proprietà ColorScale.Is3ColorScale Aggiunta**
 Aspose.Cells for Java 8.7.0 ha esposto la proprietà ColorScale.Is3ColorScale che può essere utilizzata per[creare il formato condizionale Scala a 2 colori](/cells/it/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). La suddetta proprietà è di tipo Boolean con valore predefinito true, il che significa che il formato condizionale sarà di default Scala a 3 colori. Tuttavia, l'impostazione della proprietà ColorScale.Is3ColorScale su false genererà un formato condizionale Scala a 2 colori.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Proprietà TxtLoadOptions.HasFormula aggiunto**
 Aspose.Cells for Java 8.7.0 ha fornito supporto a[identificare e analizzare le formule durante il caricamento di file CSV/TXT con dati semplici delimitati](/cells/it/java/load-or-import-csv-file-with-formulas/). La proprietà TxtLoadOptions.HasFormula appena esposta quando impostata su true indica all'API di analizzare le formule dal file delimitato di input e di impostarle sulle celle pertinenti senza richiedere alcuna elaborazione aggiuntiva.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Proprietà DataLabels.ResizeShapeToFitText Aggiunta**
 Un'altra caratteristica utile che Aspose.Cells for Java 8.7.0 ha esposto è la proprietà DataLabels.ResizeShapeToFitText che può abilitare il[ridimensionare la forma per adattarla al testo](/cells/it/java/resize-chart-s-data-label-shape-to-fit-text/) funzionalità dell'applicazione Excel per le etichette dei dati del grafico.

Di seguito è riportato il semplice scenario di utilizzo.

**Giava**

{{< highlight "csharp" >}}

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
### **Proprietà Workbook.SaveOptions Rimosso**
La proprietà Workbook.SaveOptions è stata contrassegnata come obsoleta qualche tempo fa. Con questa release è stato completamente rimosso dall'API pubblica pertanto si consiglia di utilizzare in alternativa il metodo Workbook.save(Stream, SaveOptions) o Workbook.save(string, SaveOptions).
