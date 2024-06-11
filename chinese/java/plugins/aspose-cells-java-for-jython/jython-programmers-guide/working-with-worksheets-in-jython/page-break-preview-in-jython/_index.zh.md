---
title: 在Jython中的页面分页预览
type: docs
weight: 90
url: /zh/java/page-break-preview-in-jython/
---

## **Aspose.Cells - 页面分页预览**
使用**Aspose.Cells Java for Jython**进行附加文档。这里可以看到示例代码。

**Jython 代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class PageBreakPreview:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/PageBreakPreview/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Displaying the worksheet in page break preview

        worksheet.setPageBreakPreview(True)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Page break preview is enabled for sheet 1, please check the output document." 

if __name__ == '__main__':        

    PageBreakPreview()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Append Documents (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/PageBreakPreview.py)
