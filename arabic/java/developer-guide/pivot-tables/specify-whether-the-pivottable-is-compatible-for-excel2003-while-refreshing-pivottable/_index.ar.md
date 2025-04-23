---
title: حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية
type: docs
weight: 880
url: /ar/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells خاصية [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) التي يمكنك استخدامها لتحديد ما إذا كان جدول الإحصاءات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية. إذا كانت القيمة هي **true** ، يجب أن تكون السلسلة أقل من أو تساوي 255 حرفًا ، لذا إذا كانت السلسلة أكبر من 255 حرفًا ، فسيتم قصها. إذا كانت القيمة هي **false** ، فلن تكون للسلسلة القيود المذكورة. القيمة الافتراضية هي **true**.

{{% /alert %}} 
## **حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية**
يشرح كود العينة التالي استخدام [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) الخاصية. السلسلة الأصلية طولها 383 حرفًا. ولكن عندما يتم تعيين خاصية [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) إلى **true** ويتم تحديث الجدول المحوري، يتم قص بيانات الخلية B5 في الجدول المحوري ويصبح طولها 255 حرفًا. ومع ذلك ، عندما يتم تعيين خاصية [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) إلى **false** ويتم تحديث الجدول المحوري مرة أخرى، فإن بيانات الخلية B5 في الجدول المحوري لا تُقص وتبقى بطول 383 حرفًا. يرجى تنزيل [ملف الإكسل العينة](5472558.xlsx) المستخدم في هذا الكود و [ملف الإكسل الناتج](5472557.xlsx) الذي تم إنشاؤه به وإخراج وحدة التحكم الخاصة به للرجوع إليها. يرجى أيضًا قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **مخرجات الوحدة**
إليك إخراج وحدة التحكم لكود العينة أعلاه عند تنفيذه مع [ملف الإكسل العينة](5472558.xlsx) المعطى.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
