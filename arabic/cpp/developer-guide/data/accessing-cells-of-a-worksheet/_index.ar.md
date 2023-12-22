---
title: الوصول إلى Cells من ورقة العمل
type: docs
weight: 10
url: /ar/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

نحن نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل يتم استخدامها لإنشاء ورقة العمل بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة العمل، سنحتاج إلى الوصول إلى خلاياها. لذا، سنناقش في هذا الموضوع بعض الطرق الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells.

{{% /alert %}} 
##  **الوصول إلى Cells**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل أ[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 يمكننا ان نستخدم[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)مجموعة للوصول إلى الخلايا في ورقة العمل. يوفر Aspose.Cells ثلاثة طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. استخدام فهرس الصفوف والأعمدة في الخلية.
1.  باستخدام فهرس الخلية في[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)مجموعة

{{% alert color="primary" %}} 

لقد ذكرنا أن الطريقة الثالثة هي الأسرع والطريقة الأولى هي الأبطأ. فرق الأداء بين الأساليب صغير جدًا، لذا لا تقلق بشأن انخفاض الأداء، أيًا كان الأسلوب الذي تستخدمه.

{{% /alert %}} 
###  **باستخدام Cell الاسم**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية الخاصة بها إلى الملف[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) جمع من[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)الطبقة كمؤشر.

 إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)الجمع هو صفر. عند استخدام هذا الأسلوب للوصول إلى خلية، فإنه سيتم التحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت الإجابة بنعم، فإنها تقوم بإرجاع كائن الخلية في المجموعة وإلا فإنها تقوم بإنشاء كائن جديد[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) كائن، ويضيف الكائن إلى[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)المجموعة ثم تقوم بإرجاع هذا الكائن. هذا الأسلوب هو أسهل طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel ولكنه الأبطأ مقارنة بالطرق الأخرى.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **استخدام فهرس الصفوف والأعمدة لـ Cell**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهارس الصف والعمود الخاص بها إلى ملف الخلية[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) جمع من[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)فصل. يعمل هذا النهج بنفس الطريقة التي يعمل بها النهج الأول.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **الوصول إلى الحد الأقصى لنطاق العرض لورقة العمل**
Aspose.Cells يسمح للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. يعد الحد الأقصى لنطاق العرض - نطاق الخلايا بين الخلية الأولى والأخيرة التي تحتوي على محتوى - مفيدًا عندما تحتاج إلى نسخ محتويات ورقة العمل بالكامل في صورة ما أو تحديدها أو عرضها.

يمكنك الوصول إلى الحد الأقصى لنطاق العرض لورقة العمل باستخدام[MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)مجموعة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
