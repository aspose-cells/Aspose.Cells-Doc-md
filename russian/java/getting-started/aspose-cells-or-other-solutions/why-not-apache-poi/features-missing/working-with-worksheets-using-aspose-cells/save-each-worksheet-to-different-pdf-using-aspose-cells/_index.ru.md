---
title: Сохраните каждый рабочий лист в другой PDF, используя Aspose.Cells
type: docs
weight: 80
url: /ru/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---
## **Aspose.Cells - Сохранение каждого рабочего листа в другой PDF**
Aspose.Cells поддерживает преобразование файлов XLS (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for Java может работать независимо для преобразования электронной таблицы в документ PDF, и вам больше не нужно использовать Aspose.Pdf for Java для преобразования. Преобразование также не требует создания/использования каких-либо временных файлов, так как весь процесс может выполняться в памяти.

**Java**

{{< highlight "java" >}}

 //Получить путь к файлу Excel

Строка filePath = dataDir + "workbook.xlsx";

//Создаем новую книгу и открываем Excel

//Файл из его местоположения

Книга рабочей книги = новая рабочая книга (путь к файлу);

//Получить количество рабочих листов в рабочей книге

int sheetCount = workbook.getWorksheets().getCount();

//Делаем все листы невидимыми, кроме первого рабочего листа

 для (целое я = 1; я< workbook.getWorksheets().getCount(); i++)

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
## **Скачать рабочий код**
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Сохраните каждый рабочий лист в другой файл PDF](/cells/ru/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
