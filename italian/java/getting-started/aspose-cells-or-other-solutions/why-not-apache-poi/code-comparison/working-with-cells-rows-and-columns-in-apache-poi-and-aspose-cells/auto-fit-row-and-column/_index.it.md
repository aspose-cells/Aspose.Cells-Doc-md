---
title: Adatta automaticamente riga e colonna
type: docs
weight: 10
url: /it/java/auto-fit-row-and-column/
description: Scopri come adattare automaticamente riga e colonna tramite l API Aspose.Cells for Java.
keywords: Come adattare automaticamente riga e colonna in Java, adattare automaticamente i dati della riga in un foglio di lavoro usando Java, dati della colonna in Java AutoFit. 
---

## **Come adattare automaticamente riga e colonna usando Aspose.Cells for Java**
L'approccio più diretto per adattare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo autoFitRow della Worksheet. Il metodo autoFitRow richiede un indice di riga (della riga da ridimensionare) come parametro.

**Nota:** Se desideri adattare automaticamente righe e colonne in fogli di calcolo Excel usando Java, visita [Adattamento automatico righe e colonne](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Adatta automaticamente riga e colonna**
Apache POI SS - HSSF e XSSF fornisce Sheet.autoSizeColumn per adattare automaticamente le colonne

**Java**

{{< highlight java >}}

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
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
