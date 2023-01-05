---
title: بحث واستبدال البيانات في نطاق
type: docs
weight: 60
url: /ar/java/search-and-replace-data-in-a-range/
description: توضح هذه المقالة كيفية البحث عن البيانات واستبدالها في نطاق في Excel باستخدام كود Java.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى البحث عن بيانات محددة واستبدالها في نطاق ، مع تجاهل أي قيم خلية خارج النطاق المطلوب. Aspose.Cells يسمح لك بتحديد البحث بنطاق معين. يشرح هذا المقال كيف.

{{% /alert %}}

يوفر Aspose.Cells ملف[**FindOptions.setRange ()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) لتحديد النطاق عند البحث عن البيانات.

 افترض أنك تريد البحث عن السلسلة**"بحث"** واستبدله بـ**"يحل محل"** في النطاق**E3: H6**. في لقطة الشاشة أدناه ، يمكن رؤية سلسلة "search" في عدة خلايا ولكننا نريد استبدالها فقط في نطاق معين ، مظلل هنا باللون الأصفر.

**ملف الإدخال**

![ما يجب القيام به: image_بديل_نص](search-and-replace-data-in-a-range_1.png)

بعد تنفيذ الكود ، يبدو ملف الإخراج كما يلي. تم استبدال جميع سلاسل "البحث" ضمن النطاق بكلمة "استبدال".

**ملف إلاخراج**

![ما يجب القيام به: image_بديل_نص](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## مقالات ذات صلة

- [البحث عن البيانات أو البحث عنها](/cells/ar/java/find-or-search-data/)
