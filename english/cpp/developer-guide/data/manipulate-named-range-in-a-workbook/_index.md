---
title: Manipulate Named Range in a Workbook
type: docs
weight: 90
url: /cpp/manipulate-named-range-in-a-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells supports the manipulation of existing named ranges. All the existing named ranges can be accessed from [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) collection. Once, you access the named range, you can change its various methods e.g. [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) and [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Manipulate Named Range in a Workbook**
The following sample code reads the first named-range inside the [source excel file](23167008.xlsx) and prints its [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) and [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) properties on the console. After that, it modifies `RefersTo` property and saves the [output excel file](23167009.xlsx).
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Console Output**
The following console output prints the values of [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) and [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) members of the existing *Named Range* in the above code.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
