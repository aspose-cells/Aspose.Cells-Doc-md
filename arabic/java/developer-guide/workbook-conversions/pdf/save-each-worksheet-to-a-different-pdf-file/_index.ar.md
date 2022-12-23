---
title: احفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 50
url: /ar/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل ملفات جداول البيانات (التي تحتوي على صور ومخططات وما إلى ذلك) إلى وثائق PDF. يمكن أن يعمل Aspose.Cells for Java بشكل مستقل لتحويل جدول بيانات إلى مستند PDF ولا تحتاج إلى استخدام Aspose.PDF for Java للتحويل بعد الآن. لا يتطلب التحويل إنشاء / استخدام أي ملف (ملفات) مؤقتة أيضًا حيث يمكن إجراء العملية بأكملها في الذاكرة.

{{% /alert %}}

إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف Excel النموذجي الخاص بك لإنشاء ملفات PDF مختلفة. يمكن تحقيق ذلك بسهولة. يمكنك محاولة إخفاء الأوراق في الملف وجعل ورقة واحدة مرئية في كل مرة بناءً على ما ستعرض عليه ملفات PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ ، فمن الأفضل استدعاء[**مصنف .calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()قبل تحويل جدول البيانات إلى PDF. هذا يضمن إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
