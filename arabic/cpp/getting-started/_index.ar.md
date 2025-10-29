---
title: البدء
type: docs
weight: 10
url: /ar/cpp/getting-started/
description: كيفية تثبيت Aspose Cells for C++ وإنشاء تطبيق Hello World.
---

{{% alert color="primary" %}} 

سيعرض هذا الصفحة كيفية تثبيت Aspose Cells for C++ وإنشاء تطبيق Hello World.

{{% /alert %}}

## **التثبيت**

### **تثبيت Aspose Cells من خلال NuGet**

NuGet هو أسهل طريقة لتنزيل وتثبيت Aspose.Cells for C++. 
1. إنشاء مشروع Microsoft Visual Studio لـ C++.
2. تضمين ملف الرأس "Aspose.Cells.h".
3. فتح Microsoft Visual Studio ومدير حزمة NuGet.
4. البحث عن "aspose.cells.cpp" للعثور على Aspose.Cells for C++ المطلوبة. 
5. انقر فوق "تثبيت"، سيتم تنزيل Aspose.Cells for C++ والإشارة إليه في مشروعك.

**![تثبيت Aspose Cells من خلال NuGet](InstallThroughNuget.png)**

يمكنك أيضًا تنزيله من صفحة الويب nuget ل aspose.cells: 
[حزمة NuGet لـ Aspose.Cells for C++](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[مزيد من الخطوات للتفاصيل](/cells/ar/cpp/installation/)

### **عرض توضيحي لاستخدام Aspose.Cells for C++ على Windows**

1. قم بتنزيل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك الضغط عن الحزمة وستجد مثالًا حول كيفية استخدام Aspose.Cells for C++.
3. افتح ملف example.sln باستخدام Visual Studio 2017 أو أحدث.
4. main.cpp: يظهر هذا الملف كيفية كتابة الاختبار لـ Aspose.Cells for C++.

### **عرض توضيحي لاستخدام Aspose.Cells for C++ على Linux.**

1. قم بتنزيل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك الضغط عن الحزمة وستجد مثالًا حول كيفية استخدام Aspose.Cells for C++ على Linux.
3. تأكد من أنك في المسار الذي يقع فيه المثال.
4. قم بتشغيل "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. قم بتشغيل "cmake --build example/build"

### **عرض توضيحي لاستخدام Aspose.Cells for C++ على نظام Mac OS.**

1. قم بتنزيل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك الضغط عن الحزمة وستجد مثالًا حول كيفية استخدام Aspose.Cells for C++ على نظام MacOS.
3. تأكد من أنك في المسار الذي يقع فيه المثال.
4. قم بتشغيل "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. قم بتشغيل "cmake --build example/build"

## **إنشاء تطبيق مرحبًا بالعالم**

تقوم الخطوات التالية بإنشاء تطبيق مرحبًا بالعالم باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells:

1. أنشئ نسخة من فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. إذا كان لديك ترخيص، ثم [قم بتطبيقه](/cells/ar/cpp/licensing/).
   إذا كنت تستخدم النسخة التجريبية، فتخطى خطوط الكود المتعلقة بالترخيص.
١. الوصول إلى أي خلية مرغوبة في ورقة العمل في ملف إكسل.
1. أدخل عبارة "**مرحبًا بالعالم!**" في الخلية المستخدمة.
1. إنشاء ملف Microsoft Excel المعدل.

يتم توضيح تنفيذ الخطوات أعلاه في الأمثلة أدناه.

### **مثال على الشفرة: إنشاء مصنف جديد**

المثال التالي يقوم بإنشاء مصنف جديد من البداية، يقوم بإدراج "**مرحبًا بالعالم!**" في الخلية A1 في ورقة العمل الأولى، ويحفظ ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **مثال على الشفرة: فتح ملف موجود**

المثال التالي يفتح ملف قالب Microsoft Excel موجود، يحصل على خلية ويتحقق من القيمة في الخلية A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
