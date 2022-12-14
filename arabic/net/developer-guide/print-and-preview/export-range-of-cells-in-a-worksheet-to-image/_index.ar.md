---
title: نطاق تصدير Cells في ورقة عمل إلى صورة
type: docs
weight: 60
url: /ar/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك عمل صورة لورقة عمل باستخدام Aspose.Cells. ومع ذلك ، في بعض الأحيان تحتاج فقط إلى تصدير نطاق من الخلايا في ورقة عمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

## **نطاق تصدير Cells في ورقة عمل إلى صورة**

 لالتقاط صورة لنطاق ، اضبط منطقة الطباعة على النطاق المطلوب ثم اضبط جميع الهوامش على 0. قم أيضًا بتعيين[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) إلى**حقيقي** . يأخذ الكود التالي صورة للنطاق D8: G16. يوجد أدناه لقطة شاشة لـ[نموذج لملف Excel](47153160.xlsx) المستخدمة في الكود. يمكنك تجربة الكود مع أي ملف Excel.

## **لقطة شاشة لملف Excel ونسخته المصدرة**

**! [todo: image_alt_text] (export-range-of-cells-in-a-workheet-to-image_1.png)**

يؤدي تنفيذ الكود إلى إنشاء صورة للنطاق D8: G16 فقط.

**! [todo: image_alt_text] (Output-Image.png)**

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
