---
title: 页面设置功能
type: docs
weight: 40
url: /zh/java/page-setup-features/
---
有时，需要为工作表配置页面设置以控制打印。这些页面设置设置提供了各种选项。

**页面选项** 

![待办事项：图片_替代_文本](page-setup-features_1.png)

Aspose.Cells 完全支持页面设置选项。本文介绍如何使用 Aspose.Cells 设置页面选项。

## **设置页面选项**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

Worksheet 类提供了 PageSetup 属性，用于设置页面设置选项。事实上，PageSetup 属性是 PageSetup 类的一个对象，它可以为打印的工作表设置页面布局选项。 PageSetup 类提供了各种用于设置页面设置选项的属性。下面讨论其中一些特性。

### **页面方向**

页面方向可以设置为纵向或横向使用[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**设置方向（页面方向类型）**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法。这[**设置方向（页面方向类型）**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法采用[**页面方向类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)枚举作为参数。的成员[**页面方向类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)列举如下。

|**页面方向类型**|**描述**|
|:- |:- |
|[**景观**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|横向|
|[**肖像**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|纵向|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **比例因子**

可以通过调整比例因子来缩小或放大工作表的大小[**设置缩放**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom)的方法[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages 选项**

要使工作表的内容适合特定页数，请使用[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)和[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)方法。这些方法也用于缩放工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **纸张尺寸**

使用[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**纸张大小**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize)财产。 PaperSize 属性接受[**纸张大小类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)枚举，如下所示。

|**纸张尺寸类型**|**描述**|
|:- |:- |
|纸 10x14|10 英寸 x 14 英寸|
|纸 11x17|11 英寸 x 17 英寸|
|试卷A3|A3（297 毫米 x 420 毫米）|
|纸A4|A4（210 毫米 x 297 毫米）|
|纸A4小|A4 小（210 毫米 x 297 毫米）|
|试卷A5|A5（148 毫米 x 210 毫米）|
|试卷B3|B3（13.9 x 19.7 英寸）|
|试卷B4|B4（250 毫米 x 354 毫米）|
|试卷B5|B5（182 毫米 x 257 毫米）|
|纸质名片|名片（90 毫米 x 55 毫米）|
|纸片|C尺寸床单|
|纸D表|D尺寸床单|
|纸信封10|10 号信封（4-1/8 英寸 x 9-1/2 英寸）|
|纸信封11|11 号信封（4-1/2 英寸 x 10-3/8 英寸）|
|纸信封12|12 号信封（4-1/2 英寸 x 11 英寸）|
|纸信封14|14 号信封（5 英寸 x 11-1/2 英寸）|
|纸信封9|9 号信封（3-7/8 英寸 x 8-7/8 英寸）|
|纸质信封B4|信封 B4（250 毫米 x 353 毫米）|
|纸质信封B5|信封 B5（176 毫米 x 250 毫米）|
|纸质信封B6|信封 B6（176 毫米 x 125 毫米）|
|纸质信封C3|信封 C3（324 毫米 x 458 毫米）|
|纸质信封C4|信封 C4（229 毫米 x 324 毫米）|
|纸质信封C5|信封 C5（162 毫米 x 229 毫米）|
|纸质信封C6|信封 C6（114 毫米 x 162 毫米）|
|纸质信封C65|信封 C65（114 毫米 x 229 毫米）|
|纸质信封DL|信封 DL（110 毫米 x 220 毫米）|
|纸信封意大利|意大利信封（110 毫米 x 230 毫米）|
|纸信封君主|Monarch 信封（3-7/8 英寸 x 7-1/2 英寸）|
|纸质信封个人|信封（3-5/8 英寸 x 6-1/2 英寸）|
|纸电子表|E尺寸床单|
|纸行政|行政（7-1/2 英寸 x 10-1/2 英寸）|
|PaperFanfoldLegal德语|德国 Legal 对折（8-1/2 英寸 x 13 英寸）|
|PaperFanfoldStd德语|德国标准对折（8-1/2 英寸 x 12 英寸）|
|纸质折页美国|美国标准折叠式（14-7/8 英寸 x 11 英寸）|
|对开纸|对开本（8-1/2 英寸 x 13 英寸）|
|纸账本|分类帐（17 英寸 x 11 英寸）|
|纸质法律|合法（8-1/2 英寸 x 14 英寸）|
|纸信|信纸（8-1/2 英寸 x 11 英寸）|
|纸信小号|Letter Small（8-1/2 英寸 x 11 英寸）|
|纸笔记|注（8-1/2 英寸 x 11 英寸）|
|纸质四开本|四开本（215 毫米 x 275 毫米）|
|纸质结单|报表（5-1/2 英寸 x 8-1/2 英寸）|
|纸质小报|小报（11 英寸 x 17 英寸）|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **打印质量**

设置要打印的工作表的打印质量[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**设置打印质量**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality)方法。打印质量的测量单位是每英寸点数 (DPI)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **第一页码**

使用开始工作表页面编号[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**设置第一页编号**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber)方法。 setFirstPageNumber 方法设置工作表第一页的页码，后面的页面按升序编号。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **设置边距**

Aspose.Cells 完全支持 Microsoft Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页边距。

**Microsoft Excel 中的页边距**

![待办事项：图片_替代_文本](page-setup-features_2.png)

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。 Workbook 类包含允许访问 Excel 文件中的每个工作表的 Worksheets 集合。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

Worksheet 类提供了 PageSetup 属性，用于设置页面设置选项。 PageSetup 属性是[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类，它可以为打印的工作表设置不同的页面布局选项。 PageSetup 类提供了用于设置页面设置选项的各种属性和方法。

### **页边距**

设置页面的页边距（左、右、上、下）[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级成员。下面列出了一些用于指定页边距的方法：

- [**设置左边距（整数）**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin（整数）**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**设置底部边距（整数）**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **页面居中**

可以在页面上水平和垂直居中某些内容。这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类有用于此目的的成员：[**水平居中**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally)和[**设置垂直居中**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **页眉和页脚边距**

设置页眉和页脚边距[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)成员如[**设置页眉边距**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin)和[**设置页脚边距**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **设置页眉和页脚**

页眉和页脚是页面上边距上方或底部边距下方的文本和图像部分。也可以向工作表添加页眉和页脚。页眉和页脚可用于显示任何类型的有用信息，例如页码、作者姓名、文档标题或日期和时间。页眉和页脚也可以使用“页面设置”对话框进行管理。

**页面设置对话框** 

![待办事项：图片_替代_文本](page-setup-features_3.png)

Aspose.Cells 允许在运行时将页眉和页脚添加到工作表，但建议在预先设计的文件中手动设置页眉和页脚以进行打印。您可以使用 Microsoft Excel 作为 GUI 工具轻松设置页眉和页脚以减少开发时间。 Aspose.Cells 可以导入文件并保留这些设置。

为了在运行时添加页眉和页脚，Aspose.Cells 提供了特殊的类和一些脚本命令来控制格式。

### **脚本命令**

脚本命令是 Aspose.Cells 提供的特殊命令，允许开发人员格式化页眉和页脚。

|**脚本命令**|**描述**|
|:- |:- |
|&P|当前页码。|
|＆G|照片。|
|&N|总页数。|
|&D|当前日期。|
|&T|当前时间。|
|＆一种|工作表的名称。|
|＆F|没有路径的文件名。|
|&"\<FontName>"|字体名称。例如：&"宋体"|
|&"\<FontName>, \<FontStyle>"|带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|表示字体大小。例如：“&14abc”。但是，如果此命令后跟要在标题中打印的普通数字，则应使用空格字符将其与字体大小分隔开。例如：“&14 123”。|

### **设置页眉和页脚**

这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类提供方法[**设置标题**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) 用于添加标题和[**设置页脚**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)用于向工作表添加页脚。该脚本用作上述所有方法的参数。它表示用于页眉或页脚的脚本。此脚本包含用于格式化页眉或页脚的脚本命令。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **将图形插入页眉或页脚**

这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类有方法[**设置头像**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ） 和[**设置页脚图片**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])用于将图片添加到工作表的页眉和页脚。这些方法有两个参数：

- **部分**，将放置图片的页眉或页脚部分。分为左、中、右三部分，分别用数值0、1、2表示。
- **文件输入流**图形数据。二进制数据应写入字节数组的缓冲区。

执行代码并打开文件后，在 Microsoft Excel 中检查工作表的标题：

1. 在**文件**菜单，选择**页面设置**.
1. 在“页面设置”对话框中，选择**页眉页脚**标签。

**在页眉/页脚中插入图形** 

![待办事项：图片_替代_文本](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **仅在首页页眉中插入图形**

这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类还有其他有用的方法，例如[**设置图片**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**设置第一页页眉**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**设置第一页页脚**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), 用于将图片添加到工作表的第一页页眉/页脚中。第一页是一个特殊页面：通常希望它显示特殊信息，例如公司标志。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **设置打印选项**

Microsoft Excel 的页面设置设置提供了多个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行和列标题
- 达到草稿质量。
- 打印评论。
- 打印单元错误。
- 定义页面排序。

所有这些打印选项如下所示。

**打印（纸张）选项** 

![待办事项：图片_替代_文本](page-setup-features_5.png)

### **设置打印和工作表选项**

spose.Cells 支持 Microsoft Excel 提供的所有打印选项，开发人员可以使用提供的属性轻松地为工作表配置这些选项[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级。下面将更详细地讨论如何使用这些属性。

### **设置打印区域**

默认情况下，只有打印区域包含工作表中包含数据的所有区域。开发人员可以建立工作表的特定打印区域。

要选择特定的打印区域，请使用[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**设置打印区域**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea)财产。将定义打印区域的单元格范围分配给此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **设置打印标题**

Aspose.Cells 允许您指定行和列标题以在打印的工作表的所有页面上重复。为此，请使用[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)班级'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns)和[**设置打印标题行**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows)特性。

将重复的行或列通过传递它们的行号或列号来定义。例如，行定义为 $1:$2，列定义为 $A:$B。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **设置其他打印选项**

这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类还提供了几个其他属性来设置常规打印选项，如下所示：

- [**设置打印网格线**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)一个布尔属性，定义是否打印网格线。
- [*设置打印标题*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)一个布尔属性，定义是否打印行标题和列标题。
- [**设置黑白**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)一个布尔属性，定义是否以黑白模式打印工作表。
- [**设置打印注释**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)定义是否在工作表上或工作表末尾显示打印注释。
- [**设置打印草稿**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)，一个布尔属性，定义是否以草稿质量打印工作表。
- [**设置打印错误**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)定义是否将单元格错误打印为显示、空白、破折号或 N/A。

设置[**打印评论**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)和[**打印错误**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)属性，Aspose.Cells还提供了两个枚举，[**打印注释类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)和[**打印错误类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)包含要分配给的预定义值[**设置打印注释**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)和[**设置打印错误**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)分别属性。

中的预定义值[**打印注释类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)枚举描述如下。

|**打印注释类型**|**描述**|
|:- |:- |
|[**打印位置**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|指定打印工作表上显示的注释。|
|[**打印_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|指定不打印注释。|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|指定在工作表末尾打印注释。|

的预定义值[**打印错误类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)枚举描述如下。

|**打印错误类型**|**描述**|
|:- |:- |
|[*打印_错误_空白*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|指定不打印错误。|
|[**打印错误破折号**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|指定将错误打印为“--”。|
|[**打印错误显示**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|指定打印显示的错误。|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|指定将错误打印为“#N/A”。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **设置页面顺序**

这[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类提供了[**设置顺序**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)用于订购要打印的工作表的多页的属性。页面排序有两种可能性，如下所示：

- **下来然后结束**在向右打印任何页面之前先向下打印所有页面。
- **过来然后下来**在打印下面的任何页面之前先从左到右打印页面。

 Aspose.Cells 提供枚举，[**打印订单类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)，其中包含要分配给的所有预定义订单类型[**设置顺序**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)方法。

的预定义值[**打印订单类型**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)枚举描述如下。

|**打印订单类型**|**描述**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|打印下来，然后结束。|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|打印过来，然后向下。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **删除 Excel 文件中工作表的现有打印机设置**

请参阅与此主题相关的这篇文章。

## **推进主题**
- [计算页面设置比例因子](/cells/zh/java/calculate-page-setup-scaling-factor/)
- [将源工作表中的页面设置设置复制到目标工作表](/cells/zh/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [确定工作表的纸张大小是否为自动](/cells/zh/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [从工作表的 PageSetup 获取纸张宽度和高度](/cells/zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [实现工作表的自定义纸张大小以进行渲染](/cells/zh/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [页面设置和打印选项](/cells/zh/java/page-setup-and-printing-options/)
- [删除 Excel 文件中工作表的现有打印机设置](/cells/zh/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
