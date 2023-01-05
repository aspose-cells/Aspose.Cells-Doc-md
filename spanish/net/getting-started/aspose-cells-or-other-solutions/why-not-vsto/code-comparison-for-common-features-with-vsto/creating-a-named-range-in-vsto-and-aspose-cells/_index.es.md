---
title: Creación de un rango con nombre en VSTO y Aspose.Cells
type: docs
weight: 90
url: /es/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Para crear un rango con nombre:

1.  Configure la hoja de trabajo:
 1. Cree una instancia de un objeto de aplicación (solo VSTO).
 1. Agregue un libro de trabajo.
 1. Obtenga la primera hoja.
1.  Crear un rango con nombre:
 1. Defina un rango.
 1. Asigne un nombre al rango.
 1. Guarde el archivo.

Los ejemplos de código a continuación muestran cómo realizar estos pasos usando VSTO con C#. Los ejemplos de código que siguen muestran cómo hacer lo mismo usando Aspose.Cells for .NET, nuevamente con C#.
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

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

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

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

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).Código Postal)
