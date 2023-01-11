﻿---
title: باستخدام LightCells API
type: docs
weight: 80
url: /ar/java/using-lightcells-api/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى قراءة وكتابة ملفات إكسل Microsoft كبيرة مع قائمة ضخمة من البيانات أو المحتويات في ورقة العمل. تعتبر LightCells API مفيدة في إنشاء جداول بيانات Excel ضخمة: باستخدامها ، تحتاج إلى ذاكرة وتحصل على أداء وكفاءة أفضل.

{{% /alert %}}

## **العمارة المدفوعة بالحدث**

يوفر Aspose.Cells LightCells API ، المصمم بشكل أساسي لمعالجة بيانات الخلية واحدًا تلو الآخر دون إنشاء كتلة نموذج بيانات كاملة (باستخدام مجموعة Cell وما إلى ذلك) في الذاكرة. إنه يعمل في وضع يحركه الحدث.

لحفظ المصنفات ، قم بتوفير محتوى الخلية خلية تلو الأخرى عند الحفظ ، ويحفظها المكون في ملف الإخراج مباشرة.

عند قراءة ملفات القوالب ، يوزع المكون كل خلية ويقدم قيمتها واحدة تلو الأخرى.

في كلا الإجراءين ، تتم معالجة كائن Cell واحد ثم يتم التخلص منه ، لا يحتفظ كائن المصنف بالمجموعة. في هذا الوضع ، يتم حفظ الذاكرة عند استيراد وتصدير ملف Microsoft Excel الذي يحتوي على مجموعة بيانات كبيرة والتي من شأنها أن تستخدم قدرًا كبيرًا من الذاكرة.

على الرغم من أن LightCells API يعالج الخلايا بنفس الطريقة لملفات XLSX و XLS (لا يقوم فعليًا بتحميل جميع الخلايا في الذاكرة ولكنه يعالج خلية واحدة ثم يتجاهلها) ، فإنه يوفر الذاكرة بشكل أكثر فعالية لملفات XLSX من ملفات XLS بسبب نماذج البيانات المختلفة وهياكل التنسيقين.

 لكن،**لملفات XLS** لتوفير المزيد من الذاكرة ، يمكن للمطورين تحديد موقع مؤقت لحفظ البيانات المؤقتة التي تم إنشاؤها أثناء عملية الحفظ. عادة،**قد يؤدي استخدام LightCells API لحفظ ملف XLSX إلى توفير 50٪ أو أكثر من الذاكرة** من استخدام الطريقة الشائعة ،**حفظ XLS قد يوفر حوالي 20-40٪ من الذاكرة**.

### **كتابة ملفات إكسل كبيرة**

يوفر Aspose.Cells واجهة ، LightCellsDataProvider ، يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لحفظ ملفات جداول البيانات الكبيرة في وضع الوزن الخفيف.

عند حفظ مصنف بواسطة هذا الوضع ، يتم تحديد startSheet (int) عند حفظ كل ورقة عمل في المصنف. بالنسبة إلى ورقة واحدة ، إذا كانت startSheet (int) صحيحة ، فسيتم توفير جميع بيانات وخصائص الصفوف والخلايا في هذه الورقة المراد حفظها بواسطة هذا التنفيذ. في المقام الأول ، يتم استدعاء nextRow () للحصول على فهرس الصف التالي ليتم حفظه. إذا تم إرجاع فهرس صف صالح (يجب أن يكون فهرس الصف بترتيب تصاعدي حتى يتم حفظ الصفوف) ، فسيتم توفير كائن صف يمثل هذا الصف للتنفيذ لتعيين خصائصه بواسطة startRow (الصف).

لصف واحد ، يتم التحقق من nextCell () أولاً. إذا تم إرجاع فهرس عمود صالح (يجب أن يكون فهرس العمود بترتيب تصاعدي لجميع الخلايا في صف واحد ليتم حفظه) ، فسيتم توفير كائن Cell يمثل هذه الخلية لتعيين البيانات والخصائص بواسطة startCell (Cell). بعد تعيين بيانات هذه الخلية ، يتم حفظ هذه الخلية مباشرة في ملف جدول البيانات الذي تم إنشاؤه وسيتم فحص الخلية التالية ومعالجتها.

يوضح المثال التالي كيفية عمل LightCells API.

يقوم البرنامج التالي بإنشاء ملف ضخم به 100000 سجل في ورقة عمل مليئة بالبيانات. لقد أضفنا بعض الارتباطات التشعبية وقيم السلاسل والقيم الرقمية وكذلك الصيغ إلى خلايا معينة في ورقة العمل. علاوة على ذلك ، قمنا بتنسيق مجموعة من الخلايا أيضًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **قراءة ملفات إكسل الكبيرة**

توفر Aspose.Cells واجهة ، LightCellsDataHandler ، يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لقراءة ملفات جداول البيانات الكبيرة في وضع خفيف الوزن.

عند قراءة مصنف في هذا الوضع ، يتم تحديد startSheet () عند قراءة كل ورقة عمل في المصنف. بالنسبة للورقة ، إذا أعادت startSheet () القيمة صحيحة ، فسيتم فحص ومعالجة جميع بيانات وخصائص الخلايا في صفوف وأعمدة الورقة. لكل صف ، يتم استدعاء startRow () للتحقق مما إذا كانت بحاجة إلى المعالجة. إذا احتاج الصف إلى المعالجة ، فستتم قراءة خصائص الصف أولاً ويمكن للمطورين الوصول إلى خصائصه باستخدام processRow ().

إذا كانت خلايا الصف بحاجة أيضًا إلى المعالجة ، فعندئذٍ تُرجع processRow () القيمة true ويتم استدعاء startCell () لكل خلية موجودة في الصف للتحقق مما إذا كانت بحاجة إلى المعالجة. إذا حدث ذلك ، فسيتم استدعاء processCell ().

يوضح نموذج التعليمات البرمجية التالي هذه العملية. يقوم البرنامج بقراءة ملف كبير به ملايين من السجلات. يستغرق الأمر بعض الوقت لقراءة كل ورقة في المصنف. يقرأ نموذج التعليمة البرمجية الملف ويسترد العدد الإجمالي للخلايا وعدد السلاسل وعدد الصيغ لكل ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

فئة تقوم بتنفيذ واجهة LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}