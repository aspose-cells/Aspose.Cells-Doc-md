---
title: قم بإزالة المسافات البيضاء من البيانات قبل التقديم إلى الصورة
type: docs
weight: 270
url: /ar/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى تقديم صور ورقة العمل في التطبيقات أو صفحات الويب. على سبيل المثال ، قد تحتاج إلى إدراج صور في مستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو مستند آخر. بشكل أساسي ، تريد عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. تتيح لك واجهات برمجة التطبيقات Aspose.Cells تحويل أوراق عمل Microsoft Excel إلى صور.

{{% /alert %}}

 ال[**عرض الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)فئة قادرة على تحويل ورقة عمل إلى ملف صورة بأي سمات محددة ، على سبيل المثال ، تنسيق الصورة ، والأوراق المرقمة ، وما إلى ذلك. يتم دعم العديد من تنسيقات الصور ، بما في ذلك BMP و GIF و JPG و TIFF و EMF.

 عند استخدام ميزة من ورقة إلى صورة ، فإن صورة الإخراج بها مساحة بيضاء / فارغة ، أي حد ، حولها بشكل افتراضي. يمكنك إزالة هذا. عيّن هوامش إعداد الصفحة العلوية واليسرى والسفلية واليمنى لورقة العمل المصدر على 0 وحدد[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)السمات وفقًا لذلك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
