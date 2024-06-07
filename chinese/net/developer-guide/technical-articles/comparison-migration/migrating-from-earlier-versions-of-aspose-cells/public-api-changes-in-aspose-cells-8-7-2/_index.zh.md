---
title: Aspose.Cells 8.7.2版本的公共API更改
type: docs
weight: 250
url: /zh/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.7.1到8.7.2的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **扩展了默认的计算引擎**
Aspose.Cells API具有强大的计算引擎，可以计算几乎所有Microsoft Excel函数。此外，Aspose.Cells API现在允许扩展默认计算引擎，以满足任何应用程序的自定义计算要求。

通过发布Aspose.Cells for .NET 8.7.2，以下API已被添加。

1. AbstractCalculationEngine类
1. CalculationData类
1. CalculationOptions.CustomEngine属性

{{% alert color="primary" %}} 

上述API允许实现自定义计算引擎，用于所有函数（包括Excel的原生函数），具有更大的灵活性。

{{% /alert %}} {{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于实现自定义计算引擎的详细文章。

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
Aspose.Cells for .NET 8.7.2已暴露了TextBoxCollection类的重载索引器，以便通过其名称作为字符串访问TextBox的实例。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于通过名称访问文本框的详细文章。

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


### **为GridWeb添加了OnAfterColumnFilter事件**
Aspose.Cells.GridWeb for .NET 8.7.2已公开了OnAfterColumnFilter事件，它作为通过Aspose.Cells.GridWeb UI完成的过滤机制的回调。正如名称所示，该事件在应用列过滤后触发，可用于获取上次应用过滤的列索引和选定的过滤器值。

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
