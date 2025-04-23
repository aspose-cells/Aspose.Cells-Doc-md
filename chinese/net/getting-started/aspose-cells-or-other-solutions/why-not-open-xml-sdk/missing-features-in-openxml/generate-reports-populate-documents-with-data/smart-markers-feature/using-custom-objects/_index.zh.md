---
title: 在Aspose.Cells中使用匿名类型或自定义对象
type: docs
weight: 30
url: /zh/net/using-anonymous-types-or-custom-objects-in-aspose-cells/
---

Aspose.Cells还支持智能标记中的匿名类型或自定义对象。在下面的示例中，需要在使用之前定义Product类。

{{< highlight csharp >}}

 //Instantiate the workbookdesigner object.

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet(default sheet) in the workbook.

Aspose.Cells.Worksheet w = report.Workbook.Worksheets[0];

//Input some markers to the cells.

w.Cells["A1"].PutValue("Test");

w.Cells["A2"].PutValue("&=MyProduct.Name");

w.Cells["B2"].PutValue("&=MyProduct.Age");

//Instantiate the list collection based on the custom class.

IList<MyProduct> list = new List<MyProduct>();

//Provide values for the markers using the custom class object.

list.Add(new MyProduct("Simon", 30));

list.Add(new MyProduct("Johnson", 33));

//Set the data source.

report.SetDataSource("MyProduct", list);

//Process the markers.

report.Process(false);

//Save the excel file.

report.Workbook.Save("Smart Marker Customobjects.xls");

{{< /highlight >}}
## **下载示例代码**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
