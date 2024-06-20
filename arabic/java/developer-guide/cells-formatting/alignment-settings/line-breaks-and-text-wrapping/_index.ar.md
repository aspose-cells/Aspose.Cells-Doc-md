---
title: كسر الأسطر وتضمين النص
type: docs
weight: 10
url: /ar/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

{{% /alert %}}

## **لتضمين النص في خلية**

لتضمين النص في خلية، استخدم الخاصية [**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

الشفرة المصدرية العينية التالية توضح كيفية استخدام تضمين النص وكسرات الأسطر الصريحة في خلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **للاستخدام كسرات الأسطر الصريحة**

يمكنك استخدام '\n' في الجافا لإدراج كسرات الأسطر الصريحة في خلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
