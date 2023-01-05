---
title: استخدام ميزة ICustomFunction
type: docs
weight: 30
url: /ar/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

تقدم هذه المقالة فهمًا تفصيليًا لكيفية استخدام ميزة ICustomFunction لتنفيذ وظائف مخصصة مع واجهات برمجة تطبيقات Aspose.Cells.

تسمح واجهة ICustomFunction بإضافة وظائف حساب الصيغة المخصصة لتوسيع محرك الحساب الأساسي Aspose.Cells من أجل تلبية متطلبات معينة. هذه الميزة مفيدة لتعريف الوظائف المخصصة (المعرفة من قبل المستخدم) في ملف قالب أو في التعليمات البرمجية حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة تطبيقات Aspose.Cells مثل أي وظيفة إكسل Microsoft افتراضية أخرى.

{{% /alert %}} 
## **إنشاء وتقييم وظيفة محددة من قبل المستخدم**
توضح هذه المقالة تنفيذ واجهة ICustomFunction لكتابة وظيفة مخصصة واستخدامها في جدول البيانات للحصول على النتائج. سنحدد وظيفة مخصصة بالاسم**MyFunc** والتي ستقبل معاملين مع التفاصيل التالية.

- تشير المعلمة الأولى إلى خلية واحدة
- تشير المعلمة الثانية إلى نطاق من الخلايا

ستضيف الوظيفة المخصصة جميع القيم من نطاق الخلايا المحدد كمعلمة ثانية وتقسيم النتيجة بالقيمة في المعلمة الأولى.

إليك كيفية تنفيذنا لطريقة CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


فيما يلي كيفية استخدام الوظيفة المحددة حديثًا في جدول بيانات



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **ملخص**
قامت واجهات برمجة التطبيقات Aspose.Cells بوضع الكائن RefifiedArea في "قائمة paramsList" عندما تكون المعلمة المقابلة مرجعًا أو تكون النتيجة المحسوبة مرجعًا. إذا كنت بحاجة إلى المرجع نفسه ، فيمكنك استخدام RefifiedArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية واحدة من المرجع المقابل لموضع الصيغة ، فيمكنك استخدام أسلوب RefifiedArea.GetValue (rowOffset ، int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلية للمنطقة بأكملها ، فيمكنك استخدام طريقة RefifiedArea.GetValues.

نظرًا لأن واجهات برمجة التطبيقات Aspose.Cells تعطي RefifiedArea في "paramsList" ، فلن تكون هناك حاجة إلى مجموعة RefifiedAreaCollection في "ContextObjects" بعد الآن (في الإصدارات القديمة ، لم تكن قادرة على إعطاء مخطط واحد لواحد لمعلمات الوظيفة المخصصة دائمًا) تمت إزالته من "ContextObjects".

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
