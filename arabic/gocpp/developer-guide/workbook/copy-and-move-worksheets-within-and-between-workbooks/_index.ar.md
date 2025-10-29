---
title: نسخ ونقل أوراق العمل داخل وبين المصنفات باستخدام Golang عبر C++
linktitle: نسخ وتحريك أوراق العمل
type: docs
weight: 80
url: /ar/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: تعلم كيفية نسخ وتحريك أوراق العمل داخل وبين دفاتر العمل Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى أوراق عمل متعددة ذات تصميم وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل على ميزانيات فصليّة، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على رؤوس أعمدة، رؤوس صفوف، وصيغ متطابقة. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها عدة مرات.

يدعم Aspose.Cells نسخ أو نقل الأوراق داخل أو بين أوراق العمل. تتم نسخ الأوراق بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسومات والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية متطابقة لجميع الأمثلة:

1. أنشئ دفترين عمل ببعض البيانات في Microsoft Excel. لأغراض هذا المثال، أنشأنا دفترين عمل جديدين في Microsoft Excel وأدخلنا بعض البيانات في أوراق العمل:
   - FirstWorkbook.xlsx (3 أوراق عمل)
   - SecondWorkbook.xlsx (ورقة عمل واحدة)

1. قم بتنزيل وتثبيت Aspose.Cells:
    1. [تحميل Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. قم بتثبيته على جهاز التطوير الخاص بك

1. أنشئ مشروعًا:
   1. أنشئ مشروع C++ جديد في بيئة تطويرك المفضلة

1. أضف مراجع:
   1. أضف مكتبة Aspose.Cells for C++ إلى مشروعك

1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **نسخ ورقة العمل بين دفاتر العمل**

تنفيذ الكود ينسخ ورقة العمل المسماة Copy إلى SecondWorkbook.xlsx باسم Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
