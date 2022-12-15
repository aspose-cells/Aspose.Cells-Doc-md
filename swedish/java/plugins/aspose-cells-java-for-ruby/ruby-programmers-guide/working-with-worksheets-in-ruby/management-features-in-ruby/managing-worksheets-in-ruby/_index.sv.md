---
title: Hantera arbetsblad i Ruby
type: docs
weight: 10
url: /sv/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - Hantera arbetsblad**
### **Lägga till kalkylblad till en ny Excel-fil**
 För att lägga till kalkylblad i en ny Excel-fil med**Aspose.Cells Java för Ruby** , ring helt enkelt**add_worksheet** metod av**Hantera arbetsblad** modul.

**Ruby kod**

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
### **Lägga till kalkylblad till ett designerkalkylblad**
Processen att lägga till kalkylblad till ett designerkalkylblad är helt samma som ovanstående tillvägagångssätt förutom att Excel-filen redan är skapad och vi måste öppna den Excel-filen först innan vi lägger till kalkylblad till den.

**Ruby kod**

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
### **Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn**
 För att komma åt kalkylblad efter arknamn med hjälp av**Aspose.Cells Java för Ruby** , ring helt enkelt**get_worksheet** metod av**Hantera arbetsblad** modul.

**Ruby kod**

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
### **Ta bort kalkylblad med Sheet Name**
 För att ta bort kalkylblad efter arknamn med**Aspose.Cells Java för Ruby** , ring helt enkelt**remove_worksheet_by_name** metod av**Hantera arbetsblad** modul.

**Ruby kod**

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
### **Ta bort kalkylblad med Sheet Index**
 För att ta bort kalkylblad för ark index med**Aspose.Cells Java för Ruby** , ring helt enkelt**remove_worksheet_by_index** metod av**Hantera arbetsblad** modul.

**Ruby kod**

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
## **Ladda ner Running Code**
Ladda ner**Hantera arbetsblad (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
