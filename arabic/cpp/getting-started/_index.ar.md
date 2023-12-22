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

##  **تثبيت**

###  **تثبيت Aspose Cells حتى NuGet**

 NuGet أسهل طريقة للتحميل والتثبيت Aspose.Cells for C++.
1. إنشاء مشروع Visual Studio Microsoft for C++.
2. قم بتضمين ملف الرأس "Aspose.Cells.h".
3. افتح Microsoft Visual Studio ومدير الحزم NuGet.
 4. ابحث عن "aspose.cells.cpp" للعثور على Aspose.Cells for C++ المطلوب.
5. انقر على "تثبيت"، وسيتم تنزيل Aspose.Cells for C++ والإشارة إليها في مشروعك.

**![تثبيت Aspose Cells حتى NuGet](InstallThroughNuget.png)**

 يمكنك أيضًا تنزيله من صفحة الويب nuget الخاصة بـ aspose.cells:
[Aspose.Cells for C++ NuGet الباقة](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[المزيد من الخطوات للحصول على التفاصيل](/cells/ar/cpp/installation/)

###  **تجريبي لاستخدام Aspose.Cells for C++ على Windows**

1. حمل Aspose.Cells for C++ من الصفحة التالية:
[تحميل Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك ضغط الحزمة وستجد مثالاً لكيفية الاستخدام Aspose.Cells for C++.
3. افتح example.sln باستخدام Visual Studio 2017 أو إصدار أعلى
4. main.cpp : هذا الملف يوضح كيفية البرمجة للاختبار Aspose.Cells for C++

###  **عرض توضيحي لاستخدام Aspose.Cells for C++ على Linux**

1. حمل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++ (لينكس)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك ضغط الحزمة وستجد مثالاً لكيفية استخدام Aspose.Cells for C++ لنظام التشغيل Linux.
3. تأكد من أنك في المسار الذي يوجد به المثال.
4. قم بتشغيل "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. قم بتشغيل "cmake --build example/build"

###  **عرض توضيحي لاستخدام Aspose.Cells for C++ على نظام التشغيل Mac OS**

1. حمل Aspose.Cells for C++ من الصفحة التالية:
[تنزيل Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. قم بفك ضغط الحزمة وستجد مثالاً حول كيفية استخدام Aspose.Cells for C++ لنظام التشغيل MacOS.
3. تأكد من أنك في المسار الذي يوجد به المثال.
4. قم بتشغيل "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. قم بتشغيل "cmake --build example/build"

##  **إنشاء تطبيق Hello World**

الخطوات أدناه تنشئ تطبيق Hello World باستخدام Aspose.Cells API:

1.  إنشاء مثيل لـ[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) فصل.
1.  إذا كان لديك ترخيص، ثم[قم بتطبيقه](/cells/ar/cpp/licensing/).
 إذا كنت تستخدم الإصدار التقييمي، فتخطى سطور التعليمات البرمجية المتعلقة بالترخيص.
1. الوصول إلى أي خلية مطلوبة من ورقة العمل في ملف Excel.
1. أدخل الكلمات "**Hello World!**" في الخلية التي تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

يتم توضيح تنفيذ الخطوات المذكورة أعلاه في الأمثلة أدناه.

###  **نموذج التعليمات البرمجية: إنشاء مصنف جديد**

يقوم المثال التالي بإنشاء مصنف جديد من البداية، وإدراج "**Hello World!**" في الخلية A1 في ورقة العمل الأولى وحفظ ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **نموذج التعليمات البرمجية: فتح ملف موجود**

يفتح المثال التالي ملف قالب Excel Microsoft موجودًا، ويحصل على خلية ويتحقق من القيمة في الخلية A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
