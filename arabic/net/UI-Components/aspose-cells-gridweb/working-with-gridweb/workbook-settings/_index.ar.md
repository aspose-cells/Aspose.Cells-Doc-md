---
title: إعدادات سجل العمل
type: docs
weight: 250
url: /ar/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: يصف هذا المقال إعدادات سجل العمل في GridWeb.
keywords: GridWeb، الإعدادات
---


هناك بعض الإعدادات التي يمكننا تحديدها عن طريق تعيين GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**الاسم**|**الوصف**|
| :- | :- |
|MaxIteration | يحصل أو يعين الحد الأقصى لعدد التكرارات لحل إشارة مرجع دائرية، القيمة الافتراضية هي 100. |
|Iteration | يحصل أو يعين ما إذا كان يتم استخدام التكرار لحل الإشارات المرجعية الدائرية. |
|ForceFullCalculate | يحصل أو يعين ما إذا كان يتم احتساب كلي في كل مرة يتم فيها تشغيل حساب. |
|CreateCalcChain | يحصل على قيمة أو يضبط ما إذا كان سيتم إنشاء سلسلة صيغ حسابية محسوبة. القيمة الافتراضية هي false.
|ReCalculateOnOpen | يحصل على قيمة أو يضبط ما إذا كان سيتم إعادة حساب جميع الصيغ عند فتح الملف.
|PrecisionAsDisplayed | القيمة true إذا كانت الحسابات في هذا الدفتر سيتم إجراؤها باستخدام دقة الأرقام فقط حسبما تم عرضها.
|Date1904 | يحصل على قيمة أو يضبط قيمة تمثل ما إذا كان الدفتر يستخدم نظام التاريخ 1904.
|CheckCustomNumberFormat | يحصل على قيمة أو يضبط ما إذا كان يتم فحص الشكل العددي المخصص عند ضبط الشكل المخصص للنمط.
|Author | يحصل على مؤلف الملف ويضبطه.



على سبيل المثال، يقوم الكود التالي بتعيين ReCalculateOnOpen إلى القيمة false لإيقاف الحساب عند فتح الملف:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 الكود التالي يقوم بتعيين المؤلف للملف:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


