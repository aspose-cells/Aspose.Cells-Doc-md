---
title: Find or Search Data
type: docs
weight: 80
url: /cpp/find-or-search-data/
---

## **Find or Search Data**
You can use Aspose.Cells to find or search data in various ways using the following method. These methods find the data as per their names.

- [FindNumber](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a7f90de51db6984956b5ed0b33b73a111)
- [FindFormula](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ae3a8a9cfe7f8dc84ea590a8472e194f1)
- [FindFormulaContains](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ae8d2b8cdef52ef4e501502c4b905943f)
- [FindString](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ac3e27028cf708eba8efb0997f9c9048e)
- [FindStringContains](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a4f863b51674f7b18cf20a344872ad704)
- [FindStringStartsWith](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#afa17f3d771e73731dd9f682f4ac359df)
- [FindStringEndsWith](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a7d0c58798771b7bc220fb162c30f247b)

The following sample code illustrates the usage of the above methods using the [sample excel file](21266434.xlsx) as shown in this screenshot.

![todo:image_alt_text](find-or-search-data_1.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-FindOrSearchData.cpp" >}}
## **Console Output**
This is the console output of the above sample code when executed with the given [sample excel file](21266434.xlsx).



{{< highlight java >}}

 Name of the cell containing the number 80: A8

Name of the cell containing formula =SUM(A5:A10): C6

Name of the cell containing the formula that contains CHA: C7

Name of the cell containing specified string: C8

Name of the cell containing the string that contains Two: C9

Name of the cell containing the string that starts with AAA: C10

Name of the cell containing the string that ends with BBB: C11

{{< /highlight >}}
