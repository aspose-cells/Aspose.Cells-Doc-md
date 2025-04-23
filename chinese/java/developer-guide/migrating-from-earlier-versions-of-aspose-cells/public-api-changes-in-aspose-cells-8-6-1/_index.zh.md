---
title: Aspose.Cells 8.6.1中的公共API更改
type: docs
weight: 210
url: /zh/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.6.0到8.6.1的Aspose.Cells API的变化，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增的类，还描述了在Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **支持HTML链接目标类型**
Aspose.Cells for Java API的此版本已经暴露出名为HtmlLinkTargetType的枚举，以及一个新的属性HtmlSaveOptions.LinkTargetType，它们共同允许在转换为HTML格式时[设置电子表格中链接的目标类型](/cells/zh/java/change-the-html-link-target-type/)。HtmlLinkTargetType枚举的可能值如下，其中默认值为SELF。

1. HtmlLinkTargetType.BLANK：在新窗口或选项卡中打开链接的文档/页面。
1. HtmlLinkTargetType.PARENT：在父框架中打开链接的文档/页面。
1. HtmlLinkTargetType.SELF：在单击链接的框架中打开链接的文档/页面。
1. HtmlLinkTargetType.TOP：在窗口的整个主体中打开链接的文档/页面。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **添加了 VbaModuleCollection.remove 方法**
Aspose.Cells for Java 8.6.1已经暴露出VbaModuleCollection.remove方法的另一个重载，现在可以接受Worksheet的实例，以删除与指定Worksheet相关联的所有VBA模块。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **添加了 RangeCollection.add 方法**
Aspose.Cells for Java 8.6.1已经暴露出RangeCollection.Add方法，用于向特定工作表的范围集合中添加Range对象。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **添加了 Cell.setCharacters 方法**
Cell.setCharacters 方法可用于更新给定 Cell 对象的[富文本部分](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)。Cell.getCharacters 方法用于访问文本部分，然后可以使用 Cell.setCharacters 方法进行修改，而 **get** 方法返回一个 FontSetting 对象数组，可以对其进行操作以设置各种属性，如字体名称、字体颜色、粗体等，**set** 方法可用于应用更改。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **添加了 VbaProject.isSigned 属性**
Aspose.Cells for Java 8.6.1已经暴露出VbaProject.isSigned属性，用于[测试工作簿中的VbaProject是否已签名](/cells/zh/java/check-if-vba-project-in-a-workbook-is-signed/)。布尔类型属性如果项目已签名，则返回true。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **修改的 API**
### **修改了 Cell.getFormatConditions 方法**
随着v8.6.1的发布，Aspose.Cells for Java API已修改了Cell.getFormatConditions方法的返回类型，现在返回一个FormatConditionCollection类型的数组。
## **已弃用的API**
### **作废了 Workbook.checkWriteProtectedPassword 方法**
随着 v8.6.1 的发布，Workbook.checkWriteProtectedPassword 方法已被标记为已弃用。建议使用 WorkbookSettings.WriteProtection.validatePassword 方法，该方法可以接受一个字符串值作为参数，并返回布尔值，以判断密码是否与电子表格的预设密码匹配。
{{< app/cells/assistant language="java" >}}
