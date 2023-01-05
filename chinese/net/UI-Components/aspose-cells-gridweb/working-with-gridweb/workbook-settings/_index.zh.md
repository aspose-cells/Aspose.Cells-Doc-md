---
title: 工作簿的设置
type: docs
weight: 250
url: /zh/net/aspose-cells-gridweb/workbook-settings/
description: 本文介绍 GridWeb 的工作簿设置。
keywords: settings
---
我们可以通过 set GridWorkbookSettings 指定一些设置：

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**姓名** |**描述** |
|:- |:- |
|最大迭代次数|获取或设置解决循环引用的最大迭代次数，默认值为100。|
|迭代|获取或设置是否使用迭代来解决循环引用。|
|强制完全计算|获取或设置每次触发计算时是否完全计算。|
|创建计算链|获取或设置是否创建计算公式链。默认为假。|
|打开时重新计算|获取或设置是否在打开文件时重新计算所有公式。|
|显示精度|如果此工作簿中的计算将仅使用数字显示时的精度来完成，则为真|
|日期1904|获取或设置一个值，该值表示工作簿是否使用 1904 日期系统。|
|检查自定义编号格式|获取或设置设置Style.Custom时是否勾选自定义数字格式。|
|作者|获取和设置文件的作者。|
 


例如，以下代码将 ReCalculateOnOpen 设置为 false 以在打开文件时停止计算：

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

以下代码设置文件的作者：

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 