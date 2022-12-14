---
title: Registerkarten in Ruby anzeigen oder ausblenden
type: docs
weight: 40
url: /de/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells – Registerkarten anzeigen oder ausblenden**
### **Registerkarten ausblenden**
 Tabs ausblenden mit**Aspose.Cells Java für Rubin** , Anruf**Tabs ausblenden** Modul.

**Ruby-Code**

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
### **Registerkarten sichtbar machen**
Machen Sie Registerkarten mit der setSheetTabBarHidden(false)-Methode der Workbook-Klasse sichtbar.

**Ruby-Code**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Registerkarten ausblenden oder anzeigen oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
