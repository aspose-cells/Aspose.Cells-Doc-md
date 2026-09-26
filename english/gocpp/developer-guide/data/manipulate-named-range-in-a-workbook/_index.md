---
title: Manipulate Named Range in a Workbook
type: docs
weight: 90
url: /go-cpp/manipulate-named-range-in-a-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells supports the manipulation of existing named ranges. All the existing named ranges can be accessed from the [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/getnames/) collection. Once you access the named range, you can use its various methods, e.g., [GetFullText](https://reference.aspose.com/cells/go-cpp/name/getfulltext/) and [GetRefersTo](https://reference.aspose.com/cells/go-cpp/name/getrefersto/).

## **Manipulate Named Range in a Workbook**
The following sample code reads the first named range inside the [source Excel file](23167008.xlsx) and prints its [FullText](https://reference.aspose.com/cells/go-cpp/name/getfulltext/) and [RefersTo](https://reference.aspose.com/cells/go-cpp/name/getrefersto/) properties on the console. After that, it modifies the RefersTo property and saves the [output Excel file](23167009.xlsx).

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulateNamedRangeInAWorkbook.go" >}}

## **Console Output**
The following console output prints the values of [FullText](https://reference.aspose.com/cells/go-cpp/name/getfulltext/) and [RefersTo](https://reference.aspose.com/cells/go-cpp/name/getrefersto/) members of the existing *Named Range* in the above code.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
