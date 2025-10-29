---
title: تصدير مجموعة من الخلايا في ورقة عمل إلى صورة
type: docs
weight: 60
url: /ar/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك عمل صورة لورقة عمل باستخدام Aspose.Cells للبايثون via .NET. ومع ذلك، أحيانًا تحتاج إلى تصدير نطاق معين من الخلايا في ورقة العمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

## **تصدير مجموعة من الخلايا في ورقة عمل إلى صورة**

لالتقاط صورة من مجموعة، قم بتعيين منطقة الطباعة إلى المجال المطلوب ثم قم بتعيين جميع الهوامش إلى 0. كما قم بتعيين [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) إلى **صحيح**. يأخذ الكود التالي صورة للمدى D8:G16. أدناه، صورة لل[ملف الإكسل عينة](47153160.xlsx) المستخدم في الكود. يمكنك تجربة الكود مع أي ملف إكسل.

## **صورة للملف الإكسل العيني وصورته المصدرية**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

تنفيذ الكود ينشئ صورة للمدى D8:G16 فقط.

**![todo:image_alt_text](Output-Image.png)**

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
