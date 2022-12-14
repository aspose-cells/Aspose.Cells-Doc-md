---
title: Arbeitsblätter in Ruby verwalten
type: docs
weight: 10
url: /de/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells – Verwalten von Arbeitsblättern**
### **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**
Um ein Arbeitsblatt zu einer neuen Excel-Datei hinzuzufügen, verwenden Sie**Aspose.Cells Java für Rubin** , einfach anrufen**add_worksheet** Methode von**Arbeitsblätter verwalten** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**
Der Vorgang des Hinzufügens von Arbeitsblättern zu einer Designer-Tabellenkalkulation ist völlig identisch mit dem oben beschriebenen Ansatz, außer dass die Excel-Datei bereits erstellt wurde und wir diese Excel-Datei zuerst öffnen müssen, bevor wir ihr ein Arbeitsblatt hinzufügen.

**Ruby-Code**

{{< highlight "ruby" >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Zugriff auf Arbeitsblätter mit Blattname**
 Um auf das Arbeitsblatt nach Blattname zuzugreifen, verwenden Sie**Aspose.Cells Java für Rubin** , einfach anrufen**get_worksheet** Methode von**Arbeitsblätter verwalten** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**
 So entfernen Sie Arbeitsblätter nach Blattnamen mit**Aspose.Cells Java für Rubin** , einfach anrufen**remove_worksheet_by_name** Methode von**Arbeitsblätter verwalten** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Arbeitsblätter mit Blattindex entfernen**
 Um Arbeitsblatt für Blattindex zu entfernen, verwenden Sie**Aspose.Cells Java für Rubin** , einfach anrufen**remove_worksheet_by_index** Methode von**Arbeitsblätter verwalten** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Arbeitsblätter verwalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
