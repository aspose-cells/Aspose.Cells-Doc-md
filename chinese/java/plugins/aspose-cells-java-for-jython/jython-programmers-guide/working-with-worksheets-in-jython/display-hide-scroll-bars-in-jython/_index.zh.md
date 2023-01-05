---
title: 在 Jython 中显示隐藏滚动条
type: docs
weight: 40
url: /zh/java/display-hide-scroll-bars-in-jython/
---
## **Aspose.Cells - 显示隐藏滚动条**
使用附加文档**Aspose.Cells Java 对于 Jython**.在这里您可以看到示例代码。

**Jython代码**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideScrollBars:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the vertical scroll bar of the Excel file

        workbook.getSettings().setVScrollBarVisible(False)

        #Hiding the horizontal scroll bar of the Excel file

        workbook.getSettings().setHScrollBarVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Scroll bars are now hidden, please check the output document."



if __name__ == '__main__':        

    DisplayHideScrollBars()

{{< /highlight >}}
## **下载运行代码**
下载**附加文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
