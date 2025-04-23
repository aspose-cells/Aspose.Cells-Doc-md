---
title: إدارة النطاقات
linktitle: النطاقات
type: docs
weight: 75
url: /ar/java/managing-ranges/
---

## **مقدمة**

في إكسل، يمكنك تحديد خلايا متعددة باستخدام تحديد مربع الماوس، ويُطلق على مجموعة الخلايا المحددة "نطاق".

على سبيل المثال، يمكنك النقر بزر الماوس الأيسر في الخلية "A1" في إكسل ومن ثم سحبها إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المستطيلة التي حددتها بسهولة باعتبارها كائنًا عن طريق استخدام Aspose.Cells.

هنا كيفية إنشاء نطاق ووضع قيمة وتعيين النمط، والقيام بعمليات أخرى على كائن "النطاق".

## **إدارة النطاقات باستخدام Aspose.Cells**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

### **إنشاء المدى**

عندما ترغب في إنشاء منطقة مستطيلية تمتد عبر A1:C4، يمكنك استخدام الشيفرة التالية:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **وضع قيمة في الخلايا من المدى**

فلنفترض أن لديك مدى من الخلايا يمتد عبر A1:C4. يحتوي المصفوفة على 4 * 3 = 12 خلية. ترتبت الخلايا الفردية للمدى على التوالي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

توضح الأمثلة التالية كيفية إدخال بعض القيم في الخلايا للنطاق

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **تعيين أسلوب للخلايا من المدى**

توضح الأمثلة التالية كيفية تعيين نمط الخلايا في النطاق

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **الحصول على النطاق الحالي من المدى**

CurrentRegion هو خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية 

المنطقة الحالية هي نطاق محصور بأي مزيج من الصفوف الفارغة والأعمدة الفارغة. للقراءة فقط

في Excel، يمكنك الحصول على منطقة الـ CurrentRegion عن طريق:
1. تحديد منطقة (range1) بصندوق الماوس.
2. انقر "الصفحة الرئيسية - تحرير - البحث والتحديد - اذهب إلى خاص - المنطقة الحالية"، أو استخدم "Ctrl+Shift+*"، سترى أن Excel يساعدك تلقائيًا على تحديد منطقة (range2)، الآن قمت بذلك، range2 هو المنطقة الحالية للـ range1.

من خلال Aspose.Cells، يمكنك استخدام خاصية "Range.CurrentRegion" لأداء نفس الوظيفة.

يرجى تحميل الملف الاختبار التالي، افتحه في Excel، استخدم صندوق الماوس لتحديد منطقة "A1:D7"، ثم انقر "Ctrl+Shift+*"، سترى منطقة "A1:C3" محددة.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل الأمثلة التالية، وشاهد كيفية عمل ذلك في Aspose.Cells:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **مواضيع متقدمة**
- [ملء تلقائي لنطاق ملف Excel](/cells/ar/java/autofill-ranges/)
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [نسخ النطاقات من Excel](/cells/ar/java/copy-ranges-of-Excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/java/copy-range-data-only/)
- [نسخ بيانات النطاق بالتنسيق](/cells/ar/java/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/java/copy-range-style-only/)
- [نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف](/cells/ar/java/copy-row-heights-of-source-range-to-destination-range/)
- [إنشاء مجموعة الاتحاد](/cells/ar/java/create-union-range/)
- [قص ولصق النطاقات](/cells/ar/java/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/java/delete-ranges-from-Excel/)
- [كشف الخلايا المدمجة في ورقة العمل](/cells/ar/java/detect-merged-cells-in-a-worksheet/)
- [الحصول على عنوان خلية عدد الإزاحة الكاملة للعمود والصف الكامل للنطاق](/cells/ar/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [الحصول على نطاق مع روابط خارجية](/cells/ar/java/get-range-with-external-links/)
- [تنفيذ نطاقات غير متتابعة](/cells/ar/java/implementing-non-sequential-ranges/)
- [إدراج النطاقات](/cells/ar/java/insert-ranges-to-Excel/)
- [دمج أو فصل نطاق الخلايا](/cells/ar/java/merge-or-unmerge-range-of-cells/)
- [نقل مجموعة من الخلايا في ورقة العمل](/cells/ar/java/move-range-of-cells-in-a-worksheet/)
- [النطاقات المسماة](/cells/ar/java/named-ranges/)
- [البحث والاستبدال في بيانات النطاق](/cells/ar/java/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="java" >}}
