---
title: Hinzufügen neuer Arbeitsblätter zur Arbeitsmappe und Aktivieren eines Blatts
type: docs
weight: 10
url: /de/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

Beim Arbeiten mit einer Vorlagendatei müssen manchmal zusätzliche Arbeitsblätter zur Arbeitsmappe hinzugefügt werden, um Daten zu sammeln. Die neuen Zellen werden an bestimmten Positionen und Positionen in jedem Arbeitsblatt mit Daten gefüllt.

Ebenso muss möglicherweise ein bestimmtes Arbeitsblatt aktiv sein und zuerst angezeigt werden, wenn die Datei in Microsoft Excel geöffnet wird. Ein "aktives Blatt" ist das Blatt, an dem Sie in einer Arbeitsmappe arbeiten. Der Name auf der Registerkarte des aktiven Blatts ist standardmäßig fett.

 Das Hinzufügen von Arbeitsblättern und das Festlegen, welches Blatt aktiv ist, sind häufige und einfache Aufgaben, die Entwickler wissen müssen, wie sie auszuführen sind. In diesem Artikel führen wir diese Aufgaben mit aus[VSTO](/cells/de/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) und[Aspose.Cells for .NET](/cells/de/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Arbeitsblätter hinzufügen und ein Blatt aktivieren**
Für die Zwecke dieses Migrationstipps:

1. Fügen Sie neue Arbeitsblätter zu einer bestehenden Microsoft Excel-Datei hinzu.
1. Füllen Sie Daten in die Zellen jedes neuen Arbeitsblatts ein.
1. Aktivieren Sie ein Blatt in der Arbeitsmappe.
1. Als Microsoft Excel-Datei speichern.

Nachfolgend finden Sie parallele Codeausschnitte für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB), die zeigen, wie diese Aufgaben ausgeführt werden.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

mit Microsoft.VisualStudio.Tools.Applications.Runtime;

mit Excel = Microsoft.Office.Interop.Excel;

mit Office = Microsoft.Office.Core;

mit System.Reflection;

.......

//Anwendungsobjekt instanziieren.

Excel.Application excelApp = new Excel.ApplicationClass();

//Geben Sie den Excel-Dateipfad der Vorlage an.

string myPath = @"d:\test\My_Book1.xls";

//Excel-Datei öffnen.

excelApp.Workbooks.Open(myPath, Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert);

//Ein Worksheet-Objekt deklarieren.

Excel.Worksheet newWorksheet;

// Fügen Sie der Arbeitsmappe 5 neue Arbeitsblätter hinzu und füllen Sie einige Daten aus

//in die Zellen.

 für (int i = 1; i< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

mit Aspose.Cells;

.......

//Instanziieren Sie eine Lizenzinstanz und legen Sie die Lizenzdatei fest

//durch seinen Weg

Aspose.Cells.License Lizenz = neu Aspose.Cells.License();

lizenz.SetLicense("Aspose.Cells.lic");

//Geben Sie den Excel-Dateipfad der Vorlage an.

string myPath =@"d:\test\My_Book1.xls";

// Instanziiere eine neue Arbeitsmappe.

//Excel-Datei öffnen.

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe (myPath);

//Ein Worksheet-Objekt deklarieren.

Arbeitsblatt neuesArbeitsblatt;

// Fügen Sie der Arbeitsmappe 5 neue Arbeitsblätter hinzu und füllen Sie einige Daten aus

//in die Zellen.

 für (int i = 0; i< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
