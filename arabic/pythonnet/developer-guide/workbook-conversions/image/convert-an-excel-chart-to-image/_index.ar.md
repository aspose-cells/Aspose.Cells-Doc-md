---
title: تحويل مخطط Excel إلى صورة
type: docs
weight: 20
url: /ar/python-net/convert-an-excel-chart-to-image/
description: تحويل مخطط Excel إلى صورة باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

تعد المخططات جذابة بصريًا وتسهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات. على سبيل المثال، بدلاً من تحليل أعمدة أرقام ورقة العمل، يُظهر المخطط في لمحة سريعة ما إذا كانت المبيعات تنخفض أو ترتفع، أو كيفية مقارنة المبيعات الفعلية بالمبيعات المتوقعة. يُطلب من الأشخاص في كثير من الأحيان تقديم معلومات إحصائية ورسومية بطريقة سهلة الفهم وسهلة الصيانة. صورة تساعد.

في بعض الأحيان، تكون هناك حاجة إلى المخططات في تطبيق أو صفحات ويب. أو قد تكون هناك حاجة إليها لمستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو بعض التطبيقات الأخرى. في كل حالة، تريد عرض المخطط كصورة بحيث يمكنك استخدامه في مكان آخر.

{{% /alert %}}

##  **تحويل المخططات إلى صور**

في الأمثلة الواردة هنا، يتم تحويل المخطط الدائري وحرف العمود إلى صور.

###  **تحويل مخطط دائري إلى ملف صورة**

أولاً، قم بإنشاء مخطط دائري في Microsoft Excel ثم قم بتحويله إلى ملف صورة باستخدام Aspose.Cells for Python via .NET. يقوم الكود الموجود في هذا المثال بإنشاء صورة EMF بناءً على المخطط الدائري في ملف Excel القالب Microsoft.

|**الإخراج: صورة المخطط الدائري**|
| :- |
|![ما يجب القيام به:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. إنشاء مخطط دائري في Microsoft إكسل:
 1. فتح مصنف جديد في Microsoft Excel.
 1. أدخل بعض البيانات في ورقة العمل.
 1. قم بإنشاء مخطط دائري بناءً على البيانات.
 1. احفظ الملف.

|**ملف الإدخال.**|
| :- |
|![ما يجب القيام به:image_alt_text](convert-an-excel-chart-to-image_2.png)|

نستضيف حزمنا Python في مستودعات PyPi.

قم بتثبيت Aspose.Cells for Python من pypi، استخدم الأمر كـ: $ pip install aspose-cells-python.

ويمكنك أيضًا اتباع الإرشادات خطوة بخطوة حول كيفية تثبيت "Aspose.Cells for Python via .NET" في بيئة المطور لديك.
1. تحميل وتثبيت Aspose.Cells for Python via .NET:
 1. تثبيت Aspose.Cells for Python via .NET من[pypi](https://pypi.org/project/aspose-cells-python/)استخدم الأمر كـ: $ pip install aspose-cells-python.
 1. ويمكنك أيضًا متابعة[تعليمات خطوه بخطوه](https://docs.aspose.com/cells/python-net/getting-started/)حول كيفية تثبيت "Aspose.Cells for Python via .NET" في بيئة المطور لديك.

 الجميع[Aspose](http://www.aspose.com/) تعمل المكونات في وضع التقييم عند تثبيتها لأول مرة. وضع التقييم ليس له حد زمني ويقوم فقط بإدخال العلامات المائية في المستندات الناتجة.

1. إنشاء مشروع:
 1. ابدأ تشغيل Visual Studio.
 1. أضف مرجع مكتبة (استيراد المكتبة) إلى مشروعك Python.
 1. اكتب الكود الذي يبحث عن المخطط ويحوله. يوجد أدناه الرمز الذي يستخدمه المكون لإنجاز المهمة. يتم استخدام عدد قليل جدًا من أسطر التعليمات البرمجية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **تحويل مخطط عمودي إلى ملف صورة**

قم أولاً بإنشاء مخطط عمودي في برنامج Excel Microsoft وقم بتحويله إلى ملف صورة، كما هو مذكور أعلاه. بعد تنفيذ نموذج التعليمات البرمجية، يتم إنشاء ملف JPEG بناءً على المخطط العمودي في ملف Excel القالب.

|**ملف الإخراج: صورة مخطط عمود.**|
| :- |
|![ما يجب القيام به:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. إنشاء مخطط عمودي في Microsoft Excel:
 1. افتح مصنفًا جديدًا في Microsoft Excel.
 1. أدخل بعض البيانات في ورقة العمل.
 1. قم بإنشاء مخطط عمودي بناءً على البيانات.
 1. احفظ الملف.

|**ملف الإدخال.**|
| :- |
|![ما يجب القيام به:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. قم بإعداد مشروع، مع المراجع، كما هو موضح أعلاه.
1. تحويل المخطط إلى صورة بشكل حيوي. فيما يلي الكود الذي يستخدمه المكون لإنجاز المهمة. الكود مشابه للكود السابق:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
