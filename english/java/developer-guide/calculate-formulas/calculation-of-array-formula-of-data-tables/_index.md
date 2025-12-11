---
title: Calculation of Array Formula of Data Tables
type: docs
weight: 550
url: /java/calculation-of-array-formula-of-data-tables/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

You can create a Data Table in Microsoft Excel using **Data > What‑If Analysis > Data Table**. Aspose.Cells now allows you to calculate the array formula of the data table. Please use [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) as usual for calculating any type of formulas.

{{% /alert %}} 
## **Calculation of Array Formula of Data Tables**
In the following sample code, we used this [source Excel file](5472579.xlsx), which is also shown in the image below.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

If you change the value of cell **B1** to **100**, the values of the data table that are filled with yellow color will become **120**. The sample code generates the [output PDF](5472577.pdf), which shows **120** as the values in the data table, as shown in this image.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Here is the sample code used to generate the [output PDF](5472577.pdf) from the [source Excel file](5472579.xlsx). Please read the comments for more information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
{{< app/cells/assistant language="java" >}}
