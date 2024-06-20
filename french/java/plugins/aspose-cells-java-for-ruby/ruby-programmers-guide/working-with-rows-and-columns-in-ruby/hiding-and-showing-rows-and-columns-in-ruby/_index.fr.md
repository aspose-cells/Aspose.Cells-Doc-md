---
title: Masquer et Afficher des lignes et des colonnes en Ruby
type: docs
weight: 50
url: /fr/java/hiding-and-showing-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Contrôle de la visibilité des lignes & colonnes**
### **Masquer les lignes et les colonnes**
Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes HideRow et HideColumn de la collection Cells. Les deux méthodes prennent l'index de la ligne/colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

**Code Ruby**

{{< highlight ruby >}}

 def hide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Hiding the 3rd row of the worksheet

    cells.hideRow(2)

    # Hiding the 2nd column of the worksheet

    cells.hideColumn(1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Hide Rows And Columns.xls")

    puts "Hide Rows And Columns Successfully."

end

{{< /highlight >}}
### **Afficher des lignes et des colonnes**
Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes UnhideRow et UnhideColumn de la collection Cells. Les deux méthodes prennent deux paramètres:

- **Index de la ligne ou colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne attribuée à la ligne ou la colonne après l'avoir affichée.

**Code Ruby**

{{< highlight ruby >}}

 def unhide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Unhiding the 3rd row and setting its height to 13.5

    cells.unhideRow(2,13.5)

    # Unhiding the 2nd column and setting its width to 8.5

    cells.unhideColumn(1,8.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unhide Rows And Columns.xls")

    puts "Unhide Rows And Columns Successfully."

end

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Contrôle de la visibilité des lignes & colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
