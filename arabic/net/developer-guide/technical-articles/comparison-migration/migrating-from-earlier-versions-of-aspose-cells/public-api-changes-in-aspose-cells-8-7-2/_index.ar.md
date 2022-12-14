---
title: عام API التغييرات في Aspose.Cells 8.7.2
type: docs
weight: 250
url: /ar/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.1 إلى 8.7.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمديد محرك الحساب الافتراضي**
تتميز واجهات برمجة التطبيقات Aspose.Cells بمحرك حساب قوي يمكنه حساب جميع وظائف Excel Microsoft تقريبًا. علاوة على ذلك ، تسمح واجهات برمجة التطبيقات Aspose.Cells الآن بتوسيع محرك الحساب الافتراضي لتلبية متطلبات الحساب المخصصة لأي تطبيق.

تمت إضافة واجهات برمجة التطبيقات التالية بإصدار Aspose.Cells for .NET 8.7.2.

1. الملخصالحساب فئة المحرك
1. فئة بيانات الحساب
1. CalculationOptions.CustomEngine Property

{{% alert color="primary" %}} 

تسمح واجهات برمجة التطبيقات المذكورة أعلاه بتنفيذ محرك حساب مخصص لجميع الوظائف (بما في ذلك وظائف Excel الأصلية) بمزيد من المرونة.

{{% /alert %}} {{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تنفيذ محرك الحساب المخصص](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

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


### **تمت إضافة مفهرس زائد التحميل لـ TextBoxCollection**
كشف Aspose.Cells for .NET 8.7.2 عن التحميل الزائد المفهرس لفئة TextBoxCollection للوصول إلى مثيل TextBox باستخدام اسمه كسلسلة.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[الوصول إلى TextBox عبر اسمه](/cells/ar/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

يبدو سيناريو الاستخدام البسيط على النحو التالي.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET 8.7.2 كشف حدث OnAfterColumnFilter الذي يعمل بمثابة رد اتصال لآلية التصفية التي تتم من خلال Aspose.Cells.GridWeb UI. كما يوحي الاسم ، يتم تشغيل الحدث بعد تطبيق تصفية العمود ويمكن استخدامه للحصول على معلومات التصفية مثل فهرس العمود الذي تم تطبيق الفلتر عليه وقيمة التصفية المحددة.

يبدو سيناريو الاستخدام البسيط على النحو التالي.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

لا تنس تسجيل الحدث في GridWeb control<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
