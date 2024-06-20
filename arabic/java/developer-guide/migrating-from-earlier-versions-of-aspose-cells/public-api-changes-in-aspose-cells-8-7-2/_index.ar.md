---
title: التغييرات العامة في واجهة برمجة التطبيقات في Aspose.Cells 8.7.2
type: docs
weight: 260
url: /ar/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.7.1 إلى الإصدار 8.7.2 والتي قد تكون مثيرة لاهتمام مطوري الوحدات / التطبيقات. إنه يتضمن ليس فقط الأساليب العامة الجديدة والمحدثة، والصفوف المضافة والمزالة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تم توسيع محرك الحساب الافتراضي**
الواجهات البرمجية في Aspose.Cells لديها محرك حساب قوي يمكنه حساب ما يقرب من جميع وظائف Microsoft Excel. علاوة على ذلك، تسمح واجهات برمجة التطبيقات في Aspose.Cells الآن بتوسيع محرك الحساب الافتراضي لتلبية متطلبات الحساب المخصصة لأي تطبيق.

تمت إضافة الواجهات البرمجية التالية مع إصدار Aspose.Cells for Java 8.7.2.

1. فئة AbstractCalculationEngine
1. فئة CalculationData
1. خاصية CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

الواجهات البرمجية المذكورة أعلاه تسمح بتنفيذ محرك الحساب المخصص لجميع الوظائف (بما في ذلك الوظائف الأصلية في Excel) بمزيد من المرونة.

{{% /alert %}} {{% alert color="primary" %}} 

للحصول على مزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل على [تنفيذ محرك الحساب المخصص](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة مؤشر محمل لـ TextBoxCollection**
قدمت Aspose.Cells for Java 8.7.2 المؤشر المتكرر لفئة TextBoxCollection من أجل الوصول إلى مثيل من مربع النص باستخدام اسمه كنص.

{{% alert color="primary" %}} 

للحصول على مزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل على [الوصول إلى TextBox عبر اسمه](/cells/ar/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي. 

**Java**

{{< highlight csharp >}}

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
