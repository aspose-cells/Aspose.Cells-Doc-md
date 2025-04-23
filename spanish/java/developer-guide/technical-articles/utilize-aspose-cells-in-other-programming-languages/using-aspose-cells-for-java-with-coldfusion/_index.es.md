---
title: Usar Aspose.Cells for Java con ColdFusion
type: docs
weight: 40
url: /es/java/using-aspose-cells-for-java-with-coldfusion/
---

{{% alert color="primary" %}}

Este artículo brinda la información básica y el segmento de código que los desarrolladores de ColdFusion necesitan para usar Aspose.Cells for Java en su aplicación de ColdFusion.

Este artículo muestra cómo crear una página web simple usando ColdFusion y cómo usar Aspose.Cells for Java para generar un archivo Excel simple.

{{% /alert %}}

## **Aspose.Cells: El Producto Real**

Con Aspose.Cells, los desarrolladores pueden exportar datos, formatear hojas de cálculo en cada detalle y a cada nivel, importar imágenes, importar gráficos, crear gráficos, manipular gráficos, transmitir datos de Microsoft Excel, guardar en varios formatos incluyendo XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML (integrado con [Aspose.Pdf](https://products.aspose.com/pdf/java/)) y muchos más.

Para obtener más información sobre el producto, sus características y una guía para programadores, consulte la documentación y las [demostraciones](https://github.com/aspose-cells/Aspose.Cells-for-Java) en línea de Aspose.Cells. Puede [descargarlo](https://downloads.aspose.com/cells/java) y evaluarlo de forma gratuita.

### **Requisitos Previos**

Para usar Aspose.Cells for Java en aplicaciones ColdFusion, copie el archivo Aspose.Cells.jar en la carpeta {CarpetaDeInstalación\\}\wwwroot\WEB-INF\lib.

No olvides reiniciar el servidor de aplicaciones ColdFusion después de colocar nuevos JAR en la carpeta lib.

### **Usar Aspose.Cells for Java y ColdFusion para crear un archivo de Excel**

A continuación, creamos una aplicación simple que genera un archivo vacío de Microsoft Excel, inserta algo de contenido y lo guarda como un archivo XLS.

A continuación se muestra el código real (ColdFusion & Aspose.Cells for Java). Después de ejecutar el código, se genera un archivo de Excel, output.xls.

**Archivo de salida generado: output.xls**

![todo:image_alt_text](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight java >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **Resumen**

{{% alert color="primary" %}}

Este artículo explica cómo usar Aspose.Cells for Java con ColdFusion.

Aspose.Cells ofrece una gran flexibilidad y proporciona una velocidad, eficiencia y fiabilidad excepcionales. Aspose.Cells ha aprovechado años de investigación, diseño y sintonización cuidadosa.

Damos la bienvenida a consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
