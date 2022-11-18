---
title: Load or Import CSV file with Formulas
type: docs
weight: 500
url: /java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV file mostly contains textual data and they do not contain any formulas. However sometimes it happens CSV files also contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) to **true**. Once this property will be set to **true**, Aspose.Cells will not treat formula as simple text. They will be treated as formula and Aspose.Cells formula calculation engine will process them as usual.

{{% /alert %}} 
## **Load or Import CSV file with Formulas**
The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purpose, we use the [simple csv file](5472505.csv) which contains this data. As you see it contains a formula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

The code first loads the CSV file, then import it again at cell D4. Finally, it saves the workbook object in XSLX format. The [output XLSX file](5472503.xlsx) looks like this. As you see cell C3 and F4 contains formula and its result 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
