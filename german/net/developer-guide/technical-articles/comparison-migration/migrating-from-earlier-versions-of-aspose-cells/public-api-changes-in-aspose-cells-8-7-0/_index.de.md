---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.0
type: docs
weight: 230
url: /de/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.3 bis 8.7.0, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für die digitale Signierung, Erkennung und Extraktion von VBA-Projekten**
Dieses Release von Aspose.Cells for .NET hat einige neue Eigenschaften und Methoden freigelegt, die Benutzern bei Aufgaben wie der digitalen Signierung eines VBA-Projekts, der Erkennung, ob ein VBA-Projekt signiert und gültig ist, helfen. Darüber hinaus ermöglicht die neue API die Extraktion des Zertifikats als Rohdaten aus digital signierten VBA-Projekten in der Arbeitsmappe.
###### **Digitale Signatur eines VBA-Projekts**
Aspose.Cells for .NET 8.7.0 hat die VbaProject.Sign-Methode freigelegt, die verwendet werden kann, um [das VBA-Projekt in einer Arbeitsmappe digital zu signieren](/cells/de/net/digitally-sign-a-vba-code-project-with-certificate/). Die besagte Methode akzeptiert eine Instanz der Klasse DigitalSignature, die im Namensraum Aspose.Cells.DigitalSignatures liegt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


###### **Erkennung des digital signierten VBA-Projekts**
Die neu freigelegte VbaProject.IsSigned-Eigenschaft kann [verwendet werden, um zu erkennen, ob das VBA-Projekt in einer Arbeitsmappe digital signiert ist](/cells/de/net/check-if-vba-code-is-signed/). Die VbaProject.IsSigned-Eigenschaft ist vom Typ Boolean und gibt true zurück, wenn das VBA-Projekt digital signiert ist, andernfalls false.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


###### **Extraktion der digitalen Signatur aus einem VBA-Projekt**
Diese Überarbeitung der API hat auch die VbaProject.CertRawData-Eigenschaft freigelegt, die es ermöglicht, [die Rohdaten des digitalen Zertifikats aus dem VBA-Projekt zu extrahieren](/cells/de/net/export-vba-certificate-to-file-or-stream/). Die VbaProject.CertRawData-Eigenschaft ist vom Typ Byte-Array und enthält die Rohzertifikatsdaten, wenn das VBA-Projekt digital signiert ist. Andernfalls ist die besagte Eigenschaft null.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validierung der digitalen Signatur eines VBA-Projekts**
Eine weitere Ergänzung zur öffentlichen API ist die VbaProject.IsValidSigned-Eigenschaft, die nützlich sein könnte, um [die digitale Signatur des VBA-Projekts zu validieren](/cells/de/net/check-if-digital-signature-of-vba-code-is-valid/). Die besagte Eigenschaft gibt true zurück, wenn die digitale Signatur gültig ist und false, wenn die Signatur ungültig ist.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte Protection.VerifyPassword-Methode**
Aspose.Cells for .NET 8.7.0 hat die Protection.VerifyPassword-Methode freigelegt, die verwendet werden kann, um [das Passwort zu überprüfen, das zum Schützen des Arbeitsblatts verwendet wurde](/cells/de/net/verify-password-used-to-protect-the-worksheet/). Diese Methode akzeptiert eine Instanz von string als Parameter und gibt true zurück, wenn das angegebene Passwort mit dem zum Schützen des Arbeitsblatts verwendeten Passwort übereinstimmt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte Protection.IsProtectedWithPassword-Eigenschaft**
Diese Überarbeitung der Aspose.Cells for .NET-API hat auch die Protection.IsProtectedWithPassword-Eigenschaft freigelegt, die nützlich sein kann, um [zu erkennen, ob ein Arbeitsblatt mit einem Passwort geschützt ist oder nicht](/cells/de/net/detect-if-worksheet-is-password-protected/).

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Eigenschaft ColorScale.Is3ColorScale hinzugefügt**
Aspose.Cells for .NET 8.7.0 hat die ColorScale.Is3ColorScale-Eigenschaft freigelegt, die verwendet werden kann, um bedingte Formate für 2-Farb-Skalen zu erstellen. Die genannte Eigenschaft ist vom Typ Boolean mit einem Standardwert von true, was bedeutet, dass das bedingte Format standardmäßig eine 3-Farb-Skala sein wird. Durch Umstellen der ColorScale.Is3ColorScale-Eigenschaft auf false wird jedoch ein bedingtes Format für 2-Farb-Skalen generiert.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügtes TxtLoadOptions.HasFormula-Eigenschaft**
Aspose.Cells for .NET 8.7.0 bietet Unterstützung, um die Formeln zu identifizieren und zu analysieren, während CSV-/TXT-Dateien mit delimitierten reinen Daten geladen werden. Die neu freigelegte TxtLoadOptions.HasFormula-Eigenschaft, wenn auf true gesetzt, leitet die API an, die Formeln aus der Eingabedatei mit den begrenzten Daten zu analysieren und sie den relevanten Zellen zuzuweisen, ohne zusätzliche Verarbeitung zu erfordern.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Added DataLabels.IsResizeShapeToFitText-Eigenschaft**
Eine weitere nützliche Funktion, die Aspose.Cells for .NET 8.7.0 freigelegt hat, ist die DataLabels.IsResizeShapeToFitText-Eigenschaft, die die Funktion 'Form an Text anpassen' der Excel-Anwendung für die Datenbeschriftungen des Diagramms aktivieren kann.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Added PdfSaveOptions.OptimizationType-Eigenschaft**
Aspose.Cells for .NET 8.7.0 hat die PdfSaveOptions.OptimizationType-Eigenschaft zusammen mit der PdfOptimizationType-Aufzählung freigelegt, um den Benutzern die Auswahl des gewünschten Optimierungsalgorithmus beim Exportieren von Tabellenkalkulationen im PDF-Format zu erleichtern. Es gibt 2 mögliche Werte für die PdfSaveOptions.OptimizationType-Eigenschaft, wie unten detailliert.

1. PdfOptimizationType.MinimumSize: Die Qualität wird für die resultierende Dateigröße beeinträchtigt.
1. PdfOptimizationType.Standard: Die Qualität wird nicht beeinträchtigt, daher wird die resultierende Dateigröße groß sein.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
## **Entfernte APIs**
### **Eigenschaft Workbook.SaveOptions entfernt**
Die Workbook.SaveOptions-Eigenschaft wurde vor einiger Zeit als veraltet markiert. Mit dieser Version wurde sie vollständig aus der öffentlichen API entfernt. Daher wird empfohlen, die Workbook.Save(Stream, SaveOptions) oder Workbook.Save(string, SaveOptions)-Methode als Alternative zu verwenden.
{{< app/cells/assistant language="csharp" >}}
