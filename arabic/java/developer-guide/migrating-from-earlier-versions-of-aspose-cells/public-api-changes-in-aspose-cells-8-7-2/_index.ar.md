---
title: عام API التغييرات في Aspose.Cells 8.7.2
type: docs
weight: 260
url: /ar/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.1 إلى 8.7.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمديد محرك الحساب الافتراضي**
تتميز واجهات برمجة التطبيقات Aspose.Cells بمحرك حساب قوي يمكنه حساب جميع وظائف Excel Microsoft تقريبًا. علاوة على ذلك ، تسمح واجهات برمجة التطبيقات Aspose.Cells الآن بتوسيع محرك الحساب الافتراضي لتلبية متطلبات الحساب المخصصة لأي تطبيق.

تمت إضافة واجهات برمجة التطبيقات التالية بإصدار Aspose.Cells for Java 8.7.2.

1. الملخصالحساب فئة المحرك
1. فئة بيانات الحساب
1. CalculationOptions.CustomEngine Property

{{% alert color="primary" %}} 

تسمح واجهات برمجة التطبيقات المذكورة أعلاه بتنفيذ محرك حساب مخصص لجميع الوظائف (بما في ذلك وظائف Excel الأصلية) بمزيد من المرونة.

{{% /alert %}} {{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تنفيذ محرك الحساب المخصص](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **تمت إضافة مفهرس زائد التحميل لـ TextBoxCollection**
كشف Aspose.Cells for Java 8.7.2 المفهرس الزائد لفئة TextBoxCollection للوصول إلى مثيل TextBox باستخدام اسمه String.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[الوصول إلى TextBox عبر اسمه](/cells/ar/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 يبدو سيناريو الاستخدام البسيط على النحو التالي.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
