---
title: استخدام ميزة ICustomFunction
type: docs
weight: 890
url: /ar/java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

يوفر هذا المقال فهمًا مفصلًا لكيفية استخدام ميزة ICustomFunction لتنفيذ الوظائف المخصصة باستخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells.

تسمح واجهة ICustomFunction بإضافة وظائف حساب المعادلة المخصصة لتوسيع محرك الحساب الأساسي لـ Aspose.Cells من أجل تلبية متطلبات معينة. تُستخدم هذه الميزة لتعريف الوظائف المخصصة (تعريف المستخدم) في ملف نموذج أو في الكود حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells مثل أي وظيفة افتراضية أخرى في Microsoft Excel.

يرجى ملاحظة أن هذه الواجهة قد تم استبدالها بـ [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) وستُزال في المستقبل. بعض المقالات الفنية / الأمثلة حول الواجهة الجديدة: [هنا](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) و[هنا](/cells/ar/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

إذا كنت جديدًا على واجهات Aspose.Cells for Java، يُرجى التحقق من [هذا](https://docs.aspose.com/cells/java/installation/) المقال لمعرفة كيفية الحصول على والإشارة إلى Aspose.Cells for Java في مشروعك.

{{% /alert %}} 
## **إنشاء وتقييم وظيفة معرفة المستخدم**
يُظهر هذا المقال تنفيذ واجهة ICustomFunction لكتابة وظيفة مخصصة واستخدامها في جدول البيانات للحصول على النتائج. سنقوم بتحديد وظيفة مخصصة بالاسم **MyFunc** التي ستقبل 2 معلمة بالتفاصيل التالية.

- يشير المعلم الأول إلى خلية واحدة
- يشير المعلم الثاني إلى مجموعة من الخلايا

سيقوم الدالة المخصصة بإضافة جميع القيم من نطاق الخلية المحدد كمعلم ثاني وتقسيم النتيجة على القيمة في المعلم الأول.

هنا كيف قمنا بتنفيذ طريقة calculateCustomFunction.

**Java**

{{< highlight csharp >}}

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

هنا كيفية استخدام الدالة المحددة حديثا في جدول بيانات

**Java**

{{< highlight csharp >}}

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
## **نظرة عامة**
يقوم واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells بوضع كائن ReferredArea في "paramsList" عندما يكون المعلمات المقابلة هي مرجع أو ناتج الحساب هو مرجع. إذا كنت بحاجة إلى المرجع ذاته فيمكنك استخدام ReferredArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية واحدة من المرجع المقابل لموضع الصيغة، يمكنك استخدام طريقة ReferredArea.getValue(rowOffset, int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلايا للمنطقة بأكملها فيمكنك استخدام ReferredArea.getValues method.

نظرًا لأن واجهات برمجة التطبيقات Aspose.Cells تقدم ReferredArea في "paramsList"، فستكون مجموعة ReferredArea في "contextObjects" غير مطلوبة بعد الآن (في الإصدارات القديمة لم تكن دائمًا قادرة على تقديم خريطة واحد إلى واحد لمعلمات الدالة المخصصة) ولذلك تمت إزالتها من "contextObjects".

{{< highlight java >}}

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
