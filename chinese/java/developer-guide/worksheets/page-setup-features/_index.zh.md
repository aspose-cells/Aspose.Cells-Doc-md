---
title: 页面设置功能
type: docs
weight: 40
url: /zh/java/page-setup-features/
---

有时，需要为工作表配置页面设置以控制打印。这些页面设置提供各种选项。

**页面选项** 

![todo:image_alt_text](page-setup-features_1.png)

Aspose.Cells完全支持页面设置选项。本文解释了如何使用Aspose.Cells设置页面选项。

## **设置页面选项**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个允许访问Excel文件中每张工作表的[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)。

{1}类提供了PageSetup属性，用于设置页面设置选项。实际上，PageSetup属性是PageSetup类的对象，可以设置打印工作表的页面布局选项。PageSetup类提供了各种属性，用于设置页面设置选项。下面讨论了其中一些属性。

### **页面方向**

可以使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法将页面方向设置为纵向或横向。[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法需要[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)枚举作为参数。[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)枚举的成员列在下面。

|**页面方向类型**|**描述**|
| :- | :- |
|[**横向**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|横向方向|
|[**纵向**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|纵向方向|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **缩放因子**

可以通过[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom)类的[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)方法调整缩放因子来减小或增大工作表的大小。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **适应页面选项**

要将工作表的内容调整到特定数量的页面上，可以使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)和[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)方法。这些方法也可以用于调整工作表的比例。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **纸张大小**

使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize)属性设置工作表要打印到的纸张大小。PaperSize属性接受[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)枚举中预定义的值，列在下面。

|**纸张大小类型**|**描述**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **打印质量**

使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality)方法设置要打印的工作表的打印质量。打印质量的测量单位是每英寸的点数（DPI）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **第一页页码**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的 [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) 方法开始对工作表页面进行编号。setFirstPageNumber 方法设置第一个工作表页面的页码，随后的页面将按升序编号。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **设置页边距**

Aspose.Cells完全支持Microsoft Excel的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论了如何使用Aspose.Cells配置页面边距。

**Microsoft Excel 中的页面边距**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。

Worksheet 类提供了 PageSetup 属性，用于设置页面设置选项。PageSetup 属性是 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的对象，它可以设置打印工作表的不同页面布局选项。PageSetup 类提供了用于设置页面设置选项的各种属性和方法。

### **页边距**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类成员设置页面的边距（左、右、上、下）。以下是用于指定页面边距的一些方法：

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **居中打印**

可以将内容在页面上水平和垂直居中。 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类具有为此目的的成员：[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) 和 [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **页眉和页脚页边距**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 成员设置页眉和页脚边距，如 [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) 和 [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **设置页眉和页脚**

页眉和页脚是页面上边距以上或下边距以下的文本和图像部分。也可以将页眉和页脚添加到工作表中。页眉和页脚可以用于显示任何有用的信息，例如页码、作者姓名、文档标题或日期和时间。也可以使用页面设置对话框管理页眉和页脚。

**页面设置对话框** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells 允许在运行时向工作表添加页眉和页脚，但建议手动在预先设计好的文件中设置页眉和页脚以用于打印。您可以使用 Microsoft Excel 作为GUI工具轻松设置页眉和页脚，以减少开发时间。Aspose.Cells 可以导入该文件并保留这些设置。

要在运行时添加页眉和页脚，Aspose.Cells 提供了特殊的类和一些脚本命令以控制格式。

### **脚本命令**

脚本命令是由Aspose.Cells提供的特殊命令，允许开发人员格式化页眉和页脚。

|**脚本命令**|**描述**|
| :- | :- |
|&P|当前页码。|
|&G|一张图片。|
|&N|总页数。|
|&D|当前日期。|
|&T|当前时间。|
|&A|工作表名称。|
|&F|不带路径的文件名。|
|&"\<FontName>"|字体名称。例如：&"Arial"|
|&"\<FontName>, \<FontStyle>"|带样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|表示字体大小。例如：“＆14abc”。但如果这个命令后面跟着要在页眉中打印的纯数字，则应该用一个空格字符与字体大小分隔开。例如：“＆14 123”。|

### **设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类提供了添加页眉的 [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) 方法和添加页脚的 [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String) 方法。脚本用作上述所有方法的参数。它表示要用于页眉或页脚的脚本。此脚本包含格式化页眉或页脚的脚本命令。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **在页眉或页脚中插入图形**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类具有添加图片到工作表页眉和页脚的 [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) 和 [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[]) 方法。这些方法带有两个参数：

- **Section**，将放置图片的页眉或页脚的部分。有三个部分：左、中、右，分别用数值 0、1 和 2 表示。
- **File InputStream**，图形数据。二进制数据应写入字节数组的缓冲区。

在执行代码并在 Microsoft Excel 中打开文件后，检查工作表的页眉：

1. 在 **文件** 菜单中，选择 **页面设置**。
1. 在页面设置对话框中，选择**页眉/页脚**选项卡。

**在页眉/页脚中插入图形** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **仅在第一页页眉中插入图形**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类还有其他实用的方法，例如[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])）、[**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)）、[**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)），用于向工作表的第一页页眉/页脚添加图片。第一页是一个特殊页：通常希望它显示特殊信息，比如公司标志。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **设置打印选项**

Microsoft Excel的页面设置提供了多个打印选项（也称为工作表选项），允许用户控制工作表页的打印方式。这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行和列标题
- 实现草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

所有这些打印选项如下。

**打印（工作表）选项** 

![todo:image_alt_text](page-setup-features_5.png)

### **设置打印和工作表选项**

spose.Cells支持Microsoft Excel提供的所有打印选项，并且开发人员可以使用该类提供的属性轻松配置工作表的这些选项。下面更详细地讨论了如何使用这些属性。

### **设置打印范围**

默认情况下，打印区域仅包含包含数据的工作表所有区域。开发人员可以为工作表设定特定打印区域。

要选择特定的打印区域，请使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea)属性。将定义打印区域的单元格范围分配给此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **设置打印标题**

