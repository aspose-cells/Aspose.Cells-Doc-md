---
title: Öffentlich API Änderungen in Aspose.Cells 16.12.0
type: docs
weight: 370
url: /de/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.11.0 zu 16.12.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Objekte zur Ladezeit filtern**
Aspose.Cells 16.12.0 hat die LoadFilter-Klasse zusammen mit der LoadOptions.LoadFilter-Eigenschaft verfügbar gemacht, die zusammen den zu ladenden Datentyp steuern können, während eine Instanz von Workbook aus einer Vorlagendatei initialisiert wird.

Hier ist ein einfaches Anwendungsszenario, um nur die Dokumenteigenschaften aus einer Vorlagendatei zu laden.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Das folgende Snippet lädt alles aus einer vorhandenen Tabelle mit Ausnahme der Diagramme.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Der folgende Code lädt nur die Zellendaten (zusammen mit Formeln) und die Formatierung aus einer vorhandenen Tabelle.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **FileFormatType.OTS-Enumeration hinzugefügt**
Aspose.Cells 16.12.0 hat den OTS-Eintrag zur FileFormatType-Enumeration hinzugefügt, um das Format von OTS-Dateien zu erkennen.

Das folgende Snippet verwendet FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **BuiltInDocumentPropertyCollection.ScaleCrop-Eigenschaft hinzugefügt**
Aspose.Cells 16.12.0 hat die ScaleCrop-Eigenschaft zur BuiltInDocumentPropertyCollection-Klasse hinzugefügt. ScaleCrop gibt den Anzeigemodus des Dokument-Thumbnails an. Wenn dieses Element auf „true“ gesetzt wird, wird die Miniaturansicht des Dokuments gemäß der Anzeige skaliert, während die Einstellung auf „false“ das Zuschneiden der Miniaturansicht des Dokuments ermöglicht, um den Ausschnitt anzuzeigen, der in die Anzeige passt.
### **BuiltInDocumentPropertyCollection.LinksUpToDate-Eigenschaft hinzugefügt**
 Aspose.Cells 16.12.0 hat auch die LinksUpToDate-Eigenschaft für die BuiltInDocumentPropertyCollection-Klasse verfügbar gemacht. Die Eigenschaft LinksUpToDate gibt an, ob die Hyperlinks in einem Dokument aktuell sind.
### **Workbook.exportXml-Methode hinzugefügt**
Aspose.Cells 16.12.0 hat die Workbook.exportXml-Methode verfügbar gemacht, die es ermöglicht, die XML-Zuordnungsdaten im angegebenen Dateipfad zu speichern. Die Workbook.exportXml-Methode akzeptiert 2 Parameter, wobei der erste Parameter vom Typ Zeichenfolge der Name der XML-Zuordnung und der zweite Parameter der Dateipfad zum Speichern der XML-Daten sein sollte.
### **WorksheetCollection.createRange-Methode hinzugefügt**
Aspose.Cells 16.12.0 hat die WorksheetCollection.createRange-Methode hinzugefügt, die es ermöglicht, einen Bereich basierend auf einer Adresse (Zellbereichsreferenz) und einem Arbeitsblattindex zu erstellen.

Der folgende Codeausschnitt verwendet die WorksheetCollection.createRange-Methode, um einen Zellbereich zu erstellen, der sich über A1 bis A2 im ersten (Standard-)Arbeitsblatt erstreckt.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete LoadOptions.LoadDataOptions-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.LoadDataFilterOptions-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.OnlyLoadDocumentProperties-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.LoadDataAndFormatting-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft LoadOptions.LoadFilter.

{{% alert color="primary" %}} 

Codeausschnitte für alle veralteten APIs wurden oben geteilt.

{{% /alert %}}
## **Gelöschte APIs**
### **Gelöschte DataLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die DataLabels.RotationAngle-Eigenschaft.
### **Gelöschte Title.Rotation-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft Title.RotationAngle.
### **Gelöschte DataLabels.Background-Eigenschaft**
Es wird empfohlen, stattdessen die DataLabels.BackgroundMode-Eigenschaft zu verwenden.
### **DisplayUnitLabel.Rotation-Eigenschaft gelöscht**
Bitte erwägen Sie die Verwendung der DisplayUnitLabel.RotationAngle-Eigenschaft, um dasselbe Ziel zu erreichen.
### **Title.getCharacters-Methode gelöscht**
Bitte verwenden Sie stattdessen die Title.characters-Methode.
