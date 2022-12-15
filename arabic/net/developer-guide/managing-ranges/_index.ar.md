---
title: إدارة النطاقات
linktitle: نطاقات
type: docs
weight: 105
url: /ar/net/managing-ranges/
---
## **مقدمة**

في Excel ، يمكنك تحديد خلايا متعددة مع تحديد مربع الماوس ، وتسمى مجموعة الخلايا المحددة "النطاق".

على سبيل المثال ، يمكنك النقر فوق زر الفأرة الأيسر في Cell "A1" من Excel ثم السحب إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المستطيلة التي حددتها بسهولة ككائن باستخدام Aspose.Cells.

إليك كيفية إنشاء النطاق ، ووضع القيمة ، وتعيين النمط ، والقيام بمزيد من العمليات على كائن "النطاق".

## **إدارة النطاقات باستخدام Aspose.Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة.

### **إنشاء المدى**

عندما تريد إنشاء منطقة مستطيلة تمتد عبر A1: C4 ، يمكنك استخدام الكود التالي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **ضع القيمة في Cells للمدى**

لنفترض أن لديك نطاقًا من الخلايا يمتد عبر A1: C4. تجعل المصفوفة 4 * 3 = 12 خلية. يتم ترتيب خلايا النطاق الفردية بالتسلسل: النطاق [0،0] ، النطاق [0،1] ، النطاق [0،2] ، النطاق [1،0] ، النطاق [1،1] ، النطاق [1،2] ، النطاق [2،0] ، النطاق [2،1] ، النطاق [2،2] ، النطاق [3،0] ، النطاق [3،1] ، النطاق [3،2].

يوضح المثال التالي كيفية إدخال بعض القيم في خلايا النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **تعيين نمط Cells للمجال**

يوضح المثال التالي كيفية تعيين نمط خلايا النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **احصل على CurrentRegion of the Range**

 CurrentRegion هي خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية.

المنطقة الحالية عبارة عن نطاق يحده أي مجموعة من الصفوف الفارغة والأعمدة الفارغة. يقرأ فقط.

في Excel ، يمكنك الحصول على منطقة CurrentRegion من خلال:
1. حدد منطقة (range1) باستخدام مربع الماوس.
2. انقر فوق "الصفحة الرئيسية - التحرير - البحث والاختيار - الانتقال إلى خاص - المنطقة الصحيحة" ، أو استخدم "Ctrl + Shift + *" ، سترى أن برنامج Excel يساعدك تلقائيًا في تحديد منطقة (النطاق 2) ، والآن قمت بذلك ، النطاق 2 هو المنطقة الحالية من النطاق 1.

باستخدام Aspose.Cells ، يمكنك استخدام خاصية "Range.CurrentRegion" لأداء نفس الوظيفة.

يرجى تنزيل ملف الاختبار التالي ، وفتحه في Excel ، واستخدام مربع الماوس لتحديد منطقة "A1: D7" ، ثم انقر فوق "Ctrl + Shift + *" ، سترى المنطقة "A1: C3" محددة.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل المثال التالي ، انظر كيف يعمل في Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **موضوعات مسبقة**
- [نطاق الملء التلقائي لملف Excel](/cells/ar/net/autofill-ranges/)
- [نطاقات نسخ من Excel](/cells/ar/net/copy-ranges-of-Excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/net/copy-range-data-only/)
- [نسخ بيانات النطاق بالنمط](/cells/ar/net/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/net/copy-range-style-only/)
- [إنشاء نطاق الاتحاد](/cells/ar/net/create-union-range/)
- [نطاق القص واللصق](/cells/ar/net/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/net/delete-ranges-from-Excel/)
- [احصل على العنوان Cell عدد الأوفست العمود بالكامل وصف النطاق بالكامل](/cells/ar/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [أدخل النطاقات](/cells/ar/net/insert-ranges-to-Excel/)
- [نطاق الدمج أو إلغاء الدمج Cells](/cells/ar/net/merge-or-unmerge-range-of-cells/)
- [نقل مدى Cells في ورقة عمل](/cells/ar/net/move-range-of-cells-in-a-worksheet/)
- [إنشاء نطاقات مسماة ذات نطاق وورقة عمل](/cells/ar/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [بحث واستبدال البيانات في نطاق](/cells/ar/net/search-and-replace-data-in-a-range/)
