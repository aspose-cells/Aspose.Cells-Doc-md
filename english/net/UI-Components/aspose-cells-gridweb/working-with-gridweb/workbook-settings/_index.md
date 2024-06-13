---
title: Settings for workbook
type: docs
weight: 250
url: /net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: This article describes the workbook settings in GridWeb.
keywords: GridWeb,settings
---


There are some settings we can specified by set GridWorkbookSettings :

 
- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Name** |**Description** |
| :- | :- |
|MaxIteration |Gets or sets the maximum number of iterations to resolve a circular reference,the default value is 100. |
|Iteration | Gets or sets  whether use iteration to resolve circular references. |
|ForceFullCalculate | Gets or sets   whether fully calculates every time when a calculation is triggered. |
|CreateCalcChain | Gets or sets  whether create calculated formulas chain. Default is false. |
|ReCalculateOnOpen | Gets or sets  whether re-calculate all formulas on opening file. |
|PrecisionAsDisplayed | True if calculations in this workbook will be done using only the precision of   the numbers as they're displayed |
|Date1904 | Gets or sets a value which represents if the workbook uses the 1904 date system. |
|CheckCustomNumberFormat | Gets or sets whether checking custom number format when setting Style.Custom. |
|Author |Gets and sets the author of the file. |
 


For example, the following code set the ReCalculateOnOpen to false to stop the caculate on opening the file :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 the following code set the author for the file :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 