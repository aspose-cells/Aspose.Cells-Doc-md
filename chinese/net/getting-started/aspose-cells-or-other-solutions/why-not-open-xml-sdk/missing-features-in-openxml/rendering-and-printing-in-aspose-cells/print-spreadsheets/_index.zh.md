---
title: 打印电子表格
type: docs
weight: 20
url: /zh/net/print-spreadsheets/
---

页面设置还提供了几个打印选项（也称为工作表选项），允许用户控制工作表的打印页面。这些打印选项允许用户：

- 选择工作表的特定打印区域
- 打印标题
- 打印网格线
- 打印行/列标题
- 实现草稿质量
- 打印批注
- 打印单元格错误
- 定义页面排序
  **设置打印/工作表选项**

Aspose.Cells支持所有这些打印选项，开发人员可以使用PageSetup类提供的多个属性轻松配置其所需的工作表打印选项。下面更详细地讨论了PageSetup类的这些属性的使用。
## **设置打印范围**
默认情况下，只选择包含数据的整个工作表区域作为打印区域，但开发人员还可以根据自己的需求在工作表上建立特定的打印区域。

要选择特定的打印区域，开发人员可以使用PageSetup类的**setPrintArea**方法。您可以将打印区域的单元格范围作为参数传递给此方法。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **设置打印标题**
Aspose.Cells允许您指定要在打印的所有工作表页面上重复的行和列标题。为此，开发人员可以使用PageSetup类的**setPrintTitleColumns**和**setPrintTitleRows**方法。

要在打印的工作表的所有页面上定义要重复的行或列（标题），可以通过传递它们的行号或列号来定义。例如，行可定义为 \ $1: \ $2，列可定义为 \ $A: \ $B。

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
**PageSetup** 类也提供了几种其他方法来设置常规打印选项，如下所示:

- **setPrintGridlines 方法**，将布尔参数传递给该方法，以定义是否打印网格线
- **setPrintHeadings 方法**，将布尔参数传递给该方法，以定义是否打印行和列标题
- **setBlackAndWhite 方法**，将布尔参数传递给该方法，以定义是否以黑白模式打印工作表
- **setPrintComments 方法**，定义是否在工作表上显示打印备注或在工作表末尾显示
- **setPrintDraft 方法**，将布尔参数传递给该方法，以定义是否以草稿质量打印工作表
- **setPrintErrors 方法**，定义是否打印按显示的单元格错误、空白、破折号或N/A

要使用set **PrintComments**和set **PrintErrors**方法，Aspose.Cells还提供了两个枚举PrintCommentsType和PrintErrorsType，其中包含预定义的值作为参数传递给设置PrintComments和设置PrintErrors方法。

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
**PageSetup** 类提供set Order方法，用于对要打印的工作表的多个页面进行排序。有两种可能性对页面进行排序，如下:

先下后右，这样会先打印所有页面向下，然后再打印右边的页面
先右后下，这样会先从左到右打印页面，然后再打印下面的页面
Aspose.Cells提供一个枚举PrintOrderType，其中包含所有预定义的排序类型，可分配给setPage Order方法。

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
