---
title: Hantera kalkylblad i Ruby
type: docs
weight: 10
url: /sv/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Hantera kalkylblad**
### **Lägga till kalkylblad i en ny Excelfil**
För att lägga till kalkylblad i en ny Excel-fil med **Aspose.Cells Java för Ruby**, helt enkelt anropa **add_worksheet**-metoden i **MangingWorksheets**-modulen.

**Ruby-kod**

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
### **Lägga till kalkylblad i ett designerkalkylblad**
Processen att lägga till kalkylblad i en designerkalkylblad är helt densamma som i det ovanstående tillvägagångssättet förutom att Excel-filen redan är skapad och vi behöver öppna den Excel-filen först innan vi lägger till kalkylblad i den.

**Ruby-kod**

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
### **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**
För att komma åt kalkylblad med hjälp av bladnamn med **Aspose.Cells Java för Ruby**, helt enkelt anropa **get_worksheet**-metoden i **MangingWorksheets**-modulen.

**Ruby-kod**

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
### **Ta bort kalkylblad med hjälp av kalkylbladsnamn**
För att ta bort kalkylblad med hjälp av bladnamn med **Aspose.Cells Java för Ruby**, helt enkelt anropar **remove_worksheet_by_name**-metoden i **MangingWorksheets**-modulen.

**Ruby-kod**

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
### **Ta bort kalkylblad med hjälp av kalkylbladsindex**
För att ta bort kalkylblad med hjälp av bladindex med **Aspose.Cells Java för Ruby**, helt enkelt anropa **remove_worksheet_by_index**-metoden i **MangingWorksheets**-modulen.

**Ruby-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Hantera kalkylblad (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
