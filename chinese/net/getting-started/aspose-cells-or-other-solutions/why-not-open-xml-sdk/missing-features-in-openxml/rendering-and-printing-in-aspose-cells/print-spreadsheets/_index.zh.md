---
title: 打印电子表格
type: docs
weight: 20
url: /zh/net/print-spreadsheets/
---
页面设置设置还提供了多个打印选项（也称为工作表选项），允许用户控制工作表的打印页面。这些打印选项允许用户：

- 选择工作表的特定打印区域
- 打印标题
- 打印网格线
- 打印行/列标题
- 达到草稿质量
- 打印评论
- 打印 Cell 错误
- 定义页面排序
  **设置打印/工作表选项**

Aspose.Cells 支持所有这些打印选项，开发人员可以使用 PageSetup 类提供的几个属性轻松地为他们想要的工作表配置这些选项。下面将更详细地讨论 PageSetup 类的这些属性的用法。
## **设置打印区域**
默认情况下，仅选择包含工作表整个区域的打印区域，其中包含数据，但开发人员也可以根据需要建立工作表的特定打印区域。

要选择特定的打印区域，开发人员可以使用 set**打印区域**的方法**页面设置**班级。您可以将打印区域的单元格范围作为参数提供给此方法。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **设置打印标题**
 Aspose.Cells 允许您指定要在打印工作表的所有页面上重复的行和列标题。为此，开发人员可以使用 set**打印标题列**和**设置打印标题行**的方法**页面设置**班级。

行或列（将在打印工作表的所有页面上重复）通过传递它们的行号或列号来定义。例如，行定义为 \$1:\$2，列定义为 \$A:\$B。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **设置其他打印选项**
**页面设置**类还提供了几种其他方法来设置常规打印选项，如下所示：

- **setPrintGridline 的方法** 一个布尔参数被传递给这个定义是否打印网格线的方法
- **setPrintHeadings 方法** 一个布尔参数被传递给这个定义是否打印行和列标题的方法
- **setBlackAndWhite 方法** 一个布尔参数被传递给这个定义是否以黑白模式打印工作表的方法
- **setPrintComments 方法** 定义是否在工作表上或工作表末尾显示打印注释
- **setPrintDraft 方法**，一个布尔参数被传递给这个方法，定义是否以草稿质量打印工作表
- **setPrintErrors 方法** 定义是否将单元格错误打印为显示、空白、破折号或 N/A

使用集合**打印评论**并设置**打印错误**方法，Aspose.Cells 还提供了两个枚举，PrintCommentsType 和 PrintErrorsType，它们包含要传递给参数的预定义值，以分别设置 PrintComments 和 PrintErrors 方法。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **设置页面顺序**
**页面设置**类提供 set Order 方法，用于订购要打印的工作表的多页。页面排序有两种可能性，如下所示：

Down then over 因此它会在向右打印页面之前向下打印所有页面
越过然后向下因此它会在打印下面的页面之前从左到右打印页面
Aspose.Cells 提供了一个枚举 PrintOrderType，其中包含要分配给 setPage Order 方法的所有预定义订单类型。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
