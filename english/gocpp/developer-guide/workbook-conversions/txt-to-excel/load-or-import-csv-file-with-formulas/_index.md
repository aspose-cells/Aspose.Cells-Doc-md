---
title: Load or Import CSV file with Formulas using C++
linktitle: Load or Import CSV file with Formulas
type: docs
weight: 350
url: /go-cpp/load-or-import-csv-file-with-formulas/
description: Load or import a CSV file containing formulas using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}} 

CSV files mostly contain textual data and do not typically include any formulas. However, there are cases when CSV files might contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) to **true**. Once this property is set to **true**, Aspose.Cells will not treat formulas as simple text. They will be treated as formulas, and the Aspose.Cells formula calculation engine will process them as usual.

{{% /alert %}} 

The following code illustrates how you can load and import a CSV file with formulas. You can use any CSV file. For illustration purposes, we use the [simple CSV file](5115034.csv) which contains this data. As you can see, it contains a formula.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
The code first loads the CSV file, then imports it again at cell D4. Finally, it saves the workbook object in XLSX format. The [output XLSX file](5115052.xlsx) looks like this. As you can see, cells C3 and F4 contain formulas and their result is 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |