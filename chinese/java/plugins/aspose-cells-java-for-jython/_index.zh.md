---
title: Aspose.Cells Java 对于 Jython
type: docs
weight: 70
url: /zh/java/aspose-cells-java-for-jython/
---
## **介绍**

### **什么是 Jython？**

Jython 是 Python 的 Java 实现，它结合了表达能力和清晰度。 Jython 可免费用于商业和非商业用途，并随源代码一起分发。 Jython 是 Java 的补充，特别适用于以下任务：

- **嵌入式脚本** Java 程序员可以将 Jython 库添加到他们的系统中，以允许最终用户编写简单或复杂的脚本来为应用程序添加功能。
- **交互式实验** Jython 提供了一个交互式解释器，可用于与 Java 包或运行的 Java 应用程序进行交互。这允许程序员使用 Jython 试验和调试任何 Java 系统。
- **快速应用开发** Python 程序通常比等效的 Java 程序短 2-10 倍。这直接转化为提高程序员的生产力。 Python 和 Java 之间的无缝交互允许开发人员在开发和交付产品期间自由混合两种语言。

### **Aspose.Cells for Java**

Aspose.Cells for Java 是一个高级类库 for Java，使您能够直接在 Java 中执行大量文档处理任务
应用程序。

Aspose.Cells for Java 支持处理 Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF 等所有图片格式。使用 Aspose.Cells 您可以
无需使用 Microsoft Cells 即可生成、修改和转换文档。

### **Aspose.Cells Java 对于 Jython**

Aspose.Cells Java for Jython 是一个演示/提供 Jython 中的 Aspose.Cells for Java API 使用示例的项目。

## **系统要求和支持的平台**

### **系统要求**

**以下是对 Jython 使用 Aspose.Cells Java 的系统要求：**

- Java 1.5以上安装
- 下载 Aspose.Cells 组件
- 杰通 2.7.0

### **支持的平台**

**以下是支持的平台：**

- Aspose.Cells 15.4 及以上。
- Java IDE（Eclipse、NetBeans ...）

## **下载安装及使用**

### **下载中**

**从社交编码网站下载示例**

可以在下面提到的所有社交编码网站上下载以下版本的运行示例：

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**下载Aspose.Cells for Java组件**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **安装中**

- 将下载的 Aspose.Cells for Java jar 文件放入“lib”目录。
- 在 _*init*_.py 文件中将“your-lib”替换为下载的 jar 文件名。

### **使用**

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

## **支持、扩展和贡献**

### **支持**

从 Aspose 成立之初，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，并且了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。凡是使用过我们产品的人，无论是购买过的还是正在评价中的，都值得我们充分的关注和尊重。

您可以使用以下任何平台记录与 Aspose.Cells Java for Jython 相关的任何问题或建议：

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **扩展和贡献**

Jython 的 Aspose.Cells Java 是开源的，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也可以从中受益。

### **源代码**

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
