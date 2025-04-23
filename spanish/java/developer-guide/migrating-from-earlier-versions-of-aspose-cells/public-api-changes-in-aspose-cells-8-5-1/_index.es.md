---
title: Cambios en la API pública en Aspose.Cells 8.5.1
type: docs
weight: 180
url: /es/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.5.0 hasta la 8.5.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, [clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-5-1/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Método Workbook.Dispose añadido**
Aspose.Cells for Java 8.5.1 ha expuesto el método Workbook.dispose para liberar los recursos no administrados del objeto Workbook. El patrón de disposición se usa solo para objetos que acceden a recursos no administrados, como manijas de archivos y tuberías, manijas de registro, manijas de espera o punteros a bloques de memoria no administrados. Esto se debe a que el recolector de basura es muy eficiente al volver a reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Método Cell.getHeightOfValue añadido**
Aspose.Cells for Java 8.5.1 ha expuesto el método Cell.getHeightOfValue para obtener la altura del valor de la celda. Mediante este método, puedes calcular la altura del valor de la celda y luego ajustar la altura de la fila de esa celda respectivamente. Consulta el artículo detallado sobre [cómo calcular la altura y el ancho de la celda](/cells/es/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Añadida la enumeración TableDataSourceType**
Aspose.Cells for Java 8.5.1 ha expuesto la enumeración com.aspose.cells.TableDataSourceType para recuperar el tipo de fuente de datos de un ListObject. La enumeración TableDataSourceType tiene los siguientes campos. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Añadida la propiedad ListObject.DataSourceType**
Con el lanzamiento de v8.5.1, la API de Aspose.Cells ha expuesto la propiedad de solo lectura ListObject.DataSourceType que se puede utilizar para detectar el tipo de fuente de datos de un ListObject.

Aquí se presenta el escenario de uso más simple.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
