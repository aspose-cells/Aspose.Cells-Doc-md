---
title: Insérer et Supprimer des lignes et des colonnes en Ruby
type: docs
weight: 60
url: /fr/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Gestion des lignes/colonnes**
### **Insérer une ligne**
Insérer une ligne à n'importe quel emplacement en appelant la méthode insertRows de la collection Cells. La méthode insertRows prend l'index de la ligne où la nouvelle ligne sera insérée en premier argument, et le nombre de lignes à insérer en second argument.

**Code Ruby**

{{< highlight ruby >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Insertion de plusieurs lignes**
Pour insérer plusieurs lignes dans la feuille de calcul, appelez la méthode InsertRows de la collection Cells. La méthode InsertRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, nombre total de lignes à insérer.

**Code Ruby**

{{< highlight ruby >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Suppression d'une ligne**
Pour supprimer une ligne à n'importe quel emplacement, appelez la méthode DeleteRows de la collection Cells. La méthode DeleteRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, nombre total de lignes à supprimer.

**Code Ruby**

{{< highlight ruby >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Suppression de plusieurs lignes**
Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode DeleteRows de la collection Cells. La méthode DeleteRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, nombre total de lignes à supprimer.

**Code Ruby**

{{< highlight ruby >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Insertion d'une colonne**
Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode InsertColumns de la collection Cells. La méthode InsertColumns prend deux paramètres :

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera insérée.
- Nombre de colonnes, nombre total de colonnes à insérer

**Code Ruby**

{{< highlight ruby >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Supprimer une colonne**
Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode deleteColumns de la collection Cells. La méthode deleteColumns prend les paramètres suivants:

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera supprimée.
- Nombre de colonnes, nombre total de colonnes à supprimer.
- Décaler les cellules, paramètre booléen pour indiquer s'il faut décaler les cellules vers la gauche après la suppression.

**Code Ruby**

{{< highlight ruby >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Gestion des lignes/colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
