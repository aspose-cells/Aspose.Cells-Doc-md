---
title: Ocultar y Mostrar Filas y Columnas en PHP
type: docs
weight: 50
url: /es/java/hiding-and-showing-rows-and-columns-in-php/
description: Aprenda cómo ocultar y mostrar filas y columnas a través de las APIs de Aspose.Cells para PHP via Java.
keywords: Cómo Ocultar y Mostrar Filas y Columnas en PHP, Ocultar Filas o Columnas usando PHP, Mostrar Filas o Columnas en PHP. 
---

## **Aspose.Cells para PHP - Controlar la Visibilidad de Filas y Columnas**
### **Cómo Ocultar Filas y Columnas en PHP**
Los desarrolladores pueden ocultar una fila o columna llamando a los métodos HideRow y HideColumn respectivamente de la colección Cells. Ambos métodos toman el índice de la fila/columna como parámetro para ocultar la fila o columna específica.

**Código PHP**

{{< highlight php >}}

 public static function hide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Hiding the 3rd row of the worksheet

    $cells->hideRow(2);

    # Hiding the 2nd column of the worksheet

    $cells->hideColumn(1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Hide Rows And Columns.xls");

    print "Hide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Cómo Mostrar Filas y Columnas usando PHP**
Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos UnhideRow y UnhideColumn respectivamente de la colección Cells. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o ancho de columna asignado a la fila o columna después de que se muestra.

**Código PHP**

{{< highlight php >}}

 public static function unhide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Unhiding the 3rd row and setting its height to 13.5

    $cells->unhideRow(2,13.5);

    # Unhiding the 2nd column and setting its width to 8.5

    $cells->unhideColumn(1,8.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Unhide Rows And Columns.xls");

    print "Unhide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Controlar la Visibilidad de Filas y Columnas (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
