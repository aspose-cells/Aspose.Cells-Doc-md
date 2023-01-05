---
title: Öffentlich API Änderungen in Aspose.Cells 8.7.0
type: docs
weight: 240
url: /de/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.3 zu 8.7.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für PDF-Optimierung**
 Aspose.Cells-APIs bieten bereits die Funktion zum Konvertieren von Tabellenkalkulationen in PDF. Mit dieser Version von API können Benutzer jetzt[Optimieren Sie die resultierende PDF-Größe](/cells/de/java/save-excel-into-pdf-with-standard-or-minimum-size/)sowie. Aspose.Cells for Java 8.7.0 hat die PdfSaveOptions.OptimizationType-Eigenschaft zusammen mit der PdfOptimizationType-Enumeration verfügbar gemacht, um Benutzern die Auswahl des gewünschten Optimierungsalgorithmus zu erleichtern, während sie Tabellenkalkulationen in das PDF-Format exportieren. Es gibt 2 mögliche Werte für die PdfSaveOptions.OptimizationType-Eigenschaft, wie unten beschrieben.

1. PdfOptimizationType.MINIMUM_SIZE: Die Qualität der resultierenden Dateigröße ist beeinträchtigt.
1. PdfOptimizationType.STANDARD: Die Qualität wird nicht beeinträchtigt, sodass die resultierende Dateigröße groß sein wird.

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Erkennung von digital signierten VBA-Projekten**
 Die neu verfügbar gemachte VbaProject.isSigned-Eigenschaft kann verwendet werden[erkennen, ob das VBA-Projekt in einer Arbeitsmappe digital signiert ist](/cells/de/java/check-if-vba-code-is-signed/). Die Eigenschaft VbaProject.isSigned ist vom Typ Boolean und gibt „true“ zurück, wenn das VBA-Projekt digital signiert ist und umgekehrt.

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Methode Protection.verifyPassword Hinzugefügt**
Aspose.Cells APIs haben die Protection-Klasse erweitert, indem sie die Methode verifyPassword eingeführt haben, die es ermöglicht, ein Passwort als Instanz von String und anzugeben[überprüft, ob das gleiche Passwort verwendet wurde, um das Arbeitsblatt zu schützen](/cells/de/java/verify-password-used-to-protect-the-worksheet/). Die Methode Protection.verifyPassword gibt „true“ zurück, wenn das angegebene Kennwort mit dem Kennwort übereinstimmt, das zum Schutz des angegebenen Arbeitsblatts verwendet wird, und „false“, wenn das angegebene Kennwort nicht übereinstimmt. Der folgende Codeabschnitt verwendet die Protection.verifyPassword-Methode in Verbindung mit dem Protection.isProtectedWithPassword-Feld, um den Kennwortschutz zu erkennen, und überprüft das Kennwort.

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Property Protection.isProtectedWithPassword Hinzugefügt**
 Diese Version von Aspose.Cells for Java hat auch das Feld Protection.isProtectedWithPassword verfügbar gemacht, das nützlich sein kann[Erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht](/cells/de/java/detect-if-worksheet-is-password-protected/).

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Eigenschaft ColorScale.Is3ColorScale Hinzugefügt**
 Aspose.Cells for Java 8.7.0 hat die ColorScale.Is3ColorScale-Eigenschaft bereitgestellt, die verwendet werden kann[bedingtes Format 2-Farbskala erstellen](/cells/de/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Die genannte Eigenschaft ist vom Typ Boolean mit dem Standardwert „true“, was bedeutet, dass das bedingte Format standardmäßig eine 3-Farbskala ist. Wenn Sie jedoch die Eigenschaft ColorScale.Is3ColorScale auf „false“ setzen, wird ein bedingtes Format „2-Farbskala“ generiert.

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Eigenschaft TxtLoadOptions.HasFormula Hinzugefügt**
 Aspose.Cells for Java 8.7.0 hat Unterstützung für bereitgestellt[Identifizieren und parsen Sie die Formeln beim Laden von CSV/TXT-Dateien mit getrennten Klardaten](/cells/de/java/load-or-import-csv-file-with-formulas/). Die neu verfügbar gemachte TxtLoadOptions.HasFormula-Eigenschaft weist, wenn sie auf „true“ gesetzt ist, den API an, die Formeln aus der Eingabedatei mit Trennzeichen zu analysieren und sie auf relevante Zellen festzulegen, ohne dass eine zusätzliche Verarbeitung erforderlich ist.

Es folgt das einfache Nutzungsszenario.

**Java**

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
### **Eigenschaft DataLabels.ResizeShapeToFitText Hinzugefügt**
 Eine weitere nützliche Funktion, die Aspose.Cells for Java 8.7.0 verfügbar gemacht hat, ist die DataLabels.ResizeShapeToFitText-Eigenschaft, die die aktivieren kann[Passen Sie die Größe der Form an den Text an](/cells/de/java/resize-chart-s-data-label-shape-to-fit-text/)Funktion der Excel-Anwendung für die Datenbeschriftungen des Diagramms.

Es folgt das einfache Nutzungsszenario.

**Java**

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
## **Entfernte APIs**
### **Eigenschaft Workbook.SaveOptions Entfernt**
Die Workbook.SaveOptions-Eigenschaft wurde vor einiger Zeit als veraltet markiert. Mit dieser Version wurde es vollständig aus dem öffentlichen API entfernt, daher wird empfohlen, alternativ die Methode Workbook.save(Stream, SaveOptions) oder Workbook.save(string, SaveOptions) zu verwenden.
