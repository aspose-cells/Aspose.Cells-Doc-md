---
title : "Load or Import CSV file with Formulas" 
description : "" 
weight : 12517 
toc : false
type: docs
url: /java/developerguide/technicalarticles/load+or+import+csv+file+with+formulas/
---

# Aspose.Cells for Java : Load or Import CSV file with Formulas


CSV file mostly contains textual data and they do not contain any formulas. However sometimes it happens CSV files also contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.HasFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/txtloadoptions#HasFormula) to **true**. Once this property will be set to **true**, Aspose.Cells will not treat formula as simple text. They will be treated as formula and Aspose.Cells formula calculation engine will process them as usual.

#### Load or Import CSV file with Formulas

The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purpose, we use the [simple csv file](https://docs2.aspose.com/cells/java/attachments/5276090/5472505.csv) which contains this data. As you see it contains a formula.

{{< code lang="cs" >}}
300,500,=Sum(A1:B1)
{{< /code >}}

The code first loads the CSV file, then import it again at cell D4. Finally, it saves the workbook object in XSLX format. The [output XLSX file](https://docs2.aspose.com/cells/java/attachments/5276090/5472503.xlsx) looks like this. As you see cell C3 and F4 contains formula and its result 800.

![](https://docs2.aspose.com/cells/java/attachments/5276090/5472506.png)


## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [output.xlsx](https://docs2.aspose.com/cells/java/attachments/5276090/5472503.xlsx) (application/unknown)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [output-xlsx-csv.png](https://docs2.aspose.com/cells/java/attachments/5276090/5472506.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sample.csv](https://docs2.aspose.com/cells/java/attachments/5276090/5472505.csv) (application/vnd.ms-excel)  

