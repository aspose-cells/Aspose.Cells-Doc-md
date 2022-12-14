---
title: الوصول إلى Cells من ورقة العمل
type: docs
weight: 10
url: /ar/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل تُستخدم لإنشاء ورقة العمل بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة عمل ، سنحتاج إلى الوصول إلى خلاياها. لذلك ، في هذا الموضوع ، سنناقش بعض الأساليب الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells.

{{% /alert %}} 
## **الوصول إلى Cells**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة تمثل جميع الخلايا في ورقة العمل.

 يمكننا ان نستخدم[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)جمع للوصول إلى الخلايا في ورقة عمل. يوفر Aspose.Cells ثلاث طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. استخدام فهرس صف وعمود الخلية.
1.  باستخدام فهرس الخلية في ملف[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة

{{% alert color="primary" %}} 

لقد ذكرنا أن الطريقة الثالثة هي الأسرع والأول هي الأبطأ. فرق الأداء بين الأساليب صغير جدًا ، لذا لا تقلق بشأن تدهور الأداء ، أيًا كان الأسلوب الذي تستخدمه.

{{% /alert %}} 
### **باستخدام Cell الاسم**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية الخاص بها إلى[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) جمع[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)فئة كمؤشر.

 إذا قمت بإنشاء ورقة عمل فارغة في البداية ، فسيتم حساب عدد[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) المجموعة صفر. عند استخدام هذا الأسلوب للوصول إلى خلية ، فإنه سيتحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت الإجابة بنعم ، فإنه يعيد كائن الخلية في المجموعة وإلا فإنه ينشئ كائنًا جديدًا[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) كائن ، يضيف الكائن إلى[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)جمع ثم إرجاع هذا الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel ولكنه أبطأ مقارنة بالطرق الأخرى.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **باستخدام فهرس الصف والعمود Cell**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير مؤشرات صفها وعمودها إلى ملف[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) جمع[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)صف دراسي. يعمل هذا النهج بنفس الطريقة التي يعمل بها النهج الأول.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **الوصول إلى أقصى نطاق عرض لورقة العمل**
Aspose.Cells يسمح للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. يكون نطاق العرض الأقصى - نطاق الخلايا بين الخلية الأولى والأخيرة مع المحتوى - مفيدًا عندما تحتاج إلى نسخ أو تحديد أو عرض المحتويات الكاملة لورقة العمل في صورة.

 يمكنك الوصول إلى أقصى نطاق عرض لورقة العمل باستخدام[ماكس ديسبلاييرانج](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) طريقة[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
