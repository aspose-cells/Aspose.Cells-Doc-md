---
title: إضافة الخلايا إلى نافذة مراقبة الصيغ في Microsoft Excel
type: docs
weight: 20
url: /ar/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **سيناريوهات الاستخدام المحتملة**

نافذة المراقبة في Microsoft Excel هي أداة مفيدة لمراقبة قيم الخلايا وصيغها بشكل ملائم في نافذة. يمكنك فتح *Watch Window* في Microsoft Excel عن طريق النقر على *Formulas > Watch* *Window*. يحتوي على زر *Add Watch* الذي يمكن استخدامه لإضافة الخلايا للتفتيش. بالمثل ، يمكنك استخدام الأسلوب [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) لإضافة الخلايا إلى *Watch Window* باستخدام Aspose.Cells API.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

الكود النموذجي التالي يحدد صيغة الخلايا C1 و E1 ويضيف كل منهما إلى *نافذة المراقبة*. ثم يقوم بحفظ دفتر العمل كـ [ملف Excel الناتج](67338509.xlsx). إذا فتحت ملف Excel الناتج وعرضت *نافذة المراقبة*, سترى كلا الخليتين كما هو موضح في هذا اللقطة.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
