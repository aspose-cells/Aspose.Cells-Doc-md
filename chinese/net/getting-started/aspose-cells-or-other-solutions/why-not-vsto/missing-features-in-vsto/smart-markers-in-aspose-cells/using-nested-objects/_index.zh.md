---
title: 使用嵌套对象
type: docs
weight: 50
url: /zh/net/using-nested-objects/
---

Aspose.Cells支持智能标记中的嵌套对象，嵌套对象应该是简单的。用户需要为下面的代码定义Individual类。

我们使用一个简单的模板文件。 请参阅包含一些嵌套智能标记的设计电子表格。

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Using Nested Object.xlsx";

//Initialize WorkbookDesigner object

WorkbookDesigner designer = new WorkbookDesigner();

//Load the template file

designer.Workbook = new Workbook(FileName);

//Instantiate the List based on the class

System.Collections.Generic.ICollection<Individual> list = new System.Collections.Generic.List<Individual>();

//Create an object for the Individual class

Individual p1 = new Individual("Damian", 30);

//Create the relevant Wife class for the Individual

p1.Wife = new Wife("Dalya", 28);

//Create another object for the Individual class

Individual p2 = new Individual("Mack", 31);

//Create the relevant Wife class for the Individual

p2.Wife = new Wife("Maaria", 29);

//Add the objects to the list

list.Add(p1);

list.Add(p2);

//Specify the DataSource

designer.SetDataSource("Individual", list);

//Process the markers

designer.Process(false);

//Save the Excel file.

designer.Workbook.Save(FileName);


{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Nested%20Object%20%28Aspose.Cells%29.zip)
