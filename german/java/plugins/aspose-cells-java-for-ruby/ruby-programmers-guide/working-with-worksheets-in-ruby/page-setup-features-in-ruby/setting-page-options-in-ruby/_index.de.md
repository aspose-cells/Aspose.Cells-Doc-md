---
title: Seitenoptionen in Ruby einstellen
type: docs
weight: 10
url: /de/java/setting-page-options-in-ruby/
---

## **Aspose.Cells - Seitenoptionen einstellen**
### **Seitenausrichtung**
Um Seitenausrichtungseinstellungen unter Verwendung von **Aspose.Cells Java für Ruby** anzuwenden, rufen Sie einfach die Methode **page_orientation** des Moduls **pagesetup** auf.

**Ruby-Code**

{{< highlight ruby >}}

 def page_orientation()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait

    page_setup = sheet.getPageSetup()

    page_orientation_type = Rjb::import('com.aspose.cells.PageOrientationType')

    page_setup.setOrientation(page_orientation_type.PORTRAIT)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Page Orientation.xls")

    puts "Set page orientation, please check the output file."

end   

{{< /highlight >}}
### **Maßstab**
Um die Skalierung mit Aspose.Cells Java für Ruby anzuwenden, rufen Sie einfach die Methode scaling des Moduls pagesetup auf.

**Ruby-Code**

{{< highlight ruby >}}

 def scaling()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100

    page_setup = sheet.getPageSetup()

    page_setup.setZoom(100)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Scaling.xls")

    puts "Set scaling, please check the output file."

end


{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Einstellungsoptionen für Seiten (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagesetup.rb)
