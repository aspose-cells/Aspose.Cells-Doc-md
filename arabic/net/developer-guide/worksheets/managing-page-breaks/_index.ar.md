---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/net/managing-page-breaks/
description: يقدم هذا المقال رمز مصدري مثالي ويشرح كيفية إضافة فواصل الصفحات، مسح فواصل الصفحات، أو حذف فواصل الصفحات الخاصة في أوراق العمل في إكسل برمجياً باستخدام واجهة برمجة التطبيقات C# أو المكتبة .NET.
keywords: كسر الصفحة c#، كسر الصفحة في اكسل c#، مسح كسر الصفحة c#، حذف كسر الصفحة المحدد c#
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

في الموقع الذي تمت إضافة كسر الصفحة فيه، تنتهي الصفحة ويتم طباعة بقية البيانات بعد كسر الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، كسر الصفحة يقسم ورقة العمل إلى عدة صفحات وفقًا لمواصفاتك. يمكنك أيضًا إضافة كسر الصفحة إلى ورقة العمل الخاصة بك أثناء التشغيل باستخدام Aspose.Cells. تسمح Aspose.Cells للمطورين بإضافة نوعين من كسر الصفحة:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}}

## **كسرات الصفحة**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

لإضافة كسر الصفحة، استخدم خصائص [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) للفئة والخصائص [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks).

الخصائص [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) و [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) هي مجموعات قد تحتوي على العديد من كسر الصفحة. تحتوي كل مجموعة على العديد من الطرق لإدارة كسر الصفحة الأفقي والعمودي.

### **إضافة فواصل الصفحات**

لإضافة كسر صفحة في ورقة العمل، ضع كسر الصفحة العمودي والأفقي في الخلية المحددة عن طريق استدعاء الطرق [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) و [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index). تأخذ كل طريقة **إضافة** اسم الخلية التي يجب إضافة كسرها.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}

### **مسح كافة فواصل الصفحات**

لمسح كل كسر الصفحة في ورقة العمل، استدعي طرق [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) و [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) من مجموعات [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **إزالة كسر صفحة محدد**

لإزالة كسر الصفحة المحدد، استدعي الطرق [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) و [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). تأخذ كل طريقة **إزالة في** مؤشر كسر الصفحة الذي سيتم إزالته.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **مهم معرفته**

عند ضبط خصائص **تناسب الصفحات** (أي [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) و [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) في إعدادات تكوين الصفحة، يتأثر إعدادات كسر الصفحة، لذلك، إذا قمت بطباعة ورقة العمل، فإن إعدادات كسر الصفحة لا تعتبر على الرغم من أنها ما زالت مضبوطة.
