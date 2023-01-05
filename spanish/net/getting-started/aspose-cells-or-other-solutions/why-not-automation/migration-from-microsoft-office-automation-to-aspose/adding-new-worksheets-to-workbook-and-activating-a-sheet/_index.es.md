---
title: Agregar nuevas hojas de trabajo al libro de trabajo y activar una hoja
type: docs
weight: 10
url: /es/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

Cuando se trabaja con un archivo de plantilla, a veces es necesario agregar hojas de trabajo adicionales al libro de trabajo para recopilar datos. Las nuevas celdas se llenarán con datos en posiciones y ubicaciones específicas en cada hoja de trabajo.

Del mismo modo, es posible que necesite que una hoja de trabajo específica esté activa y se vea primero cuando se abre el archivo en Microsoft Excel. Una "hoja activa" es la hoja en la que está trabajando en un libro de trabajo. El nombre en la pestaña de la hoja activa está en negrita por defecto.

 Agregar hojas de trabajo y establecer qué hoja está activa son tareas comunes y simples que los desarrolladores deben saber cómo realizar. En este artículo, llevamos a cabo estas tareas utilizando[VSTO](/cells/es/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) y[Aspose.Cells for .NET](/cells/es/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Adición de hojas de cálculo y activación de una hoja**
A los efectos de este consejo de migración:

1. Agregue nuevas hojas de trabajo a un archivo de Excel Microsoft existente.
1. Complete los datos en las celdas de cada nueva hoja de trabajo.
1. Activar una hoja en el libro de trabajo.
1. Guardar como archivo de Excel Microsoft.

continuación, se encuentran fragmentos de código paralelo para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB), que muestran cómo lograr estas tareas.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

usando Microsoft.VisualStudio.Tools.Applications.Runtime;

usando Excel = Microsoft.Office.Interop.Excel;

usando Office = Microsoft.Office.Core;

usando System.Reflection;

.......

//Crea una instancia del objeto Aplicación.

Excel.Aplicación excelApp = new Excel.ApplicationClass();

//Especifique la ruta del archivo de Excel de la plantilla.

string myPath = @"d:\test\My_Book1.xls";

//Abrir el archivo de Excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido);

//Declarar un objeto de hoja de trabajo.

Excel.Hoja de trabajo nuevaHoja de trabajo;

//Agregue 5 nuevas hojas de trabajo al libro de trabajo y complete algunos datos

//a las celdas.

 para (int i = 1; i< 6; i++)

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

usando Aspose.Cells;

.......

//Crear una instancia de licencia y configurar el archivo de licencia

//a traves de su camino

Aspose.Cells.Licencia licencia = nuevo Aspose.Cells.Licencia();

licencia.SetLicense("Aspose.Cells.lic");

//Especifique la ruta del archivo de Excel de la plantilla.

string myPath =@"d:\test\My_Book1.xls";

//Crear una instancia de un nuevo libro de trabajo.

//Abrir el archivo de Excel.

Libro de trabajo libro de trabajo = nuevo libro de trabajo (myPath);

//Declarar un objeto de hoja de trabajo.

Hoja de trabajo nuevaHoja de trabajo;

//Agregue 5 nuevas hojas de trabajo al libro de trabajo y complete algunos datos

//a las celdas.

 para (int i = 0; i< 5; i++)

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
