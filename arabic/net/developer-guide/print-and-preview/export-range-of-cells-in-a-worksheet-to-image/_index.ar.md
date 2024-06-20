---
title: تصدير مجموعة من الخلايا في ورقة عمل إلى صورة
type: docs
weight: 60
url: /ar/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إنشاء صورة لورقة عمل باستخدام Aspose.Cells. ومع ذلك، في بعض الأحيان، تحتاج إلى تصدير مجموعة من الخلايا فقط في ورقة عمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

## **تصدير مجموعة من الخلايا في ورقة عمل إلى صورة**

لالتقاط صورة من مجموعة، قم بتعيين منطقة الطباعة إلى المجال المطلوب ثم قم بتعيين جميع الهوامش إلى 0. كما قم بتعيين [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) إلى **صحيح**. يأخذ الكود التالي صورة للمدى D8:G16. أدناه، صورة لل[ملف الإكسل عينة](47153160.xlsx) المستخدم في الكود. يمكنك تجربة الكود مع أي ملف إكسل.

## **صورة للملف الإكسل العيني وصورته المصدرية**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

تنفيذ الكود ينشئ صورة للمدى D8:G16 فقط.

**![todo:image_alt_text](Output-Image.png)**

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
