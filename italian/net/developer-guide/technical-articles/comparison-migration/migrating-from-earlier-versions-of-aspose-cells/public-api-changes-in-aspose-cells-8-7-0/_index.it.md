---
title: Modifiche all'API pubblica in Aspose.Cells 8.7.0
type: docs
weight: 230
url: /it/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.3 alla 8.7.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per la firma digitale, il rilevamento e l'estrazione del progetto VBA**
Questa versione di Aspose.Cells for .NET ha esposto alcune nuove proprietà e metodi per aiutare gli utenti in attività come la firma digitale di un progetto VBA, rilevando se un progetto VBA è firmato e valido. Inoltre, la nuova API consente di estrarre il certificato come dati grezzi dal progetto VBA firmato digitalmente in Workbook.
###### **Firma digitalmente progetto VBA**
 Aspose.Cells for .NET 8.7.0 ha esposto il metodo VbaProject.Sign che può essere utilizzato per[firmare digitalmente il progetto VBA in una cartella di lavoro](/cells/it/net/digitally-sign-a-vba-code-project-with-certificate/). Detto metodo accetta un'istanza della classe DigitalSignature che risiede nel namespace Aspose.Cells.DigitalSignatures.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Rilevamento del progetto VBA con firma digitale**
 È possibile utilizzare la proprietà VbaProject.IsSigned appena esposta[rilevare se il progetto VBA in una cartella di lavoro è firmato digitalmente](/cells/it/net/check-if-vba-code-is-signed/). La proprietà VbaProject.IsSigned è di tipo Boolean, che restituisce true se il progetto VBA è firmato digitalmente e viceversa.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **Estrazione della Firma Digitale dal Progetto VBA**
Questa revisione dell'API ha anche esposto la proprietà VbaProject.CertRawData che consente di[estrarre i dati grezzi del certificato digitale dal progetto VBA](/cells/it/net/export-vba-certificate-to-file-or-stream/). La proprietà VbaProject.CertRawData è di tipo byte array, che conterrà i dati grezzi del certificato se il progetto VBA è firmato digitalmente, altrimenti tale proprietà sarà nulla.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Convalida la Firma Digitale del Progetto VBA**
 Un'altra aggiunta all'API pubblica è la proprietà VbaProject.IsValidSigned che potrebbe essere utile[convalidare la firma digitale del progetto VBA](/cells/it/net/check-if-digital-signature-of-vba-code-is-valid/). La suddetta proprietà restituisce true se la firma digitale è valida e false se la firma non è valida.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Metodo Protection.VerifyPassword aggiunto**
 Aspose.Cells for .NET 8.7.0 ha esposto il metodo Protection.VerifyPassword che può essere utilizzato per[verificare la password utilizzata per proteggere il foglio di lavoro](/cells/it/net/verify-password-used-to-protect-the-worksheet/)Questo metodo accetta un'istanza di string come parametro e restituisce true se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Proprietà Protection.IsProtectedWithPassword aggiunto**
 Questa versione dell'API Aspose.Cells for .NET ha anche esposto la proprietà Protection.IsProtectedWithPassword che può essere utile in[rilevare se un foglio di lavoro è protetto da password o meno](/cells/it/net/detect-if-worksheet-is-password-protected/).

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Proprietà ColorScale.Is3ColorScale Aggiunta**
 Aspose.Cells for .NET 8.7.0 ha esposto la proprietà ColorScale.Is3ColorScale che può essere utilizzata per creare il formato condizionale Scala a 2 colori. La suddetta proprietà è di tipo Boolean con valore predefinito true, il che significa che il formato condizionale sarà di default Scala a 3 colori. Tuttavia, il passaggio della proprietà ColorScale.Is3ColorScale a false lo farà[generare un formato condizionale Scala a 2 colori](/cells/it/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Proprietà TxtLoadOptions.HasFormula aggiunto**
 Aspose.Cells for .NET 8.7.0 ha fornito supporto a[identificare e analizzare le formule durante il caricamento di file CSV/TXT con dati semplici delimitati](/cells/it/net/load-or-import-csv-file-with-formulas/). La proprietà TxtLoadOptions.HasFormula appena esposta quando impostata su true indica all'API di analizzare le formule dal file delimitato di input e di impostarle sulle celle pertinenti senza richiedere alcuna elaborazione aggiuntiva.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **Proprietà DataLabels.IsResizeShapeToFitText Aggiunta**
 Un'altra caratteristica utile che Aspose.Cells for .NET 8.7.0 ha esposto è la proprietà DataLabels.IsResizeShapeToFitText che può abilitare il[Ridimensiona la forma per adattarla al testo](/cells/it/net/resize-chart-s-data-label-shape-to-fit-text/) funzionalità dell'applicazione Excel per le etichette dei dati del grafico.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **Proprietà PdfSaveOptions.OptimizationType aggiunta**
Aspose.Cells for .NET 8.7.0 ha esposto la proprietà PdfSaveOptions.OptimizationType insieme all'enumerazione PdfOptimizationType per facilitare agli utenti[scegli l'algoritmo di ottimizzazione desiderato durante l'esportazione dei fogli di calcolo in formato PDF](/cells/it/net/save-excel-into-pdf-with-standard-or-minimum-size/). Esistono 2 valori possibili per la proprietà PdfSaveOptions.OptimizationType come descritto di seguito.

1. PdfOptimizationType.MinimumSize: la qualità è compromessa per la dimensione del file risultante.
1. PdfOptimizationType.Standard: la qualità non è compromessa quindi la dimensione del file risultante sarà grande.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **API rimosse**
### **Proprietà Workbook.SaveOptions Rimosso**
La proprietà Workbook.SaveOptions è stata contrassegnata come obsoleta qualche tempo fa. Con questa release è stato completamente rimosso dall'API pubblica pertanto si consiglia di utilizzare in alternativa il metodo Workbook.Save(Stream, SaveOptions) o Workbook.Save(string, SaveOptions).
