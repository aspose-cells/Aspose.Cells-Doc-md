---
title: إضافة عناصر تحكم خلية في أوراق العمل
type: docs
weight: 120
url: /ar/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: يقدم هذا المقال مقدمة عن كيفية إضافة عنصر تحكم في ورقة عمل في GridDesktop.
---

{{% alert color="primary" %}} 

في الواقع، عناصر التحكم في الخلايا هي تلك العناصر التي يمكن إضافتها إلى أوراق العمل. نسميها ** عناصر تحكم الخلية ** لأن هذه العناصر يتم عرضها في الخلايا. في هذا الموضوع، سنناقش إضافة ومعالجة أحداث هذه العناصر التحكم.

{{% /alert %}} 
## **مقدمة**
حاليًا، يدعم Aspose.Cells.GridDesktop إضافة ثلاثة أنواع من عناصر التحكم في الخلايا، وتشمل ما يلي:

- **زر**
- **صندوق اختيار**
- **قائمة تحديد**

كل هذه العناصر تستند إلى فئة مجردة، **CellControl**. تحتوي كل ورقة عمل على مجموعة من **التحكم**. يمكن بسهولة إضافة عناصر تحكم جديدة في الخلايا والوصول إلى تلك الموجودة باستخدام هذه المجموعة **التحكم**.

**مهم جدًا:** إذا كنت ترغب في إضافة عناصر تحكم في جميع الخلايا لعمود بدلاً من إضافتها واحدة تلو الأخرى، فيمكنك الرجوع إلى [إدارة العناصر التحكم في الأعمدة.](/cells/ar/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **إضافة زر**
لإضافة زر إلى ورقة العمل باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات التالية:

- أضف تحكم Aspose.Cells.GridDesktop إلى النموذج الخاص بك
- الوصول إلى أي ورقة عمل مرغوبة
- إضافة زر إلى مجموعة الضوابط في ورقة العمل



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


أثناء إضافة زر، يمكننا تحديد موقع الخلية (حيث يتم عرضها) والعرض والارتفاع وتسمية الزر.
#### **معالجة حدث الزر**
لقد ناقشنا إضافة زر إلى ورقة العمل ولكن ما هي الميزة من وجود زر في ورقة العمل إذا لم نتمكن من استخدامه. لذا، هنا يأتي دور معالجة حدث الزر.

للتعامل مع حدث النقر على زر التحكم، يوفر Aspose.Cells.GridDesktop حدث CellButtonClick الذي يجب تنفيذه من قبل المطورين وفقا لاحتياجاتهم. على سبيل المثال، قمنا بعرض رسالة فقط عند النقر على الزر كما هو مبين أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **تحديد صورة خلفية لتحكم الزر**
يمكننا تعيين صورة خلفية/صورة لتحكم الزر مع تسميته/نصه كما هو مبين في الكود أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


مهم: جميع أحداث تحكمات الخلية تحتوي على وسيطة CellControlEventArgs التي توفر أرقام الصف والعمود للخلية التي تحتوي على تحكم الخلية (الذي تم تشغيل حدثه).
### **إضافة مربع اختيار**
لإضافة مربع اختيار في ورقة العمل باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات أدناه:

- أضف تحكم Aspose.Cells.GridDesktop إلى النموذج الخاص بك
- الوصول إلى أي ورقة عمل مرغوبة
- إضافة مربع اختيار إلى مجموعة الضوابط في ورقة العمل



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


أثناء إضافة مربع اختيار، يمكننا تحديد موقع الخلية (حيث يتم عرضها) وحالة مربع الاختيار.
#### **معالجة حدث مربع الاختيار**
يوفر Aspose.Cells.GridDesktop حدث CellCheckedChanged الذي يتم تشغيله عند تغيير حالة المربع اختيار. يمكن للمطورين التعامل مع هذا الحدث وفقا لاحتياجاتهم. على سبيل المثال، قمنا بعرض رسالة لإظهار حالة المربع اختيار في الكود أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **إضافة مربع القائمة المنسدلة**
لإضافة مربع القائمة المنسدلة في ورقة العمل باستخدام Aspose.Cells.GridDesktop يرجى اتباع الخطوات أدناه:

- أضف تحكم Aspose.Cells.GridDesktop إلى النموذج الخاص بك
- الوصول إلى أي ورقة عمل مرغوبة
- إنشاء مصفوفة من العناصر (أو القيم) التي سيتم إضافتها إلى **ComboBox**
- إضافة **ComboBox** إلى مجموعة **Controls** لورقة العمل بتحديد موقع الخلية (حيث سيتم عرض combobox) والعناصر/القيم التي سيتم عرضها عند النقر على combobox



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **معالجة الحدث في ComboBox**
توفر Aspose.Cells.GridDesktop حدث **CellSelectedIndexChanged** الذي يتم تشغيله عند تغيير **Selected Index** للـ combobox. يمكن للمطورين التحكم في هذا الحدث وفقًا لرغباتهم. على سبيل المثال، لقد عرضنا رسالة لإظهار **Selected Item** للـ combobox:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
