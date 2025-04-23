---
title: Сохранение книги в формате текста или CSV с использованием Aspose.Cells
type: docs
weight: 80
url: /ru/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---

{{% alert color="primary" %}} 

Иногда вам нужно преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.), по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного листа.

{{% /alert %}} 

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода конвертируются данные всех листов книги в формат TXT.

Вы можете изменить этот пример, чтобы сохранить ваш файл в формате CSV. По умолчанию разделителем является запятая, поэтому не указывайте разделитель при сохранении в формате CSV.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Save Workbook to Text or CSV Format.xlsx";

string destFileName = FilePath + "Save Workbook to Text or CSV Format.txt";

//Load your source workbook

Workbook workbook = new Workbook(FileName);

//0-byte array

byte[] workbookData = new byte[0];

//Text save options. You can use any type of separator

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copy each worksheet data in text format inside workbook data array

for (int idx = 0; idx < workbook.Worksheets.Count; idx++)

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

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
