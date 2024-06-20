---
title: Masquer ou afficher une feuille de calcul en Ruby
type: docs
weight: 60
url: /fr/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - Masquer ou afficher une feuille de calcul**
### **Masquer une feuille de calcul**
Pour masquer une feuille de calcul en utilisant Aspose.Cells Java pour Ruby, appeler le module hideunhideworksheet.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Affichage d'une feuille de calcul**
Les développeurs peuvent rendre une feuille de calcul visible en définissant la méthode setVisible(true) de la classe Worksheet.

**Code Ruby**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Masquer ou afficher une feuille de calcul (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
