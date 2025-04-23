---
title: نسخ ونقل أوراق العمل داخل وبين أوراق العمل
type: docs
weight: 80
url: /ar/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عدد من أوراق العمل مع تنسيقات وإدخال بيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الربعية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

يدعم Aspose.Cells نسخ أو نقل الأوراق داخل أو بين أوراق العمل. تتم نسخ الأوراق بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسومات والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. أنشئ معينين بيانات في Microsoft Excel. لأغراض هذا المثال، قمنا بإنشاء معينين جديدين في Microsoft Excel وإدخال بعض البيانات إلى أوراق العمل.

- FirstWorkbook.xlsx (3 ورقات عمل).
- SecondWorkbook.xlsx (ورقة عمل واحدة).

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تنزيل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. أنشئ مشروعًا:
   1. ابدأ Visual Studio.Net.
   1. أنشئ تطبيقًا جديدًا على الكونسول.
1. أضف مراجع:
   1. أضف مرجعًا إلى Aspose.Cells إلى المشروع.
      على سبيل المثال، أضف مرجعًا إلى ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **نسخ ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نسخ ورقة العمل المسماة نسخ إلى SecondWorkbook.xlsx بإسم Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
