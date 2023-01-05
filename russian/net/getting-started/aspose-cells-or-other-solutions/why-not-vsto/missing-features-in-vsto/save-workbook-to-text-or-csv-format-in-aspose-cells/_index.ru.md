---
title: Сохранить книгу в текст или формат CSV в формате Aspose.Cells
type: docs
weight: 110
url: /ru/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---
{{% alert color="primary" %}} 

Иногда вы хотите преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного рабочего листа.

{{% /alert %}} 

В следующем примере кода показано, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронной таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством рабочих листов.

Когда код выполняется, он преобразует данные всех листов книги в формат TXT.

Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию TxtSaveOptions.Separator — это запятая, поэтому не указывайте разделитель при сохранении в формате CSV.

**C#**

{{< highlight "csharp" >}}

 строка filePath = "source.xlsx";

//Загружаем исходную книгу

Книга рабочей книги = новая рабочая книга (путь к файлу);

//0-байтовый массив

byte[]workbookData = новый байт[0];

//Параметры сохранения текста. Вы можете использовать любой тип разделителя

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

// Копируем данные каждого рабочего листа в текстовом формате внутри массива данных рабочей книги

 для (int idx = 0; idx< workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
