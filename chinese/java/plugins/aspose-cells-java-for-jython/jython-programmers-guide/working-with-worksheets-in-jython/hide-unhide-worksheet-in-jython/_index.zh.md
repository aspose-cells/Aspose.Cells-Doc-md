---
title: 在Jython中隐藏或显示工作表
type: docs
weight: 70
url: /zh/java/hide-unhide-worksheet-in-jython/
---

## **Aspose.Cells - 隐藏或显示工作表**
使用**Aspose.Cells Java for Jython**进行文档追加。这里您可以查看示例代码

**Jython代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class HideUnhideWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Hiding the first worksheet of the Excel file

        worksheet.setVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Worksheet 1 is now hidden, please check the output document."

if __name__ == '__main__':        

    HideUnhideWorksheet()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**追加文档（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
