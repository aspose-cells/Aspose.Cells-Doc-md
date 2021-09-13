---
title: Apply Shading to Alternate Rows and Columns with Conditional Formatting
type: docs
weight: 10
url: /java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs provide the means to add & manipulate conditional formatting rules for [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) object. These rules can be tailored in a number of ways to get the desired formatting based on conditions or rules. This article will demonstrate the use of Aspose.Cells for Java API to apply shading to alternate rows & columns with the help of conditional formatting rules and Excel's built-in functions.

{{% /alert %}} 
## **Apply Shading to Alternate Rows & Columns using Conditional Formatting**
This article makes use of Excel's built-in functions such as ROW, COLUMN & MOD. Here are little details of these functions for a better understanding of the code snippet provided ahead.

- **ROW()** function returns the row number of a cell reference. If the reference is omitted, it assumes that the reference is the cell address in which the ROW function has been entered in.
- **COLUMN()** function returns the column number of a cell reference. If the reference is omitted, it assumes that the reference is the cell address in which the COLUMN function has been entered in.
- **MOD()** function returns the remainder after a number is divided by a divisor, where the first parameter to the function is the numeric value whose remainder you wish to find and the second parameter is the number used to divide into the number parameter. If the divisor is 0, then it will return the #DIV/0! error.

Let us start writing some code to accomplish the goal with the help of Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



The following snapshot shows the resultant spreadsheet loaded in Excel application.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

In order to apply the shading to alternative columns, all you have to do is to change the formula **=MOD(ROW(),2)=0** as **=MOD(COLUMN(),2)=0**, that is; instead of getting the row index, modify the formula to retrieve the column index. 
The resultant spreadsheet, in this case, will look like the following image.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
