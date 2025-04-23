---
title: Zusammenstellen von Arbeitsmappen
type: docs
weight: 10
url: /de/net/assemble-spreadsheets/
---

Dieser Abschnitt beschreibt, wie:

Eine neue Excel-Datei erstellen und ein Arbeitsblatt hinzufügen.

Arbeitsblätter zu Designer-Arbeitsmappen hinzufügen.
Auf Arbeitsblätter über den Blattnamen zugreifen.
Ein Arbeitsblatt aus einer Excel-Datei anhand des Blattnamens entfernen.
Ein Arbeitsblatt anhand des Blattindex aus einer Excel-Datei entfernen.
Aspose.Cells bietet eine Klasse, Workbook, die eine Excel-Datei repräsentiert. Die Workbook-Klasse enthält eine Sammlung von Arbeitsblättern, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Arbeitsblattklasse repräsentiert. Die Arbeitsblattklasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern.
## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
Um programmgesteuert eine neue Excel-Datei zu erstellen:

Ein Objekt der Klasse Workbook erstellen.
Die Add-Methode der Arbeitsblattsammlung aufrufen. Ein leeres Arbeitsblatt wird automatisch zur Excel-Datei hinzugefügt und kann durch Übergabe des Blattindex des neuen Arbeitsblatts an die Arbeitsblattsammlung referenziert werden.
Eine Arbeitslblattreferenz abrufen.
Arbeiten an den Arbeitsblättern durchführen.
Die neue Excel-Datei mit neuen Arbeitsmappen durch Aufrufen der Save-Methode der Workbook-Klasse speichern.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**
Der Prozess zum Hinzufügen von Arbeitsblättern zu einer Designer-Arbeitsmappe ist derselbe wie bei einem neuen Arbeitsblatt, außer dass die Excel-Datei bereits existiert und vor dem Hinzufügen von Arbeitsblättern geöffnet werden sollte. Eine Designer-Arbeitsmappe kann durch die Workbook-Klasse geöffnet werden.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**
Zugriff oder Abrufen eines Arbeitsblatts durch Angabe des Namens oder Index.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Arbeitsblätter anhand des Blattnamens entfernen**
Um Arbeitsblätter aus einer Datei zu entfernen, die RemoveAt-Methode der Arbeitsblattsammlung aufrufen. Übergeben Sie den Blattnamen an die RemoveAt-Methode, um ein bestimmtes Arbeitsblatt zu entfernen.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Arbeitsblätter anhand des Blattindex entfernen**
Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn der Name des Arbeitsblatts nicht bekannt ist, verwenden Sie eine überladene Version der RemoveAt-Methode, die den Blattindex des Arbeitsblatts anstelle seines Blattnamens benötigt.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
