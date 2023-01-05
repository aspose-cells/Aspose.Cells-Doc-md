---
title: إعدادات المصنف
type: docs
weight: 250
url: /ar/net/aspose-cells-gridweb/workbook-settings/
description: توضح هذه المقالة إعدادات المصنف لـ GridWeb.
keywords: settings
---
هناك بعض الإعدادات التي يمكننا تحديدها من خلال ضبط GridWorkbookSettings:

 
- **[GridWorkbookSettings] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**اسم** |**وصف** |
|:- |:- |
| MaxIteration| الحصول على أو تعيين الحد الأقصى لعدد التكرارات لحل مرجع معاد ، القيمة الافتراضية هي 100.|
| تكرار| الحصول على أو تحديد ما إذا كان سيتم استخدام التكرار لحل المراجع الدائرية.|
| ForceFullCalculate| الحصول على أو تعيين ما إذا كان سيتم إجراء الحساب بالكامل في كل مرة يتم فيها تشغيل عملية حسابية.|
| CreateCalcChain|الحصول على أو تحديد ما إذا كان يتم إنشاء سلسلة الصيغ المحسوبة. الافتراضي هو خطأ.|
| ReCalculateOnOpen| يحصل أو يحدد ما إذا كان يعيد حساب كل الصيغ عند فتح الملف.|
| الدقة| صواب إذا كانت العمليات الحسابية في هذا المصنف ستتم باستخدام دقة الأرقام فقط أثناء عرضها|
| التاريخ 1904| الحصول على أو تعيين قيمة تمثل ما إذا كان المصنف يستخدم نظام التاريخ 1904.|
| تحقق من CustomNumberFormat| الحصول على أو تحديد ما إذا كان التحقق من تنسيق الأرقام المخصص عند تعيين Style.Custom.|
| مؤلف| الحصول على كاتب الملف وتعيينه.|
 


على سبيل المثال ، تقوم الشفرة التالية بتعيين ReCalculateOnOpen على false لإيقاف caculate عند فتح الملف:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 قام الكود التالي بتعيين كاتب الملف:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 