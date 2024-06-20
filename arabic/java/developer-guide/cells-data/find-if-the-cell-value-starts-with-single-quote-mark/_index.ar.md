---
title: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 610
url: /ar/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells الآن خاصية [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) لمعرفة ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس فردية. قبل هذه الخاصية، لم يكن هناك وسيلة للتمييز بين السلاسل مثل عينة و 'عينة وما إلى ذلك.

{{% /alert %}} 
## **العثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة**
يوضح الكود المصدري التالي أنه لا يمكن تمييز السلاسل مثل عينة و 'عينة باستخدام خاصية [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). لذلك يجب علينا استخدام خاصية [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) للتمييز بينهما.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
