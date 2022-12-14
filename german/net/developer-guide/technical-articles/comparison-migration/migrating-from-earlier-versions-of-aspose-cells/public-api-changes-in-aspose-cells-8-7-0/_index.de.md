---
title: Öffentlich API Änderungen in Aspose.Cells 8.7.0
type: docs
weight: 230
url: /de/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.3 zu 8.7.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für digitales Signieren, Erkennen und Extrahieren von VBA-Projekten**
Diese Version von Aspose.Cells for .NET hat einige neue Eigenschaften und Methoden bereitgestellt, um die Benutzer bei Aufgaben wie dem digitalen Signieren eines VBA-Projekts und dem Erkennen, ob ein VBA-Projekt signiert und gültig ist, zu unterstützen. Darüber hinaus ermöglicht die neue API das Extrahieren des Zertifikats als Rohdaten aus einem digital signierten VBA-Projekt in Workbook.
###### **VBA-Projekt digital signieren**
 Aspose.Cells for .NET 8.7.0 hat die VbaProject.Sign-Methode verfügbar gemacht, die verwendet werden kann[Signieren Sie das VBA-Projekt digital in einer Arbeitsmappe](/cells/de/net/digitally-sign-a-vba-code-project-with-certificate/). Die genannte Methode akzeptiert eine Instanz der DigitalSignature-Klasse, die sich im Namensraum Aspose.Cells.DigitalSignatures befindet.

Es folgt das einfache Nutzungsszenario.

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


###### **Erkennung von digital signierten VBA-Projekten**
 Die neu verfügbar gemachte VbaProject.IsSigned-Eigenschaft kann verwendet werden[erkennen, ob das VBA-Projekt in einer Arbeitsmappe digital signiert ist](/cells/de/net/check-if-vba-code-is-signed/). Die Eigenschaft VbaProject.IsSigned ist vom Typ Boolean und gibt „true“ zurück, wenn das VBA-Projekt digital signiert ist und umgekehrt.

Es folgt das einfache Nutzungsszenario.

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


###### **Extraktion der digitalen Signatur aus dem VBA-Projekt**
Diese Revision von API hat auch die VbaProject.CertRawData-Eigenschaft verfügbar gemacht, die dies ermöglicht[extrahieren Sie die Rohdaten des digitalen Zertifikats aus dem VBA-Projekt](/cells/de/net/export-vba-certificate-to-file-or-stream/). Die Eigenschaft VbaProject.CertRawData ist vom Typ Byte-Array, das die Rohdaten des Zertifikats enthält, wenn das VBA-Projekt digital signiert ist, andernfalls ist die Eigenschaft null.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validieren Sie die digitale Signatur des VBA-Projekts**
 Eine weitere Ergänzung zum öffentlichen API ist die VbaProject.IsValidSigned-Eigenschaft, die nützlich sein könnte[Validierung der digitalen Signatur des VBA-Projekts](/cells/de/net/check-if-digital-signature-of-vba-code-is-valid/). Die genannte Eigenschaft gibt true zurück, wenn die digitale Signatur gültig ist, und false, wenn die Signatur ungültig ist.

Es folgt das einfache Nutzungsszenario.

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


### **Methode Protection.VerifyPassword Hinzugefügt**
 Aspose.Cells for .NET 8.7.0 hat die Protection.VerifyPassword-Methode bereitgestellt, die verwendet werden kann[Überprüfen Sie das zum Schutz des Arbeitsblatts verwendete Kennwort](/cells/de/net/verify-password-used-to-protect-the-worksheet/)Diese Methode akzeptiert eine Zeichenfolgeninstanz als Parameter und gibt „true“ zurück, wenn das angegebene Kennwort mit dem zum Schutz des Arbeitsblatts verwendeten Kennwort übereinstimmt.

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaftsschutz.IsProtectedWithPassword Hinzugefügt**
 Diese Version von Aspose.Cells for .NET API hat auch die Protection.IsProtectedWithPassword-Eigenschaft verfügbar gemacht, die nützlich sein kann[Erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht](/cells/de/net/detect-if-worksheet-is-password-protected/).

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaft ColorScale.Is3ColorScale hinzugefügt**
 Aspose.Cells for .NET 8.7.0 hat die Eigenschaft ColorScale.Is3ColorScale verfügbar gemacht, die zum Erstellen des bedingten Formats „2-Color Scale“ verwendet werden kann. Die genannte Eigenschaft ist vom Typ Boolean mit dem Standardwert „true“, was bedeutet, dass das bedingte Format standardmäßig eine 3-Farbskala ist. Wenn Sie jedoch die Eigenschaft ColorScale.Is3ColorScale auf false umstellen, wird dies der Fall sein[Generieren Sie ein bedingtes 2-Farbskalen-Format](/cells/de/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaft TxtLoadOptions.HasFormula hinzugefügt**
 Aspose.Cells for .NET 8.7.0 hat Unterstützung für bereitgestellt[Identifizieren und parsen Sie die Formeln beim Laden von CSV/TXT-Dateien mit getrennten Klardaten](/cells/de/net/load-or-import-csv-file-with-formulas/). Die neu verfügbar gemachte TxtLoadOptions.HasFormula-Eigenschaft weist, wenn sie auf „true“ gesetzt ist, den API an, die Formeln aus der Eingabedatei mit Trennzeichen zu analysieren und sie auf relevante Zellen festzulegen, ohne dass eine zusätzliche Verarbeitung erforderlich ist.

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaft DataLabels.IsResizeShapeToFitText Hinzugefügt**
 Eine weitere nützliche Funktion, die Aspose.Cells for .NET 8.7.0 verfügbar gemacht hat, ist die DataLabels.IsResizeShapeToFitText-Eigenschaft, die die aktivieren kann[Passen Sie die Größe der Form an den Text an](/cells/de/net/resize-chart-s-data-label-shape-to-fit-text/) Funktion der Excel-Anwendung für die Datenbeschriftungen des Diagramms.

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaft PdfSaveOptions.OptimizationType Hinzugefügt**
Aspose.Cells for .NET 8.7.0 hat die PdfSaveOptions.OptimizationType-Eigenschaft zusammen mit der PdfOptimizationType-Enumeration bereitgestellt, um Benutzern dies zu erleichtern[Wählen Sie den gewünschten Optimierungsalgorithmus, während Sie Tabellenkalkulationen in das PDF-Format exportieren](/cells/de/net/save-excel-into-pdf-with-standard-or-minimum-size/). Es gibt 2 mögliche Werte für die PdfSaveOptions.OptimizationType-Eigenschaft, wie unten beschrieben.

1. PdfOptimizationType.MinimumSize: Die Qualität ist für die resultierende Dateigröße beeinträchtigt.
1. PdfOptimizationType.Standard: Die Qualität wird nicht beeinträchtigt, sodass die resultierende Dateigröße groß sein wird.

Es folgt das einfache Nutzungsszenario.

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
## **Entfernte APIs**
### **Eigenschaft Workbook.SaveOptions Entfernt**
Die Workbook.SaveOptions-Eigenschaft wurde vor einiger Zeit als veraltet markiert. Mit dieser Version wurde es vollständig aus dem öffentlichen API entfernt, daher wird empfohlen, alternativ die Methode Workbook.Save(Stream, SaveOptions) oder Workbook.Save(string, SaveOptions) zu verwenden.
