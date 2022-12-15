---
title: ابدء
type: docs
weight: 10
url: /ar/cpp/getting-started/
description: كيفية تثبيت Aspose Cells for C++ وإنشاء تطبيق Hello World.
---
{{% alert color="primary" %}} 

ستوضح لك هذه الصفحة كيفية تثبيت Aspose Cells for C++ وإنشاء تطبيق Hello World.

{{% /alert %}}

## **تثبيت**

### **قم بتثبيت Aspose Cells حتى NuGet**

NuGet هو أسهل طريقة لتنزيل وتثبيت Aspose.Cells for C++.
1. قم بإنشاء Microsoft مشروع Visual Studio for C++.
2. قم بتضمين ملف الرأس "Aspose.Cells.h".
3. افتح Microsoft Visual Studio و NuGet مدير الحزم.
 4. ابحث عن "aspose.cells.cpp" للعثور على Aspose.Cells for C++ المطلوب.
5. انقر فوق "تثبيت" ، سيتم تنزيل Aspose.Cells for C++ والإشارة إليه في مشروعك.

**! [تثبيت Aspose Cells حتى NuGet] (InstallThroughNuget.png)**

 يمكنك أيضًا تنزيله من صفحة الويب nuget لغرض معين.
[Aspose.Cells for C++ NuGet الحزمة](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[مزيد من الخطوات للحصول على التفاصيل](/cells/ar/cpp/installation/)

### **عرض توضيحي لاستخدام Aspose.Cells for C++ على Windows**

1. تنزيل Aspose.Cells for C++ من الصفحة التالية:
[تحميل Aspose.Cells for C++ (Windows)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك ضغط الحزمة وستجد عرضًا توضيحيًا يوضح كيفية استخدام Aspose.Cells for C++.
3. افتح Demo.sln باستخدام Visual Studio 2017 أو إصدار أعلى
4. main.cpp: يوضح هذا الملف كيفية كتابة التعليمات البرمجية لاختبار Aspose.Cells for C++
 5. sourceFile / resultFile: هذين المجلدين هما مجلدات التخزين المستخدمة في main.cpp

### **كيفية استخدام Aspose.Cells for C++ على Linux OS**

1. تنزيل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك ضغط الحزمة وستجد عرضًا توضيحيًا حول كيفية استخدام for C++ Aspose.Cells لنظام التشغيل Linux.
3. قم بتشغيل "cd Demo" في سطر أوامر Linux
4. قم بتشغيل "rm -rf build؛ mkdir build؛ cd build"
5. سيؤدي تشغيل "cmake .." إلى إنشاء ملف Makefile بواسطة CMakeLists.txt في مجلد العرض التوضيحي
6. قم بتشغيل "make" للترجمة
 7. قم بتشغيل "./demo" سترى النتيجة

## **إنشاء تطبيق Hello World**

تؤدي الخطوات أدناه إلى إنشاء تطبيق Hello World باستخدام Aspose.Cells API:

1.  قم بإنشاء مثيل لـ[دفتر العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) صف دراسي.
1.  إذا كان لديك ترخيص ، إذن[قم بتطبيقه](/cells/ar/cpp/licensing/).
 إذا كنت تستخدم الإصدار التقييمي ، فتخط سطور التعليمات البرمجية المتعلقة بالترخيص.
1. قم بالوصول إلى أي خلية مرغوبة من ورقة العمل في ملف Excel.
1. تضاف عبارة "**Hello World!**"في خلية تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

يتم توضيح تنفيذ الخطوات المذكورة أعلاه في الأمثلة أدناه.

### **نموذج التعليمات البرمجية: إنشاء مصنف جديد**

ينشئ المثال التالي مصنفًا جديدًا من البداية ، يُدرج "**Hello World!**"في الخلية A1 في ورقة العمل الأولى ويحفظ ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **نموذج التعليمات البرمجية: فتح ملف موجود**

يفتح المثال التالي ملف قالب Excel Microsoft موجود ، ويحصل على خلية ويتحقق من القيمة في الخلية A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
