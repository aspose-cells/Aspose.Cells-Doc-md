---
title: Aspose.Cells 8.6.1中的公共API更改
type: docs
weight: 200
url: /zh/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.6.0到8.6.1的Aspose.Cells API的变化，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增的类，还描述了在Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **支持HTML链接目标类型**
此版本的Aspose.Cells for .NET API已公开了HtmlLinkTargetType枚举和HtmlSaveOptions.LinkTargetType属性，共同允许在将电子表格转换为HTML格式时[设置链接的目标类型](/cells/zh/net/change-the-html-link-target-type/)。HtmlLinkTargetType枚举的可能值如下，其中默认值为Self。

1. HtmlLinkTargetType.Blank：在新窗口或选项卡中打开链接的文档/页面。
1. HtmlLinkTargetType.Parent：在父框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Self：在点击链接的相同框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Top：在窗口的完整主体中打开链接的文档/页面。

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


### **添加了VbaModuleCollection.Remove方法**
Aspose.Cells for .NET 8.6.1已公开了VbaModuleCollection.Remove方法的另一个重载，现在可以接受Worksheet的实例以删除与指定工作表关联的所有VBA模块。

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


### **添加了RangeCollection.Add方法**
Aspose.Cells for .NET 8.6.1已公开了RangeCollection.Add方法，可用于向特定工作表的范围集合中添加Range对象。

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


### **添加了Cell.SetCharacters方法**
Cell.SetCharacters方法可用于更新给定Cell对象的[富文本部分](/cells/zh/net/access-and-update-the-portions-of-rich-text-of-cell/)。使用Cell.GetCharacters方法访问文本部分，然后可以使用Cell.SetCharacters方法进行修改，**Get**方法返回一组FontSetting对象，可以用于设置各种属性，如字体名称、字体颜色、粗细等，**Set**方法可用于应用更改。

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


### **添加了VbaProject.IsSigned属性**
Aspose.Cells for .NET 8.6.1已公开了VbaProject.IsSigned属性，可用于[测试工作簿中的VbaProject是否签名](/cells/zh/net/check-if-vba-project-in-a-workbook-is-signed/)。该布尔类型属性如果项目已签名则返回true。

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
## **修改的 API**
### **修改的Cell.GetFormatConditions方法**
通过v8.6.1的发布，Aspose.Cells for .NET API修改了Cell.GetFormatConditions方法的返回类型，现在返回FormatConditionCollection类型的数组。
## **已弃用的API**
### **弃用的Workbook.CheckWriteProtectedPassword方法**
随着v8.6.1版本的发布，Workbook.CheckWriteProtectedPassword方法已被标记为弃用。建议使用WorkbookSettings.WriteProtection.ValidatePassword方法，它可以接受字符串值作为参数，并在密码匹配电子表格的预设密码时返回布尔值。
{{< app/cells/assistant language="csharp" >}}
