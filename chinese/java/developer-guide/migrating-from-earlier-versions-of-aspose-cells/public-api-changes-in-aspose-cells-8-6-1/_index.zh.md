---
title: Aspose.Cells 8.6.1中的公共API更改
type: docs
weight: 210
url: /zh/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

本文描述了Aspose.Cells API从版本8.6.0到8.6.1的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新增和更新的公共方法，添加的类，还描述了Aspose.Cells背后行为的任何变化。

{{% /alert %}} 
## **已添加API**
### **支持HTML链接目标类型**
Aspose.Cells for Java API的此版本已公开了一个名为HtmlLinkTargetType的枚举类型以及一个新的属性HtmlSaveOptions.LinkTargetType，两者结合可在电子表格转换为HTML格式时[设置链接的目标类型](/cells/zh/java/change-the-html-link-target-type/)。HtmlLinkTargetType枚举的可能值如下，默认值为SELF。

1. HtmlLinkTargetType.BLANK：在新窗口或选项卡中打开链接的文档/页面。
1. HtmlLinkTargetType.PARENT：在父框架中打开链接的文档/页面。
1. HtmlLinkTargetType.SELF：在单击链接的框架中打开链接的文档/页面。
1. HtmlLinkTargetType.TOP：在窗口的完整主体中打开链接的文档/页面。

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
### **已添加 VbaModuleCollection.remove 方法**
Aspose.Cells for Java 8.6.1已公开VbaModuleCollection.remove方法的另一个重载，现在可以接受Worksheet的实例来删除与指定Worksheet关联的所有VBA模块。

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
### **已添加 RangeCollection.add 方法**
Aspose.Cells for Java 8.6.1已公开RangeCollection.Add方法，可用于向特定工作表的范围集合添加范围对象。

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
### **已添加 Cell.setCharacters 方法**
Cell.setCharacters方法可用于[更新给定Cell对象的富文本的部分](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)。要访问文本的部分，应使用Cell.getCharacters方法，然后可以使用Cell.setCharacters方法进行修订，**get**方法返回一个FontSetting对象的数组，可以操作以设置字体名称，字体颜色，加粗等各种属性 **set**方法可用于应用更改。

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
### **已添加 VbaProject.isSigned 属性**
Aspose.Cells for Java 8.6.1已经公开了VbaProject.isSigned属性，该属性可用于[检测工作簿中的VbaProject是否已签名](/cells/zh/java/check-if-vba-project-in-a-workbook-is-signed/)。Boolean类型属性，如果项目已签名，则返回true。

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
## **修改的API**
### **已修改 Cell.getFormatConditions 方法**
Aspose.Cells for Java API v8.6.1版本已修改了Cell.getFormatConditions方法的返回类型，现在返回一个类型为FormatConditionCollection的数组。
## **已废弃的API**
### **已废弃 Workbook.checkWriteProtectedPassword 方法**
在v8.6.1版本中，作废了Workbook.checkWriteProtectedPassword方法。建议使用WorkbookSettings.WriteProtection.validatePassword方法，该方法接受一个String值作为参数，并返回一个Boolean值，如果密码与电子表格的预设密码匹配，则返回true。
