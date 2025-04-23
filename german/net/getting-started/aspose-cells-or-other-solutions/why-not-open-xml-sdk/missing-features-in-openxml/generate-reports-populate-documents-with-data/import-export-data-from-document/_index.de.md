---
title: Importieren und exportieren von Daten aus Dokumenten
type: docs
weight: 10
url: /de/net/import-export-data-from-document/
---

## **Daten aus Dokument importieren**

Daten sind die Sammlung von Rohdaten und wir erstellen Tabellendokumente oder Berichte, um diese Rohdaten auf eine sinnvollere Weise zu präsentieren. Normalerweise fügen wir die Daten selbst zu Tabellenkalkulationen hinzu, aber manchmal müssen wir vorhandene Datendokumente wiederverwenden, und hier entsteht die Notwendigkeit, Daten aus verschiedenen Datenquellen in Tabellendokumente zu importieren. In diesem Thema werden einige Techniken zur Datenimport in Tabellenblätter aus verschiedenen Datenquellen erörtert.

## **Datenimport mit Aspose.Cells**

Wenn Sie **Aspose.Cells** zur Öffnung einer Excel-Datei verwenden, werden alle Daten in der Datei automatisch importiert, aber Aspose.Cells unterstützt auch den Import von Daten aus verschiedenen Datenquellen. Einige dieser Datenquellen sind unten aufgeführt:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells bietet eine Klasse, **Workbook**, die eine Excel-Datei repräsentiert. Die Klasse Workbook enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Tabellenblatt in der Excel-Datei ermöglicht. Ein Tabellenblatt wird durch die Klasse Worksheet repräsentiert. Die Klasse Worksheet bietet eine Cells-Sammlung.

Die Cells-Sammlung bietet sehr nützliche Methoden zum Importieren von Daten aus verschiedenen Datenquellen.

### **Importieren aus einem Arrays**

Entwickler können Daten aus einem Array in ihre Tabellenblätter importieren, indem sie die Methode **ImportArray** der Cells-Sammlung aufrufen. Es gibt viele überladene Versionen der ImportArray Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- Array, repräsentiert das Array-Objekt, dessen Inhalt importiert werden muss
- Zeilennummer, repräsentiert die Zeilennummer der ersten Zelle, in die die Daten importiert werden
- Spaltennummer, repräsentiert die Spaltennummer der ersten Zelle, in die die Daten importiert werden
- Ist vertikal, ein boolescher Wert, der angibt, ob die Daten vertikal oder horizontal importiert werden sollen

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importieren aus einer ArrayList**

Entwickler können Daten aus einem ArrayList in ihre Tabellenblätter importieren, indem sie die **ImportArrayList**-Methode der Cells-Sammlung aufrufen. Die ImportArray Methode nimmt die folgenden Parameter an: **ArrayList** , repräsentiert das ArrayList-Objekt, dessen Inhalt importiert werden muss

- Zeilennummer , repräsentiert die Zeilennummer der ersten Zelle, in die die Daten importiert werden
- Spaltennummer , repräsentiert die Spaltennummer der ersten Zelle, in die die Daten importiert werden
- Ist vertikal , ein boolescher Wert, der angibt, ob die Daten vertikal oder horizontal importiert werden sollen

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Importieren aus benutzerdefinierten Objekten**

Entwickler können Daten aus einer Sammlung von Objekten in ein Tabellenblatt importieren, indem sie **ImportCustomObjects** verwenden. Sie können der Methode eine Liste von Spalten/Eigenschaften bereitstellen, um Ihre gewünschte Liste von Objekten anzuzeigen.

{{< highlight csharp >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **Importieren aus einer DataTable**

Entwickler können Daten aus einem **DataTable** in ihre Tabellenblätter importieren, indem sie die **ImportDataTable**-Methode der Cells-Sammlung aufrufen. Es gibt viele überladene Versionen der **ImportDataTable**-Methode, aber eine typische Überladung nimmt die folgenden Parameter an: **DataTable** , repräsentiert das **DataTable**-Objekt, dessen Inhalt importieren werden soll

- **Wird Feldname angezeigt**, gibt an, ob die Namen der Spalten des DataTable als erste Zeile in das Arbeitsblatt importiert werden sollen oder nicht
- **Startzelle**, repräsentiert den Namen der Startzelle (d.h. "A1"), von der aus die Inhalte des DataTables importiert werden sollen

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Daten aus Dokument exportieren**

Aspose.Cells ermöglicht es nicht nur den Benutzern, Daten aus externen Datenquellen in Tabellenblätter zu importieren, sondern erlaubt es ihnen auch, ihre Tabellenblattdaten in eine **DataTable** zu exportieren. Da **DataTable** ein Teil von ADO.NET ist und zum Halten von Daten verwendet wird. Sobald die Daten in einer **DataTable** gespeichert sind, können sie nach den Anforderungen der Benutzer beliebig verwendet werden.

## **Datenexport nach **DataTable** (.NET) mit Aspose.Cells**

Entwickler können ihre Tabellenblattdaten mühelos in ein DataTable-Objekt exportieren, indem sie entweder die Methode ExportDataTable oder die Methode ExportDataTableAsString der Klasse Cells aufrufen. Beide Methoden werden in verschiedenen Szenarien verwendet, die nachfolgend genauer erläutert werden.

### **Spalten mit stark typisierten Daten**

Wir wissen, dass eine Tabelle Daten als Sequenz von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Tabellenblatts stark typisiert sind (das bedeutet, dass alle Werte in einer Spalte den gleichen Datentyp haben müssen), dann können wir den Inhalt des Tabellenblatts exportieren, indem wir die Methode **ExportDataTable** der Cells-Klasse aufrufen. Die **ExportDataTable**-Methode nimmt die folgenden Parameter an, um die Daten des Tabellenblatts als **DataTable**-Objekt zu exportieren: **Zeilennummer** , repräsentiert die Zeilennummer der ersten Zelle, von der die Daten exportiert werden

- **Spaltennummer** , repräsentiert die Spaltennummer der ersten Zelle, von der die Daten exportiert werden
- **Anzahl der Zeilen** , repräsentiert die Anzahl der zu exportierenden Zeilen
- **Anzahl der Spalten** , repräsentiert die Anzahl der zu exportierenden Spalten
- **Spaltennamen exportieren** , eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Tabellenblatts als Spaltennamen des DataTable exportiert werden sollen oder nicht

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **Spalten mit nicht stark typisierten Daten**

Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (das bedeutet, dass die Werte in einer Spalte verschiedene Datentypen haben können), dann können wir den Arbeitsblattinhalt exportieren, indem wir die Methode **ExportDataTableAsString** der Cells-Klasse aufrufen. Die Methode **ExportDataTableAsString** nimmt denselben Satz von Parametern wie die Methode **ExportDataTable** an, um die Arbeitsblattdaten als **DataTable**-Objekt zu exportieren.

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
