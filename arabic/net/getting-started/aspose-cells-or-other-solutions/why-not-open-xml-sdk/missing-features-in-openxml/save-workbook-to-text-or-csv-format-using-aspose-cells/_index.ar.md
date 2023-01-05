---
title: حفظ المصنف إلى نص أو تنسيق CSV باستخدام Aspose.Cells
type: docs
weight: 80
url: /ar/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

في بعض الأحيان ، تريد تحويل مصنف أو حفظه باستخدام أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV إلخ.) ، افتراضيًا ، يتم حفظ محتويات ورقة العمل النشطة فقط Microsoft Excel و Aspose.Cells.

{{% /alert %}} 

يوضح المثال التالي من التعليمات البرمجية كيفية حفظ مصنف بأكمله في تنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وما إلى ذلك) بأي عدد من أوراق العمل.

عندما يتم تنفيذ الكود ، فإنه يحول بيانات جميع الأوراق في المصنف إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ الملف في CSV. بشكل افتراضي ، يكون TxtSaveOptions.Separator عبارة عن فاصلة ، لذلك لا تحدد فاصلًا إذا قمت بالحفظ بتنسيق CSV.

**C#**

{{< highlight "csharp" >}}

string FilePath = @ ".. \ .. \ .. \ Sample Files \"؛

string FileName = FilePath + "حفظ المصنف إلى نص أو CSV Format.xlsx"؛

string destFileName = FilePath + "حفظ المصنف إلى نص أو CSV Format.txt"؛

// تحميل المصنف المصدر الخاص بك

مصنف المصنف = مصنف جديد (اسم الملف) ؛

// 0 بايت صفيف

بايت [] workbookData = بايت جديد [0] ؛

// خيارات حفظ النص. يمكنك استخدام أي نوع من الفواصل

TxtSaveOptions opts = new TxtSaveOptions () ؛

OPts.Separator = '\ t' ؛

// نسخ كل بيانات ورقة العمل بتنسيق نصي داخل مصفوفة بيانات المصنف

 لـ (int idx = 0 ؛ idx< workbook.Worksheets.Count; idx++)

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
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **تحميل مثال الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
