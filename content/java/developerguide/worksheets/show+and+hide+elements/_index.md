---
title : "Show and Hide Elements" 
description : "" 
weight : 12136 
toc : false
type: docs
url: /java/developerguide/worksheets/show+and+hide+elements/
---

# Aspose.Cells for Java : Show and Hide Elements



Aspose.Cells allows the user to show and hide elements of a workbook includeing worksheets, rows, columns, tabs, scrollbars, gridlines,

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Show and Hide a Worksheet](#show-and-hide-a-worksheet)
    *   1.1 [Making a Worksheet Visible](#making-a-worksheet-visible)
    *   1.2 [Hiding a Worksheet](#hiding-a-worksheet)
*   2 [Show or Hide Tabs](#show-or-hide-tabs)
    *   2.1 [Hiding Tabs](#hiding-tabs)
    *   2.2 [Making Tabs Visible](#making-tabs-visible)
*   3 [Show and Hide Rows and Columns](#show-and-hide-rows-and-columns)
    *   3.1 [Hiding Row/Column Headers](#hiding-row/column-headers)
    *   3.2 [Making Row/Column Headers Visible](#making-row/column-headers-visible)
*   4 [Show and Hide Scroll Bars](#show-and-hide-scroll-bars)
    *   4.1 [Hiding Scroll Bars](#hiding-scroll-bars)
    *   4.2 [Making Scroll Bars Visible](#making-scroll-bars-visible)
*   5 [Show and Hide Gridlines](#show-and-hide-gridlines)
    *   5.1 [Controlling the Visibility of Gridlines](#controlling-the-visibility-of-gridlines)
        *   5.1.1 [Making Gridlines Visible](#making-gridlines-visible)
        *   5.1.2 [Hiding Gridlines](#hiding-gridlines)
    *   5.2 [Related Articles](#related-articles)
{{< /panel >}}
 

## Show and Hide a Worksheet

An Excel file can have one or more than one worksheets. Whenever we create an Excel file, we add worksheets to the Excel file in which we work. Each worksheet in an Excel file is independent from the other worksheet by having its own data and formatting settings etc. Sometimes, developers may require to make few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells** allows developers to control the visibility of the worksheets in their Excel files.

**Controlling the Visibility of the Worksheets:**  
Aspose.Cells provides a class, **Workbook** that represents an Excel file. **Workbook** class contains a **WorksheetCollection** that allows to access each worksheet in the Excel file.

A worksheet is represented by the **Worksheet** class. **Worksheet** class provides a wide range of properties and methods to manage a worksheet. But, to control the visibility of a worksheet, developers may use **setVisible** *{*} method of the **Worksheet** class.

### Making a Worksheet Visible

Developers can make a worksheet visible by setting the *setVisible(* *true* *)* method of the **Worksheet** class.

### Hiding a Worksheet

Developers can hide a worksheet by setting the setVisible(false) method of the **Worksheet** class.

**Example:**  
A complete example is given below that demonstrates the use of *setVisible(* *false* *)* method of **Worksheet** class to hide the first worksheet of the Excel file.

**Worksheet - Before Modification:**  
In the screenshot below, you can see that **Book1.xls** file contains three worksheets: **Sheet1** , **Sheet2** and **Sheet3** .  
  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472332.png)

**Figure:** Worksheet view before any modification

**Worksheet - After Executing the Example Code**  
{\_}  
**Book1.xls** file is opened by calling the **Open** method of **Workbook** class and then the first worksheet of the **Book1.xls** file is made hidden. The modified file is saved as **output.xls** file whose pictorial view is shown below:  
  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472333.png)

**Figure:** Worksheet view after modification

**Setting VisibilityType**  
You can also hide the worksheets in a special way. This feature can h ide the worksheet so that the only way for you to make it visible again is by giving **VisibilityType.VERY\_HIDDEN** as parameter value for the **setVisibilityType** \*\* method in the code ( it is to be noted here, the user s cannot make the object visible in MS Excel directly by using its menu options). Users can also use **getVisibilityType** method to check whether a worksheet is marked as VeryHidden or not.

## Show or Hide Tabs

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

*   Sheet tabs.
*   Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

**Sheet tabs & tab scrolling buttons**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472329.png)

Using Aspose.Cells, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.

**Controlling the Visibility of Tabs:**  
Aspose.Cells provides a class, [`Workbook`](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook), that represents a Microsoft Excel file. The `Workbook` class provides a wide range of properties and methods for managing an Excel file. To control the visibility of tabs in an Excel file, developers can use the `Workbook` class' `setSheetTabBarHidden` method.

### Hiding Tabs

Hide tabs in an Excel file by setting the `Workbook` class' `getSettings().setShowTabs(false)` method.

### Making Tabs Visible

Make tabs visible with the `Workbook` class' `setSheetTabBarHidden(false)` method.

**Complete Code Example:**

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls.

You can see that Book1.xls file contains tabs in the figure below. After the example code is executed, the tabs are hidden, as you can see from the screenshot of the output.xls file below.

**book1.xls: Excel file before any modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472330.png)

**output.xls: Excel file after modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472331.png)

## Show and Hide Rows and Columns

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them, and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.

**Controlling the Visibility of the Worksheets:**

Aspose.Cells provides a class, [`Workbook`](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook), that represents a Microsoft Excel file. The `Workbook` class contains a `WorksheetCollection` that allows access to each worksheet in an Excel file.

A worksheet is represented by the [`Worksheet`](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The `Worksheet` class provides a wide range of properties and methods for managing worksheets. To control the visibility of row and column headers, use the `Worksheet` class' `setRowColumnHeadersVisible` method.

### Hiding Row/Column Headers

Hide row and column headers by using the `Worksheet` class' `setRowColumnHeadersVisible(false)` method.

### Making Row/Column Headers Visible

Make row and column headers visible by using the `Worksheet` class' `setRowColumnHeadersVisible(true)` method.

A complete example is given below that demonstrates how to use the `Worksheet` class' `setRowColumnHeadersVisible(false)` method to hide row and column headers of the first worksheet of an Excel file.

The screenshot below shows that Book1.xls contains three worksheets: Sheet1, Sheet2 and Sheet3. Each worksheet is showing row and column headers.

**Book1.xls: worksheet before modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472325.png)

Book1.xls is opened by calling the `Workbook` class' `Open` method and the row and column headers on the first worksheet are hidden. The modified file is saved as output.xls.

**Worksheet view after modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472326.png)

## Show and Hide Scroll Bars

Scroll bars are very used to navigate the contents of any file. Normally, there are two kinds of scroll bars:

*   Vertical scroll bars
*   Horizontal scroll bars

Microsoft Excel also provides horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells, developers can control the visibility of both types of scroll bars in Excel files.

**Controlling the Visibility of the Scroll Bars:**

Aspose.Cells provides a class, **Workbook** that represents an Excel file. **Workbook** class provides a wide range of properties and methods to manage an Excel file. But, to control the visibility of the scroll bars in the Excel file, developers may **use** **setVerticalScrollBarHidden** & **setHorizontalScrollBarHidden** methods of the **Workbook** class.

### Hiding Scroll Bars

Hide scroll bars by setting the `Workbook` class' `setVerticalScrollBarHidden()` or `setHorizontalScrollBarHidden()` methods to false.

### Making Scroll Bars Visible

Make scroll bars visible by setting the `Workbook` class' `setVerticalScrollBarHidden()` or `setHorizontalScrollBarHidden()` methods to true.

**Complete Code Example:**

Below is a complete code that opens an Excel file, book1.xls, hides both scroll bars and then saves the modified file as output.xls.

The screenshot below shows Book1.xls file containing both scroll bars. The modified file is saved as output.xls file, also shown below.

**Book1.xls: Excel file before any modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472327.png)

**output.xls: Excel file after modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472328.png)

## Show and Hide Gridlines

All Microsoft Excel worksheets have gridlines by default. They help delineate cells, so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.

Aspose.Cells also allows you to control the visibility of the gridlines.

### Controlling the Visibility of Gridlines

Aspose.Cells provides a class, [`Workbook`](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) that represents a Microsoft Excel file. The `Workbook` class contains a `WorksheetCollection` that allows access to each worksheet in the file.

A worksheet is represented by the [`Worksheet`](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The `Worksheet` class provides a wide range of properties and methods for managing worksheets. To control the visibility of gridlines, use the the `Worksheet` class' `setGridlinesVisible` method.

#### Making Gridlines Visible

To make gridlines visible, use the the `Worksheet` class' `setGridlinesVisible(true)` method.

#### Hiding Gridlines

Hide gridlines using the the `Worksheet` class' `setGridlinesVisible(false)` method.

Gridlines are applied to the entire sheet. To 'hide' gridlines on a section of a worksheet, use [border formatting](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/create+table+by+using+border+lines+for+a+range) to set the borders to a color that blends into the sheet's color scheme.

**Example: Hiding Gridlines on a Particular Worksheet**

The example below demonstrates the use of the `Worksheet` class' `setGridlinesVisible(false)` method to hide gridlines of the first worksheet of an Excel file.

The screenshot below shows that the Book1.xls file contains three worksheets: Sheet1, Sheet2 and Sheet3. All of these worksheets have gridlines.  
  
**Worksheet view before modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472323.png)

The Book1.xls file is opened by calling the `Open` method of the `Workbook` class and then the gridlines of the first worksheet are hidden. The modified file is saved as output.xls file.  
  
**Worksheet view after modification**  
![](https://docs2.aspose.com/cells/java/attachments/5276190/5472324.png)

### Related Articles

*   [Printing gridlines and setting other printing options](/pages/createpage.action?spaceKey=cellsjava&title=Setting+Print+Options&linkCreation=true&fromPageId=5276190).
*   [Adding borders to cells to create a table](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/create+table+by+using+border+lines+for+a+range).

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Gridlines-001.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472323.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Gridlines-002.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472324.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Row Column Headers-001.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472325.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Row Column Headers-002.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472326.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Scroll Bars-001.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472327.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Scroll Bars-002.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472328.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Tabs-001.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472329.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Tabs-002.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472330.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Display or Hide Tabs-003.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472331.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Hide or Unhide a Worksheet-001.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472332.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Hide or Unhide a Worksheet-002.png](https://docs2.aspose.com/cells/java/attachments/5276190/5472333.png) (image/png)  

