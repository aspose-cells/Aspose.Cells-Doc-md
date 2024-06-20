---
title: العمل مع التحقق من الصحة في الأعمدة
type: docs
weight: 80
url: /ar/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop، تحقق، التحقق من الصحة
description: يقدم هذا المقال كيفية استخدام التحقق من الصحة في الأعمدة في GridDesktop.
---

{{% alert color="primary" %}} 

في أحد مواضيعنا السابقة، ناقشنا التحقق ولكن ذلك كان في سياق [التحقق في ورقات العمل](/cells/ar/net/working-with-validations-in-worksheets/) (للحصول على معلومات عامة حول التحقق وأوضاع التحقق، يمكن للمطورين الرجوع إلى هذا الموضوع). في هذا الموضوع، سنشرح التحقق في الأعمدة. باستخدام هذه الميزة، يمكن للمطورين تطبيق قاعدة تحقق على أي عمود من أعمدة ورقة العمل. لنناقش ذلك بالتفصيل.

{{% /alert %}} 
## **إضافة تحقق الصف**
لإضافة أي نوع من التحقق إلى الصف، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- **إضافة** تحقق مطلوب إلى أي صف

**مهم:** للحصول على مزيد من المعلومات حول أنواع التحقق (أو أوضاع التحقق مثل **التحقق من الصحة المطلوب**، **التحقق من التعبيرات العادية** و **التحقق المخصص**) وتنفيذ **التحقق المخصص**، يرجى الرجوع إلى [العمل مع التحقق في الأوراق العمل.](/cells/ar/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **الوصول إلى تحقق الصف**
للوصول إلى تحقق الصف الخاص بعمود معين، يرجى اتباع الخطوات التالية:

- الوصول إلى **ورقة العمل** المطلوبة
- الوصول إلى **تحقق الصف** المعين في **ورقة العمل**
- تحرير سمات **التحقق** ، إذا لزم الأمر



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **إزالة تحقق الصف**
لإزالة تحقق معين من الورقة العمل، يرجى اتباع الخطوات التالية:

- الوصول إلى **ورقة العمل** المطلوبة
- إزالة **تحقق الصف** المعين من **ورقة العمل**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
