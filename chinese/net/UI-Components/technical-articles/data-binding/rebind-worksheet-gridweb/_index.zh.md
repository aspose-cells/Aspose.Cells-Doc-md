---
title: 重新绑定工作表 GridWeb
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb，重新绑定
description: 本文介绍了如何重新绑定GridWeb中的工作表。
---

{{% alert color="primary" %}} 

当您使用IDE中的Worksheets Designer将一个工作表绑定到数据集时，在APSX文件中将创建一个工作表标记。它可能看起来像这样： 

当您调用GridWeb1.DataBind()或WebWorksheet.DataBind()时，工作表将被数据集11中的数据填充。 

有时候您可能希望重新绑定工作表： 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

无论在运行时如何更改工作表的DataSource属性，工作表始终会绑定到数据集11。这是因为工作表始终使用ASPX文件中工作表标记中的数据源绑定信息。要在运行时将工作表绑定到另一个数据源，请删除ASPX文件中工作表标记中的数据源绑定信息。将标记编辑为： 

在调用DataBind方法之前，请指定worksheet.DataSource和worksheet.DataMember属性。 

**C#】

{{< highlight csharp >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WorkSheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WorkSheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WorkSheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WorkSheets(0).DataBind()

End Sub



{{< /highlight >}}

以下代码展示了如何在单元B3中添加一个名为MYTESTFUNC()的自定义函数。然后通过实现GridAbstractCalculationEngine接口来计算此函数的值。我们计算MYTESTFUNC()的方式是将其参数乘以2并返回结果。因此，如果其参数是9，它将返回2*9 = 18。 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

在GridWeb中使用下拉列表、列表、自由列表单元

{{% /alert %}}
