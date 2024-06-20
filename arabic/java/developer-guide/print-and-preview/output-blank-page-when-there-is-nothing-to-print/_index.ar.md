---
title: إخراج صفحة فارغة عند عدم وجود شيء للطباعة
type: docs
weight: 80
url: /ar/java/output-blank-page-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

إذا كانت الورقة فارغة، فإن Aspose.Cells لن تقوم بطباعة أي شيء عند تصدير ورقة العمل إلى صورة. يمكنك تغيير هذا السلوك عن طريق استخدام [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint). عندما تقوم بتعيينه إلى **true**، ستقوم بطباعة الصفحة الفارغة.

## **إخراج صفحة فارغة عند عدم وجود شيء للطباعة**

الكود العيني التالي ينشئ جدول البيانات الفارغ الذي يحتوي على ورقة العمل الفارغة ويقوم بتقديم الورقة الفارغة إلى صورة بعد ضبط الخاصية [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) كـ **true**. ونتيجة لذلك، سيتم إنشاء الصفحة الفارغة حيث لا يوجد شيء لطباعته والذي يمكنك رؤيته كما يلي.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
