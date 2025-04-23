---
title: إزالة المسافات البيضاء من البيانات قبل الرسم إلى صورة
type: docs
weight: 270
url: /ar/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى عرض صور ورقة البيانات في تطبيقات أو صفحات ويب. على سبيل المثال، قد تحتاج إلى إدراج صور في مستند Word أو ملف PDF أو عرض PowerPoint أو مستند آخر. بشكل أساسي، ترغب في تقديم ورقة بيانات كصورة حتى يمكن للمستخدم لصقها في تطبيقات أخرى. تسمح واجهات برمجة التطبيقات لـ Aspose.Cells بتحويل صفحات الجداول في Microsoft Excel إلى صور.

{{% /alert %}}

يمكن لصنف [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) تحويل صفحة العمل إلى ملف صورة مع تحديد الصفات المحددة، على سبيل المثال تنسيق الصورة، صفحات الورق المكتبية، إلخ. يتم دعم عدة تنسيقات صور، بما في ذلك BMP وGIF وJPG وTIFF وEMF.

عند استخدام ميزة التحويل إلى صورة، يكون للصورة الناتجة مساحة بيضاء فارغة، أي حاشية، حولها افتراضياً. يمكنك إزالة ذلك. قم بتحديد هوامش إعدادات صفحة الأعلى واليسار والسفل واليمين لصفحة الورق المصدر إلى 0 وحدد [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) بناءً على ذلك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
{{< app/cells/assistant language="java" >}}
