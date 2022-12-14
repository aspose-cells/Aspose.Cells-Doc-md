---
title: Público API Cambios en Aspose.Cells 8.5.1
type: docs
weight: 170
url: /es/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.0 a la 8.5.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-5-1/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Método Workbook.Dispose Agregado**
El objeto Workbook ahora implementa la interfaz System.IDisposable que tiene un solo método Dispose. Puede llamar directamente al método Workbook.Dispose o crear un objeto Workbook en una estructura Using para llamar a este método automáticamente.

**C#**

{{< highlight "csharp" >}}

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


### **Método Cell.GetHeightOfValue agregado**
 Aspose.Cells for .NET 8.5.1 ha expuesto el método Cell.GetHeightOfValue para obtener la altura del valor de la celda. Al usar este método, puede calcular la altura del valor de la celda y luego establecer la altura de la fila de esa celda respectivamente. Consulte el artículo detallado sobre[cómo calcular la altura y el ancho de la celda](/cells/es/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Tabla de enumeraciónDataSourceType agregado**
Aspose.Cells for .NET 8.5.1 ha expuesto la enumeración Aspose.Cells.Tables.TableDataSourceType para recuperar el tipo de fuente de datos de ListObject. La enumeración TableDataSourceType como los siguientes campos.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Hoja de trabajo
1. TableDataSourceType.XML
### **Propiedad ListObject.DataSourceType agregado**
Con el lanzamiento de v8.5.1, el Aspose.Cells API ha expuesto la propiedad ListObject.DataSourceType de solo lectura que se puede usar para detectar el tipo de fuente de datos de un ListObject.

Este es el escenario de uso más simple.

**C#**

{{< highlight "csharp" >}}

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
