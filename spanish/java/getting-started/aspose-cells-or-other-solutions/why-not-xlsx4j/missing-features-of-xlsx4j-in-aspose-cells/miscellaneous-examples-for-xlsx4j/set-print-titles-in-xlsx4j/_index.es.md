---
title: Establecer títulos de impresión en xlsx4j
type: docs
weight: 40
url: /es/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - Establecer títulos de impresión**
Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de trabajo impresa. Para hacerlo, utilice el[Configuración de página](/java/PageSetup)Propiedades class'setPrintTitleColumns y setPrintTitleRows.

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Configuración de las opciones de impresión](/cells/es/java/page-setup-features/#setting-print-options).

{{% /alert %}}
