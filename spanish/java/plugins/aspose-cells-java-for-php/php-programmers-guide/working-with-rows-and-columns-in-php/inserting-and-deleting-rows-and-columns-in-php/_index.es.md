---
title: Insertar y eliminar filas y columnas en PHP
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns-in-php/
---
## **Aspose.Cells - Gestión de filas/columnas**
### **Insertar una fila**
Inserte una fila en cualquier ubicación llamando al método insertRows de la colección Cells. El método insertRows toma el índice de la fila donde se insertará la nueva fila como primer argumento y el número de filas que se insertarán como segundo argumento.

**Código PHP**

{{< highlight "php" >}}

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
### **Insertar varias filas**
Para insertar varias filas en la hoja de cálculo, llame al método insertRows de la colección Cells. El método InsertRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, número total de filas que deben insertarse.

**Código PHP**

{{< highlight "php" >}}

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
### **Eliminación de una fila**
Para eliminar una fila en cualquier ubicación, llame al método deleteRows de la colección Cells. El método DeleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben eliminarse.

**Código PHP**

{{< highlight "php" >}}

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
### **Eliminación de varias filas**
Para eliminar varias filas de una hoja de cálculo, llame al método deleteRows de la colección Cells. El método DeleteRows toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, número total de filas que deben eliminarse.

**Código PHP**

{{< highlight "php" >}}

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
Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al método insertColumns de la colección Cells. El método insertColumns toma dos parámetros:

- Índice de columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, número total de columnas que deben insertarse

**Código PHP**

{{< highlight "php" >}}

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
### **Eliminación de una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método deleteColumns de la colección Cells. El método deleteColumns toma los siguientes parámetros:

- Índice de columna, el índice de la columna desde donde se eliminará la columna.
- Número de columnas, número total de columnas que deben eliminarse.
- Desplazar celdas, parámetro booleano para indicar si se desplazan las celdas a la izquierda después de la eliminación.

**Código PHP**

{{< highlight "php" >}}

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
## **Descargar código de ejecución**
 Descargar**Gestión de filas/columnas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
