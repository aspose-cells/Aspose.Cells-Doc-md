---
title: 在 Jython 中将工作表转换为 SVG
type: docs
weight: 40
url: /zh/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - 将工作表转换为 SVG**
使用附加文档**Aspose.Cells Java 对于 Jython**.在这里您可以看到示例代码。

**Jython代码**

{{< highlight "java" >}}

从 aspose-cells 导入设置

从 com.aspose.cells 导入工作簿

从 com.aspose.cells 导入 ImageFormat

从 com.aspose.cells 导入 ImageOrPrintOptions

从 com.aspose.cells 导入 SheetRender

从 com.aspose.cells 导入 SaveFormat



类 ConvertingWorksheetToSVG：

定义__在里面__（自己）：

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



保存格式 = 保存格式

工作簿 = 工作簿 (dataDir + "Book1.xls")

 #在单个页面中将每个工作表转换为 svg 格式。

 imgOptions = 图像或打印选项()

 imgOptions.setSaveFormat(保存格式.SVG)

 imgOptions.setOnePagePerSheet(真)

 #将每个工作表转换成svg格式

sheetCount = workbook.getWorksheets().getCount()

 #for(我=0;我<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **下载运行代码**
下载**附加文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
