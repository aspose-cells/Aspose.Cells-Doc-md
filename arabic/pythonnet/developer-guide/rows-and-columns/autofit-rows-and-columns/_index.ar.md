---
title: ضبط تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/python-net/autofit-rows-and-columns/
description: يوضح هذا المقال كيفية تحجيم الصفوف والأعمدة تلقائيًا، صفوف الخلية المدمجة والصف في نطاق الخلايا باستخدام Aspose.Cells لـ Python via .NET.
keywords: مكتبة Python Excel، تحجيم الصفوف في Python، تحجيم الأعمدة في Python، تحجيم الصف في نطاق الخلايا في Python، تحجيم صفوف الخلية المدمجة في Python.
---

{{% alert color="primary" %}}

يتيح Microsoft Excel للمستخدمين تغيير حجم عرض وارتفاع الخلايا وفقًا لمحتواها. تتوفر هذه الخاصية أيضًا من خلال Aspose.Cells لـ Python via .NET بحيث يمكن للمطورين تغيير أبعاد خلية أثناء التشغيل.

{{% /alert %}}

## **ضبط تلقائي**

Aspose.Cells لبيثون via .NET توفر فئة تمثل ملف Excel لميكروسوفت. فئة تحتوي على مجموعة تسمح بالوصول إلى كل ورق عمل في ملف Excel. الورقة العمل ممثلة بفئة. فئة توفر مجموعة واسعة من الخصائص والطرق لإدارة ورقة عمل. هذا المقال يستعرض استخدام الفئة لتناسب صفوف أو أعمدة.

### **ضبط تلقائي للصف - بسيط**

أبسط الطرق لضبط عرض وارتفاع الصف هي استدعاء [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الفئة [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int). يستغرق الأمر المنهج [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) فهو خطوة بسيطة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **كيفية ضبط صف تلقائيًا في مجموعة من الخلايا**

الصف يتكون من عدة أعمدة. Aspose.Cells لبيثون via .NET تسمح للمطورين بتحديد الصف على أساس المحتوى في نطاق الخلايا داخل الصف عن طريق استدعاء النسخة المعدلة من الطريقة. تأخذ المعلمات التالية:

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.
- **فهرس العمود الأول**, فهرس العمود الأول للصف.
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.

يقوم الأسلوب [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) بفحص محتوى كل الأعمدة في الصف ثم يضبط الصف تلقائيًا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **كيفية ضبط العمود تلقائيًا في مجموعة من الخلايا**

يتكون العمود من العديد من الصفوف. يمكن ضبط عرض العمود تلقائيًا بناءً على المحتوى في مجموعة من الخلايا في العمود عن طريق استدعاء نسخة محملة من [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) الذي يأخذ المعلمات التالية:

- **فهرس العمود**: فهرس العمود الذي سيتم تلائم حجمه تلقائياً.
- **فهرس الصف الأول**: فهرس أول صف في العمود.
- **فهرس الصف الأخير**: فهرس آخر صف في العمود.

يقوم الطريقة [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) بفحص محتويات جميع الصفوف في العمود ثم يقوم بضبط حجم العمود تلقائياً.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **كيفية تلائم حجم الصفوف للخلايا المدمجة**

مع Aspose.Cells لبيثون via .NET من الممكن تحديد تناسب صفوف حتى للخلايا المدمجة باستخدام واجهة. توفر فئة خاصية يمكن استخدامها لتحديد تناسب الصفوف للخلايا المدمجة. تقبل مجموعة تفاضلية تحتوي على الأعضاء التالية.

- NONE: تجاهل الخلايا المدمجة.
- FIRST_LINE: فقط يوسع ارتفاع السطر الأول.
- السطر_الأخير: يزيد فقط ارتفاع الصف الأخير.
- كل_سطر: يزيد فقط ارتفاع كل صف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

يمكنك أيضًا محاولة استخدام الإصدارات الزائدة من الأساليب [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) و [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) التي تقبل مجموعة من الصفوف/الأعمدة ومثيلًا من [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) لتلائم حجم الصفوف/الأعمدة المحددة بالطريقة التي ترغب فيها [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions).

توقيعات الأساليب المذكورة أعلاه هي كالتالي:

1. تلائم_آلي_الصفوف(الصف_الأول، الصف_الأخير، [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) خيارات)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **مهم معرفته**

{{% alert color="primary" %}}

إذا كانت الخلية مدمجة، فلن تُطبق الأساليب تلقائي التلائم، وهو نفس السلوك الذي تظهره Microsoft Excel. يمكنك حل هذا عن طريق استخدام API تصفية تلقائية. علاوة على ذلك، إذا كان النص في الخلية ملتفًّا، فلن يتم تطبيق أسلوب [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) أيضًا. شيء آخر تحتاج إلى معرفته هو أن أساليب التلائم التلقائي تستهلك الوقت. لذا، يجب عليك استدعاء هذه الأساليب بأقل عدد ممكن من المرات لضمان كفاءة تطبيقك.

{{% /alert %}}

## **مواضيع متقدمة**
- [تلائم حجم الصفوف للخلايا المدمجة](/cells/ar/python-net/autofit-rows-for-merged-cells/)
