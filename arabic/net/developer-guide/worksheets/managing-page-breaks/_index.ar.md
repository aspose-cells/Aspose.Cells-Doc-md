---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/net/managing-page-breaks/
---
{{% alert color="primary" %}}

وفقًا للتعريف ، فاصل الصفحة هو مكان في تدفق النص حيث تنتهي إحدى الصفحات وتبدأ الصفحة التالية. Microsoft يتيح Excel للمستخدمين إضافة فواصل الصفحات إلى أي خلية محددة بورقة العمل.

موقع الخلية حيث تمت إضافة فاصل الصفحة وانتهاء الصفحة وبقية البيانات بعد طباعة فاصل الصفحة على الصفحة التالية أثناء الطباعة. بكلمات بسيطة ، تقسم فواصل الصفحات ورقة العمل إلى صفحات متعددة وفقًا لمواصفاتك. يمكنك أيضًا إضافة فواصل صفحات إلى أوراق العمل الخاصة بك في وقت التشغيل باستخدام Aspose.Cells. يسمح Aspose.Cells للمطورين بإضافة نوعين من فواصل الصفحات:

- فاصل صفحة أفقي
- فاصل صفحة عمودي

في بقية المناقشة ، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}}

## **فواصل الصفحة**

يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)توفر فئة مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

 لإضافة فواصل الصفحات ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) و[**عمودي PageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)الخصائص.

 ال[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) و[**عمودي PageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)الخصائص هي مجموعات قد تحتوي على عدة فواصل صفحات. تحتوي كل مجموعة على عدة طرق لإدارة فواصل الصفحات الأفقية والعمودية.

### **مضيفا فواصل الصفحات**

 لإضافة فاصل صفحات في ورقة عمل ، قم بإدراج فواصل صفحات عمودية وأفقية في الخلية المحددة عن طريق استدعاء ملف[**أفقي PageBreakCollection.Add ()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) و[**VerticalPageBreakCollection.Add ()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) طُرق. كل**يضيف** تأخذ الطريقة اسم الخلية حيث يجب إضافة الفاصل.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

في أوضاع معاينة فاصل الصفحة أو معاينة الطباعة ، يمكنك مشاهدة كيفية عمل فواصل الصفحات هذه.

{{% /alert %}}

### **مسح كافة فواصل الصفحات**

 لمسح كل فواصل الصفحات في ورقة عمل ، قم باستدعاء[**أفقي بيجبريككولكشن**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) و[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) المجموعات[**صافي()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)طُرق.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **إزالة فاصل صفحة معين**

 لإزالة فاصل صفحة معين ، اتصل بـ[**أفقي PageBreakCollection.RemoveAt ()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) و[**VerticalPageBreakCollection.RemoveAt ()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) طُرق. كل**RemoveAt**يأخذ الأسلوب فهرس فاصل الصفحة على وشك إزالته.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **من المهم أن تعرف**

 عندما تحدد**FitToPages** الخصائص (أي[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) و[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) في إعدادات إعداد الصفحة ، تتأثر إعدادات فاصل الصفحة ، لذلك إذا قمت بطباعة ورقة العمل ، فلن يتم أخذ إعدادات فاصل الصفحة في الاعتبار على الرغم من استمرار تعيينها.
