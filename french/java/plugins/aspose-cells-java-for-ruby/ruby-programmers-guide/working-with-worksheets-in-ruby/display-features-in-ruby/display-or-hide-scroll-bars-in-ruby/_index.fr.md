---
title: Afficher ou masquer les barres de défilement en Ruby
type: docs
weight: 30
url: /fr/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Afficher ou Masquer les barres de défilement**
### **Masquer les barres de défilement**
Pour masquer les barres de défilement en utilisant **Aspose.Cells Java pour Ruby**, appelez le module **displayhidescrollbars**.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **Rendre les barres de défilement visibles**
Rendez les barres de défilement visibles en définissant les méthodes **setVerticalScrollBarHidden()** ou **setHorizontalScrollBarHidden()** de la classe **Workbook** à true.

**Code Ruby**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Afficher ou Masquer les barres de défilement (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
