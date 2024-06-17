---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /zh/java/aspose-cells-java-for-jython/
---

## **介绍**

### **什么是Jython？**

Jython是Python的Java实现，它将表达力和清晰性相结合。Jython可以免费用于商业和非商业用途，并且可以通过源代码分发。Jython是与Java互补的，特别适用于以下任务：

- **嵌入式脚本** - Java程序员可以将Jython库添加到其系统中，以允许最终用户编写简单或复杂的脚本，为应用程序添加功能。
- **交互式实验** - Jython提供了一个交互式解释器，可以用于与Java包或正在运行的Java应用程序进行交互。这允许程序员使用Jython对任何Java系统进行实验和调试。
- **快速应用程序开发** - Python程序通常比等效的Java程序短2-10倍。这直接转化为增加的程序员生产力。Python和Java之间的无缝交互允许开发人员在开发过程中和产品发布时自由混合这两种语言。

### **Aspose.Cells for Java**

Aspose.Cells for Java是Java的先进类库，使您能够在您的Java应用程序中直接执行广泛的文档处理任务。
应用程序。

Aspose.Cells for Java支持处理单元格（DOC、DOCX、OOXML、RTF）HTML、OpenDocument、PDF、EPUB、XPS、SWF和所有图片格式。通过Aspose.Cells，您可以
**以下是用于Struts 1.3 Web应用程序的Aspose.Cells Java系统要求：**

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jython是一个项目，演示/提供了在Jython中使用Aspose.Cells for Java API的示例。

## **系统要求和支持的平台**

### **系统要求**

以下是使用 Aspose.Cells Java for Jython 的系统要求：

- 已安装 Java 1.5 或更高版本
- 已下载 Aspose.Cells 组件
- Jython 2.7.0

### **支持的平台**

**以下是支持的平台：**

- Aspose.Cells 15.4 及更高版本。
- Java 集成开发环境（Eclipse、NetBeans ...）

## **下载安装和使用**

### **下载**

**从社交编码网站下载示例**

可在以下所有社交编码网站上下载运行示例的发布版本:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

下载Aspose.Cells for Java组件

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **安装**

-将下载的Aspose.Cells for Java jar文件放入"lib"目录。
- 在 _*init*_.py文件中用下载的jar文件名替换"your-lib"。

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

## **支持，扩展和贡献**

### **支持**

从Aspose的最初时期开始，我们就知道仅仅提供给客户优质产品是不够的。我们还需要提供良好的服务。作为开发者，我们深知当技术问题或软件中的瑕疵阻止您完成所需工作时会有多么令人沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了产品还是在评估中使用，都应得到我们的全力关注和尊重。

您可以在以下任一平台上记录与Aspose.Cells Java for Jython相关的任何问题或建议:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **扩展和贡献**

Aspose.Cells Java for Jython是开源的，其源代码可在下面列出的主要社交编码网站上获取。鼓励开发人员下载源代码，通过建议或添加新功能或改进现有功能来贡献，以便他人也能从中受益。

### **源代码**

您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
