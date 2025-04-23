---
title: نسخ ونقل أوراق العمل داخل وبين أوراق العمل
type: docs
weight: 80
url: /ar/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عدد من أوراق العمل مع تنسيقات وإدخال بيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الربعية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

يدعم Aspose.Cells لبايثون via .NET نسخ أو نقل أوراق العمل داخل أو بين ملفات العمل. يتم نسخ أوراق العمل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والمخططات والصور وغيرها من الكائنات بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. أنشئ معينين بيانات في Microsoft Excel. لأغراض هذا المثال، قمنا بإنشاء معينين جديدين في Microsoft Excel وإدخال بعض البيانات إلى أوراق العمل.

- FirstWorkbook.xlsx (3 ورقات عمل).
- SecondWorkbook.xlsx (ورقة عمل واحدة).

1. قم بتنزيل وتثبيت Aspose.Cells for Python via .NET:
   1. [تحميل Aspose.Cells لبايثون via .NET](https://downloads.aspose.com/cells/python-net).
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. أنشئ مشروعًا وأضف مراجع:   
1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **نسخ ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نسخ ورقة العمل المسماة نسخ إلى SecondWorkbook.xlsx بإسم Sheet2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
