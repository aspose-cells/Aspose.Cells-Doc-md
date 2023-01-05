---
title: Establecer títulos de impresión
type: docs
weight: 30
url: /es/net/set-print-titles/
---
## **Aspose.Cells - Establecer títulos de impresión**
Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de trabajo impresa. Para hacerlo, utilice el[Configuración de página](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)propiedades de clase PrintTitleColumns y PrintTitleRows.

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Establecer títulos de impresión** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Configuración de las opciones de impresión](/cells/es/net/setting-print-options/).

{{% /alert %}}
