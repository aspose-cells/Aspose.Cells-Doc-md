---
title: استخدام خيارات التحقق من الأخطاء
type: docs
weight: 140
url: /ar/python-net/use-error-checking-options/
description: في هذه المقالة، ستجد رمز عيني يستخدم خيارات فحص الأخطاء لورقات العمل في Excel على سبيل المثال، الأرقام المخزنة كنص باستخدام واجهة برمجة تطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Excel Python، تخزين عدد كنص في Excel بواسطة Python، كيفية التعامل مع خيارات فحص الأخطاء في Excel باستخدام Python.
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بتعريف خيارات وقواعد التحقق من الأخطاء. يرى المستخدمون في كثير من الأحيان التحقق من الأخطاء عند إنشاء الصيغ، حيث يوضح مثلث صغير في الزاوية العلوية اليمنى للخلية عند وجود مشكلة في الخلية. يوفر Excel معلومات تساعد المستخدمين على تصحيح المشاكل الشائعة.

{{% /alert %}}

## **أنواع الأخطاء**

الأخطاء التي تعني أن الصيغة لا يمكن أن تُعيد نتيجة - مثل قسمة عدد على صفر - تتطلب اهتماماً فوريًا ويتم عرض قيمة خطأ في الخلية. يُظهر النقر على المثلث الأخضر علامة تعجب، والنقر على ذلك يفتح قائمة الخيارات.

يمكن حل الخطأ باستخدام الخيارات، أو تجاهله. تجاهل الخطأ يعني أن هذا الخطأ لن يظهر في عمليات التحقق من الأخطاء في المستقبل.

يوفر Aspose.Cells for Python via .NET ميزات خيارات فحص الأخطاء. تدير فئة [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) أنواعًا مختلفة من فحوصات الأخطاء، على سبيل المثال، الأرقام المخزنة كنص، أخطاء حساب الصيغ وأخطاء الصحة. استخدم تعداد [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) لضبط الفحص الخطأ المرغوب فيه.

## **الأرقام المخزنة كنص**

في بعض الأحيان، قد تكون الأرقام مهيأة ومخزنة في الخلايا كنص. يمكن أن يسبب هذا مشاكل في الحسابات أو إنتاج ترتيبات فرز مربكة. الأرقام التي تم تهيئتها كنص تكون محاذية إلى اليسار بدلاً من اليمين في الخلية. إذا لم تُعَد الصيغة التي يجب أن تقوم بعملية رياضية على الخلايا قيمة، فحقق محاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض أو كل تلك الخلايا أرقامًا تم تهيئتها كنص.

يمكنك استخدام خيارات التحقق من الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:

1. على قائمة **الأدوات**، انقر على **خيارات**.
1. حدد علامة التبويب فحص الأخطاء. يتم تحديد خيار **العدد المخزن كنص** افتراضيًا.
1. قم بتعطيله.

يظهر الرمز العيني التالي كيفية تعطيل خيار فحص الأخطاء للأرقام المخزنة كنص لورقة عمل في ملف XLS النموذج باستخدام واجهات مستخدم برمجة تطبيقات Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
