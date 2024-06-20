---
title: Cambios en la API pública en Aspose.Cells 8.2.2
type: docs
weight: 90
url: /es/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.1 hasta la 8.2.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se agregó la propiedad BuiltInDocumentPropertyCollection.Version**
Se ha agregado la nueva propiedad Version a la clase BuiltInDocumentPropertyCollection para permitir a los desarrolladores recuperar la versión de la aplicación que creó una determinada hoja de cálculo.

{{% alert color="primary" %}} 

Consulte el artículo detallado [Obtener la Versión de la Aplicación que Creó la Hoja de Cálculo](/cells/es/net/get-the-version-number-of-the-application-that-created-the-excel-document/) para obtener más información.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Se agregó la propiedad Chart.Worksheet.**
Antes del lanzamiento de Aspose.Cells 8.2.2, no era posible recuperar la instancia de Worksheet de un objeto Chart. Aspose.Cells 8.2.2 ha llenado este vacío proporcionando la propiedad Chart.Worksheet.

{{% alert color="primary" %}} 

Consulte el artículo detallado [Obtener la Hoja de Cálculo del Gráfico](/cells/es/net/get-worksheet-of-the-chart/) para obtener más información.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
