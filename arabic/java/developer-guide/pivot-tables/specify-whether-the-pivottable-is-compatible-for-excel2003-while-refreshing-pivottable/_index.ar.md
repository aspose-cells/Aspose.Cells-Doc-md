---
title: حدد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable
type: docs
weight: 880
url: /ar/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 يوفر Aspose.Cells ملف[PivotTable.IsExcel2003 متوافق](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)الخاصية التي يمكنك استخدامها لتحديد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable. إذا**حقيقي** ، يجب أن تكون السلسلة أقل من أو تساوي 255 حرفًا ، لذلك إذا كانت السلسلة أكبر من 255 حرفًا ، فسيتم اقتطاعها. إذا**خاطئة** ، لن يكون للسلسلة القيود المذكورة أعلاه. النظام الأساسي**حقيقي**.

{{% /alert %}} 
## **حدد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable**
 يشرح نموذج التعليمات البرمجية التالي استخدام[PivotTable.IsExcel2003 متوافق](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) منشأه. يبلغ طول السلسلة الأصلية 383 حرفًا. لكن عندما[PivotTable.IsExcel2003 متوافق](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) تم تعيين الخاصية على**حقيقي** ويتم تحديث الجدول المحوري ، ويتم قطع بيانات الخلية B5 في الجدول المحوري ويصبح طولها 255 حرفًا. رغم ذلك، متى[PivotTable.IsExcel2003 متوافق](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) تم تعيين الملكية**خاطئة** ويتم تحديث الجدول المحوري مرة أخرى ، ولا يتم اقتطاع بيانات الخلية B5 في الجدول المحوري ويظل طولها 383 حرفًا. يرجى تنزيل ملف[نموذج ملف اكسل](5472558.xlsx) المستخدمة في هذا الرمز ،[ملف اكسل الناتج](5472557.xlsx) تم إنشاؤه بواسطته وإخراج وحدة التحكم الخاصة به للرجوع إليه. يرجى أيضًا قراءة التعليقات الموجودة داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه عندما يتم تنفيذه مع المعطى[نموذج ملف اكسل](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
