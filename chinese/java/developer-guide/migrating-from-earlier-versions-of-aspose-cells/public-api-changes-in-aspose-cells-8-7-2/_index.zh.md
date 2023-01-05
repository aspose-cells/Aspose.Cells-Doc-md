---
title: 公共 API Aspose.Cells 8.7.2 的变化
type: docs
weight: 260
url: /zh/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.7.1 到 8.7.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **扩展默认计算引擎**
Aspose.Cells API 具有强大的计算引擎，可以计算几乎所有的Microsoft Excel 函数。此外，Aspose.Cells API 现在允许扩展默认计算引擎以满足任何应用程序的自定义计算要求。

Aspose.Cells for Java 8.7.2 版本添加了以下 API。

1. 抽象计算引擎类
1. 计算数据类
1. CalculationOptions.CustomEngine 属性

{{% alert color="primary" %}} 

上述 API 允许更灵活地为所有函数（包括 Excel 的本机函数）实现自定义计算引擎。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[实现自定义计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **为 TextBoxCollection 添加了重载索引器**
Aspose.Cells for Java 8.7.2 公开了 TextBoxCollection 类的重载索引器，以便使用其名称作为 String 访问 TextBox 的实例。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[通过名称访问文本框](/cells/zh/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

简单的使用场景如下。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
