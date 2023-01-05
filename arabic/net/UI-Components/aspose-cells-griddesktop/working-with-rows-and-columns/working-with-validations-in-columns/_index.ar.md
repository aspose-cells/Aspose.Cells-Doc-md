---
title: العمل مع عمليات التحقق من الصحة في الأعمدة
type: docs
weight: 80
url: /ar/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 في أحد موضوعاتنا السابقة ، ناقشنا حول عمليات التحقق ولكن كان ذلك في سياق[عمليات التحقق من الصحة في أوراق العمل](/cells/ar/net/working-with-validations-in-worksheets/) (للحصول على معلومات عامة حول أوضاع التحقق والتحقق ، يمكن للمطورين الرجوع إلى هذا الموضوع). في هذا الموضوع ، سنشرح عمليات التحقق من الصحة فيما يتعلق بالأعمدة. باستخدام هذه الميزة ، يمكن للمطورين تطبيق قاعدة التحقق من الصحة على أي عمود في ورقة العمل. دعونا نناقشها بالتفصيل.

{{% /alert %}} 
## **إضافة التحقق من صحة العمود**
لإضافة أي نوع من التحقق إلى عمود ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
- **يضيف** المطلوب**تصديق** إلى أي عمود

**الأهمية:**لمزيد من المعلومات حول أنواع التحقق من الصحة (أو أوضاع التحقق مثل**مطلوب التحقق من الصحة**, **التحقق من صحة التعبيرات العادية** و**التحقق المخصص** ) والتنفيذ**التحقق المخصص** ، يرجى الرجوع إلى[العمل مع عمليات التحقق من الصحة في أوراق العمل.](/cells/ar/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **الوصول إلى التحقق من العمود**
للوصول إلى التحقق من عمود معين ، يرجى اتباع الخطوات أدناه:

-  قم بالوصول إلى ملف**ورقة عمل**
-  الوصول إلى عمود محدد**تصديق** في ال**ورقة عمل**
-  تعديل**تصديق** السمات ، إذا رغبت في ذلك



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **إزالة التحقق من العمود**
لإزالة التحقق من عمود معين من ورقة العمل ، يرجى اتباع الخطوات التالية:

-  قم بالوصول إلى ملف**ورقة عمل**
-  قم بإزالة عمود معين**تصديق** من**ورقة عمل**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
