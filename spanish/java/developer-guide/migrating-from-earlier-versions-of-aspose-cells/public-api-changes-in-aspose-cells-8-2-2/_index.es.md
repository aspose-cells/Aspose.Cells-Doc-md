---
title: Cambios en la API pública en Aspose.Cells 8.2.2
type: docs
weight: 100
url: /es/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.1 hasta la 8.2.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se agregó la propiedad Version para la clase BuiltInDocumentPropertyCollection**
Se ha agregado la nueva propiedad Versión a la clase BuiltInDocumentPropertyCollection para permitir a los desarrolladores obtener o establecer la versión de la aplicación para una hoja de cálculo específica.

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Obtener la Versión de la Aplicación que Creó la Hoja de Cálculo](/cells/es/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Se agregó la propiedad Chart.Worksheet.**
Antes del lanzamiento de Aspose.Cells 8.2.2, no era posible recuperar la instancia de la hoja de cálculo de un objeto Chart que contiene. Aspose.Cells 8.2.2 ha cubierto esta brecha al proporcionar la propiedad Chart.Worksheet.

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado [Obtener la Hoja de Cálculo del Gráfico](/cells/es/java/get-worksheet-of-the-chart/) para obtener más información.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
