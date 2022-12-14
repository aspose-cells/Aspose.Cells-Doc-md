---
title: Afficher ou masquer les en-têtes de colonne de ligne dans Ruby
type: docs
weight: 20
url: /fr/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells - Afficher ou masquer les en-têtes de colonne de ligne**
### **Masquer les en-têtes de ligne/colonne**
 Pour masquer les en-têtes de ligne/colonne à l'aide**Aspose.Cells Java pour rubis** , appel**AfficherMasquerRowColumnHeaders** module.

**Code rubis**

{{< highlight "ruby" >}}

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
### **Rendre les en-têtes de ligne/colonne visibles**
Rendez les en-têtes de ligne et de colonne visibles à l'aide de la méthode setRowColumnHeadersVisible(true) de la classe Worksheet.

**Code rubis**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Afficher ou masquer les en-têtes de colonne de ligne (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
