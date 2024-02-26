---
title: Setting Dynamic Array Formulas
description: How to use Aspose.Cells library to calculate dynamic array formulas in Microsoft Excel. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to calculate the dynamic array formula and get the result. Finally, we save the modified Excel file to disk.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /net/calculation-of-dynamic-array-formulas/
---
## **What is the Excel Array Formula**
In Excel, an array formula is a special type of formula that allows you to perform calculations on arrays of data rather than individual cells. Array formulas can be used to perform complex calculations, manipulate data, and solve specific problems efficiently. They are entered differently from regular formulas and often require the use of Ctrl + Shift + Enter.

Here are some key points about array formulas in Excel:
1. Syntax:
<br>
Array formulas are written like regular formulas but involve operations on arrays of values. They are enclosed in curly braces { } to indicate that they are array formulas. However, you don't type these curly braces yourself; Excel adds them automatically when you enter the formula correctly.
1. Entering Array Formulas:
<br>
To enter an array formula, you type the formula into the formula bar.Instead of pressing Enter to finish, you press Ctrl + Shift + Enter. This tells Excel that it's an array formula. When entered correctly, Excel displays the formula within curly braces in the formula bar to indicate that it's an array formula.
1. Use Cases:
<br>
Array formulas are useful for performing calculations across multiple cells or ranges simultaneously. They can be used for advanced mathematical calculations, conditional operations, filtering data, and more.
1. Benefits:
<br>
Array formulas allow you to perform complex calculations in a single formula, which can improve efficiency and simplify your worksheets. They can handle large datasets and perform calculations that would otherwise require multiple intermediate steps.
1. Limitations:
<br>
Array formulas can be more difficult to understand and troubleshoot than regular formulas. They can slow down worksheet performance, especially if used extensively or with large datasets.
1. Examples:
<br>
Summing the values in a range: **{=SUM(A1:A5*B1:B5)}**
<br>
Finding the maximum value in a range: **{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Remember that array formulas should be used judiciously, and it's important to understand how they work before implementing them in your worksheets. They can be powerful tools for data analysis and manipulation in Excel.

## **What is the Excel Dynamic Array Formula**
Dynamic array formulas are a new feature introduced in Excel 365 and Excel 2021. They allow you to work with arrays of data more seamlessly and efficiently compared to traditional array formulas. Dynamic array formulas automatically spill results into neighboring cells, eliminating the need for Ctrl + Shift + Enter and allowing for easier manipulation of data.

Key points about dynamic array formulas in Excel:
1. Automatic Spilling:
<br>
Dynamic array formulas automatically spill results into adjacent cells based on the size of the output data. This means you don't need to select a range of cells before entering the formula or use Ctrl + Shift + Enter to confirm the formula.
1. Single-Cell Entry:
<br>
Dynamic array formulas are entered into a single cell, and Excel automatically populates the neighboring cells with the results. This makes it easier to manage and understand formulas, as you only need to input the formula once.
1. New Functions:
<br>
Dynamic array formulas introduce new functions that can handle arrays natively, such as **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY**, and **RANDARRAY**. These functions can return multiple values or manipulate arrays directly, simplifying complex calculations.
1. Flexible Range Handling:
<br>
Dynamic array formulas adjust the size of the spilled range dynamically based on the size of the input data or the calculation performed. This flexibility allows for more efficient use of worksheet space and simplifies formula creation.
1. Improved Performance:
<br>
Dynamic array formulas can improve performance compared to traditional array formulas, especially when working with large datasets or complex calculations.
1. Compatibility:
<br>
Dynamic array formulas are available in Excel 365 and Excel 2021. They may not be supported in older versions of Excel.
1. Examples of dynamic array formulas:
<br>
**FILTER**: Returns an array of values that meet specified criteria.
<br>
**SORT**: Sorts the values in a range or array.
<br>
**UNIQUE**: Returns unique values from a list or range.
<br>
**SEQUENCE**: Generates a sequence of numbers or dates.
<br>
**RANDARRAY**: Generates an array of random numbers.
<br>
<image src="2.png" width="70%" />
<br>

Dynamic array formulas offer powerful capabilities for data manipulation and analysis in Excel, making it easier to work with arrays of data and perform complex calculations efficiently.

## **What is the difference of Array Formulas and Dynamic Array Formulas in Excel**
In Excel, both array formulas and dynamic array formulas are used to perform calculations on multiple values simultaneously, but they have some differences in terms of functionality and how they are implemented.

### **Array Formulas Features**
1. Array formulas are traditional formulas in Excel that can perform calculations on arrays of data.
1. They are entered by pressing Ctrl + Shift + Enter after typing the formula, which tells Excel that it's an array formula.
1. Array formulas have limitations in terms of their ability to spill results into adjacent cells. They typically return a 1. single result, although that result might be a cell array.
1. They have been around for a long time and are supported in all versions of Excel.

### **Dynamic Array Formulas Features**
1. Dynamic array formulas are a new feature introduced in Excel 365 (Office 365 subscription) and Excel 2021.
1. They automatically spill results into adjacent cells based on the size of the input data or the formula's calculation.
1. Dynamic array formulas don't require pressing Ctrl + Shift + Enter; you simply type the formula into one cell, and Excel automatically populates the adjacent cells with the results.
1. These formulas have the ability to return multiple results (a range of cells) directly without the need for an array formula or Ctrl + Shift + Enter.
1. They have new functions like **FILTER**, **SORT**, **UNIQUE**, etc., which can handle arrays natively and return results in a dynamic array format.
In summary, dynamic array formulas are a more modern and convenient way to work with arrays in Excel, providing automatic spilling of results and simplifying the process of working with arrays compared to traditional array formulas. However, they are only available in the newer versions of Excel that support dynamic arrays.

## **How to Set and Refresh Dynamic Array Formulas in Excel**
Setting up dynamic array formulas in Excel involves using specific functions that are designed to work with arrays of data and allow the results to automatically spill into neighboring cells. 

Here's a step-by-step guide to setting up dynamic array formulas:
1. Select the Cell:
<br>
Choose the cell where you want the dynamic array formula results to appear. Dynamic array formulas spill the results into adjacent cells, so make sure there's enough space for the spilled output.
1. Enter the Formula:
<br>
Type the dynamic array formula into the formula bar of the selected cell. Use one of the dynamic array functions available in Excel 365 and Excel 2021, such as **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY**, or **RANDARRAY**. 
<br>
For example, you might use the FILTER function to filter a list of data based on specific criteria: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Press Enter:
<br>
After typing the formula, simply press Enter on your keyboard. Unlike traditional array formulas, you don't need to press Ctrl + Shift + Enter.
1. Observe the Spilled Range:
<br>
Excel automatically spills the results of the formula into neighboring cells. The spilled range adjusts dynamically based on the size of the output data or the calculation performed by the formula. Excel highlights the spilled range with a border and a diagonal arrow icon to indicate that it contains spilled data.
1. Interact with the Spilled Range:
<br>
You can interact with the spilled range just like any other range of cells in Excel. Use the spilled range in other formulas, perform calculations on it, format it, or reference it in charts or tables.
1. Update the Formula:
<br>
If you need to modify the dynamic array formula, simply edit the formula in the original cell where it was entered.
After editing, press Enter again to confirm the changes. Excel will automatically update the spilled range if necessary.
1. Clearing the Spilled Range:
<br>
If you want to clear the spilled data, you can delete the formula from the original cell. Excel will clear the spilled range as well. Alternatively, you can delete the spilled range directly by selecting it and pressing the Delete key.
<br>

By following these steps, you can set up dynamic array formulas in Excel to efficiently analyze and manipulate arrays of data, allowing for easier data analysis and reporting tasks.

## **How to Set and Refresh Dynamic Array Formulas Using Aspose.Cells**
Please see the following sample code that loads the [sample Excel file](dynamicArrayFormula.xlsx) which contains some dummy data. After loading the file, call the [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) function to set dynamic array formula and  [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) function to refresh dynamic array formulas before calling formula calculation, and finally save the workbook as [output Excel file](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

The output snapshot:
<br>
<image src="4.png" width="70%" />