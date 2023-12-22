---
title: الوصول إلى Cells من ورقة العمل
type: docs
weight: 10
url: /ar/net/accessing-cells-of-a-worksheet/
description: توضح هذه المقالة كيفية الحصول على أقصى نطاق لعرض ورقة العمل والوصول إلى الخلايا من خلال Aspose.Cells for .NET API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

نحن نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل يتم استخدامها لإنشاء ورقة العمل بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة العمل، سنحتاج إلى الوصول إلى خلاياها. لذا، سنناقش في هذا الموضوع بعض الطرق الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells.

{{% /alert %}}

##  **كيفية الوصول إلى Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)يحتوي الفصل على أ[**مجموعة أوراق العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 يمكننا ان نستخدم[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة للوصول إلى الخلايا في ورقة العمل. يوفر Aspose.Cells ثلاثة طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. استخدام فهرس الصفوف والأعمدة في الخلية.
1.  باستخدام فهرس الخلية في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة

**مهم:**لقد ذكرنا أن الطريقة الثالثة هي الأسرع والطريقة الأولى هي الأبطأ. فرق الأداء بين الأساليب صغير جدًا، لذا لا تقلق بشأن انخفاض الأداء، أيًا كان الأسلوب الذي تستخدمه.

###  **كيفية الحصول على كائن Cell بواسطة اسم Cell**

 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية الخاصة بها إلى الملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) جمع من[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)الطبقة كمؤشر.

 إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)الجمع هو صفر. عند استخدام هذا الأسلوب للوصول إلى خلية، فإنه سيتم التحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت الإجابة بنعم، فإنها تقوم بإرجاع كائن الخلية في المجموعة وإلا فإنها تقوم بإنشاء كائن جديد[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) كائن، ويضيف الكائن إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع ومن ثم إرجاع الكائن. هذا الأسلوب هو أسهل طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel ولكنه الأبطأ مقارنة بالطرق الأخرى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **كيفية الحصول على كائن Cell حسب فهرس الصف والعمود لـ Cell**

 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهارس الصف والعمود الخاص بها إلى ملف الخلية[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) جمع من[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فصل.

يعمل هذا النهج بنفس الطريقة التي يعمل بها النهج الأول.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **كيفية الحصول على كائن Cell بواسطة فهرس Cell في مجموعة Cells**

 يمكن أيضًا الوصول إلى الخلية عن طريق تمرير الفهرس الرقمي للخلية إلى ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة.

إذا كنت تستخدم هذا الأسلوب للوصول إلى الخلايا، فيمكن طرح استثناء إذا كان الفهرس الرقمي للخلية خارج النطاق. هذا الأسلوب هو الأسرع للوصول إلى الخلايا ولكن الشيء المهم الذي يجب معرفته هو أنه إذا استخدمت هذا الأسلوب للوصول إلى كائن خلية، فقد يتغير الفهرس الرقمي بعد إضافة خلايا جديدة إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كائنات الخلية في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)يتم فرز المجموعة داخليًا حسب مؤشرات الصفوف والأعمدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **كيفية الحصول على أقصى نطاق عرض لورقة العمل**

Aspose.Cells يسمح للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. يعد الحد الأقصى لنطاق العرض - نطاق الخلايا بين الخلية الأولى والأخيرة التي تحتوي على محتوى - مفيدًا عندما تحتاج إلى نسخ محتويات ورقة العمل بالكامل في صورة ما أو تحديدها أو عرضها.

يمكنك الوصول إلى الحد الأقصى لنطاق العرض لورقة العمل باستخدام[**ورقة عمل.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . يوضح نموذج التعليمات البرمجية التالي كيفية الوصول إلى[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
