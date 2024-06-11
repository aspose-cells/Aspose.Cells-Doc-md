---
title: 在Ruby中管理工作表
type: docs
weight: 10
url: /zh/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - 管理工作表**
### **向新的Excel文件添加工作表**
通过**Aspose.Cells Java for Ruby**的**MangingWorksheets**模块的**add_worksheet**方法向新的Excel文件添加工作表。

**Ruby 代码**

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
### **向设计电子表格添加工作表**
向设计者电子表格添加工作表的过程与上述方法完全相同，除了Excel文件已经创建，我们需要先打开该Excel文件，然后再添加工作表。

**Ruby 代码**

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
### **使用工作表名称访问工作表**
要使用**Aspose.Cells Java for Ruby**通过工作表名称访问工作表，只需调用**MangingWorksheets**模块的**get_worksheet**方法。

**Ruby 代码**

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
### **使用工作表名称移除工作表**
要使用**Aspose.Cells Java for Ruby**通过工作表名称删除工作表，只需调用**MangingWorksheets**模块的**remove_worksheet_by_name**方法。

**Ruby 代码**

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
### **通过页索引删除工作表**
要使用**Aspose.Cells Java for Ruby**通过工作表索引删除工作表，只需调用**MangingWorksheets**模块的**remove_worksheet_by_index**方法。

**Ruby 代码**

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
## **下载运行代码**
从下面提到的任何社交编码网站下载**Managing Worksheets (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
