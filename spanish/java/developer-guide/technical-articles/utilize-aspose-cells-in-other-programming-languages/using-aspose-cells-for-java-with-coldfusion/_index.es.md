---
title: Usando Aspose.Cells for Java con ColdFusion
type: docs
weight: 40
url: /es/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

Este artículo brinda la información básica y el segmento de código que los desarrolladores de ColdFusion necesitan para usar Aspose.Cells for Java en la aplicación ColdFusion.

Este artículo muestra cómo crear una página web simple usando ColdFusion y usar Aspose.Cells for Java para generar un archivo de Excel simple.

{{% /alert %}}

## **Aspose.Cells: El producto real**

Con Aspose.Cells, los desarrolladores pueden exportar datos, formatear hojas de cálculo con todos los detalles y en todos los niveles, importar imágenes, importar gráficos, crear gráficos, manipular gráficos, transmitir Microsoft datos de Excel, guardar en varios formatos, incluidos XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/java/) integrado) y muchos más.

 Para obtener más información sobre el producto, las funciones y la guía del programador, consulte la documentación Aspose.Cells y las funciones en línea[población](https://github.com/aspose-cells/Aspose.Cells-for-Java) . Usted puede[descargar](https://downloads.aspose.com/cells/java) y evaluarlo gratis.

### **requisitos previos**

Para usar Aspose.Cells for Java en aplicaciones ColdFusion, copie el archivo Aspose.Cells.jar en la carpeta {CarpetaInstalación\\}\wwwroot\WEB-INF\lib.

No olvide reiniciar el servidor de aplicaciones ColdFusion después de colocar nuevos archivos JAR en la carpeta lib.

### **Uso de Aspose.Cells for Java y ColdFusion para crear un archivo de Excel**

A continuación, creamos una aplicación simple que genera un archivo Excel Microsoft vacío, inserta algún contenido y lo guarda como un archivo XLS.

El siguiente es el código real (ColdFusion & Aspose.Cells for Java). Después de ejecutar el código, se genera un archivo de Excel, output.xls.

**Salida generada.xls**

![todo:imagen_alternativa_texto](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

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

Aspose.Cells ofrece una gran flexibilidad y brinda una velocidad, eficiencia y confiabilidad sobresalientes. Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso.

 Agradecemos consultas, comentarios y sugerencias en el[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
