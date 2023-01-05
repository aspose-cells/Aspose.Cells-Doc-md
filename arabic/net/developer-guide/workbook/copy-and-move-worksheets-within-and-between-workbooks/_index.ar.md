---
title: نسخ ونقل أوراق العمل داخل وبين المصنفات
type: docs
weight: 80
url: /ar/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى عدد من أوراق العمل ذات التنسيق المشترك وإدخال البيانات. على سبيل المثال ، إذا كنت تعمل باستخدام ميزانيات ربع سنوية ، فقد ترغب في إنشاء مصنف بأوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

Aspose.Cells يدعم نسخ أوراق العمل أو نقلها داخل مصنفات العمل أو بينها. يتم نسخ أوراق العمل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والمخططات والصور والكائنات الأخرى بأعلى درجات الدقة.

{{% /alert %}}

## **نسخ أوراق العمل ونقلها**

### **نسخ ورقة عمل داخل مصنف**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. قم بإنشاء مصنفين مع بعض البيانات في Microsoft Excel. لأغراض هذا المثال ، أنشأنا مصنفين جديدين في Microsoft Excel وأدخلنا بعض البيانات في أوراق العمل.

- FirstWorkbook.xlsx (3 أوراق عمل).
- SecondWorkbook.xlsx (ورقة عمل واحدة).

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. قم بتثبيته على جهاز الكمبيوتر الخاص بك.
 الجميع[Aspose](http://www.aspose.com/) المكونات ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.
1. أنشئ مشروعًا:
 1. ابدأ تشغيل Visual Studio.Net.
 1. إنشاء تطبيق وحدة تحكم جديد.
1. أضف المراجع:
 1. قم بإضافة مرجع إلى Aspose.Cells إلى المشروع.
 على سبيل المثال ، أضف مرجعًا إلى ... \ Program Files \ Aspose \ Aspose.Cells \ Bin \ Net1.0 \ Aspose.Cells.dll
1. انسخ ورقة العمل داخل مصنف
 ينسخ المثال الأول ورقة العمل الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ التعليمات البرمجية ، يتم نسخ ورقة العمل المسماة "نسخ" داخل FirstWorkbook.xlsx باسم الورقة الأخيرة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **نقل ورقة عمل داخل مصنف**

يوضح الكود أدناه كيفية نقل ورقة عمل من موضع واحد في مصنف إلى آخر. يؤدي تنفيذ التعليمات البرمجية إلى نقل ورقة العمل المسماة Move from index 1 إلى index 2 في FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **نسخ ورقة عمل بين المصنفات**

يؤدي تنفيذ التعليمات البرمجية إلى نسخ ورقة العمل المسماة Copy إلى SecondWorkbook.xlsx باسم Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **نقل ورقة العمل بين المصنفات**

يؤدي تنفيذ التعليمات البرمجية إلى نقل ورقة العمل المسماة Move from FirstWorkbook.xlsx إلى SecondWorkbook.xlsx باسم Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
