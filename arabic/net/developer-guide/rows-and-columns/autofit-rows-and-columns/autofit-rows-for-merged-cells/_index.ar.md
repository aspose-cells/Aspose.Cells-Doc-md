---
title: إعداد الصفوف تلقائياً للخلايا المدمجة
type: docs
weight: 120
url: /ar/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

يوفر Microsoft Excel ميزة تسمح لك بتحجيم ارتفاع الخلية وفقًا لمحتواها. الخاصية تسمى ضبط الصفوف تلقائيًا. لا يقوم Microsoft Excel بتعيين عملية التحجيم التلقائي على الخلايا المدمجة بشكل أصلي. أحيانًا تصبح الخاصية حيوية للمستخدم الذي يحتاج حقًا إلى تنفيذ ضبط الصفوف تلقائيًا على الخلايا المدمجة أيضًا.

{{% /alert %}}

## **كيفية استخدام نوعية AutoFitMergedCells لضبط ارتفاع الصفوف تلقائيًا**
يدعم Aspose.Cells هذه الميزة من خلال واجهة التطبيقات [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/). باستخدام هذه واجهة التطبيقات، يمكن تلقائيًا تكييف الصفوف في ورقة العمل بما في ذلك الخلايا المدمجة. هنا قائمة بجميع أنواع تكييف الصفوف في الخلايا المدمجة الممكنة:

- لا شيء
- السطر الأول
- السطر الأخير
- كل سطر

## **ضبط تلقائي للصفوف للخلايا المدمجة**

يرجى الاطلاع على الشفرة التالية، تقوم بإنشاء كائن ورقة عمل وإضافة أوراق عمل متعددة. استخدم طرق مختلفة لعمليات الضبط التلقائي في كل ورقة عمل. تُظهر اللقطة الشاشية النتائج بعد تنفيذ شفرة العينة.

<br>
<img src="result.png" width=80% />

## **شفرة C# عينة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
