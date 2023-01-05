---
title: Público API Cambios en Aspose.Cells 8.2.2
type: docs
weight: 90
url: /es/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.2.1 a la 8.2.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Propiedad BuiltInDocumentPropertyCollection.Versión añadida**
La nueva propiedad Version se agregó a la clase BuiltInDocumentPropertyCollection para permitir que los desarrolladores recuperen la versión de la aplicación que creó una hoja de cálculo determinada.

{{% alert color="primary" %}} 

 Por favor revise el artículo detallado[Obtener la versión de la aplicación que creó la hoja de cálculo](/cells/es/net/get-the-version-number-of-the-application-that-created-the-excel-document/) para más información.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Gráfico de propiedad. Hoja de trabajo agregada**
Antes del lanzamiento de Aspose.Cells 8.2.2, no era posible recuperar la instancia de la hoja de trabajo de un objeto de gráfico que contiene. Aspose.Cells 8.2.2 ha llenado este vacío al proporcionar la propiedad Chart.Worksheet.

{{% alert color="primary" %}} 

 Por favor revise el artículo detallado[Obtener hoja de trabajo del gráfico](/cells/es/net/get-worksheet-of-the-chart/) para más información.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
