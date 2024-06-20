---
title: Copia de filas y columnas en PHP
type: docs
weight: 30
url: /es/java/copying-rows-and-columns-in-php/
---

## **Aspose.Cells - Copiando Filas y Columnas**
### **Copiando Filas**
Aspose.Cells proporciona el método copyRow de la clase Cells. Este método copia todo tipo de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

El método copyRow toma los siguientes parámetros:

- el objeto Cells de origen,
- el índice de fila de origen, y
- el índice de fila de destino.

**Código PHP**

{{< highlight php >}}

 public static function copy_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the $worksheet->

    $worksheet->getCells()->copyRow($worksheet->getCells(),1,11);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Rows.xls");

    print "Copy Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Copiar columnas**
Aspose.Cells proporciona el método copyColumn de la clase Cells, este método copia todo tipo de datos, incluyendo fórmulas - con referencias actualizadas - y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo, desde la columna de origen a la columna de destino.

El método copyColumn toma los siguientes parámetros:

- el objeto Cells de origen,
- índice de columna de origen, y
- el índice de columna de destino.

**Código PHP**

{{< highlight php >}}

 public static function copy_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook();

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Put some data into header rows (A1:A4)

    $i = 0;

    while($i < 5)

    {

        $worksheet->getCells()->get($i, 0)->setValue("Header Row #$i");

        $i++;

    }


    # Put some detail data (A5:A999)

    $i = 5;

    while ($i < 1000) {

        $worksheet->getCells()->get($i, 0)->setValue("Detail Row #$i");

        $i++;

    }

    # Create another Workbook.

    $workbook1 = new Workbook();

    # Get the first worksheet in the book.

    $worksheet1 = $workbook1->getWorksheets()->get(0);

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    $worksheet1->getCells()->copyColumn($worksheet->getCells(),0,2);

    # Autofit the column.

    $worksheet1->autoFitColumn(2);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Columns.xls");

    print "Copy Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Copiar Filas y Columnas (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
