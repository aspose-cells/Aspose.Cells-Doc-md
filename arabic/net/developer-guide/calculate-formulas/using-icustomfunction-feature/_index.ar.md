---
title: استخدام ميزة ICustomFunction
description: توضح هذه المقالة كيفية إنشاء دالة مخصصة في Microsoft Excel باستخدام ميزة ICustomFunction في مكتبة Aspose.Cells. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لتحديد وتسجيل الوظائف المخصصة والحصول على النتائج. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /ar/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

توفر هذه المقالة فهمًا تفصيليًا لكيفية استخدام ميزة ICustomFunction لتنفيذ الوظائف المخصصة باستخدام واجهات برمجة التطبيقات Aspose.Cells.

تسمح واجهة ICustomFunction بإضافة وظائف حساب الصيغة المخصصة لتوسيع محرك الحساب الأساسي Aspose.Cells من أجل تلبية متطلبات معينة. هذه الميزة مفيدة لتحديد الوظائف المخصصة (المحددة من قبل المستخدم) في ملف قالب أو في التعليمات البرمجية حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام Aspose.Cells APIs مثل أي وظيفة Excel افتراضية أخرى Microsoft.

 يرجى ملاحظة أنه تم استبدال هذه الواجهة بـ[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/)وسيتم إزالتها في المستقبل. بعض المقالات/الأمثلة الفنية حول API الجديد:[هنا](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) و[هنا](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **إنشاء وتقييم وظيفة محددة من قبل المستخدم**
 توضح هذه المقالة تنفيذ واجهة ICustomFunction لكتابة دالة مخصصة واستخدامها في جدول البيانات للحصول على النتائج. سوف نقوم بتحديد وظيفة مخصصة بالاسم**MyFunc** والتي سوف تقبل معلمتين مع التفاصيل التالية.

- تشير المعلمة الأولى إلى خلية واحدة
- تشير المعلمة الثانية إلى نطاق من الخلايا

ستضيف الوظيفة المخصصة جميع القيم من نطاق الخلايا المحدد كمعلمة ثانية وتقسم النتيجة على القيمة الموجودة في المعلمة الأولى.

إليك كيفية تنفيذ طريقة CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


فيما يلي كيفية استخدام الوظيفة المحددة حديثًا في جدول البيانات



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **ملخص**
تقوم واجهات برمجة التطبيقات Aspose.Cells فقط بوضع كائن ReferredArea في "paramsList" عندما تكون المعلمة المقابلة مرجعًا أو تكون النتيجة المحسوبة مرجعًا. إذا كنت بحاجة إلى المرجع نفسه، فيمكنك استخدام المنطقة المشار إليها مباشرة. إذا كنت تريد الحصول على قيمة خلية واحدة من المرجع المتوافق مع موضع الصيغة، فيمكنك استخدام طريقة ReferredArea.GetValue(rowOffset, int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلايا للمنطقة بأكملها، فيمكنك استخدام طريقة ReferredArea.GetValues.

نظرًا لأن واجهات برمجة التطبيقات Aspose.Cells تعطي المنطقة المشار إليها في "paramsList"، فلن تكون هناك حاجة إلى ReferredAreaCollection في "contextObjects" بعد الآن (في الإصدارات القديمة لم يكن قادرًا على إعطاء خريطة فردية لمعلمات الوظيفة المخصصة دائمًا) لذلك تمت إزالته من "كائنات السياق".

{{< highlight "java" >}}

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
