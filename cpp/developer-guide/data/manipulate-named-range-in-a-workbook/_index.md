---
title: Manipulate Named Range in a Workbook
type: docs
weight: 90
url: /cpp/manipulate-named-range-in-a-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells supports the manipulation of existing named ranges. All the existing named ranges can be accessed from [IWorkbook.GetIWorksheets().GetINames()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/#aa9e7bc07917a152a2c0de161cca133fa) collection. Once, you access the named range, you can change its various methods e.g. [GetFullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [GetRefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36).
## **Manipulate Named Range in a Workbook**
The following sample code reads the first named-range inside the [source excel file](attachments/22970927/23167008.xlsx) and prints its [FullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) properties on the console. After that, it modifies [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) property and saves the [output excel file](attachments/22970927/23167009.xlsx).
## **Sample Code**
{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Console Output**
The following console output prints the values of [FullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) members of the existing *Named Range* in the above code.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
