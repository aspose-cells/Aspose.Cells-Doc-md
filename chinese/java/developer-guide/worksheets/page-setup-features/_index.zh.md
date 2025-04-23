---
title: 页面设置功能
type: docs
weight: 40
url: /zh/java/page-setup-features/
---

有时，需要为工作表配置页面设置以控制打印。这些页面设置选项提供各种选项。

**页面选项** 

![todo:image_alt_text](page-setup-features_1.png)

Aspose.Cells完全支持页面设置选项。本文说明了如何使用Aspose.Cells设置页面选项。

## **设置页面选项**

Aspose.Cells提供一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。

Worksheet类提供PageSetup属性，用于设置页面设置选项。实际上，PageSetup属性是PageSetup类的对象，它可以设置打印工作表的页面布局选项。PageSetup类提供各种属性，用于设置页面设置选项。以下讨论了其中一些属性。

### **页面方向**

可以使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法将页面方向设置为纵向或横向。[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法接受[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)枚举作为参数。[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)枚举的成员列在下面。

|**页面方向类型**|**描述**|
| :- | :- |
|[**横向**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|横向方向|
|[**纵向**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|纵向方向|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **缩放因子**

可以通过[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom)方法调整缩放因子以减小或放大工作表的大小。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **适合页码选项**

为了使工作表内容适合特定页数，使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)和[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)方法。这些方法还用于缩放工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **纸张尺寸**

使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类的[**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize)属性设置工作表将要打印到的纸张尺寸。PaperSize属性接受[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)枚举中的预定义值之一。下面列出了这些值。

|**纸张尺寸类型**|**描述**|
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

将工作表的打印质量设置为使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的 [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) 方法进行打印。打印质量的测量单位是每英寸点数（DPI）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **首页页码**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的 [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) 方法开始对工作表页面进行编号。setFirstPageNumber 方法设置第一个工作表页面的页码，随后的页面按升序编号。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **设置页边距**

Aspose.Cells 完全支持微软 Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页面边距。

微软 Excel 中的页面边距

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells 提供了一个代表微软 Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类。Workbook 类包含了允许访问 Excel 文件中每个工作表的 Worksheets 集合。工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。

Worksheet 类提供了 PageSetup 属性，用于设置页面设置选项。PageSetup 属性是 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的对象，使得可以为打印的工作表设置不同的页面布局选项。PageSetup 类提供了各种属性和方法，用于设置页面设置选项。

### **页面边距**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的成员设置页面的边距（左、右、上、下）。以下列出了用于指定页面边距的一些方法：

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **页面居中**

可以水平和垂直地将页面居中。[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类具有以下专门用于此目的的成员：[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) 和 [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **页眉和页脚边距**

使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的成员设置页眉和页脚的边距，例如 [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) 和 [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **设置页眉和页脚**

页眉和页脚是页面上边缘之上或下边缘之下的文本和图像部分。还可以向工作表添加页眉和页脚。页眉和页脚可用于显示任何类型的有用信息，例如页码、作者姓名、文档标题或日期和时间。也可以使用页眉和页脚来管理 Page Setup 对话框中的内容。

页面设置对话框 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells 允许在运行时向工作表添加页眉和页脚，但建议手动在预设计的文件中设置页眉和页脚以供打印。您可以使用 Microsoft Excel 作为 GUI 工具轻松设置页眉和页脚，从而减少开发时间。Aspose.Cells 可以导入文件并保留这些设置。

要在运行时添加页眉和页脚，Aspose.Cells 提供了特殊的类和一些脚本命令来控制格式。

### **脚本命令**

脚本命令是由Aspose.Cells提供的特殊命令，允许开发人员格式化页眉和页脚。

|**脚本命令**|**描述**|
| :- | :- |
|&P|当前页面数字。
|&G|图片。
|&N|总页数。
|&D|当前日期。
|&T|当前时间。
|&A|工作表名称。
|&F|不带路径的文件名。
|&&文本|显示 &文本。例如：&&WO 将显示为 &WO|
|&"\<FontName>"|字体名称。例如：&"Arial"
|&"\<FontName>, \<FontStyle>"|带有样式的字体名称。例如：&"Arial,Bold"
|&\<FontSize>|代表字体大小。例如：“&14abc”。但如果此命令后跟一个要在页眉中打印的普通数字，则应与字体大小用空格分隔。例如：“&14 123”。

### **设置页眉和页脚**

类[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)提供了添加页眉的方法[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-)和添加页脚的方法[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-)。该脚本被用作上述方法的参数。它表示用于页眉或页脚的脚本。此脚本包含用于格式化页眉或页脚的脚本命令。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **在页眉或页脚中插入图形**

The [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类有方法[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-)和[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-)，用于向工作表的页眉和页脚添加图片。这些方法接受两个参数：

- **节**，将放置图片的页眉或页脚的部分。有三个部分：左侧，中心和右侧，分别由数值0、1和2表示。
- **文件InputStream**，图形数据。二进制数据应写入字节数组的缓冲区。

在执行代码并打开文件后，检查Microsoft Excel中的工作表页眉:

1. 在**文件**菜单上，选择**页面设置**。
1. 在页面设置对话框中，选择**页眉/页脚**选项卡。

**在页眉/页脚中插入图形** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **仅在第一页页眉中插入图形**

除了其他有用的方法，[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类还有例如[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-)、[**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-)、[**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-)的方法，用于将图片添加到工作表的第一页页眉/页脚。第一页是一个特殊的页面：通常会希望它显示特殊信息，例如公司标志。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **设置打印选项**

Microsoft Excel的页面设置提供了几个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行和列标题
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

所有这些打印选项如下所示。

**打印（工作表）选项** 

![todo:image_alt_text](page-setup-features_5.png)

### **设置打印和工作表选项**

spose.Cells支持Microsoft Excel提供的所有打印选项，开发人员可以轻松地使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)类提供的属性配置工作表的这些选项。下面更详细地讨论了这些属性的使用方式。

### **设置打印区域**

默认情况下，只有打印区域包括所有包含数据的工作表区域。开发人员可以为工作表设定特定的打印区域。

要选择特定的打印区域，请使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的 [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) 属性。将定义打印区域的单元范围分配给此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **设置打印标题**

Aspose.Cells 允许您指定行列标题在打印工作表的所有页面上重复显示。要这样做，请使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类的 [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) 和 [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) 属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类还提供了几个其他属性来设置常规打印选项如下：

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)，一个布尔属性，定义是否打印网格线或不打印。
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)，一个布尔属性，定义是否打印行和列标题或不打印。
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)，一个布尔属性，定义是否以黑白模式打印工作表或不打印。
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)，定义是否在工作表上显示打印备注或在工作表末尾显示。
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)，一个布尔属性，定义是否以草稿质量打印工作表或不打印。
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)，定义是否按照显示，空白，破折号或 N/A 打印单元格错误。

