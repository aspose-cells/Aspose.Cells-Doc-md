---
title: Adatta automaticamente riga e colonna
type: docs
weight: 10
url: /it/java/auto-fit-row-and-column/
description: Scopri come adattare automaticamente riga e colonna tramite Aspose.Cells for Java API.
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
---
##  **Come adattare automaticamente riga e colonna utilizzando Aspose.Cells for Java**
L'approccio più semplice per ridimensionare automaticamente la larghezza e l'altezza di una riga consiste nel chiamare il metodo Worksheet.autoFitRow. Il metodo autoFitRow accetta come parametro un indice di riga (della riga da ridimensionare).

**Notare che:**Se desideri adattare automaticamente righe e colonne nei fogli di calcolo Excel utilizzando Java, visita[Adatta automaticamente righe e colonne](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
##  **Apache POI SS - HSSF XSSF - Adatta automaticamente riga e colonna**
Apache POI SS - HSSF e XSSF forniscono Sheet.autoSizeColumn per adattare automaticamente le colonne

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
##  **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
##  **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowcolumns/autofitrowandcolumn)
