---
title: 打印电子表格
type: docs
weight: 20
url: /zh/net/print-spreadsheets/
---

页面设置还提供了几个打印选项（也称为工作表选项），允许用户控制其工作表的打印页面。 这些打印选项允许用户：

- 选择工作表的特定打印区域
- 打印标题
- 打印网格线
- 打印行/列标题
- 达到草稿质量
- 打印注释
- 打印单元格错误
- 定义页面排序
  **设置打印/工作表选项**

Aspose.Cells支持所有这些打印选项，开发人员可以轻松地使用PageSetup类提供的几个属性配置所需工作表的这些选项。 下面更详细地讨论了PageSetup类的这些属性的用法。
## **设置打印区域**
默认情况下，只选择包含数据的工作表的整个区域作为打印区域，但开发人员也可以根据需要为工作表建立特定的打印区域。

要选择特定的打印区域，开发人员可以使用**PageSetup**类的**setPrintArea**方法。 您可以将打印区域的单元格范围作为参数提供给这个方法。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **设置打印标题**
Aspose.Cells允许您指定要在打印的工作表的所有页面上重复的行和列标题。 为此，开发人员可以使用**PageSetup**类的**setPrintTitleColumns**和**setPrintTitleRows**方法。

通过传递它们的行或列号来定义要在打印的工作表的所有页面上重复的行或列（例如，行定义为\ $1: \ $2，列定义为\ $A: \ $B）。

{{< highlight csharp >}}

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
**PageSetup**类还提供了几种其他方法来设置常规打印选项，如下所示：

- **setPrintGridline s方法**，传递一个布尔参数给这个方法，定义是否打印网格线
- **setPrintHeadings方法**，传递一个布尔参数给这个方法，定义是否打印行和列标题
- **setBlackAndWhite方法**，传递一个布尔参数给这个方法，定义是否以黑白模式打印工作表
- **setPrintComments方法**，定义是否在工作表上显示打印备注或在工作表末尾显示
- **setPrintDraft方法**，传递一个布尔参数给这个方法，定义是否以草稿质量打印工作表
- **setPrintErrors方法**，定义是否根据显示、空白、破折号或N/A打印单元格错误

要使用set **PrintComments**和set **PrintErrors**方法，Aspose.Cells还提供了两个枚举类型，PrintCommentsType和PrintErrorsType，它们包含预定义的值，可以作为参数传递给set PrintComments和set PrintErrors方法。

{{< highlight csharp >}}

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
**PageSetup**类提供了set Order方法，用于对工作表的多个页面进行打印排序。有两种可能性来排序页面，如下所示：

先向下再向右，这样打印页面时将首先打印所有向下的页面，然后再向右打印页面
先向右再向下，这样打印页面时将首先从左至右打印页面，然后再向下打印页面
Aspose.Cells提供了一个枚举类型PrintOrderType，其中包含了所有预定义的排序类型，可以赋值给setPage Order方法。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
