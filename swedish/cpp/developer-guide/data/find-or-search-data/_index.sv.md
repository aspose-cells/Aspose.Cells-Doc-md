﻿---
title: Hitta eller sök data
type: docs
weight: 80
url: /sv/cpp/find-or-search-data/
---
## **Hitta eller sök data**
Du kan använda Aspose.Cells för att hitta eller söka efter data på olika sätt med följande metod. Dessa metoder hittar data enligt deras namn.

- [FindNumber](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7f90de51db6984956b5ed0b33b73a111)
- [Hitta Formel](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae3a8a9cfe7f8dc84ea590a8472e194f1)
- [FindFormulaContains](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae8d2b8cdef52ef4e501502c4b905943f)
- [FindString](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac3e27028cf708eba8efb0997f9c9048e)
- [FindStringContains](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4f863b51674f7b18cf20a344872ad704)
- [FindStringStartsWith](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa17f3d771e73731dd9f682f4ac359df)
- [FindStringEndsWith](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7d0c58798771b7bc220fb162c30f247b)

 Följande exempelkod illustrerar användningen av ovanstående metoder med hjälp av[exempel på excel-fil](21266434.xlsx) som visas i denna skärmdump.

![todo:image_alt_text](find-or-search-data_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-FindOrSearchData.cpp" >}}
## **Konsolutgång**
 Detta är konsolutgången för ovanstående exempelkod när den körs med den givna[exempel på excel-fil](21266434.xlsx).



{{< highlight "java" >}}

 Name of the cell containing the number 80: A8

Name of the cell containing formula =SUM(A5:A10): C6

Name of the cell containing the formula that contains CHA: C7

Name of the cell containing specified string: C8

Name of the cell containing the string that contains Two: C9

Name of the cell containing the string that starts with AAA: C10

Name of the cell containing the string that ends with BBB: C11

{{< /highlight >}}