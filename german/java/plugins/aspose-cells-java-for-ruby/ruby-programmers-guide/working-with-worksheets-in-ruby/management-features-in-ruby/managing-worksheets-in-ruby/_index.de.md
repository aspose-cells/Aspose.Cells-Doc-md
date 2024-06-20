---
title: Arbeitsblätter verwalten in Ruby
type: docs
weight: 10
url: /de/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Arbeitsblätter verwalten**
### **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
Um ein Arbeitsblatt zu einer neuen Excel-Datei mit Aspose.Cells Java für Ruby hinzuzufügen, rufen Sie einfach die Methode add_worksheet des Moduls MangingWorksheets auf.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**
Der Prozess zum Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist vollständig identisch mit dem obigen Ansatz, mit der Ausnahme, dass die Excel-Datei bereits erstellt wurde und wir zuerst diese Excel-Datei öffnen müssen, bevor das Arbeitsblatt hinzugefügt wird.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**
Um auf ein Arbeitsblatt nach dem Blattnamen mit Aspose.Cells Java für Ruby zuzugreifen, rufen Sie einfach die Methode get_worksheet des Moduls MangingWorksheets auf.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Arbeitsblätter anhand des Blattnamens entfernen**
Um ein Arbeitsblatt nach dem Blattnamen mit Aspose.Cells Java für Ruby zu entfernen, rufen Sie einfach die Methode remove_worksheet_by_name des Moduls MangingWorksheets auf.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Arbeitsblätter anhand des Blattindex entfernen**
Um ein Arbeitsblatt nach dem Blattindex mit Aspose.Cells Java für Ruby zu entfernen, rufen Sie einfach die Methode remove_worksheet_by_index des Moduls MangingWorksheets auf.

**Ruby-Code**

{{< highlight ruby >}}

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
## **Laufenden Code herunterladen**
Download **Arbeitsblätter verwalten (Aspose.Cells)** von einer der unten genannten sozialen Coding-Seiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
