---
title : "Managing Page Breaks" 
description : "" 
weight : 12146 
toc : false
type: docs
url: /net/developerguide/worksheets/managing+page+breaks/
---

# Aspose.Cells for .NET : Managing Page Breaks


According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

The location of the cell where the page break is added, the page is ended and the rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

*   Horizontal page break
*   Vertical page break

In the rest of the discussion, we will describe how can you add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Page Breaks](#page-breaks)
    *   1.1 [Adding Page Breaks](#adding-page-breaks)
    *   1.2 [Clearing All Page Breaks](#clearing-all-page-breaks)
    *   1.3 [Removing Specific Page Break](#removing-specific-page-break)
*   2 [Important to know](#important-to-know)
{{< /panel >}}
 

 

## Page Breaks

Aspose.Cells provides a [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a wide range of properties and methods used to manage a worksheet.

To add the page breaks, use the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class' [HorizontalPageBreaks](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/horizontalpagebreaks) and [VerticalPageBreaks](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/verticalpagebreaks) properties.

The [HorizontalPageBreaks](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/horizontalpagebreaks) and [VerticalPageBreaks](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/verticalpagebreaks) properties are collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks.

### Adding Page Breaks

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [HorizontalPageBreakCollection.Add()](https://apireference.aspose.com/net/cells/aspose.cells/horizontalpagebreakcollection/methods/add/index) and [VerticalPageBreakCollection.Add()](https://apireference.aspose.com/net/cells/aspose.cells/verticalpagebreakcollection/methods/add/index) methods. Each **`Add`** method takes the name of the cell where the break should be added.

In page break preview or print preview modes, you can see how these page breaks work.

### Clearing All Page Breaks

To clear all page breaks in a worksheet, call the [HorizontalPageBreakCollection](https://apireference.aspose.com/net/cells/aspose.cells/horizontalpagebreakcollection) and [VerticalPageBreakCollection](https://apireference.aspose.com/net/cells/aspose.cells/verticalpagebreakcollection) collections' [Clear()](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear) methods.

### Removing Specific Page Break

To remove a specific page break, call the [HorizontalPageBreakCollection.RemoveAt()](https://apireference.aspose.com/net/cells/aspose.cells/horizontalpagebreakcollection/methods/removeat) and [VerticalPageBreakCollection.RemoveAt()](https://apireference.aspose.com/net/cells/aspose.cells/verticalpagebreakcollection/methods/removeat) methods. Each **RemoveAt **method takes the index of the page break about to be removed.

## Important to know

When you set **FitToPages **properties (that is [FitToPagesTall](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopagestall) and [FitToPagesWide](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopageswide)) in page setup settings, the page break settings are affected, so, if you print the worksheet, the page break settings are not considered although they are still set.

