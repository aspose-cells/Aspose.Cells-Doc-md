---
title: Modifiche all API pubblica in Aspose.Cells 8.7.0
type: docs
weight: 230
url: /it/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.3 alla 8.7.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per la firma digitale del progetto VBA, rilevamento ed estrazione**
Questa release di Aspose.Cells for .NET ha esposto alcune nuove proprietà e metodi per aiutare gli utenti nelle attività come la firma digitale di un progetto VBA, il rilevamento se un progetto VBA è firmato e valido. Inoltre, la nuova API consente di estrarre il certificato come dati grezzi dal progetto VBA firmato digitalmente in Workbook.
###### **Firma digitalmente il progetto VBA**
Aspose.Cells for .NET 8.7.0 ha esposto il metodo VbaProject.Sign che può essere utilizzato per [firmare digitalmente il progetto VBA in un Workbook](/cells/it/net/digitally-sign-a-vba-code-project-with-certificate/). Il suddetto metodo accetta un'istanza della classe DigitalSignature che risiede nello spazio dei nomi Aspose.Cells.DigitalSignatures.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Rilevamento del progetto VBA firmato digitalmente**
La nuova proprietà VbaProject.IsSigned esposta può essere utilizzata per [rilevare se il progetto VBA in un Workbook è firmato digitalmente](/cells/it/net/check-if-vba-code-is-signed/). La proprietà VbaProject.IsSigned è di tipo Boolean, che restituisce true se il progetto VBA è firmato digitalmente e viceversa.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


###### **Estrazione della firma digitale dal progetto VBA**
Questa revisione dell'API ha esposto anche la proprietà VbaProject.CertRawData che consente di [estrarre i dati grezzi del certificato digitale dal progetto VBA](/cells/it/net/export-vba-certificate-to-file-or-stream/). La proprietà VbaProject.CertRawData è di tipo array di byte, che conterrà i dati grezzi del certificato se il progetto VBA è firmato digitalmente, altrimenti la suddetta proprietà sarà nulla.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Convalida della firma digitale del progetto VBA**
Un'altra aggiunta all'API pubblica è la proprietà VbaProject.IsValidSigned che potrebbe essere utile nel [validare la firma digitale del progetto VBA](/cells/it/net/check-if-digital-signature-of-vba-code-is-valid/). La suddetta proprietà restituisce true se la firma digitale è valida e false se la firma è non valida.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Aggiunto il metodo Protection.VerifyPassword**
Aspose.Cells for .NET 8.7.0 ha esposto il metodo Protection.VerifyPassword che può essere utilizzato per [verificare la password utilizzata per proteggere il Foglio di lavoro](/cells/it/net/verify-password-used-to-protect-the-worksheet/). Questo metodo accetta un'istanza di stringa come parametro e restituisce true se la password specificata corrisponde alla password utilizzata per proteggere il Foglio di lavoro.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Aggiunta la proprietà Protection.IsProtectedWithPassword**
Questa release dell'API Aspose.Cells for .NET ha esposto anche la proprietà Protection.IsProtectedWithPassword che può essere utile nel [rilevare se un Foglio di lavoro è protetto da password o meno](/cells/it/net/detect-if-worksheet-is-password-protected/).

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Proprietà aggiunta ColorScale.Is3ColorScale**
Aspose.Cells for .NET 8.7.0 ha esposto la proprietà ColorScale.Is3ColorScale che può essere utilizzata per creare la formattazione condizionale con Scala colori a 2 colori. La suddetta proprietà è di tipo Boolean con valore predefinito true, il che significa che la formattazione condizionale sarà di Scala colori a 3 colori per impostazione predefinita. Tuttavia, passando la proprietà ColorScale.Is3ColorScale a false verrà generata una formattazione condizionale a 2 colori.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Proprietà aggiunta TxtLoadOptions.HasFormula**
Aspose.Cells for .NET 8.7.0 ha fornito supporto per identificare e analizzare le formule durante il caricamento di file CSV/TXT con dati delimitati. La nuova proprietà TxtLoadOptions.HasFormula esposta quando impostata su true indica all'API di analizzare le formule dal file delimitato in input e impostarle nelle celle pertinenti senza richiedere ulteriori elaborazioni.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Proprietà aggiunta DataLabels.IsResizeShapeToFitText**
Un'altra funzionalità utile che Aspose.Cells for .NET 8.7.0 ha esposto è la proprietà DataLabels.IsResizeShapeToFitText che può abilitare la funzione di Ridimensiona la forma per adattare il testo dell'applicazione Excel per le etichette dati del grafico.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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


### **Proprietà aggiunta PdfSaveOptions.OptimizationType**
Aspose.Cells for .NET 8.7.0 ha esposto la proprietà PdfSaveOptions.OptimizationType insieme all'enumerazione PdfOptimizationType per facilitare agli utenti la scelta dell'algoritmo di ottimizzazione desiderato durante l'esportazione dei fogli di calcolo nel formato PDF. Ci sono 2 possibili valori per la proprietà PdfSaveOptions.OptimizationType come dettagliato di seguito.

1. PdfOptimizationType.MinimumSize: La qualità è compromessa per le dimensioni del file risultante.
1. PdfOptimizationType.Standard: La qualità non è compromessa quindi le dimensioni del file risultante saranno grandi.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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
### **Proprietà Workbook.SaveOptions Rimossa**
La proprietà Workbook.SaveOptions è stata dichiarata obsoleta qualche tempo fa. Con questa versione, è stata completamente rimossa dall'API pubblica, pertanto si consiglia di utilizzare il metodo Workbook.Save(Stream, SaveOptions) o Workbook.Save(string, SaveOptions) come alternativa.
{{< app/cells/assistant language="csharp" >}}
