---
title: Público API Cambios en Aspose.Cells 8.5.1
type: docs
weight: 180
url: /es/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.0 a la 8.5.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-5-1/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Método Workbook.Dispose Agregado**
Aspose.Cells for Java 8.5.1 ha expuesto el método Workbook.dispose para liberar los recursos no administrados del objeto Workbook. El patrón de eliminación se usa solo para objetos que acceden a recursos no administrados, como identificadores de archivos y conductos, identificadores de registro, identificadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de elementos no utilizados es muy eficaz para reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Método Cell.getHeightOfValue añadido**
 Aspose.Cells for Java 8.5.1 ha expuesto el método Cell.getHeightOfValue para obtener la altura del valor de la celda. Al usar este método, puede calcular la altura del valor de la celda y luego establecer la altura de la fila de esa celda respectivamente. Consulte el artículo detallado sobre[cómo calcular la altura y el ancho de la celda](/cells/es/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Tabla de enumeraciónDataSourceType agregado**
Aspose.Cells for Java 8.5.1 ha expuesto la enumeración com.aspose.cells.TableDataSourceType para recuperar el tipo de fuente de datos de ListObject. La enumeración TableDataSourceType como los siguientes campos.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.HOJA DE TRABAJO
1. TableDataSourceType.XML
### **Propiedad ListObject.DataSourceType agregado**
Con el lanzamiento de v8.5.1, el Aspose.Cells API ha expuesto la propiedad ListObject.DataSourceType de solo lectura que se puede usar para detectar el tipo de fuente de datos de un ListObject.

Este es el escenario de uso más simple.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
