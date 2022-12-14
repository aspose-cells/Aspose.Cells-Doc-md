---
title: Copiar hojas de trabajo entre libros de trabajo
type: docs
weight: 10
url: /es/net/copy-worksheets-between-workbooks/
---
Aspose.Cells proporciona un método, Aspose.Cells.Worksheet.Copy(), que se usa para copiar datos y formato de una hoja de trabajo de origen a otra hoja de trabajo dentro o entre libros de trabajo. El método toma el objeto de la hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo de un libro de trabajo a otro libro de trabajo.

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Archivos de muestra\";

string FileName = FilePath + "Copiar hoja entre Workbook.xlsx";

//Crear un nuevo libro de trabajo.

Libro de trabajo excelWorkbook0 = nuevo libro de trabajo ();

//Obtener la primera hoja de trabajo del libro.

Hoja de trabajo ws0 = excelWorkbook0.Worksheets[0];

//Pon algunos datos en las filas del encabezado (A1:A4)

 para (int i = 0; i< 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **Descargar código de muestra**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

El siguiente ejemplo muestra cómo copiar una hoja de trabajo de un libro de trabajo a otro libro de trabajo.

{{< highlight "csharp" >}}

 //Crear un nuevo libro de trabajo.

Libro de trabajo excelWorkbook0 = nuevo libro de trabajo ();

//Obtener la primera hoja de trabajo del libro.

Hoja de trabajo ws0 = excelWorkbook0.Worksheets[0];

//Pon algunos datos en las filas del encabezado (A1:A4)

 para (int i = 0; i< 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)
