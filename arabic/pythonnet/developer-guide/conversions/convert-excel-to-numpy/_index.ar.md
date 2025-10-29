---
title: تحويل إكسل إلى NumPy
type: docs
weight: 30
url: /ar/python-net/convert-excel-to-numpy/
description: تحويل إكسل إلى NumPy باستخدام واجهة برمجة التطبيقات Aspose.Cells لإكسل بالبايثون via .NET.
keywords: تحويل إكسل في بايثون إلى مصفوفة NumPy، تصدير ورقة العمل إلى مصفوفة NumPy في بايثون via NET، تحويل الصف إلى مصفوفة NumPy في بايثون، تحويل الجدول إلى مصفوفة NumPy في بايثون، تصدير ListObject إلى مصفوفة NumPy في بايثون via NET، تحويل النطاق إلى مصفوفة NumPy، العمود إلى مصفوفة NumPy باستخدام بايثون.
---

## **مقدمة إلى NumPy**
NumPy (Numerical Python) هو امتداد لحسابات Python الرقمية مفتوح المصدر. يمكن استخدام هذه الأداة لتخزين ومعالجة المصفوفات الكبيرة، والتي تكون أكثر كفاءة بكثير من هيكل القائمة المتداخلة في Python (والتي يمكن أيضًا استخدامها لتمثيل المصفوفات). يدعم مجموعة كبيرة من المصفوفات ذات الأبعاد وعمليات المصفوفات، كما يوفر أيضًا عددًا كبيرًا من مكتبات الدوال الرياضية لعمليات المصفوفات. 

الوظائف الرئيسية لـ NumPy:
1. Ndarray ، وهي كائن مصفوفة متعددة الأبعاد ، هي هيكل بيانات سريع ومرن وموفر للمساحة.
1. العمليات الجبر الخطي ، بما في ذلك ضرب المصفوفة ، والانعكاس ، وغيرها.
1. تحويل فورييه ، القيام بتحويل فورييه سريع على مصفوفة.
1. عملية سريعة لمصفوفات الأعداد العائمة.
1. دمج كود اللغة C في Python لجعله يعمل بشكل أسرع.

عن طريق استخدام واجهة برمجة تطبيقات Aspose.Cells for Python via .NET API يمكنك تحويل Excel، TSV، CSV، Json والعديد من التنسيقات المختلفة إلى Numpy ndarray.

## **كيفية تحويل كتاب عمل Excel إلى NumPy ndarray**
إليك مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات Excel إلى مصفوفة NumPy باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. قم بتصفح بيانات Excel وتصدير البيانات إلى NumPy ndarray باستخدام Aspose.Cells for Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

نتيجة الإخراج:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **كيفية تحويل ورق العمل إلى NumPy ndarray**
إليك مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات ورق العمل إلى Numpy ndarray باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. تحويل بيانات ورق العمل إلى Numpy ndarray باستخدام مكتبة Aspose.Cells for Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

نتيجة الإخراج:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **كيفية تحويل مجموعة Excel إلى NumPy ndarray**
إليك مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات المجموعة إلى Numpy ndarray باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. إنشاء المجموعة.
1. تحويل بيانات المجموعة إلى Numpy ndarray باستخدام مكتبة Aspose.Cells for Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

نتيجة الإخراج:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **كيفية تحويل ListObject من Excel إلى NumPy ndarray**
إليك مقتطف كود مثالي يوضح كيفية تصدير بيانات ListObject إلى NumPy ndarray باستخدام Aspose.Cells for Python via .NET
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. أنشئ كائن ListObject.
1. قم بتحويل بيانات ListObject إلى NumPy ndarray باستخدام مكتبة Aspose.Cells for Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

نتيجة الإخراج:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **كيفية تحويل صف Excel إلى NumPy ndarray**
إليك مقتطف كود مثالي يوضح كيفية تصدير بيانات الصف إلى NumPy ndarray باستخدام Aspose.Cells for Python via .NET
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. احصل على كائن الصف بواسطة فهرس الصف.
1. قم بتحويل بيانات الصف إلى NumPy ndarray باستخدام مكتبة Aspose.Cells for Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

نتيجة الإخراج:
```
['Detroit' 'Central' '3074']
```

## **كيفية تحويل عمود Excel إلى NumPy ndarray**
إليك مقتطف كود مثالي يوضح كيفية تصدير بيانات العمود إلى NumPy ndarray باستخدام Aspose.Cells for Python via .NET
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. احصل على كائن العمود بواسطة فهرس العمود.
1. قم بتحويل بيانات العمود إلى NumPy ndarray باستخدام مكتبة Aspose.Cells for Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

نتيجة الإخراج:
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
