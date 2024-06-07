---
title: 在Jython中将文件转换为MHTML
type: docs
weight: 20
url: /zh/java/converting-to-mhtml-files-in-jython/
---

## **Aspose.Cells - 将文件转换为MHTML**
使用**Aspose.Cells Java for Jython**进行文档追加。这里您可以查看示例代码

**Jython代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import HtmlSaveOptions

from com.aspose.cells import SaveFormat


class ConvertingToMhtmlFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'



        saveFormat = SaveFormat

        #Specify the file path

        filePath = dataDir + "Book1.xlsx"

        #Specify the HTML saving options

        sv = HtmlSaveOptions(saveFormat.M_HTML)

        #Instantiate a workbook and open the template XLSX file

        wb = Workbook(filePath)

        #Save the MHT file

        wb.save(filePath + ".out.mht", sv)

        # Print message

        print "Excel to MHTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToMhtmlFiles()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**追加文档（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
