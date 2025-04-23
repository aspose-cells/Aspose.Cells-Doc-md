---
title: Creando un rango nombrado
type: docs
weight: 70
url: /es/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET permite a los desarrolladores realizar la mayoría de las tareas que los usuarios pueden realizar en Microsoft Excel a través de sus aplicaciones. Este artículo explica cómo aplicar un rango nombrado programáticamente.

Un rango nombrado es una característica de Excel que te permite asignar un nombre a una celda, o a un rango de celdas, en una hoja de cálculo de Excel. Luego puedes usar el nombre en fórmulas para referirte a la celda (o rango). Los rangos con nombres descriptivos hacen que las fórmulas sean más fáciles de entender.

Un rango con nombre debe ser único dentro de su ámbito, por lo que no uses el mismo nombre para varios rangos en una hoja de cálculo. Los nombres de rango descriptivos ayudan a evitar esto: por ejemplo, OrderSubTotal es más descriptivo que SubTotal y también es menos probable que se duplique en una hoja.

{{% /alert %}}

## **Creando un Rango Nombrado**

Para crear un rango con nombre:

1. Configurar la hoja de cálculo:
   1. Instancia un objeto de Aplicación.
      (Solo VSTO.)
   1. Agregar un libro.
   1. Obtener la primera hoja.
1. Crear un rango con nombre:
   1. Definir un rango.
   1. Nombrar el rango.
1. Guarde el archivo.

Los ejemplos de código a continuación muestran cómo realizar estos pasos utilizando [VSTO](/cells/es/net/creating-a-named-range/) ya sea con C# o Visual Basic. Los ejemplos de código que siguen muestran cómo hacer lo mismo utilizando [Aspose.Cells for .NET](/cells/es/net/creating-a-named-range/), nuevamente con C# o Visual Basic.
### **Creando un Rango Nombrado con VSTO**

**C#**

{{< highlight csharp >}}

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

### **Creando un Rango Nombrado con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
