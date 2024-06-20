---
title: تحويل إكسيل إلى بيانات Python
type: docs
weight: 30
url: /ar/python-net/convert-excel-to-list/
description: تحويل إكسيل إلى قائمة باستخدام مكتبة Aspose.Cells for Python via .NET API.
keywords: تحويل إكسيل إلى قاموس باستخدام مكتبة Python Excel, تحويل دفتر العمل إلى قاموس باستخدام مكتبة Python Excel, تحويل كائن الصف إلى قائمة باستخدام مكتبة Python Excel, كيفية تحويل كائن القائمة إلى قائمة, تحويل كائن العمود إلى قائمة باستخدام مكتبة Python Excel, تحويل النطاق إلى قائمة باستخدام مكتبة Python Excel, تحويل ورقة العمل إلى قائمة باستخدام مكتبة Python Excel.
---

{{% alert color="primary" %}}

 باستخدام مكتبة Aspose.Cells for Python via .NET API, يمكنك تحويل دفتر العمل، ورقة العمل، النطاق، الصف، العمود والبيانات الأخرى في إكسيل إلى قائمة Python.

{{% /alert %}}

## **كيفية تحويل دفتر العمل في إكسيل إلى قاموس**
 فيما يلي مثال لكود مقتطف لتوضيح كيفية تصدير بيانات إكسيل إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. عبر جميع أوراق العمل وتحويل دفتر العمل إلى قاموس باستخدام مكتبة Python Excel ل Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

نتيجة الإخراج:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **كيفية تحويل دفتر العمل في إكسيل إلى قائمة**
فيما يلي مثال لكود مقتطف لتوضيح كيفية تصدير بيانات إكسيل إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. عبر جميع أوراق العمل وتحويل دفتر العمل إلى قائمة باستخدام مكتبة Python Excel ل Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

نتيجة الإخراج:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **كيفية تحويل ورقة العمل إلى قائمة**
فيما يلي مثال لكود مقتطف لتوضيح كيفية تصدير بيانات ورقة العمل إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. تحويل بيانات الورقة العمل إلى قائمة باستخدام Aspose.Cells for Python مكتبة Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

نتيجة الإخراج:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **كيفية تحويل كائن القائمة في Excel إلى قائمة**
فيما يلي مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات ListObject إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. أنشئ كائن ListObject.
1. تحويل بيانات ListObject إلى قائمة باستخدام Aspose.Cells for Python مكتبة Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

نتيجة الإخراج:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **كيفية تحويل صف Excel إلى قائمة**
فيما يلي مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات الصف إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. احصل على كائن الصف بواسطة فهرس الصف.
1. تحويل بيانات الصف إلى قائمة باستخدام Aspose.Cells for Python مكتبة Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

نتيجة الإخراج:
```
['Detroit', 'Central', 3074]
```

## **كيفية تحويل عمود Excel إلى قائمة**
فيما يلي مثال على مقتطفات الكود لتوضيح كيفية تصدير بيانات العمود إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. احصل على كائن العمود بواسطة فهرس العمود.
1. تحويل بيانات العمود إلى قائمة باستخدام مكتبة Aspose.Cells لإكسل بالبايثون.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

نتيجة الإخراج:
```
['Store', 3055, 3036, 3074]
```

## **كيفية تحويل نطاق إكسل إلى قائمة**
إليك مقتطف الكود المثالي لتوضيح كيفية تصدير بيانات النطاق إلى قائمة باستخدام Aspose.Cells for Python via .NET:
1. قم بتحميل [ملف العينة](sample_data.xlsx).
1. احصل على ورقة العمل الأولى.
1. إنشاء المجموعة.
1. تحويل بيانات النطاق إلى قائمة باستخدام مكتبة Aspose.Cells لإكسل بالبايثون.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

نتيجة الإخراج:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
