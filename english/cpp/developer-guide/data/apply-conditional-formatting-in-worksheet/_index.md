---
title: Apply Conditional Formatting in Worksheet
type: docs
weight: 40
url: /cpp/apply-conditional-formatting-in-worksheet/
---

## **Possible Usage Scenario**
Aspose.Cells allows you to add all sorts of Conditional Formatting e.g. Formula, Above Average, Color Scale, Data Bar, Icon Set, Top10, etc. It provides the [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) class which has all the necessary methods to apply conditional formatting of your choice. Here is the list of a few of Get methods.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Apply Conditional Formatting in Worksheet**
The following sample code shows how to add a Cell Value conditional formatting on cells A1 and B2. Please see the [output excel file](23167004.xlsx) generated by the code and the following screenshot which explains the effect of the code on the [output excel file](23167004.xlsx). If you will put some value greater than 100 in cell A2 and B2, the Red fill color from cell A1 and B2 will disappear.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
