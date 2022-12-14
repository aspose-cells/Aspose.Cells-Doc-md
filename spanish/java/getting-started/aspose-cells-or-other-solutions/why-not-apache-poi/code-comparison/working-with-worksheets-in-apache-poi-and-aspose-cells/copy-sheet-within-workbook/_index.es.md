---
title: Copiar hoja dentro del libro
type: docs
weight: 40
url: /es/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - Mover o copiar hojas dentro del libro**
Los siguientes son los pasos necesarios para copiar y mover hojas de trabajo dentro o entre libros de trabajo.

1. Para mover o copiar hojas dentro o entre libros de trabajo, abra el libro de trabajo que recibirá las hojas.
1. Cambie al libro de trabajo que contiene las hojas que desea mover o copiar y luego seleccione las hojas.
1.  Sobre el**Editar** menú, haga clic**Mover o copiar hoja**.
1. En el cuadro Para reservar, haga clic en el libro de trabajo para recibir las hojas.
1.  Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en**Nuevo libro**.
1.  En el**antes de la hoja** cuadro, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1.  Para copiar las hojas en lugar de moverlas, seleccione la**crear una copia** casilla de verificación
## **Aspose.Cells - Copiar hoja dentro del libro de trabajo**
{{% alert color="primary" %}} 

Aspose.Cells proporciona un método sobrecargado, WorksheetCollection.addCopy(), que se usa para agregar una hoja de trabajo a la colección y copiar datos de una hoja de trabajo existente. Una versión del método toma el índice de la hoja de cálculo de origen como parámetro. La otra versión toma el nombre de la hoja de trabajo de origen.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro de trabajo.

{{% /alert %}} 

Copie hojas usando Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copiar hoja dentro del libro de trabajo**
{{% alert color="primary" %}} 

Workbook.cloneSheet() se usa para copiar hojas con el libro de trabajo.

{{% /alert %}} 

Copie hojas usando Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Para más detalles, visite[Copiar y mover hojas de trabajo](/cells/es/java/copying-and-moving-worksheets).

{{% /alert %}}
