---
title: Obtener información de la hoja de trabajo
type: docs
weight: 50
url: /es/net/get-worksheet-information/
---
## **Excel XML abierto**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Archivos de muestra\";

string FileName = FilePath + "Obtener información de la hoja de trabajo.xlsx";

ObtenerInfoHoja(NombreArchivo);

Consola.ReadKey();

}

vacío estático público GetSheetInfo (nombre de archivo de cadena)

{  // Abrir archivo como solo lectura.  usando (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  S sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets; _/  hoja, muestra la información de la hoja.  foreach (Hoja E en hojas)  {  foreach (A attr en hoja.GetAttributes())  {  Console.WriteLine("{0}: {1}" , attr.localName, attr.value); _ x000d_ }  }  }   {{< /highlight >}} ## ** Aspose.Cells ** _ XX Archivos\";  string FileName = FilePath + "Obtener información de la hoja de trabajo.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

vacío estático privado GetSheetInfo (nombre de archivo de cadena)

{  //Crear una instancia de un libro de trabajo object  Workbook workbook = new Workbook(fileName);  //Recorre todas las hojas del libro de trabajo  foreach (Hoja de trabajo en libro de trabajo. Hojas de trabajo)  __x000 y //_x000 // Obtener nombre Índice de Sheet  Console.WriteLine("Nombre de hoja: {0}", Sheet.Name);  Console.WriteLine("Índice de hoja: {0}", Sheet.Index);  //Recorra todos los Properties_X000D_ _X000D_ foreach (CustomProperty Property en Sheet.CustomProperties) _X000D_ _X000D_ {_X000D_ _X000D_ CONSOLE.WriteLine ("{0}: {1}", Property.NAME, Property.Value); _ x000D_ } **Descargar código de muestra** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)