为了设置 [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) 和 [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) 属性，Aspose.Cells 还提供了两个枚举，[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) 和 [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)，其中包含预定义的值分配给 [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) 和 [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) 属性。

[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) 枚举中的预定义值如下所述。

|**打印备注类型**|**描述**|
| :- | :- |
|[**在原地打印**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|指定以工作表上的显示方式打印批注。|
|[**不打印批注**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|指定不打印批注。|
|[**打印在工作表末端**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|指定在工作表末端打印批注。|

[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) 枚举中的预定义值如下所述。

|**打印错误类型**|**描述**|
| :- | :- |
|[**打印错误为空**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|指定不打印错误。|
|[**用“--”打印错误**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|指定将错误以“--”显示。|
|[**显示打印错误**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|指定按显示方式打印错误。|
|[**打印为“#N/A”**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|指定将错误打印为“#N/A”。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **设置页面顺序**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) 类提供 [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) 属性，用于对要打印的工作表的多个页面进行排序。有两种可能的页面排序方式如下：

- **先向下再向右** 打印所有页面向下后再打印任何页面向右。
- **先向右再向下** 依次打印页面从左到右再打印页面向下。

Aspose.Cells 提供一个枚举，[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)，其中包含所有预定义的排序类型，可分配给 [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) 方法。

[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) 枚举的预定义值如下所述。

|**打印顺序类型**|**描述**|
| :- | :- |
|[**向下打印，然后横向**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|优先向下打印，然后横向。|
|[**向右打印，然后向下**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|优先向右打印，然后向下。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **删除Excel文件中工作表的现有打印设置**

请参阅与此主题相关的文章。

## **高级主题**
- [计算页面设置缩放因子](/cells/zh/java/calculate-page-setup-scaling-factor/)
- [将源工作表中的页面设置复制到目标工作表](/cells/zh/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [确定工作表的纸张大小是否自动](/cells/zh/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [从工作表的页面设置获取纸张的宽度和高度](/cells/zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [实现工作表的自定义纸张大小以进行渲染](/cells/zh/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [页面设置和打印选项](/cells/zh/java/page-setup-and-printing-options/)
- [删除Excel文件中工作表的现有打印设置](/cells/zh/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
