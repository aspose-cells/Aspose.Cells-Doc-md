---
title: Afficher ou masquer le quadrillage dans Ruby
type: docs
weight: 10
url: /fr/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells - Afficher ou masquer le quadrillage**
### **Masquer le quadrillage**
 Pour masquer la feuille de calcul à l'aide de**Aspose.Cells Java pour rubis** , appel**affichermasquerleslignesdegrille** module.

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the gridlines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."

{{< /highlight >}}
### **Rendre le quadrillage visible**
Pour rendre le quadrillage visible, utilisez la méthode setGridlinesVisible(true) de la classe Worksheet.

**Code rubis**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Afficher ou masquer le quadrillage (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
