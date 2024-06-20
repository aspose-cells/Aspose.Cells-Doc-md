---
title: Afficher ou masquer les en têtes de lignes ou colonnes en Ruby
type: docs
weight: 20
url: /fr/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Afficher ou masquer les en-têtes de lignes ou colonnes**
### **Masquer les entêtes de ligne/colonne**
Pour masquer les en-têtes de lignes/colonnes en utilisant **Aspose.Cells Java pour Ruby**, appelez le module **DisplayHideRowColumnHeaders**.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **Rendre les entêtes de ligne/colonne visibles**
Rendez les en-têtes de lignes et de colonnes visibles en utilisant la méthode **setRowColumnHeadersVisible(true)** de la classe **Worksheet**.

**Code Ruby**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Afficher ou masquer les en-têtes de lignes ou colonnes (Aspose.Cells)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
