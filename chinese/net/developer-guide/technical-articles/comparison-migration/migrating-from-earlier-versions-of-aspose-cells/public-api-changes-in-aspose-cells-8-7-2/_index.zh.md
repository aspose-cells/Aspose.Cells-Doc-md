---
title: Aspose.Cells 8.7.2中的公共API更改
type: docs
weight: 250
url: /zh/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.7.1到8.7.2的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新和更新的公共方法、添加和删除的类等，还描述了Aspose.Cells背后的行为中的任何变化。

{{% /alert %}} 
## **添加的 API**
### **扩展了默认计算引擎**
Aspose.Cells API具有强大的计算引擎，可以计算几乎所有的Microsoft Excel函数。此外，Aspose.Cells API现在允许扩展默认计算引擎，以满足任何应用程序的定制计算要求。

通过Aspose.Cells for .NET 8.7.2发布了以下API。

1. AbstractCalculationEngine类
1. CalculationData类
1. CalculationOptions.CustomEngine属性

{{% alert color="primary" %}} 

上述API允许为所有函数（包括Excel的原生函数）实现自定义计算引擎，具有更多的灵活性。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [实现自定义计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) 的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **为TextBoxCollection添加了重载的索引器**
Aspose.Cells for .NET 8.7.2已公开了TextBoxCollection类的重载索引，以便使用其名称作为字符串来访问TextBox实例。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [通过名称访问TextBox](/cells/zh/net/access-the-text-box-by-the-name/) 的详细文章。

{{% /alert %}} 

简单的使用场景如下。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **为GridWeb添加了OnAfterColumnFilter事件。**
Aspose.Cells.GridWeb for .NET 8.7.2已经公开了OnAfterColumnFilter事件，该事件用作通过Aspose.Cells.GridWeb UI进行的筛选机制的回调。正如名称所示，该事件在应用列过滤后触发，并可用于获取筛选信息，例如应用筛选的列索引和所选筛选值。

简单的使用场景如下。

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
