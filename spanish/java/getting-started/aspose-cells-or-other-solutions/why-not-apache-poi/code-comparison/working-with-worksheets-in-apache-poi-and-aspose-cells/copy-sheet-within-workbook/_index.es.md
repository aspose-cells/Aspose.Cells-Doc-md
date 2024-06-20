---
title: Copiar hoja dentro del libro de trabajo
type: docs
weight: 40
url: /es/java/copy-sheet-within-workbook/
---

## **Microsoft Excel: Mover o copiar hojas dentro del libro**
A continuación se presentan los pasos involucrados para copiar y mover hojas de trabajo dentro o entre libros.

1. Para mover o copiar hojas dentro o entre libros, abra el libro que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro Libro, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en **nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla de verificación **Crear una copia**.
## **Aspose.Cells - Copiar hoja dentro del libro**
{{% alert color="primary" %}} 

Aspose.Cells proporciona un método sobrecargado, WorksheetCollection.addCopy(), que se utiliza para agregar una hoja de trabajo a la colección y copiar datos de una hoja de trabajo existente. Una versión del método toma el índice de la hoja de trabajo de origen como parámetro. La otra versión toma el nombre de la hoja de trabajo de origen.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{% /alert %}} 

Copiar hojas usando Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copiar hoja dentro del libro**
{{% alert color="primary" %}} 

Workbook.cloneSheet() se utiliza para copiar hojas dentro del libro.

{{% /alert %}} 

Copiar hojas usando Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Para obtener más detalles, visite [Copiar y mover hojas de cálculo](/cells/es/java/copia-y-movimiento-de-hojas-de-calculo).

{{% /alert %}}
