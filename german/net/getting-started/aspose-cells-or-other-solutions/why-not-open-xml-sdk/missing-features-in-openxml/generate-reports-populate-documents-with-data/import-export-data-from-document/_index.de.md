---
title: Import Daten aus Dokument exportieren
type: docs
weight: 10
url: /de/net/import-export-data-from-document/
---
## **Daten aus Dokument importieren**

Daten sind die Sammlung von Rohdaten, und wir erstellen Tabellendokumente oder Berichte, um diese Rohdaten aussagekräftiger darzustellen. Normalerweise fügen wir Daten selbst zu Tabellenkalkulationen hinzu, aber manchmal müssen wir vorhandene Datenressourcen wiederverwenden, und hier kommt die Notwendigkeit, Daten aus verschiedenen Datenquellen in Tabellenkalkulationen zu importieren. In diesem Thema werden wir einige Techniken zum Importieren von Daten in Arbeitsblätter aus verschiedenen Datenquellen erörtern.

## **Importieren von Daten mit Aspose.Cells**

 Wenn Sie verwenden**Aspose.Cells** Um eine Excel-Datei zu öffnen, werden alle Daten in der Datei automatisch importiert, aber Aspose.Cells unterstützt auch den Import von Daten aus verschiedenen Datenquellen. Einige dieser Datenquellen sind unten aufgeführt:

- **Array**
- **Anordnungsliste**
- **Datentabelle**
- **Datenspalte**
- **Datenansicht**
- **DataGrid**
- **DataReader**
- **Rasteransicht**

 Aspose.Cells bietet eine Klasse,**Arbeitsmappe** die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse repräsentiert. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit.

Cells-Sammlung bietet sehr nützliche Methoden zum Importieren von Daten aus verschiedenen Datenquellen.

### **Import aus Array**

 Entwickler können Daten aus einem Array in ihre Arbeitsblätter importieren, indem sie die aufrufen**ImportArray** Methode der Sammlung Cells. Es gibt viele überladene Versionen der ImportArray-Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- Array stellt das Array-Objekt dar, dessen Inhalt importiert werden muss
- Zeilennummer, stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden
- Spaltennummer, stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden
- Ist Vertical, ein boolescher Wert, der angibt, Daten vertikal oder horizontal zu importieren

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importieren aus ArrayList**

 Entwickler können Daten aus einer ArrayList in ihre Arbeitsblätter importieren, indem sie die aufrufen**ArrayListe importieren** Methode der Sammlung Cells. Die ImportArray-Methode akzeptiert die folgenden Parameter:**Anordnungsliste** , stellt das ArrayList-Objekt dar, dessen Inhalt importiert werden muss

- Zeilennummer stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden
- Spaltennummer stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden
- Is Vertical , ein boolescher Wert, der angibt, dass Daten vertikal oder horizontal importiert werden

{{< highlight "csharp" >}}

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

### **Importieren von benutzerdefinierten Objekten**

 Entwickler können mithilfe von Daten aus einer Sammlung von Objekten in ein Arbeitsblatt importieren**Benutzerdefinierte Objekte importieren**. Sie können der Methode eine Liste von Spalten/Eigenschaften zur Verfügung stellen, um die gewünschte Liste von Objekten anzuzeigen.

{{< highlight "csharp" >}}

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

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

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

### **Importieren aus DataTable**

 Entwickler können Daten aus einer importieren**Datentabelle** zu ihren Arbeitsblättern durch Aufrufen der**Datentabelle importieren** Methode der Sammlung Cells. Es gibt viele überladene Versionen der**Datentabelle importieren** -Methode, aber eine typische Überladung nimmt die folgenden Parameter an:**Datentabelle** , repräsentiert die**Datentabelle** Objekt, dessen Inhalt importiert werden muss

- **Wird der Feldname angezeigt**, gibt an, ob die Namen der Spalten von DataTable als erste Zeile in das Arbeitsblatt importiert werden sollen oder nicht
- **Start Cell** repräsentiert den Namen der Startzelle (dh "A1"), aus der der Inhalt der DataTable importiert werden soll

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Daten aus Dokument exportieren**

 Aspose.Cells erleichtert seinen Benutzern nicht nur den Import von Daten in Arbeitsblätter aus externen Datenquellen, sondern ermöglicht ihnen auch den Export ihrer Arbeitsblattdaten in a**Datentabelle** . Wie wir das kennen**Datentabelle** ist Teil von ADO.NET und dient zum Speichern von Daten. Sobald die Daten in a gespeichert sind**Datentabelle**, es kann auf beliebige Weise gemäß den Anforderungen der Benutzer verwendet werden.

## **Exportieren von Daten in DataTable (.NET) mit Aspose.Cells**

Entwickler können ihre Arbeitsblattdaten einfach in ein DataTable-Objekt exportieren, indem sie entweder die ExportDataTable- oder die ExportDataTableAsString-Methode der Klasse Cells aufrufen. Beide Methoden werden in unterschiedlichen Szenarien verwendet, auf die weiter unten näher eingegangen wird.

### **Spalten mit stark typisierten Daten**

 Wir wissen, dass eine Tabelle Daten als eine Folge von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Arbeitsblatts stark typisiert sind (d. h. alle Werte in einer Spalte müssen denselben Datentyp haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen**ExportDataTable** Methode der Klasse Cells.**ExportDataTable** -Methode verwendet die folgenden Parameter, um Arbeitsblattdaten als zu exportieren**Datentabelle** Objekt:**Zeilennummer** , stellt die Zeilennummer der ersten Zelle dar, aus der die Daten exportiert werden

- **Spaltennummer** , stellt die Spaltennummer der ersten Zelle dar, aus der die Daten exportiert werden
- **Reihenanzahl** , stellt die Anzahl der zu exportierenden Zeilen dar
- **Anzahl der Spalten** stellt die Anzahl der zu exportierenden Spalten dar
- **Spaltennamen exportieren** , eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Arbeitsblatts als Spaltennamen der DataTable exportiert werden sollen oder nicht

{{< highlight "csharp" >}}

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

 Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (d. h. die Werte in einer Spalte können unterschiedliche Datentypen haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen**ExportDataTableAsString** Methode der Klasse Cells.**ExportDataTableAsString** Die Methode verwendet denselben Satz von Parametern wie die von**ExportDataTable** Methode zum Exportieren von Arbeitsblattdaten als**Datentabelle** Objekt.

{{< highlight "csharp" >}}

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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
