---
title: Ajuster automatiquement les lignes et les colonnes en Ruby
type: docs
weight: 20
url: /fr/java/autofit-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Ajuster automatiquement les lignes et les colonnes**
### **Ajuster automatiquement la ligne**
L'approche la plus directe pour ajuster automatiquement la largeur et la hauteur d'une ligne est d'appeler la méthode autoFitRow de la classe Worksheet. La méthode autoFitRow prend un indice de ligne (de la ligne à redimensionner) en tant que paramètre.

**Code Ruby**

{{< highlight ruby >}}

 def autofit_row()

        data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



        # Instantiating a Workbook object by excel file path

        workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet

        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

        # cells (from 1st to 9th column) within the row

        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(data_dir + "Autofit Row.xls")

        puts "Autofit Row Successfully."

    end

{{< /highlight >}}
### **Ajustement automatique de colonne**
La manière la plus simple pour auto-dimensionner la largeur et la hauteur d'une colonne est d'appeler la méthode autoFitColumn de la classe Worksheet. La méthode autoFitColumn prend l'indice de la colonne (de la colonne à redimensionner) en tant que paramètre.

**Code Ruby**

{{< highlight ruby >}}

 def autofit_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Auto-fitting the 4th column of the worksheet

    worksheet.autoFitColumn(3)

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Autofit Column.xls")

    puts "Autofit Column Successfully."

end

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger **Ajustement automatique des lignes et des colonnes (Aspose.Cells)** de n'importe lequel des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
