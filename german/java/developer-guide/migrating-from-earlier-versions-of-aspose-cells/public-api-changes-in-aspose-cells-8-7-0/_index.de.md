---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.0
type: docs
weight: 240
url: /de/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.3 bis 8.7.0, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für PDF-Optimierung**
Aspose.Cells-APIs bieten bereits die Möglichkeit, Tabellenkalkulationen in PDF umzuwandeln. Mit dieser Version der API können Benutzer nun auch die [Größe des resultierenden PDF optimieren](/cells/de/java/save-excel-into-pdf-with-standard-or-minimum-size/). Aspose.Cells for Java 8.7.0 hat die Eigenschaft PdfSaveOptions.OptimizationType zusammen mit der Aufzählung PdfOptimizationType freigegeben, um den Benutzern die Wahl des gewünschten Optimierungsalgorithmus beim Export von Tabellenkalkulationen in das PDF-Format zu erleichtern. Die Eigenschaft PdfSaveOptions.OptimizationType kann 2 mögliche Werte annehmen, die wie folgt detailliert sind. 

1. PdfOptimizationType.MINIMUM_SIZE: Qualität wird zugunsten der resultierenden Dateigröße beeinträchtigt.
1. PdfOptimizationType.STANDARD: Qualität wird nicht beeinträchtigt, sodass die resultierende Dateigröße groß sein wird.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Erkennung des digital signierten VBA-Projekts**
Die neu freigegebene Eigenschaft VbaProject.isSigned kann verwendet werden, um [zu erkennen, ob das VBA-Projekt in einer Arbeitsmappe digital signiert ist](/cells/de/java/check-if-vba-code-is-signed/). Die Eigenschaft VbaProject.isSigned ist vom Typ Boolean, der true zurückgibt, wenn das VBA-Projekt digital signiert ist, und umgekehrt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Methode Protection.verifyPassword hinzugefügt**
Die Aspose.Cells-APIs haben die Protection-Klasse erweitert, indem sie die Methode verifyPassword eingeführt haben, mit der ein Passwort als Instanz von String angegeben werden kann und [überprüft wird, ob dasselbe Passwort verwendet wurde, um das Arbeitsblatt zu schützen](/cells/de/java/verify-password-used-to-protect-the-worksheet/). Die Methode Protection.verifyPassword gibt true zurück, wenn das angegebene Passwort mit dem zum Schützen des gegebenen Arbeitsblatts verwendeten Passwort übereinstimmt, und false, wenn das angegebene Passwort nicht übereinstimmt. Der folgende Code verwendet die Methode Protection.verifyPassword in Verbindung mit dem Feld Protection.isProtectedWithPassword, um den Passwortschutz zu erkennen und das Passwort zu überprüfen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Eigenschaft Protection.isProtectedWithPassword hinzugefügt**
Diese Version von Aspose.Cells for Java hat auch das Feld Protection.isProtectedWithPassword freigegeben, das [hilfreich sein kann, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht](/cells/de/java/detect-if-worksheet-is-password-protected/).

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Eigenschaft ColorScale.Is3ColorScale hinzugefügt**
Aspose.Cells for Java 8.7.0 hat die Eigenschaft ColorScale.Is3ColorScale freigegeben, die dazu verwendet werden kann, [bedingte 2-Farbskalen zu erstellen](/cells/de/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Die genannte Eigenschaft ist vom Typ Boolean mit einem Standardwert true, was bedeutet, dass das bedingte Format standardmäßig 3-Farbskala sein wird. Wenn jedoch die Eigenschaft ColorScale.Is3ColorScale auf false gesetzt wird, wird ein bedingtes Format mit 2-Farbskala erstellt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügtes TxtLoadOptions.HasFormula-Eigenschaft**
Aspose.Cells for Java 8.7.0 hat Unterstützung zum [Identifizieren und Parsen von Formeln beim Laden von CSV-/TXT-Dateien mit delimiterbasierten einfachen Daten](/cells/de/java/load-or-import-csv-file-with-formulas/) bereitgestellt. Die neu freigegebene TxtLoadOptions.HasFormula-Eigenschaft leitet die API an, beim Festlegen auf true die Formeln aus der Eingabedelimiterdatei zu parsen und sie den relevanten Zellen zuzuweisen, ohne dass weitere Verarbeitung erforderlich ist.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte DataLabels.ResizeShapeToFitText-Eigenschaft**
Eine weitere nützliche Funktion, die Aspose.Cells for Java 8.7.0 freigegeben hat, ist die DataLabels.ResizeShapeToFitText-Eigenschaft, die die Funktion [Form an Text anpassen](/cells/de/java/resize-chart-s-data-label-shape-to-fit-text/) der Excel-Anwendung für die Datenbeschriftungen des Diagramms aktivieren kann.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
## **Entfernte APIs**
### **Entfernte Workbook.SaveOptions-Eigenschaft**
Die Workbook.SaveOptions-Eigenschaft wurde vor einiger Zeit als veraltet markiert. Mit diesem Release wurde sie vollständig aus der öffentlichen API entfernt, daher wird empfohlen, die Workbook.save(Stream, SaveOptions)- oder Workbook.save(string, SaveOptions)-Methode als Alternative zu verwenden.
