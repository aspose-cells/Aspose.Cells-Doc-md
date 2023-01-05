---
title: احصل على تحذيرات لاستبدال الخط أثناء عرض ملف Excel
type: docs
weight: 120
url: /ar/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

في بعض الأحيان ، عند تحويل ملفات Excel Microsoft إلى PDF ، يقوم Aspose.Cells باستبدال الخطوط. يوفر Aspose.Cells ميزة تتيح للمطورين معرفة أنه تم استبدال خط معين بإطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب اختلاف Aspose.Cells الذي تم تقديمه عن PDF عن ملف Excel الفعلي ويمكنك بعد ذلك اتخاذ الإجراءات المناسبة. على سبيل المثال ، يمكنك تثبيت الخطوط المفقودة بحيث تبدو نتائج العرض كما هي.

إذا كنت ترغب في الحصول على التحذيرات لاستبدال الخط أثناء تقديم ملف Excel إلى PDF ، فقم بتنفيذ واجهة IWarningCallback وقم بتعيين طريقة PdfSaveOptions.setWarningCallback () مع الواجهة التي تم تنفيذها.

{{% /alert %}}

توضح لقطة الشاشة أدناه ملف Excel المصدر المستخدم في الكود التالي. يحتوي على بعض النصوص في الخلايا A6 و A7 في الخطوط التي لم يتم تقديمها بشكل جيد بواسطة Microsoft Excel.

![ما يجب القيام به: image_بديل_نص](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

سيقوم Aspose.Cells باستبدال الخطوط الموجودة في الخلايا A6 و A7 بخطوط مناسبة كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **تنزيل الملف المصدر والإخراج PDF**

يمكنك تنزيل ملف Excel المصدر والمخرج PDF من الروابط التالية

- [المصدر. xlsx](5472700.xlsx)
- [الإخراج. pdf](5472699.pdf)

 الكود التالي يطبق[**IWarning استدعاء**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) وضبط[**PdfSaveOptions.setWarningCallback ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) الطريقة مع الواجهة المنفذة. الآن ، عندما يتم استبدال أي خط في أي خلية ، سيقوم Aspose.Cells بإطلاق تحذير داخل طريقة WarningCallback.warning ().

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **إخراج التحذيرات**

بعد تحويل الملف المصدر ، يتم إخراج التحذيرات التالية إلى وحدة التحكم في تصحيح الأخطاء:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل استدعاء طريقة Workbook.calculateFormula قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
