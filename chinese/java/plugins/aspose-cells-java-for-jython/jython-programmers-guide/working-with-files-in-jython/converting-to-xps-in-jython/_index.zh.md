---
title: 在Jython中将文件转换为XPS
type: docs
weight: 30
url: /zh/java/converting-to-xps-in-jython/
---

## **Aspose.Cells - 将文件转换为XPS**
使用**Aspose.Cells Java for Jython**进行文档追加。这里您可以查看示例代码

**Jython代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import ImageFormat;

from com.aspose.cells import ImageOrPrintOptions;

from com.aspose.cells import SheetRender;

from com.aspose.cells import SaveFormat;



class ConvertingToXPS:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToXPS/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Get the first worksheet.

        sheet = workbook.getWorksheets().get(0)

        #Apply different Image and Print options

        options = ImageOrPrintOptions()

        #Set the Format

        options.setSaveFormat(saveFormat.XPS)

        # Render the sheet with respect to specified printing options

        sr = SheetRender(sheet, options)

        sr.toImage(0, dataDir + "out_printingxps.xps")

        #Save the complete Workbook in XPS format

        workbook.save(dataDir + "out_whole_printingxps", saveFormat.XPS)

        # Print message

        print "Excel to XPS conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToXPS()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**追加文档（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToXPS.py)
