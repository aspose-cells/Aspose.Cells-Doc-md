---
title: Afficher ou masquer les onglets dans Ruby
type: docs
weight: 40
url: /fr/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells - Afficher ou masquer les onglets**
### **Masquer les onglets**
 Pour masquer les onglets à l'aide de**Aspose.Cells Java pour rubis** , appel**afficher les onglets masqués** module.

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Rendre les onglets visibles**
Rendez les onglets visibles avec la méthode setSheetTabBarHidden(false) de la classe Workbook.

**Code rubis**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Masquer ou afficher ou masquer les onglets (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
