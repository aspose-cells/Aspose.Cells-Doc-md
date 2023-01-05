---
title: إضافة Cell ضوابط في أوراق العمل
type: docs
weight: 120
url: /ar/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 عناصر التحكم Cell هي في الواقع تلك الضوابط التي يمكن إضافتها إلى أوراق العمل. نحن نتصل بهم**Cell الضوابط** لأنه يتم عرض عناصر التحكم هذه في الخلايا. في هذا الموضوع ، سنناقش حول إضافة أحداث عناصر التحكم في الخلايا هذه والتعامل معها.

{{% /alert %}} 
## **مقدمة**
حاليًا ، يدعم Aspose.Cells.GridDesktop إضافة ثلاثة أنواع من عناصر التحكم في الخلية ، والتي تشمل ما يلي:

- **زر**
- **خانة الاختيار**
- **صندوق التحرير**

كل هذه الضوابط مشتقة من فئة مجردة ،**CellControl**تحتوي كل ورقة عمل على مجموعة من**ضوابط**. يمكن إضافة عناصر تحكم خلية جديدة ويمكن الوصول إلى العناصر الموجودة باستخدام هذا**ضوابط**جمع بسهولة.

**الأهمية:**إذا كنت ترغب في إضافة عناصر تحكم الخلية إلى جميع خلايا العمود بدلاً من إضافة واحدة تلو الأخرى ، فيمكنك الرجوع إليها[إدارة Cell عناصر التحكم في الأعمدة.](/cells/ar/net/adding-cell-controls-in-worksheets/)
### **إضافة زر**
لإضافة زر إلى ورقة العمل باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

- أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
- الوصول إلى أي ملفات**ورقة عمل**
- يضيف**زر**الى**ضوابط**جمع**ورقة عمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


أثناء الإضافة**زر**، يمكننا تحديد موقع الخلية (مكان عرضها) والعرض والارتفاع وتعليق الزر.
#### **التعامل مع حدث الزر**
لقد ناقشنا حول الإضافة**زر**السيطرة على**ورقة عمل**ولكن ما هي ميزة وجود زر فقط في ورقة العمل إذا لم نتمكن من استخدامه. لذلك ، هنا تأتي الحاجة إلى معالجة الحدث للزر.

للتعامل مع**انقر**حدث**زر**التحكم ، Aspose.Cells.GridDesktop**CellButtonClick**الحدث الذي يجب على المطورين تنفيذه حسب احتياجاتهم. على سبيل المثال ، لقد عرضنا للتو رسالة عند النقر فوق الزر كما هو موضح أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **تحديد صورة خلفية لعنصر التحكم في الزر**
يمكننا تعيين صورة / صورة خلفية للتحكم في الزر مع التسمية / النص الخاص به كما هو موضح في الكود أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**الأهمية:**تحتوي جميع أحداث عناصر التحكم في الخلية على ملف**CellControlEventArgs**الوسيطة التي توفر أرقام الصفوف والأعمدة للخلية التي تحتوي على عنصر تحكم الخلية (الذي يتم تشغيل الحدث الخاص به).
### **إضافة CheckBox**
لإضافة خانة اختيار إلى ورقة العمل باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

- أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
- الوصول إلى أي ملفات**ورقة عمل**
- يضيف**خانة الاختيار**الى**ضوابط**جمع**ورقة عمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


أثناء الإضافة**خانة الاختيار**، يمكننا تحديد موقع الخلية (مكان عرضها) وحالة مربع الاختيار.
#### **معالجة حدث CheckBox**
Aspose.Cells.GridDesktop يوفر**CellCheckedChanged**الحدث الذي يتم تشغيله عندما**التحقق**تم تغيير حالة مربع الاختيار. يمكن للمطورين التعامل مع هذا الحدث وفقًا لمتطلباتهم. على سبيل المثال ، لقد عرضنا للتو رسالة لإظهار ملف**التحقق**حالة خانة الاختيار في الكود أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **مضيفا ComboBox**
لإضافة مربع تحرير وسرد إلى ورقة العمل باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

- أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
- الوصول إلى أي ملفات**ورقة عمل**
- قم بإنشاء مصفوفة من العناصر (أو القيم) التي ستتم إضافتها إليها**صندوق التحرير**
- يضيف**صندوق التحرير**الى**ضوابط**جمع**ورقة عمل**من خلال تحديد موقع الخلية (حيث سيتم عرض مربع التحرير والسرد) والعناصر / القيم التي سيتم عرضها عند النقر فوق مربع التحرير والسرد



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **التعامل مع حدث ComboBox**
Aspose.Cells.GridDesktop يوفر**CellSelectedIndexChanged**الحدث الذي يتم تشغيله عندما**الفهرس المختار**من combobox تغيرت. يمكن للمطورين التعامل مع هذا الحدث وفقًا لرغباتهم. على سبيل المثال ، لقد عرضنا للتو رسالة لإظهار ملف**العنصر المحدد**من التحرير والسرد:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
