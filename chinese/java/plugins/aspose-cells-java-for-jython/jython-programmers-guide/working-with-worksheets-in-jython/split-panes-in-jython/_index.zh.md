---
title: 在 Jython 中拆分窗格
type: docs
weight: 140
url: /zh/java/split-panes-in-jython/
---

## **Aspose.Cells - 拆分窗格**
使用**Aspose.Cells Java for Jython**进行附加文档。这里可以看到示例代码。

**Jython 代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class SplitPanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SplitPanes/'



        saveFormat = SaveFormat;



        workbook = Workbook(dataDir + "Book1.xls")

        #Set the active cell

        workbook.getWorksheets().get(0).setActiveCell("A20");

        #Split the worksheet window

        workbook.getWorksheets().get(0).split();

        #Save the excel file

        workbook.save(dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

        #Print Message

        print "Panes split successfully."

if __name__ == '__main__':        

    SplitPanes()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Append Documents (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
