---
title: كيفية إصلاح خطأ java.lang.OutOfMemoryError أثناء تحميل جداول البيانات الكبيرة
type: docs
weight: 20
url: /ar/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 هناك احتمالات معقولة أن يقوم مُنشئ المصنف بإلقاء خطأ java.lang.OutOfMemoryError أثناء تحميل جداول بيانات كبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة ، وبالتالي يجب تحميل جدول البيانات أثناء تمكين[تفضيلات الذاكرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **كيفية إصلاح خطأ java.lang.OutOfMemoryError أثناء تحميل جدول بيانات كبير**
توفر واجهات برمجة التطبيقات Aspose.Cells تفضيلات الذاكرة لتحسين استهلاك الذاكرة أثناء تحميل جداول البيانات ومعالجتها. هذه الخيارات مفيدة أيضًا في التحميل الفعال لجداول البيانات الكبيرة التي تحتوي على مجموعات بيانات ضخمة في كائن المصنف كما هو موضح أدناه.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
