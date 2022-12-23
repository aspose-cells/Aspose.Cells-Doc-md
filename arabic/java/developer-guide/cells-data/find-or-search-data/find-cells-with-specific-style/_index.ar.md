---
title: ابحث عن خلايا ذات نمط محدد
type: docs
weight: 80
url: /ar/java/find-cells-with-specific-style/
description: توضح هذه المقالة كيفية العثور على خلايا ذات نمط معين باستخدام MS Excel و Aspose.Cells for Java API.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى العثور على الخلايا بنمط معين. توضح هذه المقالة كيفية تحقيق ذلك باستخدام Microsoft Excel وكذلك Aspose.Cells for Java API.

{{% /alert %}}

## باستخدام Microsoft إكسل

هذه هي الخطوات المطلوبة للبحث في الخلايا ذات الأنماط المحددة في MS Excel.

1.  يختار**بحث وتحديد** في ال**علامة التبويب الصفحة الرئيسية**.
1.  يختار**يجد**.
1.  انقر**خيارات**إذا كانت الخيارات المتقدمة غير مرئية.
1.  يختار**اختر التنسيق من Cell ...** من**شكل** اسقاط.
1. حدد الخلية ذات النمط الذي تريد البحث فيه.
1.  انقر**جد كل** للعثور على جميع الخلايا ذات النمط المشابه للخلية المحددة.

## باستخدام Aspose.Cells for Java

 Aspose.Cells for Java يوفر خاصية البحث عن الخلايا في ورقة العمل بنمط معين. لهذا ، يوفر API[**FindOptions.setStyle ()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) خاصية.

### عينة من الرموز

 يجد مقتطف الشفرة التالي جميع الخلايا التي لها نفس نمط الخلية**أ 1** ويغير النص داخل تلك الخلايا. يرجى الاطلاع على لقطة الشاشة للملفات المصدر والمخرجات لتحليل إخراج نموذج التعليمات البرمجية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

بعد تنفيذ التعليمات البرمجية ، سيكون لجميع الخلايا التي لها نفس نمط الخلية A1 نص "تم العثور عليه".

### لقطات

![ما يجب القيام به: image_بديل_نص](find-cells-with-specific-style_1.png)

**شكل:** ملف مصدر به خلايا لها أنماط

 هنا ملف الإخراج الذي تم إنشاؤه بواسطة الكود التالي. يمكنك رؤية جميع الخلايا التي لها نفس نمط الخلية**أ 1** يحتوي على نص "تم العثور عليه"

![ما يجب القيام به: image_بديل_نص](find-cells-with-specific-style_2.png)

**شكل:**ملف الإخراج مع الخلايا التي تم العثور عليها بعد البحث عن طريق**أ 1** نمط
