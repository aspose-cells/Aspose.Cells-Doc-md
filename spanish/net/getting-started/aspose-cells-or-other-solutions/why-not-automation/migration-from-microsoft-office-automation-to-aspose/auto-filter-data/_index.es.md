---
title: Datos de filtro automático
type: docs
weight: 120
url: /es/net/auto-filter-data/
---
{{% alert color="primary" %}}

Para comprender qué datos se encuentran en un rango, a menudo es más fácil ordenar y filtrar los datos que mirar columnas de datos desordenados. La clasificación organiza los datos en orden ascendente o descendente, lo que facilita la búsqueda de valores específicos. Filtrar los datos le permite mostrar solo ciertos valores. Ayuda a centrarse en elementos particulares en los registros de ventas, por ejemplo.

Los usuarios de Microsoft Excel pueden aplicar filtrado automático a las columnas. El filtrado automático agrega un menú en la parte superior de la columna, desde el cual puede ordenar los datos de la columna de filtrado. Esta característica también está disponible para los desarrolladores que trabajan con hojas de cálculo de Excel, ya sea a través de VSTO o Aspose.Cells for .NET.

{{% /alert %}}

## **Filtrado automático de datos**

Para aplicar el filtrado automático a una columna:

1. Crear un libro de trabajo.
1. Consigue una hoja de trabajo.
1. Agregar datos de muestra.
1. Aplicar filtro automático.
1. Columnas de ajuste automático para que la pantalla sea atractiva.
1. Guarde la hoja de cálculo.

 Los ejemplos de código en este artículo muestran cómo realizar estos pasos usando[VSTO](/cells/es/net/auto-filter-data/) con C# o Visual Basic, o usando[Apose.Cells](/cells/es/net/auto-filter-data/), nuevamente con C# o Visual Basic.

### **Filtrado automático de datos con VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Filtro automático aplicado con VSTO** 

![todo:imagen_alternativa_texto](auto-filter-data_1.png)

### **Filtrado automático de datos con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Autofiltro aplicado con Aspose.Cells for .NET** 

![todo:imagen_alternativa_texto](auto-filter-data_2.png)
