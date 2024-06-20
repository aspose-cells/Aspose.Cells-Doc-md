---
title: Ajustando la Altura de Fila y el Ancho de Columna en PHP
type: docs
weight: 10
url: /es/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Ajustar altura de fila y ancho de columna**
### **Establecer la altura de la fila**
Es posible establecer la altura de una sola fila llamando al método setRowHeight de la colección Cells. El método setRowHeight toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.
- **Altura de fila**, la altura de fila para aplicar en la fila.

**Código PHP**

{{< highlight php >}}

 public static function set_row_height($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the height of the second row to 13

    $cells->setRowHeight(1, 13);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Row Height.xls");

    print "Set Row Height Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Configurar ancho de columna**
Establezca el ancho de una columna llamando al método setColumnWidth de la colección Cells. El método setColumnWidth toma los siguientes parámetros:

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.
- **Ancho de la columna**, el ancho de columna deseado.

**Código PHP**

{{< highlight php >}}

 public static function set_column_width($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the width of the second column to 17.5

    $cells->setColumnWidth(1, 17.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Column Width.xls");

    print "Set Column Width Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Ajuste de altura de fila y ancho de columna (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
