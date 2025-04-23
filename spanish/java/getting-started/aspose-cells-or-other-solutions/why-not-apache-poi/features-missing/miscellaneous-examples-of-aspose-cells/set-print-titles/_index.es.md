---
title: Establecer títulos de impresión
type: docs
weight: 10
url: /es/java/set-print-titles/
---

## **Aspose.Cells - Establecer títulos de impresión**
Aspose.Cells te permite designar encabezados de filas y columnas para que se repitan en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utiliza las propiedades setPrintTitleColumns y setPrintTitleRows de la clase [PageSetup](/java/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Configuración de opciones de impresión](/cells/es/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
