---
title: 在Jython中冻结窗格
type: docs
weight: 60
url: /zh/java/freeze-panes-in-jython/
---

## **Aspose.Cells - 冻结窗格**
使用**Aspose.Cells Java for Jython**进行文档追加。这里您可以查看示例代码

**Jython代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class FreezePanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Applying freeze panes settings

        worksheet.freezePanes(3,2,3,2)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Panes freeze successfull."

if __name__ == '__main__':        

    FreezePanes()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**追加文档（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)
