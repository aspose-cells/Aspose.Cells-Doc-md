---
title: Aspose.Cells for Java Vs Open Source Competitors
type: docs
weight: 1089
url: /java/aspose-cells-for-java-vs-open-source-competitors/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article compares the feature of [Aspose.Cells for Java](https://products.aspose.com/cells/java/) with its open source competitors. The document compares Aspose.Cells for Java with [JExcelAPI](http://jexcelapi.sourceforge.net/) and [POI](http://poi.apache.org/)'s HSSF for some common set of features.

{{% /alert %}}

## **Overview**

The majority of business scenarios demand sophisticated reports that are rich in content and focused on the needs of the specific decisions or tasks that general management will use them for. They also require some means of data collection, analysis and interfacing with database systems.

A common solution is using spreadsheets for data collection, analysis and as a presentation tool. The solution should be able to create fully formatted Microsoft Excel files that can analyze a business scenario and, ideally, extend these basic features to explore the processes of capturing and exporting data to other widely used office applications. These developments may include making use of the built-in features and functions of Microsoft Excel.

We come across different spreadsheet components in the market today that really promise to feature-rich APIs for spreadsheet management. Here, we do a feature analysis of Aspose.Cells for Java compared to its open source competitors JExcelAPI and POI's HSSF. Let me give some introduction of the three first.

## **Aspose.Cells for Java**

Aspose.Cells for Java is a flexible component that enables Java applications to create and manage Excel spreadsheets without Microsoft Excel installed on the system (client or server). Unlike similar products from other vendors, Aspose.Cells for Java not only supports spreadsheet generation and basic file formatting features, but also a number of advanced features. These advanced features make it easy for developers to manipulate spreadsheet contents, cell formatting and file protection options.

Aspose.Cells for Java can also import data into spreadsheets from different data sources, add common and complex mathematical, date/time, financial, text formulas and functions, import pictures (all major formats are supported including BMP, GIF, JPG, PNG, WMF, EMF and more), create comments, create drawing objects and controls, and perform a range of other tasks.

Aspose.Cells for Java also sup ports add-ins, VBA and macros.

### **Open and Save**

Besides supporting common features like creating or reading native Excel files, Aspose.Cells for Java also offers many valuable features such as saving and opening Excel files (Excel 97 - Excel 2007) to and from streams, importing and exporting data from a ResultSet and array,

Aspose.Cells can import charts, named ranges, headers and footers with all attributes that Microsoft Excel provides, insert hyperlinks and images, and import formulae from a designer spreadsheet.

### **Formatting**

Worksheet data formatting is important because it can change the meaning of your data. If you plan to print a worksheet, email it to clients, or show it to your boss, you need to think about whether it is formatted in a viewer-friendly way. Careful use of color, shading, borders, fonts, number formatting, alignment, indentation and orientation can make the difference between a messy glob of data and a worksheet that’s easy to work with and understand.

Aspose.Cells for Java provides the flexibility to draw borders around cells and cell ranges easily. Moreover the AIP can apply font settings (family and type, style, size, color and alignment) and shade cells with background patterns. The API is efficient enough that you can format a complete row or column, set alignments, wrap and rotate the text in cells.

Aspose.Cells for Java supports all types of number formats including general format, numbers in decimal notations, currency symbols, percentages, scientific format, date/time values and even custom number formats.

Aspose.Cells allows developers to auto-fit rows and columns in one action, as well as configure all types of page setup options in a convenient API: top, left, bottom, right, header and footer margins, orientation - portrait or landscape - scaling, paper size, print area, repeating rows and columns and many more.

### **Unique Features**

There are also a number of unique features that developers will only find in Aspose.Cells for Java, for example support for a wide range of formats including XLS, XLT, XLSX, CSV, SpreadsheetML, Tab delimited, TXT, XML and HTML.

The API also allows developers to add a copy of an existing worksheet (with full contents, images and charts) to a file, set gradient background for charts through the API, create comments, set locale and region settings, auto-filters and page breaks, set complex formulae, conditional formatting, all types of protection options introduced in Microsoft Excel XP or above, and manipulate named ranges.

Further, Aspose.Cells adds a custom chart API and efficient formula calculation engine.

### **Try Aspose.Cells for Java**

Aspose.Cells for Java has a huge list of features. To find out more about the features and for the Programmer’s Guide, please check [the documentation](/cells/java/) and [online demos](https://github.com/aspose-cells/Aspose.Cells-for-Java).

Please try the component to see the difference between it and its competitors. The evaluation version is totally free without any time limitation. [Download](https://downloads.aspose.com/cells/java) the evaluation version for free.

## **Other APIs**

### **JExcelAPI**

JExcelAPI is a Java API used to read, write and modify Excel spreadsheets. It is an open source Java API which allows Java developers to read Excel spreadsheets and to generate Excel spreadsheets dynamically. In addition, it contains a mechanism which allows Java applications to read a spreadsheet, modify cells, and write the new spreadsheet.

At the time of writing, it has a limited set of features. It supports: reading and writing native Microsoft Excel file (Excel97-2003) in XLS file format only. It has some limited formula calculation support. It can manipulate fonts, support number and date formatting, modify existing worksheets, locale settings, preserving charts (but does not allow developers to create or manipulate charts), inserting images and so on.

#### **Limited Chart Support**

JExcelApi has limited support for charts: It does not support to create and manipulate charts. When copying a spreadsheet containing a chart, the chart is written out to the generated spreadsheet (as long as the sheet containing the chart contains other data as well as the chart). All image information is preserved when copying excel files, however, when adding an image to a spreadsheet only image s in PNG format are supported.

#### **Cannot Copy Worksheets**

There is no API for copying worksheets within or between workbooks directly. This task can be done in an indirect way, but requires some work to be done. For example, using loops, copy cell by cell with the WritableCell.copyTo() method, which will produce a deep copy. However the format is only shallow copied, so you will need to get the cell format and use the copy constructor of that, and then call WritableCell.setCellFormat() on the cell you have just copied. It's quite a big job.

#### **No Optimization**

Another limitation is JExcelAPI does not perform optimizations to reduce file size, we should not be surprised to see an output file generated by the component with a huge size in MBs.

JExcelAPI has no API for auto-fitting rows or columns. You'll need to write code that scans the cells in each column, calculates the maximum length, and then make calls to WritableSheet.setColumnView() and Writable Sheet.setRowView() accordingly.

#### **Missing Features**

There are also a few more hurdles: The API does not support pivot tables and drop down lists. It has limited validation options to set on the cells. The page setup and printing options are not completely supported, for example repeating rows and columns and not all types of protection options (including password protection related sheets) are supported. It also does not support data sorting, auto-filter data, conditional formatting, drawing objects, controls and many more valuable features.

### **POI-HSSF**

HSSF is the component of POI that reads and writes Excel spreadsheets. It has an extended set of features compared to JExcelAPI, including reading and writing native Microsoft Excel file (Excel97-2003 - XLSX OOXML file format is not supported yet), formatting cells (number formats, fonts, colors, borders, alignments etc.), merging cells, page setup options, importing images, shapes, named ranges, creating comments, headers and footers, hyperlinks, auto-fitting rows and columns etc.

#### **Limited Chart Support**

There are a few known limitations for the POI-HSSF API. For example, you can not currently create charts. You can however create a chart in Excel, modify the chart data values using HSSF and write a new spreadsheet out. Another one is pivot table support, generating pivot tables is not possible.

#### **Formula Calculation**

Although POI's org.apache.poi.hssf.usermodel does support formulas but it lacks a rich formula calculation engine. It supports formulas containing cell references string, integer and floating point literals, relative or absolute references, arithmetic and logical operators but it does not support array formulas, unary operators and 3D references.

#### **Missing Features**

HSSF API does not support PivotTables either. It has limited data validation options to set on the cells. It also does not support the features like data sorting and auto-filtering data.

## **Feature Comparison**

The following table attempts to provide a feature overview on how Aspose.Cells for Java matches up to the open source components (mentioned above) although it does not challenge to cover all features provided by the products involved. This is just an outline which is taken at some specific time and it is quite possible that the missing features could be supported when you will be reading out the document.

|**Feature** |**JExcelAPI** |**POI’s HSSF** |**Aspose.Cells for Java** |
| :- | :- | :- | :- |
|**File formats**|  |  |  |
|Read and write file formats (XLS, XLT, XLSX, CSV, SpreadsheetML, Tab Delimited, TXT, XML and HTML) |Partially Supported |Partially Supported |Supported |
|Open file and save to a stream |  | |Supported |
|Convert Excel file to PDF document |  | |Supported |
|Password protected files | |Supported |Supported |
|Manipulate spreadsheet content |  |  |  |
|Modify the document properties of Excel files |  | |Supported |
|Export Worksheet data to an array |  |  |Supported |
|Import data from a ResultSet |  |  |Supported |
|Import data from an array, collection |  | |Supported |
|Add a copy of existing worksheet (all contents including images and charts) |Partially Supported |Partially Supported |Supported |
|Import images |  | |Supported |
|Import charts |  | |Supported |
|Set gradient background for charts using API |  |  |Supported |
|Protect worksheet, including contents, objects and scenarios |Partially Supported |Supported |Supported |
|Create auto-filters using API |  |  |Supported |
|Page setup features (top, left, bottom, right, header and footer margins, orientation - portrait or landscape, scaling, paper size, printing area, repeating rows and columns) |Partially Supported |Supported |Supported |
|Horizontal and vertical page breaks through the API |Supported |Supported |Supported |
|Copy and move worksheets within and between workbooks | |Supported |Supported |
|Inserting and deleting rows and columns |Supported | |Supported |
|Auto-fit rows and columns | |Supported |Supported |
|Copy rows and columns | | |Supported |
|Data sorting | | |Supported |
|Trace precedents and dependents | | |Supported |
|Auto-filtering | | |Supported |
|Data Validation (all types) |Partially Supported |Partially Supported |Supported |
|Import formulae from designer spreadsheet |Partially Supported |Partially Supported |Supported |
|Set complex formulae through API |  |  |Supported |
|Conditional formatting |  |Supported   |Supported |
|Activating sheets and making an active Cell in the workbook. |Supported |Supported |Supported |
|**Advanced Features**| | | |
|Smart markers |  |  |Supported |
|Create standard charts (column, bar, line, pie, scatter, area, doughnut, radar, surface 3D, bubble, stock, cylinder, cone, pyramid etc.) | | |Supported |
|Custom chart API | | |Supported |
|Document properties settings |  | |Supported |
|Advanced Excel XP protection options |  |  |Supported |
|Add-ins, VBA, macros |  | |Supported |
|Manipulate named ranges |Supported |Supported |Supported |
|Pivot tables | | |Supported |
|Create common drawing objects, shapes and controls | |Supported |Supported |
|Insert controls into charts | | |Supported |
|Formula Calculation Engine |  |  |Supported |
|Find API |Supported |Supported |Supported |
{{< app/cells/assistant language="java" >}}
