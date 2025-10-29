---
title: إخراج صفحة فارغة عند عدم وجود شيء للطباعة
type: docs
weight: 90
url: /ar/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

إذا كانت الورقة فارغة، فلن يطبع Aspose.Cells للبايثون via .NET شيئًا عند تصدير ورقة العمل إلى صورة. يمكنك تغيير هذا السلوك باستخدام خاصية [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print). عند تعيينها إلى **صحيح**، ستطبع الصفحة الفارغة.

## **إخراج صفحة فارغة عند عدم وجود شيء للطباعة**

يقوم الكود العيني التالي بإنشاء السجل الفارغ الذي يحتوي على ورقة عمل فارغة ويقوم بتقديم الصورة للورقة الفارغة بعد ضبط الخاصية [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) بقيمة **true**. وبالتالي، يتم إنشاء الصفحة الفارغة نتيجة عدم وجود شيء للطباعة والذي يمكنك رؤيته في الصورة أدناه.

![todo:image_alt_text](1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
