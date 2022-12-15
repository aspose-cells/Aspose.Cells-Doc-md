---
title: Jython 中的缩放因子
type: docs
weight: 170
url: /zh/java/zoom-factor-in-jython/
---
## **Aspose.Cells - 缩放系数**
使用附加文件**Aspose.Cells Java 对于 Jython**.在这里您可以看到示例代码。

**Jython代码**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ZoomFactor:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ZoomFactor/'



        workbook = Workbook(dataDir + "Book1.xls")

        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Setting the zoom factor of the worksheet to 75

        worksheet.setZoom(75)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Zoom factor set to 75% for sheet 1, please check the output document."

if __name__ == '__main__':        

    ZoomFactor()

{{< /highlight >}}
## **下载运行代码**
下载**附加文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/ZoomFactor.py)
