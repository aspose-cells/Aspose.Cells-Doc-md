---
title: Ajuster la hauteur des lignes et la largeur des colonnes en PHP
type: docs
weight: 10
url: /fr/java/adjusting-row-height-and-column-width-in-php/
---
## **Aspose.Cells - Réglage de la hauteur de ligne et de la largeur de colonne**
### **Définition de la hauteur de ligne**
Il est possible de définir la hauteur d'une seule ligne en appelant la méthode setRowHeight de la collection Cells. La méthode setRowHeight prend les paramètres suivants :

- **Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- **Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.

**Code PHP**

{{< highlight "php" >}}

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
### **Définition de la largeur de colonne**
Définissez la largeur d'une colonne en appelant la méthode setColumnWidth de la collection Cells. La méthode setColumnWidth prend les paramètres suivants :

- **Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- **Largeur de colonne**, la largeur de colonne souhaitée.

**Code PHP**

{{< highlight "php" >}}

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
## **Télécharger le code d'exécution**
Télécharger**Réglage de la hauteur des lignes et de la largeur des colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
