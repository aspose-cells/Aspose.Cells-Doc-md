---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /zh/java/aspose-cells-java-for-jython/
---

## **介绍**

### **什么是Jython?**

Jython是Python的Java实现，它结合了表现力和清晰度。Jython可供商业和非商业用途免费使用，并附带源代码。Jython对Java具有补充作用，特别适用于以下任务:

- **嵌入式脚本** - Java程序员可以将Jython库添加到系统中，以允许最终用户编写简单或复杂的脚本，以增加应用程序的功能。
- **交互式实验** - Jython提供了一个交互式解释器，可用于与Java包或正在运行的Java应用程序交互。这使得程序员可以使用Jython实验和调试任何Java系统。
- **快速应用开发** - Python程序通常比等效的Java程序短2-10倍。这直接转化为增加的程序员生产率。Python和Java之间的无缝交互允许开发人员在开发和发布产品时自由地混合这两种语言。

### **Java的Aspose.Cells**

Java的Aspose.Cells是一个先进的Java类库，让您可以直接在Java中执行各种文档处理任务
应用程序。

Java的Aspose.Cells支持处理单元格（DOC，DOCX，OOXML，RTF）HTML，OpenDocument，PDF，EPUB，XPS，SWF和所有图像格式。使用Aspose.Cells，您可以
生成、修改和转换文档，而无需使用Microsoft Cells。

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jython是一个项目，它演示/提供了在Jython中使用Aspose.Cells for Java API的示例。

## **系统要求和支持的平台**

### **系统要求**

**以下是使用Aspose.Cells Java for Jython的系统要求:**

- 已安装Java 1.5或更高版本
- 下载Aspose.Cells组件
- Jython 2.7.0

### **支持的平台**

**以下是支持的平台:**

- Aspose.Cells 15.4及以上版本。
- Java集成开发环境（Eclipse, NetBeans ...）

## **下载安装和使用**

### **下载中**

**从社交编码网站下载示例代码**

以下运行示例的发行版可在以下所有社交编码站点上下载:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**下载Aspose.Cells for Java组件**

- [Java的Aspose.Cells](https://releases.aspose.com/cells/java/)

### **安装**

- 将下载的Aspose.Cells for Java jar文件放入"lib"目录。
- 在_init_.py文件中用下载的jar文件名替换"your-lib"。

### **使用**

您可以使用以下示例代码创建HelloWorld文档:

{{< highlight java >}}

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

自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以在以下任一平台上记录与Aspose.Cells Java for Jython相关的任何问题或建议:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **扩展和贡献**

Aspose.Cells Java for Jython是开源的，其源代码可在下面列出的主要社交编码网站上获取。鼓励开发人员下载源代码，通过建议或添加新功能或改进现有功能来做贡献，以便他人也能从中受益。

### **源代码**

您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
