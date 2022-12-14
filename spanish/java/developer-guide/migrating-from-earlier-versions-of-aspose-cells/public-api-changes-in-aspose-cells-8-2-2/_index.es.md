---
title: Público API Cambios en Aspose.Cells 8.2.2
type: docs
weight: 100
url: /es/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.2.1 a la 8.2.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Versión de propiedad agregada para la clase BuiltInDocumentPropertyCollection**
La nueva propiedad Version se agregó a la clase BuiltInDocumentPropertyCollection para permitir a los desarrolladores obtener o establecer la versión de la aplicación para una hoja de cálculo determinada.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Obtener la versión de la aplicación que creó la hoja de cálculo](/cells/es/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Gráfico de propiedad. Hoja de trabajo agregada**
Antes del lanzamiento de Aspose.Cells 8.2.2, no era posible recuperar la instancia de la hoja de trabajo de un objeto de gráfico que contiene. Aspose.Cells 8.2.2 ha llenado este vacío al proporcionar la propiedad Chart.Worksheet.

{{% alert color="primary" %}} 

 Por favor revise el artículo detallado[Obtener hoja de trabajo del gráfico](/cells/es/java/get-worksheet-of-the-chart/) para más información.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
