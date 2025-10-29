---
title: إعداد الصفوف تلقائياً للخلايا المدمجة
type: docs
weight: 120
url: /ar/python-net/autofit-rows-for-merged-cells/
description: يوضح هذا المقال كيفية ضبط الصفوف تلقائيًا للخلايا المدمجة من خلال برنامج Aspose.Cells لبرنامج Python via .NET.
keywords: مكتبة بايثون لإكسل، كيفية استخدام AutoFitMergedCellsType لضبط الصفوف تلقائيًا، ضبط الصفوف تلقائيًا للخلايا المدمجة في Python.
---

{{% alert color="primary" %}}

يوفر Microsoft Excel ميزة تسمح لك بتحجيم ارتفاع الخلية وفقًا لمحتواها. الخاصية تسمى ضبط الصفوف تلقائيًا. لا يقوم Microsoft Excel بتعيين عملية التحجيم التلقائي على الخلايا المدمجة بشكل أصلي. أحيانًا تصبح الخاصية حيوية للمستخدم الذي يحتاج حقًا إلى تنفيذ ضبط الصفوف تلقائيًا على الخلايا المدمجة أيضًا.

{{% /alert %}}

## **كيفية استخدام نوعية AutoFitMergedCells لضبط ارتفاع الصفوف تلقائيًا**
يدعم Aspose.Cells لبرنامج Python via .NET هذه الميزة من خلال [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/). باستخدام هذا الواجهة البرمجية، من الممكن ضبط ارتفاع الصفوف تلقائيًا في ورقة العمل بما في ذلك الخلايا المدمجة. هنا قائمة بكافة أنواع الضبط التلقائي الممكنة للخلايا المدمجة:

- NONE
- السطر_الأول
- السطر_الأخير
- كل_سطر

## **ضبط تلقائي للصفوف للخلايا المدمجة**

يرجى الاطلاع على الشفرة التالية، تقوم بإنشاء كائن ورقة عمل وإضافة أوراق عمل متعددة. استخدم طرق مختلفة لعمليات الضبط التلقائي في كل ورقة عمل. تُظهر اللقطة الشاشية النتائج بعد تنفيذ شفرة العينة.

<br>
<img src="result.png" width=80% />

## **شفرة C# عينة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
