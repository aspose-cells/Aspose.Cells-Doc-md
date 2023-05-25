---
title: Aspose.Cells for Python via Java 23.5 ملاحظات الإصدار
type: docs
weight: 8
url: /ar/python-java/aspose-cells-for-python-via-java-23-5-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Python via Java 23.5](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-23.5/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSJAVA-45230|دعم لإضافة علامة مائية أثناء التقديم إلى pdf|
|CELLSJAVA-45334|البيانات الموجودة في مربع النص خارج الحدود|
|CELLSJAVA-45336|يتم نقل النص عند تحويل الأشكال التلقائية المجمعة إلى pdf|
|CELLSJAVA-45364|يكون النص العمودي في الشكل في Excel مائلاً عند تحويله إلى PDF|
|CELLSJAVA-45366|خطأ في عرض الشكل البيضاوي عند تصدير الملف إلى html|
|CELLSJAVA-45369| تم استبدال خط مربعات النص|
|CELLSJAVA-45290|لا يتم تحديث قواعد مرجع التنسيق الشرطي بشكل جيد عند نسخ نطاقات من مصنف إلى مصنف آخر|
|CELLSJAVA-45362|لا يتم عرض مخطط الخطأ|
|CELLSJAVA-45363|حلقة لا نهاية لها عند تحويل المخططات إلى صورة|
|CELLSJAVA-45239|Cell محاذاة الضبط الرأسي لا تسري عند الحفظ في html|
|CELLSJAVA-45335|يتم وضع النص في غير مكانه عندما يتم تنسيق الخلية كرقم في إخراج html|
|CELLSJAVA-45323| تؤدي إزالة إعدادات الاحتواء التلقائي في أعمدة الجدول المحوري إلى إزالة نمط / تنسيق الجدول المحوري|
|CELLSJAVA-45341|يتم فقدان نمط المخططات عند تحميل دفق المصنف القديم وحفظه|
|CELLSJAVA-45351|لا تتضمن المساحة المحورية للتنسيق إلا الإجماليات الفرعية للحقل المحوري|
|CELLSJAVA-45374|توقف البرنامج عند فتح ملف XML|
|CELLSJAVA-45319|زاوية شريحة المخطط الدائري ثلاثي الأبعاد غير صحيحة عند تحويل الملف إلى ODS|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يغير سلوك طرق ExternalLinkCollection.Clear (bool) / RemoveAt (int ، bool)**

في الإصدارات القديمة ، عندما يكون "updateReferencesAsLocal" صحيحًا ، نقوم فقط بتحديث تلك المراجع للأسماء الخارجية للأسماء المحلية للمصنف الحالي. بالنسبة لمراجع بيانات الورقة الخارجية ، قمنا بتحديثها كـ "#REF!" دائماً. بدءًا من 23.5 ، إذا كانت هناك ورقة عمل واحدة في المصنف الحالي بنفس اسم الورقة للمرجع الخارجي ، فسيتم تحديث المرجع إلى الورقة المحلية أيضًا.

###  **يضيف طريقة Row.iterator (المعكوسة المنطقية ، المزامنة المنطقية)**

تزويد المستخدم بإمكانية اجتياز Cell بترتيب معكوس.

###  **عفا عليها الزمن Cells.getRowEnumerator ()**

الرجاء استخدام RowCollection.iterator () بدلاً من ذلك.

###  **مخطط قديم. أسلوب IsReferedByChart () ويضيف طريقة Chart.IsCellReferedByChart ()**

الرجاء استخدام Chart.IsCellReferedByChart () بدلاً من ذلك.

###  **يضيف خاصية SeriesLayoutProperties.IsIntervalLeftClosed**

يشير إلى ما إذا كان الفاصل الزمني مغلقًا على الجانب الأيسر.

###  **يضيف خاصية ShapeTextAlignment.IsLockedText**

يشير إلى ما إذا كان نص الشكل مؤمنًا أم لا.

###  **يزيل فئة ShapeFormat القديمة والشكل**

استخدم Shape.Line و Shape.Fill بدلاً من ذلك.

###  **إضافة خاصية ListColumn.TotalsRowLabel**

الحصول على وتعيين تسمية صف toals في الجدول.

###  **إضافة أسلوب ListObject.PutCellValue (Int32 ، Int32 ، كائن ، منطقي)**

يضبط القيمة على الخلية في الجدول.

###  **إضافة تعداد PivotAreaType وخاصية PivotArea.RuleType**

الحصول على نوع المنطقة المحورية وتعيينها في الجدول المحوري.

###  **يضيف فئة PivotTableFormat**

يمثل تنسيق PivotTable.

###  **إضافة فئة PivotTableFormatCollection**

يمثل كل تنسيقات PivotTable.

###  **إضافة خاصية PivotTable.PivotFormats**

الحصول على كافة التنسيقات الخاصة بجدول PivotTable وإضافتها.

###  **إضافة خاصية PivotTable.AutofitColumnWidthOnUpdate**

يشير إلى ما إذا كان auot يناسب عرض العمود عند تحديث PivotTable.

###  **إضافة فئة PivotAreaFilter و PivotAreaFilterCollection**

يمثل عوامل التصفية لتحديد المنطقة المحورية في PivotTable.

###  **إضافة خاصية PivotArea.Filters**

يمثل عوامل التصفية لتحديد المنطقة المحورية في PivotTable.

###  **إضافة PivotArea.IsRowGrandIncluded و PivotArea.IsColumnGrandIncluded Properties**

يشير إلى ما إذا كان سيتم تضمين الإجمالي الكلي للصف أو العمود في المنطقة.

###  **إضافة خاصية PivotArea.AxisType**

الحصول على منطقة PivotTable التي تنطبق عليها هذه القاعدة وتعيينها.

###  **إضافة خاصية PivotArea.IsOutline**

يشير إلى ما إذا كانت القاعدة تشير إلى المنطقة المحورية الموجودة في وضع المخطط التفصيلي.

###  **يضيف طريقة ImageOrPrintOptions.SetDesiredSize (حسب العرض المطلوب ، والارتفاع المطلوب ، وطريقة KeepAspectRatio المنطقية)**

يضبط العرض والارتفاع المطلوبين للصورة ، ويحدد ما إذا كان سيتم الاحتفاظ بنسبة العرض إلى الارتفاع للصورة الأصلية.

###  **طريقة التقادم ImageOrPrintOptions.SetDesiredSize (حسب العرض المطلوب ، والارتفاع المطلوب)**

يُرجى استخدام ImageOrPrintOptions.SetDesiredSize (العرض المرغوب ، والارتفاع المطلوب ، والخطأ) بدلاً من ذلك.

###  **يضيف PdfSaveOptions.Watermark الملكية**

الحصول على أو تعيين العلامة المائية للإخراج.

###  **يضيف فئات RenderingFont و RenderingWatermark**

لإضافة العلامة المائية إلى إخراج التقديم.

###  **يضيف خاصية AutoFitterOptions.ForRendering**

يشير إلى ما إذا كان مناسبًا لغرض العرض.
 
###  **يغير تعريف EquationNodeParagraph.EquationHorizontalJustificationType**

التغيير من متغير المثيل إلى خاصية / طريقة الوصول.
