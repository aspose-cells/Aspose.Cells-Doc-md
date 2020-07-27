+++
title = "Working with Hyperlinks to Link Data" 
description = "" 
weight = 12175 
+++

Aspose.Cells for Java : Working with Hyperlinks to Link Data  

# Aspose.Cells for Java : Working with Hyperlinks to Link Data



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Hyperlinks to Link Data](#WorkingwithHyperlinkstoLinkData-AddingHyperlinkstoLinkData)
    *   1.1 [Adding Hyperlinks](#WorkingwithHyperlinkstoLinkData-AddingHyperlinks)
        *   1.1.1 [Adding Link to a URL](#WorkingwithHyperlinkstoLinkData-AddingLinktoaURL)
        *   1.1.2 [Adding a Link to a Cell in the Same File](#WorkingwithHyperlinkstoLinkData-AddingaLinktoaCellintheSameFile)
        *   1.1.3 [Adding a Link to an External File](#WorkingwithHyperlinkstoLinkData-AddingaLinktoanExternalFile)
{{< /panel >}}
 

## Adding Hyperlinks to Link Data

A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.

Using Aspose.Cells, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells and how they can be used in our Excel files.

### Adding Hyperlinks

Three types of hyperlink can be added to a cell using Aspose.Cells:

*   [Adding a link to a URL](https://docs2.aspose.com/cells/java/developerguide/data/working+with+hyperlinks+to+link+data).
*   [Adding a link to another cell in the same file](https://docs2.aspose.com/cells/java/developerguide/data/working+with+hyperlinks+to+link+data).
*   [Adding a link to an external file](https://docs2.aspose.com/cells/java/developerguide/data/working+with+hyperlinks+to+link+data).

Aspose.Cells allows developers to add hyperlinks to Excel files either by using the API or [designer spreadsheets](https://docs2.aspose.com/cells/java/developerguide/introduction/what+is+a+designer+spreadsheet) (spreadsheets where hyperlinks are created manually and Aspose.Cells is used to import them into other spreadsheets).

Aspose.Cells provides a class, [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) that represents a Microsoft Excel file. The [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) class contains a [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class provides different methods for adding different hyperlinks to Excel files.

#### Adding Link to a URL

The [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class contains a [Hyperlinks](https://apireference.aspose.com/java/cells/com.aspose.cells/HyperlinkCollection) collection. Each item in the [Hyperlinks](https://apireference.aspose.com/java/cells/com.aspose.cells/HyperlinkCollection) collection represents a [Hyperlink](https://apireference.aspose.com/java/cells/com.aspose.cells/Hyperlink). Add hyperlinks to URLs by calling the [Hyperlinks](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Hyperlinks) collection's [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method. The [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method takes the following parameters:

*   Cell name, the name of the cell the hyperlink will be added to.
*   Number of rows, the number of rows in this hyperlink range.
*   Number of columns, the number of columns of this hyperlink range
*   URL, the URL address.

  
In the above example, a hyperlink is added to a URL in an empty cell, **A1**. In such cases, if a cell is empty then the URL address is also added to that empty cell as its value. If the cell is not empty and a hyperlink is added the value of the cell looks like plain text. To make it look like a hyperlink, apply the appropriate formatting settings on that cell.

  

#### Adding a Link to a Cell in the Same File

It is possible to add hyperlinks to cells in the same Excel file by calling the [Hyperlinks](https://apireference.aspose.com/java/cells/com.aspose.cells/HyperlinkCollection) collection's [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method. The [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:

*   Cell name, the name of the cell the hyperlink will be added to.
*   Number of rows, the number of rows in this hyperlink range.
*   Number of columns, the number of columns in this hyperlink range.
*   URL, the address of the target cell.

  

#### Adding a Link to an External File

It is possible to add hyperlinks to external Excel files by calling the [Hyperlinks](https://apireference.aspose.com/java/cells/com.aspose.cells/HyperlinkCollection) collection's [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method. The [Add ](https://apireference.aspose.com/java/cells/com.aspose.cells/hyperlinkcollection#add(int,%20int,%20int,%20int,%20java.lang.String))method takes the following parameters:

*   Cell name, the name of the cell the hyperlink will be added to.
*   Number of rows, the number of rows in this hyperlink range.
*   Number of columns, the number of columns in this hyperlink range.
*   URL, the address of the target, external Excel file.

