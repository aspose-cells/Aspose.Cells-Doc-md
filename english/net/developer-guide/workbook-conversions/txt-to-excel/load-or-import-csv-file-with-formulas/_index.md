---
title: Load or Import CSV file with Formulas
type: docs
weight: 350
url: /net/load-or-import-csv-file-with-formulas/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

CSV files mostly contain textual data and do not contain any formulas. However, sometimes it happens that CSV files also contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) as **true**. Once this property is set to **true**, Aspose.Cells will not treat the formula as simple text. They will be treated as formulas and Aspose.Cells' formula calculation engine will process them as usual.

{{% /alert %}}

The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purposes, we use the simple CSV file (5115034.csv) which contains this data. As you see, it contains a formula.

{{< highlight java >}}

300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



The code first loads the CSV file, then imports it again at cell D4. Finally, it saves the workbook object in **XLSX** format. The [output XLSX file](5115052.xlsx) looks like this. As you see, cells C3 and F4 contain formulas and their result, 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="csharp" >}}
