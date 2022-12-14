---
title: Автоподбор строки и столбца
type: docs
weight: 10
url: /ru/java/auto-fit-row-and-column/
---
## **Aspose.Cells - Автоподбор строки и столбца**
Самый простой подход к автоматическому изменению ширины и высоты строки — вызвать метод Worksheet.autoFitRow. Метод autoFitRow принимает в качестве параметра индекс строки (строки, размер которой нужно изменить).

**Пожалуйста, обрати внимание:** Если вы хотите автоматически подогнать строки и столбцы в электронных таблицах Excel с помощью Java, посетите страницу[Автоподбор строк и столбцов](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

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
## **Apache POI SS — HSSF XSSF — автоподбор строки и столбца**
Apache POI SS — HSSF и XSSF предоставляют Sheet.autoSizeColumn для автоматического подбора столбцов

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
