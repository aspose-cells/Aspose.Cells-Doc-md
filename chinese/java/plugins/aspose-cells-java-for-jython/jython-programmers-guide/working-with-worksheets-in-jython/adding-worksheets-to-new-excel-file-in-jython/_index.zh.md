---
title: 在 Jython 中将工作表添加到新的 Excel 文件
type: docs
weight: 10
url: /zh/java/adding-worksheets-to-new-excel-file-in-jython/
---
## **Aspose.Cells - 将工作表添加到新 Excel**
使用附加文档**Aspose.Cells Java 对于 Jython**.在这里您可以看到示例代码。

**Jython代码**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class AddingWorksheetstoNewExcelFile:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'



        workbook = Workbook(dataDir + "Book1.xls")

        #Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        sheetIndex = worksheets.add()

        worksheet = worksheets.get(sheetIndex)

        #Setting the name of the newly added worksheet

        worksheet.setName("My Worksheet")

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Sheet added successfully."

if __name__ == '__main__':        

    AddingWorksheetstoNewExcelFile()

{{< /highlight >}}
## **下载运行代码**
下载**附加文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
