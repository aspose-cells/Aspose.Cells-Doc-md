---
title: Excel – R1C1 Reference Style vs. A1
type: docs
weight: 30
url: /nodejs-cpp/r1c1-reference-style-vs-a1/
description: R1C1 Reference Style VS. A1 style by using Aspose.Cells for Node.js via C++.
keywords: R1C1 Reference Style VS. A1 style Node.js via C++, R1C1 Reference Style Node.js via C++, How to switch between R1C1 Reference Style and A1 Reference Style Node.js via C++, A1 Reference style Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In Excel, R1C1 and A1 are two different reference styles used to identify cells in a worksheet. Note that the choice between A1 and R1C1 is largely a matter of personal preference. Most users are more familiar with A1 style, but R1C1 can be useful in certain situations, especially when working with formulas and calculations.

## **A1 Reference Style**

This is the default reference style in Excel. In A1 style, columns are identified by letters (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), and rows are identified by numbers (1, 2, 3, ...). For example, the cell in the first column and second row is referred to as A2.

## **R1C1 Reference Style**

In R1C1 style, both rows and columns are identified by numbers. The letter “R” represents the row number, and the letter “C” represents the column number. For example, R2C1 refers to the cell in the second row and first column.

Any numbers in square brackets refer to relative distance from the current cell. Unlike A1, which refers to columns followed by the row number, R1C1 does the opposite—rows followed by columns (which does take some getting used to). Positive numbers will refer to cells below and/or across to the right. Negative numbers will refer to cells above and/or to the left.

For example, R[2]C[3] is a cell 2 rows down and 3 columns to the right. R[-1]C[-4] is a cell 1 row up and 4 columns to the left. If no number is shown in brackets, then you are referring to the same row or column, i.e., R[3]C will be a cell 3 rows below the current cell in the same column.  
<br>
<image src="2.png" width="70%" />

## **Comparison for R1C1 Reference Style and A1 Reference Style**
Here's a quick comparison:
|**A1 Style**|**R1C1 Style**|
| :- | :- |
|A1|R1C1|
|B3|R3C2|
|G10|R10C7|
|AA25|R25C27|

## **How to switch between R1C1 Reference Style and A1 Reference Style**
You can switch between these reference styles in Excel settings. To change the reference style:

1. Go to the "File" tab.  
2. Select "Options" at the bottom.  
3. In the Excel Options dialog box, go to the "Formulas" category.  
4. Under the "Working with formulas" section, check or uncheck the "R1C1 reference style" option.  
5. Click "OK" to apply the changes.  
<br>
<image src="1.png" width="70%" />

## **How to use R1C1 Reference Style and A1 Reference Style in Excel**
The following example shows how to calculate the sum of two cell values in two styles.  
<br>
A1 Reference Style:  
<br>
<image src="4.png" width="70%" />

R1C1 Reference Style:  
<br>
<image src="3.png" width="70%" />
{{< app/cells/assistant language="nodejs-cpp" >}}
