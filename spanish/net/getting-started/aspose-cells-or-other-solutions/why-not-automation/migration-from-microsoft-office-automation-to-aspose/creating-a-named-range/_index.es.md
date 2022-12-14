---
title: Creación de un rango con nombre
type: docs
weight: 70
url: /es/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET permite a los desarrolladores realizar la mayoría de las tareas que los usuarios pueden realizar en Microsoft Excel a través de sus aplicaciones. Este artículo explica cómo aplicar un rango con nombre mediante programación.

Un rango con nombre es una función de Excel que le permite asignar un nombre a una celda o un rango de celdas en una hoja de cálculo de Excel. Luego puede usar el nombre en fórmulas para hacer referencia a la celda (o rango). Los rangos con nombres sensatos hacen que las fórmulas sean más fáciles de entender.

Un rango con nombre tiene que ser único dentro de su alcance, por lo que no use el mismo nombre para varios rangos en una hoja de trabajo. Los nombres de rango descriptivos ayudan a evitar esto: por ejemplo, OrderSubTotal es más descriptivo que SubTotal y también es menos probable que se duplique en una hoja.

{{% /alert %}}

## **Creación de un rango con nombre**

Para crear un rango con nombre:

1. Configure la hoja de trabajo:
 1. Cree una instancia de un objeto de aplicación.
 (Solo VSTO).
 1. Agregue un libro de trabajo.
 1. Obtenga la primera hoja.
1. Crear un rango con nombre:
 1. Defina un rango.
 1. Asigne un nombre al rango.
1. Guarda el archivo.

 Los ejemplos de código a continuación muestran cómo realizar estos pasos usando[VSTO](/cells/es/net/creating-a-named-range/) con C# o Visual Basic. Los ejemplos de código que siguen muestran cómo hacer lo mismo usando[Aspose.Cells for .NET](/cells/es/net/creating-a-named-range/), nuevamente con C# o Visual Basic.
### **Creación de un rango con nombre con VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Crear un rango con nombre con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

usando Aspose.Cells;

.......


// Instanciando un objeto Workbook

Libro de trabajo libro de trabajo = nuevo libro de trabajo ();

//Accediendo a la primera hoja de trabajo en el archivo de Excel

Hoja de trabajo hoja de trabajo = libro de trabajo.Hojas de trabajo[0];

//Creando un rango con nombre

Rango rango = hoja de trabajo.Cells.CreateRange("A1", "B4");

//Establecer el nombre del rango con nombre

rango.Nombre = "Rango_Prueba";

 para (int fila = 0; fila< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
