---
title: Copier des lignes et des colonnes en PHP
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns-in-php/
---

## **Aspose.Cells - Copier des lignes et des colonnes**
### **Copier des lignes**
Aspose.Cells propose la méthode copyRow de la classe Cells. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode copyRow prend les paramètres suivants :

- l'objet source Cells,
- l'indice de ligne source, et
- l'indice de ligne de destination.

**Code PHP**

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
### **Copier des colonnes**
Aspose.Cells propose la méthode copyColumn de la classe Cells, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la colonne source à la colonne de destination.

La méthode copyColumn prend les paramètres suivants :

- l'objet source Cells,
- indice de la colonne source, et
- indice de la colonne de destination.

**Code PHP**

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
## **Télécharger le code en cours d'exécution**
Télécharger **Copier des lignes et des colonnes (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
