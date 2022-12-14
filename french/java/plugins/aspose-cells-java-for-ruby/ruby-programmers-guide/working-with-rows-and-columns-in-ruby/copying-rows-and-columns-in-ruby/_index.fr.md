---
title: Copier des lignes et des colonnes dans Ruby
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Copier des lignes et des colonnes**
### **Copier des lignes**
Aspose.Cells fournit la méthode copyRow de la classe Cells. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la ligne source vers la ligne de destination.

La méthode copyRow prend les paramètres suivants :

- l'objet source Cells,
- l'index de la ligne source, et
- l'index de la ligne de destination.

**Code rubis**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Copier des colonnes**
Aspose.Cells fournit la méthode copyColumn de la classe Cells, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la colonne source vers la colonne de destination.

La méthode copyColumn prend les paramètres suivants :

- l'objet source Cells,
- index de colonne source, et
- l'index de la colonne de destination.

**Code rubis**

{{< highlight "ruby" >}}

 def copy_columns()

Les données_dir = File.dirname(File.dirname(File.dirname(__DOSSIER__))) + '/données/'



# Instanciation d'un objet Workbook par le chemin du fichier Excel

classeur = Rjb::import('com.aspose.cells.Workbook').new

# Accéder à la première feuille de calcul du fichier Excel

feuille de calcul = classeur.getWorksheets().get(0)

# Mettez des données dans les lignes d'en-tête (A1:A4)

je = 0

 alors que je< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Copie de lignes et de colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
