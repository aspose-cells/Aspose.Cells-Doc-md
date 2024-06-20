---
title: Insertar y Eliminar Filas y Columnas en PHP
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns-in-php/
description: Aprenda a insertar y eliminar filas y columnas a través de las API de Aspose.Cells para PHP via Java.
keywords: Cómo insertar y eliminar filas y columnas en PHP, insertar filas y columnas usando PHP, eliminar filas y columnas en PHP, insertar filas o columnas con PHP, eliminar filas y columnas mediante PHP.
---

## **Aspose.Cells - Administración de Filas/Columnas**
### **Insertar una Fila**
Insertar una fila en cualquier ubicación llamando al método insertRows de la colección Cells. El método insertRows toma el índice de la fila donde se insertará la nueva fila como primer argumento, y el número de filas a insertar como segundo argumento.

**Código PHP**

{{< highlight php >}}

 public static function insert_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Row.xls");

    print "Insert Row Successfully." . PHP_EOL;

}  

{{< /highlight >}}
### **Insertar Múltiples Filas**
Para insertar múltiples filas en la hoja de cálculo, llame al método insertRows de la colección Cells. El método insertRows toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, número total de filas que deben ser insertadas.

**Código PHP**

{{< highlight php >}}

 public static function insert_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,10);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Multiple Rows.xls");

    print "Insert Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Eliminar una Fila**
Para eliminar una fila en cualquier ubicación, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código PHP**

{{< highlight php >}}

 public static function delete_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 3rd row from the worksheet

    $worksheet->getCells()->deleteRows(2,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Row.xls");

    print "Delete Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Eliminar Múltiples Filas**
Para eliminar múltiples filas de una hoja de cálculo, llame al método deleteRows de la colección Cells. El método deleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben ser eliminadas.

**Código PHP**

{{< highlight php >}}

 public static function delete_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 10 rows from the worksheet starting from 3rd row

    $worksheet->getCells()->deleteRows(2,10,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Multiple Rows.xls");

    print "Delete Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Insertar una columna**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método insertColumns de la colección Cells. El método insertColumns toma dos parámetros:

- Índice de la columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, el número total de columnas que se deben insertar

**Código PHP**

{{< highlight php >}}

 public static function insert_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a column into the worksheet at 2nd position

    $worksheet->getCells()->insertColumns(1,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Column.xls");

    print "Insert Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método deleteColumns de la colección Cells. El método deleteColumns toma los siguientes parámetros:

- Índice de columna, el índice de la columna desde donde se va a eliminar la columna.
- Número de columnas, el número total de columnas que se deben eliminar.
- Desplazar celdas, parámetro booleano para indicar si se deben desplazar las celdas a la izquierda después de la eliminación.

**Código PHP**

{{< highlight php >}}

 public static function delete_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting a column from the worksheet at 2nd position

    $worksheet->getCells()->deleteColumns(1,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Column.xls");

    print "Delete Column Successfully." . PHP_EOL;

}  

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestión de Filas/Columnas (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
