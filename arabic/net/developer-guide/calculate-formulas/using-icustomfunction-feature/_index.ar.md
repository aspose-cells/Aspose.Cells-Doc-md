---
title: استخدام ميزة ICustomFunction
description: يصف هذا المقال كيفية إنشاء وظيفة مخصصة في Microsoft Excel باستخدام ميزة ICustomFunction في مكتبة Aspose.Cells. من خلال تحميل ملف Excel الحالي أو إنشاء ملف Excel جديد ، يمكننا استخدام الطرق المقدمة من Aspose.Cells لتعريف وتسجيل الوظائف المخصصة والحصول على النتائج. في النهاية ، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: ميزات Aspose.Cells، Excel، ICustomFunction، الدوال المخصصة، كيفية حساب الدوال المخصصة.
type: docs
weight: 30
url: /ar/net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

يوفر هذا المقال فهمًا مفصلًا لكيفية استخدام ميزة ICustomFunction لتنفيذ الوظائف المخصصة باستخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells.

تسمح واجهة ICustomFunction بإضافة وظائف حساب المعادلة المخصصة لتوسيع محرك الحساب الأساسي لـ Aspose.Cells من أجل تلبية متطلبات معينة. تُستخدم هذه الميزة لتعريف الوظائف المخصصة (تعريف المستخدم) في ملف نموذج أو في الكود حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells مثل أي وظيفة افتراضية أخرى في Microsoft Excel.

يرجى ملاحظة أن هذه الواجهة قد تم استبدالها بـ [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) وستُزال في المستقبل. بعض المقالات الفنية/الأمثلة حول الواجهة البرمجية الجديدة: [هنا](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) و[هنا](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **إنشاء وتقييم وظيفة معرفة المستخدم**
يُظهر هذا المقال تنفيذ واجهة ICustomFunction لكتابة وظيفة مخصصة واستخدامها في جدول البيانات للحصول على النتائج. سنقوم بتحديد وظيفة مخصصة بالاسم **MyFunc** التي ستقبل 2 معلمة بالتفاصيل التالية.

- يشير المعلم الأول إلى خلية واحدة
- يشير المعلم الثاني إلى مجموعة من الخلايا

سيقوم الدالة المخصصة بإضافة جميع القيم من نطاق الخلية المحدد كمعلم ثاني وتقسيم النتيجة على القيمة في المعلم الأول.

هنا كيف قمنا بتنفيذ طريقة CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


هنا كيفية استخدام الدالة المحددة حديثا في جدول بيانات



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **نظرة عامة**
تضع واجهات برمجة التطبيقات للخلايا Aspose.Cells كائن ReferredArea في "paramsList" عندما يكون المعلم المقابل مرجعًا أو نتاجه المحسوب هو مرجع. إذا كنت بحاجة إلى المرجع نفسه ثم يمكنك استخدام ReferredArea مباشرة. إذا كنت تحتاج إلى الحصول على قيمة خلية واحدة من المرجع المقابل مع وضع الصيغة، يمكنك استخدام طريقة ReferredArea.GetValue(rowOffset، int colOffset). إذا كنت بحاجة إلى مجموعة قيم الخلية للمنطقة بأكملها ثم يمكنك استخدام طريقة ReferredArea.GetValues.

نظرًا لأن واجهات برمجة التطبيقات Aspose.Cells تقدم ReferredArea في "paramsList"، فستكون مجموعة ReferredArea في "contextObjects" غير مطلوبة بعد الآن (في الإصدارات القديمة لم تكن دائمًا قادرة على تقديم خريطة واحد إلى واحد لمعلمات الدالة المخصصة) ولذلك تمت إزالتها من "contextObjects".

{{< highlight java >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
