---
title: إضافة الخلايا إلى نافذة مراقبة الصيغ في Microsoft Excel
description: كيفية استخدام مكتبة Aspose.Cells لإضافة الخلايا إلى نافذة مراقبة الصيغ في Excel. من خلال تحميل ملف Excel الحالي أو إنشاء ملف جديد، يمكننا التلاعب بالخلايا فيه وضبط الصيغ. في النهاية، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، نافذة مراقبة الصيغ، الخلايا، الإضافة
type: docs
weight: 60
url: /ar/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **سيناريوهات الاستخدام المحتملة**

نافذة مراقبة Microsoft Excel هي أداة مفيدة لمراقبة قيم الخلية وصيغها بشكل ملائم في نافذة. يمكنك فتح *Watch Window* في Microsoft Excel عن طريق النقر على *Formulas > Watch Window*. لديها زر *Add Watch* الذي يمكن استخدامه لإضافة الخلايا للتفتيش. بالمثل، يمكنك استخدام الطريقة [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) لإضافة الخلايا إلى *Watch Window* باستخدام واجهة برمجة التطبيقات Aspose.Cells.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

يقوم الكود العيني التالي بتعيين صيغة للخلايا C1 و E1 وإضافة كلتاهما إلى نافذة المراقبة. ثم يقوم بحفظ دفتر العمل كـ [ملف Excel الناتج](67338481.xlsx). إذا فتحت ملف Excel الناتج وعرضت *Watch Window*، سترى كلا الخليتين كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
