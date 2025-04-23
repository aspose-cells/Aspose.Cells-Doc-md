---
title: Сохранить каждый лист в отдельный PDF в xlsx4j
type: docs
weight: 50
url: /ru/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - Сохранить каждый лист в отдельный PDF-файл**
Aspose.Cells поддерживает преобразование файлов XLS (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for Java может работать независимо для преобразования электронной таблицы в документ Pdf, и вам больше не нужно использовать Aspose.Pdf для Java для этого преобразования. Преобразование также не требует создания / использования каких-либо временных файлов, так как весь процесс может быть выполнен в памяти.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Сохранение каждого листа в отдельный файл PDF](/cells/ru/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
