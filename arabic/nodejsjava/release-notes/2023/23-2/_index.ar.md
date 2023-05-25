---
title: Aspose.Cells for Node.js via Java 23.2 ملاحظات الإصدار
type: docs
weight: 11
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-23-2-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 23.2](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-23.2/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSJAVA-43438|ملء `<Application>` العلامة في XLSX|
|CELLSJAVA-45119|عند القراءة بتنسيق 03 excel ، لا تتم معالجة "FillType" للخط المستقيم|
|CELLSJAVA-45128|يبدو أن الوجه الأفقي مفقود عند قراءة خطوط الأسهم|
|CELLSJAVA-45061|XLS إلى HTML: الصورة ممتدة|
|CELLSJAVA-45062|XLS إلى HTML: إزاحة السهم|
|CELLSJAVA-45085|Diagram مشكلة مبعثرة في Excel لتقديم PDF|
|CELLSJAVA-45118|عرض شكل غير مكتمل بعد التدوير عند الحفظ في pdf|
|CELLSJAVA-45078|حساب متوسط SUM `#VALUE!` |
|CELLSJAVA-45088|النتيجة المعروضة غير صحيحة لـ html الناتج عندما تكون قيمة الخلية عبارة عن سلسلة بتنسيق مخصص|
|CELLSJAVA-45094|النطاقات العالمية المسماة بمراجع مثل `=!$K$23` تنفصل في الإصدار الجديد|
|CELLSJAVA-45115|تتسبب طريقة deleteRows في تنسيق غير صحيح|
|CELLSJAVA-45077|يُبلغ الملف المحفوظ عن خطأ عند التحميل والفتح في قرص Onedrive|
|CELLSJAVA-45109|يتم طرح استثناء عند تحويل الرسم البياني إلى صورة|
|CELLSJAVA-45112|عرض خط شبكة رئيسي خاص لمخطط الرادار|
|CELLSJAVA-45103|تصبح الصور الملونة المدرجة في Excel سوداء عند تحويلها إلى pdf|
|CELLSJAVA-45155| يتم اقتطاع Center Across text إذا كان في العمود الأخير عند التحويل إلى pdf|
|CELLSJAVA-45160|HTML لتحويل EXCEL فشل مع خطأ غير صالح `#`|
|CELLSJAVA-45079|يتم تجاهل تنسيق الأرقام المخصص مع النقاط اللاحقة عند التصدير إلى HTML|
|CELLSJAVA-45084|تم تغيير الخط في ملف xls المعاد حفظه|
|CELLSJAVA-45106|ملف النتيجة غير طبيعي عند تحويل Excel إلى html|
|CELLSJAVA-45117|خطأ في تدوير الشكل عند الحفظ في html|
|CELLSJAVA-45123|يجب أن يكون شكل القوس مقلوبًا أفقيًا في Excel 95|
|CELLSJAVA-45132|دعم نمط ملء الشكل في Excel95 / 5.0|
|CELLSJAVA-45147|يتم قطع بعض النص في العمود الأخير عند حفظ الملف إلى html|
|CELLSJAVA-45148|فقدت المناطق المدمجة بعد الحفظ بتنسيق html|
|CELLSJAVA-45087|يتم عرض الحد على النص الخاص بعنوان المخطط في Excel لعرض PDF|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يضيف خاصية ChartTextFrame.IsAutomaticRotation**

يشير إلى ما إذا كان سيتم تدوير نص المخطط تلقائيًا.

###  **Obsoletes JsonLayoutOptions.IgnoreObjectTitle و JsonLayoutOptions.IgnoreArrayTitle Properties**

يُرجى استخدام الخاصية JsonLayoutOptions.IgnoreTitle بدلاً من ذلك.

###  **يضيف خاصية JsonLayoutOptions.IgnoreTitle**

عناوين Ingores لسمات Json عند تحويل json إلى Excel.

###  **يضيف طريقة Style.ToJson ()**

يحول نمط ملفات Excel إلى ملف json

###  **يضيف Cell.ToJson () طريقة**

يحول خلية من الخلايا إلى ملف json.