Aspose.Cells允许您指定要在打印的工作表的所有页面上重复的行和列标题。要做到这一点，请使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns)和[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows)属性。

将重复的行或列由其行号或列号传递定义。例如，行定义为$1:$2，列定义为$A:$B。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类还提供了几个其他用于设置常规打印选项的属性，如下：

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)，一个布尔属性，定义是否打印网格线。
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)，一个布尔属性，定义是否打印行和列标题。
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)，一个布尔属性，定义是否以黑白模式打印工作表。
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)，定义是否在工作表上显示打印备注或在工作表末尾显示。
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)，一个布尔属性，定义是否以草稿质量打印工作表。
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)，定义是否按照显示的方式、空白、破折号或N/A打印单元格错误。

为设置[**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)和[**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)属性，Aspose.Cells还提供了两个枚举，[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)和[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)，包含要分配给[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)和[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)属性的预定义值。

[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)枚举中的预定义值如下。

|**打印注释类型**|**描述**|
| :- | :- |
|[**就地打印**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|指定将批注打印为工作表上显示的内容。|
|[**不打印批注**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|指定不打印批注。|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|指定在工作表末尾打印注释。|

[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)枚举的预定义值如下。

|**打印错误类型**|**描述**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|指定不打印错误。|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|指定将错误打印为“--”。|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|指定打印显示的错误。|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|指定将错误打印为“#N/A”。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **设置页面顺序**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类提供[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)属性，用于指定要打印工作表的多个页面的顺序。有两种可能的页面顺序，如下：

- **先下后右** 在打印纸张之前，先打印所有页面向下。
- **先右后下** 在打印纸张之前，先打印所有页面向右。

Aspose.Cells 提供了一个枚举，[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)，其中包含可分配给[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)方法的所有预定义顺序类型。

[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)枚举的预定义值如下所述。

|**打印顺序类型**|**描述**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|先纵向再横向打印。|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|先横向再纵向打印。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **删除Excel文件中工作表的现有PrinterSettings**

请参阅与此主题相关的文章。

## **高级主题**
- [计算页面设置比例因子](/cells/zh/java/calculate-page-setup-scaling-factor/)
- [将源工作表中的页面设置复制到目标工作表](/cells/zh/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [确定工作表的纸张大小是否为自动](/cells/zh/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [从工作表的PageSetup中获取纸张宽度和高度](/cells/zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [实现呈现的工作表的自定义纸张大小](/cells/zh/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [页面设置和打印选项](/cells/zh/java/page-setup-and-printing-options/)
- [删除Excel文件中工作表的现有PrinterSettings](/cells/zh/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
