---
title: إضافة Cell تحكمات في الأعمدة
type: docs
weight: 90
url: /ar/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

في مناقشاتنا اللاحقة ، ناقشنا حول إضافة عناصر تحكم الخلية وإدارتها في ورقة العمل. ولكن باستخدام هذه الأساليب ، يمكننا إضافة عناصر تحكم خلية إلى خلايا مفردة واحدة تلو الأخرى. ماذا لو رغب شخص ما في إضافة عناصر تحكم خلية إلى جميع خلايا عمود واحد أو أكثر؟ في مثل هذه الحالات ، لتقليل جهود المطورين ، يوفر Aspose.Cells.GridDesktop ميزة إضافة عناصر تحكم الخلية لكل أساس عمود. هذا يعني أن المطورين يمكنهم فقط تحديد العمود المطلوب وتحديد أي عنصر تحكم في الخلية. ستتم إضافة عنصر تحكم الخلية المحدد إلى كافة خلايا العمود المحدد. دعونا نرى كيف يمكننا استخدام هذه الميزة.

{{% /alert %}} 
## **مقدمة**
حاليًا ، يدعم Aspose.Cells.GridDesktop إضافة ثلاثة أنواع من عناصر التحكم في الخلية ، والتي تشمل ما يلي:

- **زر**
- **خانة الاختيار**
- **صندوق التحرير**

 كل هذه الضوابط مشتقة من فئة مجردة ،**CellControl**.

**مهم:** إذا كنت ترغب في إضافة عناصر تحكم الخلية إلى خلية واحدة بدلاً من العمود بأكمله ، فيمكنك الرجوع إلى[إضافة Cell ضوابط في أوراق العمل.](/cells/ar/net/adding-cell-controls-in-worksheets/)
### **إضافة زر**
لإضافة أزرار إلى عمود باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  يضيف**زر** لأي محدد**عمودي** التابع**ورقة عمل**

**ملاحظة:** أثناء الإضافة**زر**، يمكننا تحديد عرض الزر وارتفاعه والتعليق عليه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 يضيف مقتطف الشفرة أعلاه أزرارًا إلى جميع خلايا العمود المحدد. عندما يتم تحديد أي خلية من هذا العمود المحدد ، يصبح الزر مرئيًا. لمزيد من المعلومات حول معالجة الأزرار ، يرجى الرجوع إلى[معالجة الحدث لعنصر تحكم زر.](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **إضافة CheckBox**
لإضافة مربعات اختيار إلى عمود باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  يضيف**خانة الاختيار** لأي محدد**عمودي** التابع**ورقة عمل**

**ملاحظة:** أثناء الإضافة**خانة الاختيار**، يمكننا أيضًا تحديد حالة مربع الاختيار.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 يضيف مقتطف الشفرة أعلاه مربعات اختيار إلى جميع خلايا العمود المحدد. لمزيد من المعلومات حول التعامل مع مربعات الاختيار ، يرجى الرجوع إلى[معالجة الحدث لعنصر تحكم CheckBox.](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **مضيفا ComboBox**
لإضافة مربعات التحرير والسرد إلى عمود باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  قم بإنشاء مصفوفة من العناصر (أو القيم) التي ستتم إضافتها إليها**صندوق التحرير**
-  يضيف**صندوق التحرير** (تحتوي على عناصر أو قيم) لأي محدد**عمودي** التابع**ورقة عمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 أعلاه مقتطف الشفرة يضيف مربعات التحرير والسرد لجميع خلايا العمود المحدد. عندما يتم تحديد أي خلية من هذا العمود المحدد ، يصبح مربع التحرير والسرد مرئيًا. للحصول على مزيد من المعلومات حول معالجة الحدث من مربعات التحرير والسرد ، يرجى الرجوع إلى[معالجة الحدث لعنصر تحكم ComboBox.](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
