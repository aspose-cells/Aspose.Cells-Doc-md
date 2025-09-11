---
title: Load or Import CSV file with Formulas
type: docs
weight: 350
url: /python-net/load-or-import-csv-file-with-formulas/
description: Load or Import CSV file with Formulas by using Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---

{{% alert color="primary" %}} 

CSV file mostly contains textual data and they do not contain any formulas. However, sometimes it happens that CSV files also contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) as **true**. Once this property will be set **true**, Aspose.Cells will not treat formula as simple text. They will be treated as formula and Aspose.Cells formula calculation engine will process them as usual.

{{% /alert %}} 

The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purpose, we use the [simple csv file](5115034.csv) which contains this data. As you see it contains a formula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



The code first loads the CSV file, then import it again at cell D4. Finally, it saves the workbook object in XSLX format. The [output XLSX file](5115052.xlsx) looks like this. As you see cell C3 and F4 contain formula and its result 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}