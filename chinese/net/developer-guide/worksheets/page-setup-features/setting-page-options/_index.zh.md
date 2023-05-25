---
title: 设置页面选项
type: docs
weight: 10
url: /zh/net/setting-page-options/
description: 本文提供示例代码以使用 C# API 和 .NET 库以编程方式设置 Excel 工作表的页面选项。您将能够设置页面方向、比例因子、FitToPages 选项、纸张尺寸、打印质量、首页页码。
keywords: set excel page orientation c#, set excel scaling factor c#, set excel worksheets paper size c#
---
{{% alert color="primary" %}}

有时，需要为工作表配置页面设置以控制打印。这些页面设置设置提供了各种选项。

{{% /alert %}}

##  **设置页面选项**

Aspose.Cells 完全支持页面设置选项。本文介绍了如何使用 Aspose.Cells 设置页面选项，并显示了用于设置的代码示例：

 Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)用于设置工作表页面设置选项的属性。事实上，这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)属性是[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)用于为打印工作表设置不同页面布局选项的类。这[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类提供用于设置页面设置选项的各种属性。下面讨论其中一些特性。

###  **页面方向**

页面方向可以设置为纵向或横向使用[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**方向**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)财产。这[**方向**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)属性接受中的预定义值之一[**页面方向类型**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)枚举，如下所示。

|**页面方向类型**|**描述**|
| :- | :- |
|景观|横向|
|肖像|纵向|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

###  **比例因子**

可以通过调整比例因子来缩小或放大工作表的大小[**页面设置.缩放**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)财产。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

###  **FitToPages 选项**

要使工作表的内容适合特定页数，请使用[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**适合页面高**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)和[**适合页面宽度**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)特性。这些属性还用于缩放工作表。

{{% alert color="primary" %}}

您可以选择[**适合页面高**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**适合页面宽度**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)或者[**飞涨**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)财产，但不能同时拥有。

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

###  **纸张尺寸**

使用[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**纸张大小**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)财产。这[**纸张大小**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)属性接受中的预定义值之一[**纸张大小类型**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)枚举，如下所示。

|**纸张尺寸类型**|**描述**|
| :- | :- |
|纸信|信纸（8-1/2 英寸 x 11 英寸）|
|纸信小号|Letter Small（8-1/2 英寸 x 11 英寸）|
|纸质小报|小报（11 英寸 x 17 英寸）|
|纸账本|分类帐（17 英寸 x 11 英寸）|
|纸质法律|合法（8-1/2 英寸 x 14 英寸）|
|纸质结单|报表（5-1/2 英寸 x 8-1/2 英寸）|
|纸行政|行政（7-1/4 英寸 x 10-1/2 英寸）|
|试卷A3|A3（297 毫米 x 420 毫米）|
|纸A4|A4（210 毫米 x 297 毫米）|
|纸A4小|A4 小（210 毫米 x 297 毫米）|
|试卷A5|A5（148 毫米 x 210 毫米）|
|试卷B4|JIS B4（257 毫米 x 364 毫米）|
|试卷B5|JIS B5（182 毫米 x 257 毫米）|
|对开纸|对开本（8-1/2 英寸 x 13 英寸）|
|纸质四开本|四开本（215 毫米 x 275 毫米）|
|纸 10x14|10 英寸 x 14 英寸|
|纸 11x17|11 英寸 x 17 英寸|
|纸笔记|注（8-1/2 英寸 x 11 英寸）|
|纸信封9|9 号信封（3-7/8 英寸 x 8-7/8 英寸）|
|纸信封10|10 号信封（4-1/8 英寸 x 9-1/2 英寸）|
|纸信封11|11 号信封（4-1/2 英寸 x 10-3/8 英寸）|
|纸信封12|12 号信封（4-1/2 英寸 x 11 英寸）|
|纸信封14|14 号信封（5 英寸 x 11-1/2 英寸）|
|纸片|C尺寸床单|
|纸D表|D尺寸床单|
|纸电子表|E尺寸床单|
|纸质信封DL|信封 DL（110 毫米 x 220 毫米）|
|纸质信封C5|信封 C5（162 毫米 x 229 毫米）|
|纸质信封C3|信封 C3（324 毫米 x 458 毫米）|
|纸质信封C4|信封 C4（229 毫米 x 324 毫米）|
|纸质信封C6|信封 C6（114 毫米 x 162 毫米）|
|纸质信封C65|信封 C65（114 毫米 x 229 毫米）|
|纸质信封B4|信封 B4（250 毫米 x 353 毫米|
|纸质信封B5|信封 B5（176 毫米 x 250 毫米）|
|纸质信封B6|信封 B6（176 毫米 x 125 毫米）|
|纸信封意大利|意大利信封（110 毫米 x 230 毫米）|
|纸信封君主|Monarch 信封（3-7/8 英寸 x 7-1/2 英寸）|
|纸质信封个人|信封（3-5/8 英寸 x 6-1/2 英寸）|
|纸质折页美国|美国标准折叠式（14-7/8 英寸 x 11 英寸）|
|PaperFanfoldStd德语|德国标准对折（8-1/2 英寸 x 12 英寸）|
|PaperFanfoldLegal德语|德国 Legal 对折（8-1/2 英寸 x 13 英寸）|
|纸质ISOB4|B4 (ISO) 250 x 353 毫米|
|纸日本明信片|日本明信片 (100mm x 148mm)|
|纸9x11|9 英寸 x 11 英寸|
|纸10x11|10 英寸 x 11 英寸|
|纸15x11|15 英寸 x 11 英寸|
|纸质信封请柬|信封请柬(220mm x 220mm)|
|纸信特|US Letter Extra 9 \275 x 12 英寸|
|PaperLegalExtra|US Legal Extra 9 \275 x 15 英寸|
|PaperTabloidExtra|美国小报 11.69 x 18 英寸|
|纸A4特|A4 特大 9.27 x 12.69 英寸|
|纸信横版|Letter 横向 8 \275 x 11 英寸|
|纸A4横向|A4 横向 210 x 297 毫米|
|纸信超横向|Letter Extra Transverse 9\275 x 12 英寸|
|纸超A|SuperA/SuperA/A4 227 x 356 毫米|
|纸超级B|SuperB/SuperB/A3 305 x 487 毫米|
|纸信加号|US Letter Plus 8.5 x 12.69 英寸|
|纸A4Plus|A4 加 210 x 330 毫米|
|纸A5横向|A5 横向 148 x 210 毫米|
|纸JISB5横向|B5 (JIS) 横向 182 x 257 毫米|
|纸A3特|A3 超大 322 x 445 毫米|
|纸A5特|A5 超大 174 x 235 毫米|
|纸张ISOB5特级|B5 (ISO) 额外 201 x 276 毫米|
|试卷A2|A2 420 x 594 毫米|
|纸A3横向|A3 横向 297 x 420 毫米|
|纸A3超横向|A3 超横向 322 x 445 毫米|
|纸日本双面明信片|日本双面明信片 200 x 148 毫米|
|试卷A6|A6 105 x 148 毫米|
|纸日本信封卡库 2|日本信封 Kaku #2|
|纸日本信封角 3|日本信封 Kaku #3|
|纸日本信封Chou3|日本信封周 #3|
|纸日本信封Chou4|日本信封周 #4|
|纸质字母旋转|11 英寸 x 8.5 英寸|
|纸A3旋转|420 毫米 x 297 毫米|
|纸A4旋转|297 毫米 x 210 毫米|
|纸A5旋转|210 毫米 x 148 毫米|
|纸质JISB4旋转|B4 (JIS) 旋转 364 x 257 毫米|
|纸质JISB5旋转|B5 (JIS) 旋转 257 x 182 毫米|
|纸日本明信片旋转|日本明信片旋转 148 x 100 毫米|
|纸日本双面明信片旋转|双面日本明信片旋转 148 x 200 毫米|
|纸A6旋转|A6 旋转 148 x 105 毫米|
|纸日本信封 Kaku2 旋转|日本信封 Kaku #2 旋转|
|纸日本信封 Kaku3 旋转|日本信封 Kaku #3 旋转|
|纸日本信封周 3 旋转|日本信封周 #3 旋转|
|纸日本信封周 4 旋转|日本信封周 #4 旋转|
|纸质JISB6|B6 (日本工业标准) 128 x 182 毫米|
|纸质JISB6旋转|B6 (JIS) 旋转 182 x 128 毫米|
|纸12x11|12 x 11 英寸|
|纸日本信封You4|日本信封你 #4|
|纸日本信封You4Rotated|日本信封 You #4 旋转|
|纸PRC16K|中国 16K 146 x 215 毫米|
|纸PRC32K|中国 32K 97 x 151 毫米|
|论文PRCBig32K|PRC 32K（大）97 x 151 毫米|
|纸PRC信封1|PRC 信封 #1 102 x 165 毫米|
|纸PRC信封2|PRC 信封 #2 102 x 176 毫米|
|纸PRC信封3|PRC 信封 #3 125 x 176 毫米|
|纸PRC信封4|PRC 信封 #4 110 x 208 毫米|
|纸PRC信封5|PRC 信封 #5 110 x 220 毫米|
|纸PRC信封6|PRC 信封 #6 120 x 230 毫米|
|纸PRC信封7|PRC 信封 #7 160 x 230 毫米|
|纸PRC信封8|PRC 信封 #8 120 x 309 毫米|
|纸PRC信封9|PRC 信封 #9 229 x 324 毫米|
|纸PRC信封10|PRC 信封 #10 324 x 458 毫米|
|纸PRC16K旋转|PRC 16K 旋转|
|纸PRC32K旋转|PRC 32K 旋转|
|纸PRCBig32KRotated|PRC 32K(大)旋转|
|纸PRC信封1旋转|PRC 信封 #1 旋转 165 x 102 毫米|
|纸PRC信封2旋转|PRC 信封 #2 旋转 176 x 102 毫米|
|纸PRC信封3旋转|PRC 信封 #3 旋转 176 x 125 毫米|
|纸PRC信封4旋转|PRC 信封 #4 旋转 208 x 110 毫米|
|纸PRC信封5旋转|PRC 信封 #5 旋转 220 x 110 毫米|
|纸PRC信封6旋转|PRC 信封 #6 旋转 230 x 120 毫米|
|纸PRC信封7旋转|PRC 信封 #7 旋转 230 x 160 毫米|
|纸PRC信封8旋转|PRC 信封 #8 旋转 309 x 120 毫米|
|纸PRC信封9旋转|PRC 信封 #9 旋转 324 x 229 毫米|
|纸PRC信封10旋转|PRC 信封 #10 旋转 458 x 324 毫米|
|试卷B3|通常 B3（13.9 x 19.7 英寸）|
|纸质名片|名片(90mm x 55mm)|
|热敏纸|热量（3 x 11 英寸）|
|风俗|表示自定义纸张尺寸。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

###  **打印质量**

设置要打印的工作表的打印质量[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**打印质量**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)财产。打印质量的测量单位是每英寸点数 (DPI)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

###  **第一页码**

使用开始工作表页面编号[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)班级'[**首页编号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)财产。这[**首页编号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)属性设置第一个工作表页的页码，下一页按升序编号。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
