---
title: التغييرات العامة في واجهة برمجة التطبيقات في Aspose.Cells 8.7.2
type: docs
weight: 250
url: /ar/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.7.1 إلى الإصدار 8.7.2 والتي قد تكون مثيرة لاهتمام مطوري الوحدات / التطبيقات. إنه يتضمن ليس فقط الأساليب العامة الجديدة والمحدثة، والصفوف المضافة والمزالة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تم توسيع محرك الحساب الافتراضي**
الواجهات البرمجية في Aspose.Cells لديها محرك حساب قوي يمكنه حساب ما يقرب من جميع وظائف Microsoft Excel. علاوة على ذلك، تسمح واجهات برمجة التطبيقات في Aspose.Cells الآن بتوسيع محرك الحساب الافتراضي لتلبية متطلبات الحساب المخصصة لأي تطبيق.

تمت إضافة الـ APIs التالية مع الإصدار Aspose.Cells for .NET 8.7.2.

1. فئة AbstractCalculationEngine
1. فئة CalculationData
1. خاصية CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

الواجهات البرمجية المذكورة أعلاه تسمح بتنفيذ محرك الحساب المخصص لجميع الوظائف (بما في ذلك الوظائف الأصلية في Excel) بمزيد من المرونة.

{{% /alert %}} {{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة التفصيلية على [تنفيذ محرك الحساب المخصص](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **تمت إضافة مؤشر محمل لـ TextBoxCollection**
Aspose.Cells for .NET 8.7.2 قام بتعريض الفهرس الزائد لـ فئة TextBoxCollection من أجل الوصول إلى مثيل من TextBox باستخدام اسمه كسلسلة.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة التفصيلية على [الوصول إلى مربع النص عن طريق اسمه](/cells/ar/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **تمت إضافة حدث OnAfterColumnFilter لـ GridWeb**
تعرض Aspose.Cells.GridWeb for .NET 8.7.2 حدث OnAfterColumnFilter الذي يعمل كاستدعاء لآلية التصفية التي تمت من خلال واجهة المستخدم Aspose.Cells.GridWeb. كما يشير الاسم، يتم تشغيل الحدث بعد تطبيق تصفية العمود ويمكن استخدامه للحصول على معلومات حول التصفية مثل فهرس العمود الذي تم تطبيق التصفية عليه وقيمة التصفية المحددة.

سيناريو الاستخدام البسيط يبدو كما يلي.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
