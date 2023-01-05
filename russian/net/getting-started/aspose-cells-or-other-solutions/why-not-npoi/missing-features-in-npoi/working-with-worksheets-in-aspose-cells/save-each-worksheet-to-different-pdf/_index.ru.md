---
title: Сохраните каждый рабочий лист в другой PDF
type: docs
weight: 10
url: /ru/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Сохранение каждого рабочего листа в другой PDF**
Aspose.Cells поддерживает преобразование файлов XLS (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for .NET может работать независимо для преобразования электронной таблицы в документ PDF, и вам больше не нужно использовать Aspose.Pdf for .NET для преобразования. Преобразование также не требует создания/использования каких-либо временных файлов, так как весь процесс может выполняться в памяти.

**C#**

{{< highlight "cs" >}}

 //Создаем новую книгу и открываем Excel

//Файл из его местоположения

Рабочая книга рабочая книга = новая рабочая книга("../../data/test.xlsx");

//Получить количество рабочих листов в рабочей книге

int sheetCount = workbook.Worksheets.Count;

//Делаем все листы невидимыми, кроме первого рабочего листа

 для (целое я = 1; я< workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Сохраните каждый рабочий лист в другой PDF** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Сохраните каждый рабочий лист в другой файл PDF](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
