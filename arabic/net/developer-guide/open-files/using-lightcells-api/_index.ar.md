---
title: استخدام واجهة LightCells API
type: docs
weight: 160
url: /ar/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

في بعض الأحيان تحتاج إلى قراءة وكتابة ملفات Microsoft Excel الكبيرة بقائمة كبيرة من البيانات أو المحتوى في ورقة العمل. واجهة برمجة التطبيقات المبسطة مفيدة لإنشاء جداول بيانات Excel الضخمة: معها، تحتاج إلى أقل كمية من الذاكرة وتحصل على أداء وكفاءة أفضل.

{{% /alert %}} 
# الهندسة المعمارية المدفوعة بالأحداث
توفر Aspose.Cells واجهة LightCells API مصممة بشكل رئيسي للتلاعب ببيانات الخلية واحدة تلو الأخرى دون بناء نموذج بيانات كاملاً (باستخدام مجموعة الخلية إلخ) في الذاكرة. تعمل في وضع محفز بالأحداث.

لحفظ دفاتر العمل، يتم تقديم محتوى الخلية خلية بخلية عند الحفظ، ويقوم المكون بحفظه في ملف الإخراج مباشرةً.

عند قراءة ملفات القالب، يُحلل المكون كل خلية ويقدم قيمها واحدة تلو الأخرى.

في كل من الإجراءين، يتم معالجة كائن Cell ومن ثم التخلّص منه، ولا يحمل كائن Workbook المجموعة. وبالتالي، يتم توفير الذاكرة عند استيراد وتصدير ملف Microsoft Excel الذي يحتوي على مجموعة بيانات كبيرة والتي ستستخدم وحدة كبيرة من الذاكرة وإلا.

على الرغم من أن واجهة LightCells API تعالج الخلايا بنفس الطريقة لملفات XLSX وXLS (حيث لا تقوم فعليًا بتحميل كل الخلايا في الذاكرة ولكن تعالج خلية ومن ثم تتخلص منها)، إلا أنها تحفظ الذاكرة بشكل أكثر فعالية لملفات XLSX من ملفات XLS بسبب النماذج والهياكل المختلفة للصيغتين.

ومع ذلك، **بالنسبة لملفات XLS**، يمكن للمطورين تحديد موقع مؤقت لحفظ البيانات المؤقتة التي تُولد أثناء عملية الحفظ، لتحفيظ المزيد من الذاكرة. بشكل شائع، **يمكن لاستخدام واجهة LightCells API لحفظ ملف XLSX توفير 50% أو أكثر من الذاكرة** مقارنة بالطريقة الشائعة، **حفظ ملف XLS قد يوفر حوالي 20-40% من الذاكرة**.
## كتابة ملف إكسل كبير
توفر Aspose.Cells واجهة برمجة التطبيقات (API) تحت مسمى LightCellsDataProvider يجب تنفيذها في برنامجك. تمثل هذه الواجهة مزود البيانات لحفظ ملفات جداول بيانات كبيرة بنمط خفيف الوزن.

عند حفظ دفتر العمل بهذا النمط، يتم التحقق من StartSheet(int) عند حفظ كل ورقة عمل في دفتر العمل. بالنسبة لورقة واحدة، إذا كان StartSheet(int) يعيد قيمة true، فإن جميع البيانات والخصائص للصفوف والخلايا في هذه الورقة التي يجب حفظها يتم توفيرها بواسطة هذا التنفيذ. في المقام الأول، يتم استدعاء NextRow() للحصول على فهرس الصف التالي الذي يجب حفظه. إذا تم إرجاع فهرس صف سار (يجب أن يكون فهرس الصف في تصاعدي للصفوف المراد حفظها)، فإن كائن الصف الذي يمثل هذا الصف يتم توفيره للتنفيذ لتعيين خصائصه من خلال StartRow(Row).

بالنسبة لصف واحد، يتم التحقق من NextCell() أولاً. إذا تم إرجاع فهرس صف صالح (يجب أن يكون فهرس العمود في تصاعدي لجميع الخلايا الخاصة بصف واحد التي يجب حفظها)، فإن كائن الخلية الذي يمثل تلك الخلية يتم توفيره للتنفيذ لتعيين بياناتها وخصائصها من خلال StartCell(Cell). بعد تعيين بيانات الخلية، يتم حفظ الخلية مباشرة في ملف الجدول الرقمي المنشأ ويتم التحقق ومعالجة الخلية التالية.
### كتابة ملف إكسل كبير: مثال
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.

يقوم البرنامج بإنشاء ملف ضخم يحتوي على **10,000 سجل (مصفوفة 10000x30)** في ورقة عمل ويملأها بالبيانات الوهمية. يمكنك تحديد مصفوفتك الخاصة عن طريق تغيير متغيرات عدد الصفوف وعدد الأعمدة في الطريقة الرئيسية().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## قراءة ملفات إكسل الكبيرة
توفر Aspose.Cells واجهة برمجة التطبيقات (API) LightCellsDataHandler التي يجب تنفيذها في برنامجك. تمثل هذه الواجهة مزود البيانات لقراءة ملفات جداول البيانات الكبيرة بنمط خفيف الوزن.

عند قراءة دفتر العمل بهذا النمط، يتم التحقق من StartSheet عند قراءة كل ورقة عمل في دفتر العمل. بالنسبة للورقة، إذا كان StartSheet يعيد قيمة true، فإن جميع البيانات والخصائص للخلايا في الصفوف والأعمدة للورقة يتم التحقق ومعالجتها بمن قام بتنفيذ هذه الواجهة. بالنسبة لكل صف، يتم استدعاء StartRow للتحقق مما إذا كان يحتاج إلى معالجته. إذا كان الصف يحتاج إلى معالجة أيضًا، فإنه يتم أولاً قراءة خصائصه ويمكن للمطور الوصول إلى خصائصه من خلال ProcessRow. إذا كانت خلايا الصف تحتاج أيضًا إلى معالجة، فإن ProcessRow يجب أن تعيد قيمة true وبعد ذلك يتم استدعاء StartCell لكل خلية موجودة في الصف للتحقق مما إذا كانت خلية معينة تحتاج إلى معالجة. إذا كانت خلية معينة تحتاج إلى معالجة، فإنه يتم استدعاء ProcessCell لمعالجة الخلية من خلال تنفيذ هذه الواجهة.
### قراءة ملفات إكسل الكبيرة: مثال
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.

البرنامج يقرأ ملفاً ضخمًا يحتوي على ملايين السجلات في ورقة عمل. يستغرق الأمر بعض الوقت لقراءة كل ورقة في دفتر العمل. يقرأ الكود النموذجي الملف ويسترجع العدد الإجمالي للخلايا، وعدد السلاسل وعدد الصيغ في كل ورقة عمل.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
