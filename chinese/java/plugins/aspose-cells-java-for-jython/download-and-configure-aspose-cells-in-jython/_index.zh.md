---
title: 在 Jython 中下载并配置 Aspose.Cells
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-jython/
---
## **下载中**

**从社交编码网站下载示例**

可以在下面提到的所有社交编码网站上下载以下版本的运行示例：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**下载Aspose.Cells for Java组件**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **安装中**

- 将下载的 Aspose.Cells for Java jar 文件放入“lib”目录。
- 在 _*init*_.py 文件中将“your-lib”替换为下载的 jar 文件名。

## **使用**

您可以使用以下示例代码创建 HelloWorld 文档：

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}
