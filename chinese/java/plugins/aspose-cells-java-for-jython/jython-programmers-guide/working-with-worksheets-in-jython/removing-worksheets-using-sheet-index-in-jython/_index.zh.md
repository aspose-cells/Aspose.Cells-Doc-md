---
title: 在Jython中使用工作表索引删除工作表
type: docs
weight: 110
url: /zh/java/removing-worksheets-using-sheet-index-in-jython/
---

## **Aspose.Cells - 使用工作表索引删除工作表**
使用**Aspose.Cells Java for Jython**进行附加文档。这里可以看到示例代码。

**Jython 代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from java.io import FileInputStream;


class RemovingWorksheetsusingSheetIndex:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'



        fstream=FileInputStream(dataDir + "Book1.xls");

        #Instantiating a Workbook object with the stream

        workbook = Workbook(fstream)

        #Removing a worksheet using its sheet index

        workbook.getWorksheets().removeAt(0)

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Closing the file stream to free all resources

        fstream.close()


        #Print Message

        print "Sheet removed successfully."

if __name__ == '__main__':        

    RemovingWorksheetsusingSheetIndex()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Append Documents (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
