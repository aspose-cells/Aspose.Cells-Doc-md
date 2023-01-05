---
title: Tabellen zusammenstellen
type: docs
weight: 10
url: /de/net/assemble-spreadsheets/
---
In diesem Abschnitt wird beschrieben, wie Sie:

Erstellen Sie eine neue Excel-Datei von Grund auf neu und fügen Sie ihr ein Arbeitsblatt hinzu.

- Fügen Sie Arbeitsblätter zu Designer-Tabellen hinzu.
- Greifen Sie über den Blattnamen auf Arbeitsblätter zu.
- Entfernen Sie ein Arbeitsblatt aus einer Excel-Datei unter Verwendung seines Blattnamens.
- Entfernen Sie ein Arbeitsblatt aus einer Excel-Datei, indem Sie seinen Blattindex verwenden.
- Aspose.Cells stellt eine Klasse Workbook bereit, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern.
## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**
So erstellen Sie programmgesteuert eine neue Excel-Datei:

- Erstellen Sie ein Objekt der Workbook-Klasse.
- Rufen Sie die Add-Methode der Worksheets-Auflistung auf. Der Excel-Datei * wird automatisch ein leeres Arbeitsblatt hinzugefügt. Es kann darauf verwiesen werden, indem der Blattindex des neuen Arbeitsblatts an die Worksheets-Auflistung übergeben wird.
- Besorgen Sie sich eine Arbeitsblattreferenz.
- Bearbeiten Sie die Arbeitsblätter.
- Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die Save-Methode der Workbook-Klasse aufrufen.

{{< highlight "csharp" >}}

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
## **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**
Der Vorgang zum Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist der gleiche wie beim Hinzufügen eines neuen Arbeitsblatts, mit der Ausnahme, dass die Excel-Datei bereits vorhanden ist und daher geöffnet werden sollte, bevor Arbeitsblätter hinzugefügt werden. Ein Designer-Arbeitsblatt kann von der Workbook-Klasse geöffnet werden.

{{< highlight "csharp" >}}

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
## **Zugriff auf Arbeitsblätter mit Blattname**
Greifen Sie auf ein beliebiges Arbeitsblatt zu oder rufen Sie es ab, indem Sie seinen Namen oder Index angeben.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**
Um Arbeitsblätter aus einer Datei zu entfernen, rufen Sie die RemoveAt-Methode der Worksheets-Auflistung auf. Übergeben Sie den Blattnamen an die RemoveAt-Methode, um ein bestimmtes Arbeitsblatt zu entfernen.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Arbeitsblätter mit Blattindex entfernen**
Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version der RemoveAt-Methode, die den Blattindex des Arbeitsblatts anstelle des Blattnamens übernimmt.

{{< highlight "csharp" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
