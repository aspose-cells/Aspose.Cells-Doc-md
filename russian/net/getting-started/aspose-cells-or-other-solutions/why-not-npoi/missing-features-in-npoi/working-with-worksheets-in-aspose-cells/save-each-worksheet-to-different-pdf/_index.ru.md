---
title: Сохранить каждый лист в отдельный PDF файл
type: docs
weight: 10
url: /ru/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Сохранить каждый лист в отдельный PDF-файл**
Aspose.Cells поддерживает преобразование файлов XLS (с изображениями, графиками и др.) в PDF-документы. Aspose.Cells for .NET может работать независимо для преобразования электронной таблицы в PDF-документ, и для этого вам не нужно больше использовать Aspose.Pdf for .NET. Для преобразования также не требуется создание или использование каких-либо временных файлов, так как весь процесс можно выполнить в памяти.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

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
## **Скачать работающий код**
Загрузить **Сохранение каждого листа в отдельный PDF-файл** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Дополнительные сведения см. в разделе [Сохранение каждого листа в отдельный PDF-файл](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
