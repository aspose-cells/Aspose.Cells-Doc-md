---
title: Aspose.Cells 8.7.2中的公共API更改
type: docs
weight: 260
url: /zh/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.7.1到8.7.2的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新和更新的公共方法、添加和删除的类等，还描述了Aspose.Cells背后的行为中的任何变化。

{{% /alert %}} 
## **添加的 API**
### **扩展了默认计算引擎**
Aspose.Cells API具有强大的计算引擎，可以计算几乎所有的Microsoft Excel函数。此外，Aspose.Cells API现在允许扩展默认计算引擎，以满足任何应用程序的定制计算要求。

随着Aspose.Cells for Java 8.7.2的发布，以下API已添加。

1. AbstractCalculationEngine类
1. CalculationData类
1. CalculationOptions.CustomEngine属性

{{% alert color="primary" %}} 

上述API允许为所有函数（包括Excel的原生函数）实现自定义计算引擎，具有更多的灵活性。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关[实现自定义计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **为TextBoxCollection添加了重载的索引器**
Aspose.Cells for Java 8.7.2已公开了TextBoxCollection类的重载索引器，以便使用它的名称作为String来访问TextBox的实例。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关[通过名称访问TextBox](/cells/zh/java/access-the-text-box-by-the-name/)的详细文章。

{{% /alert %}} 

简单的使用场景如下。 

**Java**

{{< highlight csharp >}}

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
