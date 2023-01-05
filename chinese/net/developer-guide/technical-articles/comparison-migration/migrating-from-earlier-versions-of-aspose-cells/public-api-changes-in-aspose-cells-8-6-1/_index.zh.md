---
title: 公共 API Aspose.Cells 8.6.1 的变化
type: docs
weight: 200
url: /zh/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.0 到 8.6.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 HTML 链接目标类型**
此版本的 Aspose.Cells for .NET API 公开了一个枚举，即 HtmlLinkTargetType 以及一个新属性 HtmlSaveOptions.LinkTargetType，它们一起允许[转换为 HTML 格式时设置电子表格中链接的目标类型](/cells/zh/net/change-the-html-link-target-type/)HtmlLinkTargetType 枚举的可能值如下，其中默认值为 Self。

1. HtmlLinkTargetType.Blank：在新窗口或选项卡中打开链接的文档/页面。
1. HtmlLinkTargetType.Parent：在父框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Self：在点击链接的同一框架中打开链接的文档/页面。
1. HtmlLinkTargetType.Top：在整个窗口中打开链接的文档/页面。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **方法 VbaModuleCollection.Remove 添加**
Aspose.Cells for .NET 8.6.1 公开了 VbaModuleCollection.Remove 方法的另一个重载，该方法现在可以接受 Worksheet 的实例以删除与指定 Worksheet 关联的所有 VBA 模块。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **方法 RangeCollection.Add 添加**
Aspose.Cells for .NET 8.6.1 公开了 RangeCollection.Add 方法，可用于将 Range 对象添加到特定工作表的范围集合中。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **添加方法 Cell.SetCharacters**
 Cell.SetCharacters 方法可用于[更新部分富文本](/cells/zh/net/access-and-update-the-portions-of-rich-text-of-cell/)给定的 Cell 对象。 Cell.GetCharacters 方法用于访问文本部分，然后可以使用 Cell.SetCharacters 方法进行修改，而**得到**方法返回一个 FontSetting 对象数组，可以对其进行操作以设置各种属性字体名称、字体颜色、粗体等，以及**放**方法可用于应用更改。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **已添加属性 VbaProject.IsSigned**
 Aspose.Cells for .NET 8.6.1公开了可用于的VbaProject.IsSigned属性[测试工作簿中的 VbaProject 是否已签名](/cells/zh/net/check-if-vba-project-in-a-workbook-is-signed/).如果项目已签名，则布尔类型属性返回 true。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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
## **修改后的 API**
### **方法 Cell.GetFormatConditions 已修改**
随着v8.6.1的发布，Aspose.Cells for .NET API修改了Cell.GetFormatConditions方法的返回类型，现在返回一个FormatConditionCollection类型的数组。
## **过时的 API**
### **方法 Workbook.CheckWriteProtectedPassword 已废弃**
随着 v8.6.1 的发布，Workbook.CheckWriteProtectedPassword 方法已被标记为弃用。建议使用 WorkbookSettings.WriteProtection.ValidatePassword 方法，该方法可以接受字符串值作为参数，如果密码与电子表格的预设密码匹配，则返回布尔值。
