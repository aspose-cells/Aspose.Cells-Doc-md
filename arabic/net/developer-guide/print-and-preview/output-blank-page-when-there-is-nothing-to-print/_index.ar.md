---
title: إخراج صفحة فارغة عند عدم وجود شيء للطباعة
type: docs
weight: 90
url: /ar/net/output-blank-page-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

إذا كانت الورقة فارغة، فلن يقوم Aspose.Cells بطباعة أي شيء عند تصدير ورقة العمل إلى صورة. يمكنك تغيير هذا السلوك باستخدام الخاصية [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint). عند تعيين القيمة **true**، سيتم طباعة الصفحة الفارغة.

## **إخراج صفحة فارغة عند عدم وجود شيء للطباعة**

يقوم الكود العيني التالي بإنشاء السجل الفارغ الذي يحتوي على ورقة عمل فارغة ويقوم بتقديم الصورة للورقة الفارغة بعد ضبط الخاصية [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) بقيمة **true**. وبالتالي، يتم إنشاء الصفحة الفارغة نتيجة عدم وجود شيء للطباعة والذي يمكنك رؤيته في الصورة أدناه.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
