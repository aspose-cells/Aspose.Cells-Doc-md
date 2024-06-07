---
title: Aspose.Cells 8.6.1中的公共API更改
type: docs
weight: 200
url: /zh/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

本文描述了Aspose.Cells API从版本8.6.0到8.6.1的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新增和更新的公共方法，添加的类，还描述了Aspose.Cells背后行为的任何变化。

{{% /alert %}} 
## **已添加API**
### **支持HTML链接目标类型**
这个Aspose.Cells for .NET API的版本公开了一个枚举HtmlLinkTargetType，以及一个新属性HtmlSaveOptions.LinkTargetType，共同允许在将电子表格转换为HTML格式时设置链接的目标类型。

1. HtmlLinkTargetType.Blank：在新窗口或选项卡中打开链接的文档/页面。
1. HtmlLinkTargetType.Parent：在父框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Self：在单击链接的相同框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Top：在窗口的整个主体中打开链接的文档/页面。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **添加VbaModuleCollection.Remove方法**
Aspose.Cells for .NET 8.6.1现在公开了另一个VbaModuleCollection.Remove方法的重载，该方法现在可以接受Worksheet实例以删除与指定Worksheet相关联的所有VBA模块。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **添加RangeCollection.Add方法**
Aspose.Cells for .NET 8.6.1已公开了RangeCollection.Add方法，可用于将Range对象添加到特定工作表的范围集合中。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **添加Cell.SetCharacters方法**
Cell.SetCharacters方法可用于更新给定Cell对象的富文本部分。Cell.GetCharacters方法用于访问文本部分，然后可以使用Cell.SetCharacters方法进行修改，**Get**方法返回一个FontSetting对象数组，可用于设置各种属性，如字体名称、字体颜色、粗体等，而**Set**方法可用于应用更改。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **添加VbaProject.IsSigned属性**
Aspose.Cells for .NET 8.6.1公开了VbaProject.IsSigned属性，可用于检查工作簿中的VbaProject是否签名。如果项目已签名，布尔类型属性将返回true。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **修改的API**
### **修改Cell.GetFormatConditions方法**
随着 v8.6.1 的发布，Aspose.Cells for .NET API 修改了 Cell.GetFormatConditions 方法的返回类型，现在返回一个名为 FormatConditionCollection 类型的数组。
## **已废弃的API**
### **已弃用Workbook.CheckWriteProtectedPassword方法**
随着 v8.6.1 的发布，Workbook.CheckWriteProtectedPassword 方法已被标记为过时。建议使用 WorkbookSettings.WriteProtection.ValidatePassword 方法，该方法可以接受一个字符串值作为参数，并在密码与电子表格的预设密码匹配时返回布尔值。
