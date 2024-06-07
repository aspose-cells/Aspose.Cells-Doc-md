---
title: 工作簿设置
type: docs
weight: 250
url: /zh/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: 本文描述了GridWeb中的工作簿设置。
keywords: GridWeb,设置
---


我们可以通过设置GridWorkbookSettings来指定一些设置：


- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**名称** |**描述** |
| :- | :- |
|MaxIteration |获取或设置解析循环引用的最大迭代次数，默认值为100。|
|Iteration |获取或设置是否使用迭代来解析循环引用。|
|ForceFullCalculate |获取或设置是否在触发计算时每次都完全计算。|
|CreateCalcChain |获取或设置是否创建计算公式链。默认为false。|
|ReCalculateOnOpen |获取或设置是否在打开文件时重新计算所有公式。|
|PrecisionAsDisplayed |如果此工作簿中的计算仅使用显示为数字的精度，则为True。|
|Date1904 |获取或设置一个值，表示工作簿是否使用1904日期系统。|
|CheckCustomNumberFormat |获取或设置在设置Style.Custom时是否检查自定义数字格式。|
|Author |获取和设置文件的作者。|



例如，以下代码将ReCalculateOnOpen设置为false，以停止在打开文件时进行计算：

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 以下代码为文件设置了作者：

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


