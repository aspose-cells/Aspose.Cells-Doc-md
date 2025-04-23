---
title: Cambios en la API pública en Aspose.Cells 8.5.1
type: docs
weight: 170
url: /es/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.5.0 hasta la 8.5.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, [clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-5-1/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Método Workbook.Dispose añadido**
Ahora el objeto Workbook implementa la interfaz System.IDisposable que tiene un solo método Dispose. Puedes llamar directamente al método Workbook.Dispose o crear un objeto Workbook en una estructura Using para llamar a este método automáticamente.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Se añadió el método Cell.GetHeightOfValue**
Aspose.Cells for .NET 8.5.1 ha expuesto el método Cell.GetHeightOfValue para obtener la altura del valor de la celda. Al usar este método, puedes calcular la altura del valor de la celda y luego ajustar la altura de la fila de esa celda respectivamente. Consulta el artículo detallado sobre [cómo calcular la altura y el ancho de la celda](/cells/es/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Se añadió la enumeración TableDataSourceType**
Aspose.Cells for .NET 8.5.1 ha expuesto la enumeración Aspose.Cells.Tables.TableDataSourceType para recuperar el tipo de origen de datos de un ListObject. La enumeración TableDataSourceType tiene los siguientes campos.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Añadida la propiedad ListObject.DataSourceType**
Con el lanzamiento de v8.5.1, la API de Aspose.Cells ha expuesto la propiedad de solo lectura ListObject.DataSourceType que se puede utilizar para detectar el tipo de fuente de datos de un ListObject.

Aquí se presenta el escenario de uso más simple.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
