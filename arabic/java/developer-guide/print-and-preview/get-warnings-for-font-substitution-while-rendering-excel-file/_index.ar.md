---
title: الحصول على تحذيرات لاستبدال الخطوط أثناء تقديم ملف Excel
type: docs
weight: 120
url: /ar/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

في بعض الأحيان، عند تقديم ملفات Microsoft Excel إلى PDF، تقوم Aspose.Cells بتعويض الخطوط. توفر Aspose.Cells ميزة تسمح للمطورين بمعرفة أن تم الاستبدال لخط معين عن طريق إطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب اختلاف PDF الذي تم تقديمه بواسطة Aspose.Cells عن الملف الفعلي لـ Excel ومن ثم اتخاذ الإجراءات المناسبة. على سبيل المثال، يمكنك تثبيت الخطوط المفقودة حتى يمكن أن تبدو نتائج التقديم متماثلة.

إذا كنت ترغب في الحصول على التحذيرات لاستبدال الخطوط أثناء تقديم ملف Excel إلى PDF، قم بتنفيذ واجهة IWarningCallback وضبط PdfSaveOptions.setWarningCallback() بأسلوب الواجهة المنفذة الخاصة بك.

{{% /alert %}}

تُظهر اللقطة الشاشية أدناه الملف الفعلي لـ Excel المستخدم في الكود التالي. تحتوي على نص في الخلايا A6 و A7 بخطوط لم يتم تقديمها بشكل جيد بواسطة Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

ستقوم Aspose.Cells بتعويض الخطوط في الخلايا A6 و A7 بخطوط مناسبة كما يظهر أدناه.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **تحميل ملف المصدر وملف PDF الناتج**

يمكنك تحميل ملف Excel المصدر وملف PDF الناتج من الروابط التالية

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

يقوم الكود التالي بتنفيذ [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) وضبط [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) بأسلوب الواجهة المنفذة. الآن، كلما قام Aspose.Cells بعوض أي خط في أي خلية، سيقوم بإطلاق تحذير داخل أسلوب WarningCallback.warning().

{{< highlight java >}}

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

## **نتائج التحذيرات**

بعد تحويل الملف المصدر، يتم إخراج التحذيرات التالية إلى وحدة التحكم في التصحيح:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل أن تقوم بإتصال طريقة Workbook.calculateFormula قبل تقديم الجدول إلى تنسيق PDF. من خلال ذلك ستضمن أن القيم التي تعتمد على الصيغ تم احتسابها من جديد وتم تقديم القيم الصحيحة في الـPDF. 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
