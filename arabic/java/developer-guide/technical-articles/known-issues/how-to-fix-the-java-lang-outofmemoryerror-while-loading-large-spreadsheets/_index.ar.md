---
title: كيفية إصلاح java.lang.OutOfMemoryError أثناء تحميل جداول بيانات كبيرة
type: docs
weight: 20
url: /ar/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

هناك فرص كبيرة لأن يطرح مُنشئ الورقة (Workbook) استثناء java.lang.OutOfMemoryError أثناء تحميل جداول بيانات كبيرة. يُقترح هذا الاستثناء أن الذاكرة المتاحة غير كافية لتحميل الجدول بالكامل في الذاكرة لذا يتعين تحميل الجدول بتمكين [تفضيلات الذاكرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **كيفية إصلاح java.lang.OutOfMemoryError أثناء تحميل جدول بيانات كبيرة**
تقدم واجهات برمجة التطبيقات لـ Aspose.Cells تفضيلات الذاكرة لتحسين استهلاك الذاكرة أثناء تحميل ومعالجة الجداول. هذه الخيارات أيضًا مفيدة في تحميل الجداول الكبيرة التي تحتوي على مجموعات بيانات ضخمة بشكل كفء في كائن Workbook كما هو موضح أدناه. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
