---
title: إدارة النطاقات
linktitle: النطاقات
type: docs
weight: 105
url: /ar/python-net/managing-ranges/
description: يوضح هذا المقال كيفية إدارة النطاقات باستخدام واجهة تطبيقات Aspose.Cells لبرمجة Python via .NET.
keywords: مكتبة إكسل برمجة Python، إدارة النطاقات في Python، إنشاء نطاق في Python، وضع قيمة في خلايا النطاق بواسطة Python، تعيين نمط خلايا النطاق بواسطة Python، الحصول على منطقة الخلية الحالية من النطاق.
---

## **مقدمة**

في إكسل، يمكنك تحديد خلايا متعددة باستخدام تحديد مربع الماوس، ويُطلق على مجموعة الخلايا المحددة "نطاق".

على سبيل المثال، يمكنك النقر بزر الماوس الأيسر في الخلية "A1" في إكسل ثم سحبها إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المستطيلة التي قمت باختيارها بسهولة ككائن باستخدام واجهة تطبيقات Aspose.Cells لبرمجة Python via .NET.

هنا كيفية إنشاء نطاق ووضع قيمة وتعيين النمط، والقيام بعمليات أخرى على كائن "النطاق".

## **إدارة النطاقات باستخدام Aspose.Cells for Python مكتبة Excel**

Aspose.Cells for Python via .NET يوفر فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Excel من مايكروسوفت. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة عمل ممثلة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) توفر مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)

## **كيفية إنشاء نطاق**

عندما ترغب في إنشاء منطقة مستطيلية تمتد عبر A1:C4، يمكنك استخدام الشيفرة التالية:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **كيفية وضع قيمة في الخلايا للنطاق**

لنفترض أن لديك مجموعة من الخلايا التي تمتد عبر A1:C4. المصفوفة تجعل 4 * 3 = 12 خلية. تتم ترتيب الخلايا المجموعة الفردية على التوالي.

توضح الأمثلة التالية كيفية إدخال بعض القيم في الخلايا للنطاق

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **كيفية تعيين نمط الخلايا في النطاق**

توضح الأمثلة التالية كيفية تعيين نمط الخلايا في النطاق

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **كيفية الحصول على المنطقة الحالية من النطاق**

CurrentRegion هو خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية 

المنطقة الحالية هي نطاق محصور بأي مزيج من الصفوف الفارغة والأعمدة الفارغة. للقراءة فقط

في Excel، يمكنك الحصول على منطقة الـ CurrentRegion عن طريق:
1. تحديد منطقة (range1) بصندوق الماوس.
2. انقر "الصفحة الرئيسية - تحرير - البحث والتحديد - اذهب إلى خاص - المنطقة الحالية"، أو استخدم "Ctrl+Shift+*"، سترى أن Excel يساعدك تلقائيًا على تحديد منطقة (range2)، الآن قمت بذلك، range2 هو المنطقة الحالية للـ range1.

باستخدام Aspose.Cells for Python via .NET. يمكنك استخدام خاصية "Range.current_region" لتنفيذ نفس الوظيفة.

يرجى تحميل الملف الاختبار التالي، افتحه في Excel، استخدم صندوق الماوس لتحديد منطقة "A1:D7"، ثم انقر "Ctrl+Shift+*"، سترى منطقة "A1:C3" محددة.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل الرمز التالي، انظر كيف يعمل في Aspose.Cells for Python via .NET

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **مواضيع متقدمة**
- [ملء تلقائي لنطاق ملف Excel](/cells/ar/python-net/autofill-ranges/)
- [نسخ النطاقات من Excel](/cells/ar/python-net/copy-ranges-of-excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/python-net/copy-range-data-only/)
- [نسخ بيانات النطاق بالتنسيق](/cells/ar/python-net/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/python-net/copy-range-style-only/)
- [إنشاء مجموعة الاتحاد](/cells/ar/python-net/create-union-range/)
- [قص ولصق النطاق](/cells/ar/python-net/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/python-net/delete-ranges-from-excel/)
- [الحصول على عنوان خلية عدد الإزاحة الكاملة للعمود والصف الكامل للنطاق](/cells/ar/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [إدراج النطاقات](/cells/ar/python-net/insert-ranges-to-excel/)
- [دمج أو فصل نطاق الخلايا](/cells/ar/python-net/merge-or-unmerge-range-of-cells/)
- [نقل مجموعة من الخلايا في ورقة العمل](/cells/ar/python-net/move-range-of-cells-in-a-worksheet/)
- [إنشاء أسماء مسماة محددة بنطاق العمل وورقة العمل](/cells/ar/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [البحث والاستبدال في بيانات النطاق](/cells/ar/python-net/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="python-net" >}}
