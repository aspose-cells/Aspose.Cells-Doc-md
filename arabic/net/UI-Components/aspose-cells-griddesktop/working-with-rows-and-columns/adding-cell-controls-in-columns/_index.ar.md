---
title: إضافة عناصر تحكم الخلية في الأعمدة
type: docs
weight: 90
url: /ar/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: يقدم هذا المقال كيفية إضافة عنصر تحكم في العمود في GridDesktop.
---

{{% alert color="primary" %}} 

في مناقشاتنا لاحقًا، قمنا بمناقشة إضافة وإدارة عناصر تحكم الخلية في ورقة العمل. ولكن، باستخدام تلك الطرق، يمكننا إضافة عناصر تحكم الخلية إلى خلايا فردية واحدة تلو الأخرى. ماذا لو أراد شخص ما إضافة عناصر تحكم الخلية إلى جميع خلايا عمود أو أكثر؟ في مثل هذه الحالات، ولتقليل جهود المطورين، يوفر Aspose.Cells.GridDesktop ميزة إضافة عناصر تحكم الخلية بناءً على العمود. يعني أن المطورين يمكنهم فقط تحديد عمود مرغوب وتحديد أي عنصر تحكم خلية. سيتم إضافة عنصر تحكم الخلية المحدد إلى جميع الخلايا في العمود المحدد. دعنا نرى كيف يمكننا استخدام هذه الميزة.

{{% /alert %}} 
## **مقدمة**
حاليًا، يدعم Aspose.Cells.GridDesktop إضافة ثلاثة أنواع من عناصر التحكم في الخلايا، وتشمل ما يلي:

- **زر**
- **صندوق اختيار**
- **قائمة تحديد**

كل هذه الضوابط مشتقة من فئة مجردة، **CellControl**.

**مهم:** إذا كنت ترغب في إضافة ضوابط الخلية إلى خلية واحدة بدلاً من العمود بأكمله ، فيمكنك الرجوع إلى [إضافة ضوابط الخلية في صفحات العمل.](/cells/ar/net/adding-cell-controls-in-worksheets/)
### **إضافة زر**
لإضافة أزرار إلى عمود باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إضافة **الزر** إلى أي **عمود** محدد في **ورقة العمل**

**ملاحظة:** أثناء إضافة **زر**، يمكننا تحديد عرض وارتفاع وشرح الزر.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


يضيف مقتطف الكود أعلاه أزرارًا إلى جميع خلايا العمود المحدد. كلما تم تحديد أي خلية من ذلك العمود المحدد، يصبح الزر مرئيًا. لمزيد من المعلومات حول معالجة الأحداث للأزرار، يرجى الرجوع إلى [معالجة الأحداث لضوابط الأزرار.](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **إضافة مربع اختيار**
لإضافة مربعات اختيار إلى عمود باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إضافة **مربع اختيار** إلى أي **عمود** محدد في **ورقة العمل**

**ملاحظة:** أثناء إضافة **مربع اختيار**، يمكننا أيضًا تحديد حالة المربع اختيار.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


يضيف مقتطف الكود أعلاه مربعات اختيار إلى جميع خلايا العمود المحدد. لمزيد من المعلومات حول معالجة الأحداث للمربعات اختيار، يرجى الرجوع إلى [معالجة الأحداث لمربع اختيار.](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **إضافة مربع القائمة المنسدلة**
لإضافة مربعات نص منسدلة إلى عمود باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إنشاء مصفوفة من العناصر (أو القيم) التي سيتم إضافتها إلى **ComboBox**
- إضافة **ComboBox** (تحتوي على عناصر أو قيم) إلى أي **Column** محدد من **Worksheet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


يضيف مقتطف الكود أعلاه comboboxes إلى جميع الخلايا في العمود المحدد. كلما تم تحديد أي خلية في تلك العمود المحدد ، يصبح combobox مرئيًا. لمزيد من المعلومات حول التعامل مع الأحداث لـcomboboxes ، يرجى الرجوع إلى [التعامل مع الأحداث لعنصر تحكم ComboBox](/cells/ar/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
