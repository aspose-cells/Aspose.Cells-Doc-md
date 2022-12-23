---
title: استخدام ميزة ICustomFunction
type: docs
weight: 890
url: /ar/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

تقدم هذه المقالة فهمًا تفصيليًا لكيفية استخدام ميزة ICustomFunction لتنفيذ وظائف مخصصة مع واجهات برمجة تطبيقات Aspose.Cells.

تسمح واجهة ICustomFunction بإضافة وظائف حساب الصيغة المخصصة لتوسيع محرك الحساب الأساسي Aspose.Cells من أجل تلبية متطلبات معينة. هذه الميزة مفيدة لتعريف الوظائف المخصصة (المعرفة من قبل المستخدم) في ملف قالب أو في التعليمات البرمجية حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة تطبيقات Aspose.Cells مثل أي وظيفة إكسل Microsoft افتراضية أخرى.

 يرجى ملاحظة أنه تم استبدال هذه الواجهة بـ[الخلاصةحساب المحرك](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) وستتم إزالتها في المستقبل. بعض المقالات / الأمثلة الفنية حول API الجديد:[هنا](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) و[هنا](/cells/ar/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 إذا كنت مستخدمًا جديدًا لـ Aspose.Cells for Java APIs ، فيرجى التحقق[هذه](https://docs.aspose.com/cells/java/installation/) مقال لمعرفة كيف يمكنك الحصول على Aspose.Cells for Java والرجوع إليه في مشروعك.

{{% /alert %}} 
## **إنشاء وتقييم وظيفة محددة من قبل المستخدم**
توضح هذه المقالة تنفيذ واجهة ICustomFunction لكتابة وظيفة مخصصة واستخدامها في جدول البيانات للحصول على النتائج. سنحدد وظيفة مخصصة بالاسم**MyFunc** والتي ستقبل معاملين مع التفاصيل التالية.

- تشير المعلمة الأولى إلى خلية واحدة
- تشير المعلمة الثانية إلى نطاق من الخلايا

ستضيف الوظيفة المخصصة جميع القيم من نطاق الخلايا المحدد كمعلمة ثانية وتقسيم النتيجة بالقيمة في المعلمة الأولى.

إليك كيفية تنفيذنا لطريقة calculateCustomFunction.

**Java**

{{< highlight "csharp" >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

فيما يلي كيفية استخدام الوظيفة المحددة حديثًا في جدول بيانات

**Java**

{{< highlight "csharp" >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **ملخص**
قامت واجهات برمجة التطبيقات Aspose.Cells بوضع الكائن RefifiedArea في "قائمة paramsList" عندما تكون المعلمة المقابلة مرجعًا أو تكون النتيجة المحسوبة مرجعًا. إذا كنت بحاجة إلى المرجع نفسه ، فيمكنك استخدام RefifiedArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية واحدة من المرجع المطابق لموضع الصيغة ، فيمكنك استخدام أسلوب RefifiedArea.getValue (rowOffset ، int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلية للمنطقة بأكملها ، فيمكنك استخدام طريقة RefifiedArea.getValues.

نظرًا لأن واجهات برمجة التطبيقات Aspose.Cells تعطي RefifiedArea في "paramsList" ، فلن تكون هناك حاجة إلى مجموعة RefifiedAreaCollection في "ContextObjects" بعد الآن (في الإصدارات القديمة ، لم تكن قادرة على إعطاء مخطط واحد لواحد لمعلمات الوظيفة المخصصة دائمًا) تمت إزالته من "ContextObjects".

{{< highlight "java" >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
