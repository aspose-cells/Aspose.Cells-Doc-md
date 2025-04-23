---
title: البحث واستبدال البيانات في نطاق
type: docs
weight: 60
url: /ar/java/search-and-replace-data-in-a-range/
description: يوضح هذا المقال كيفية البحث والاستبدال للبيانات في نطاق في Excel باستخدام كود Java.
keywords: جافا البحث واستبدال البيانات في اكسل، جافا البحث عن البيانات في اكسل، جافا البحث واستبدال البيانات في نطاق، جافا البحث عن البيانات في نطاق، جافا البحث عن البيانات في نطاق، جافا البحث عن البيانات في نطاق، جافا البحث عن البيانات في اكسل، جافا البحث عن البيانات في نطاق، البحث واستبدال البيانات في اكسل بجافا، البحث واستبدال البيانات في نطاق بجافا، البحث واستبدال البيانات في النطاق بجافا
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى البحث عن بيانات محددة واستبدالها في نطاق وتجاهل أي قيم خلية خارج النطاق المطلوب. تسمح Aspose.Cells لك بتقييد البحث إلى نطاق محدد. يشرح هذا المقال ذلك.

{{% /alert %}}

توفر Aspose.Cells الطريقة [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange-com.aspose.cells.CellArea-) لتحديد نطاق عند البحث عن البيانات.

فرضًا، ترغب في البحث عن سلسلة **"بحث"** واستبدالها بـ **"استبدال"** في النطاق **E3:H6**. يمكن رؤية سلسلة "بحث" في العديد من الخلايا ولكن نريد استبدالها فقط في النطاق المعطى، هنا مظلل باللون الأصفر.

**الملف الداخلي**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

بعد تنفيذ الشفرة، تبدو ملف الإخراج كما هو فيما يلي. تم استبدال جميع سلاسل "البحث" ضمن النطاق بـ "استبدال".

**ملف الإخراج**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## مقالات ذات صلة

- [العثور على البيانات أو البحث](/cells/ar/java/find-or-search-data/)
{{< app/cells/assistant language="java" >}}
