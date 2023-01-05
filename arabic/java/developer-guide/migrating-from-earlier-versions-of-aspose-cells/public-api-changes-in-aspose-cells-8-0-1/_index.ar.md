---
title: API العام التغييرات في Aspose.Cells 8.0.1
type: docs
weight: 30
url: /ar/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

تسرد هذه الصفحات التغييرات API العامة التي تم تقديمها في Aspose.Cells 8.0.1. لا يشمل فقط الأساليب العامة الجديدة والمتقادمة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells والتي قد تؤثر على الكود الحالي. أي سلوك يتم تقديمه يمكن اعتباره انحدارًا ويقوم بتعديل السلوك الحالي له أهمية خاصة ويتم توثيقه هنا.

{{% /alert %}} 
## **تمت إضافة خاصية MemorySetting إلى الفئة Cells**
كشفت الفئة Cells عن طرق setMemorySetting & getMemorySetting التي يمكن استخدامها لتحسين استخدام الذاكرة لبيانات الخلايا ، وبالتالي تقليل التكلفة الإجمالية للذاكرة. يوضح المثال التالي كيفية كتابة بيانات كبيرة إلى ورقة عمل في الوضع الأمثل.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

 لن تعمل إعدادات الذاكرة للورقة الافتراضية التي تم إنشاؤها تلقائيًا بواسطة المصنف. لتغيير إعدادات الذاكرة للأوراق الموجودة ، يرجى تطبيق إعدادات الذاكرة يدويًا قبل إجراء أي معالجة للبيانات.

{{% /alert %}} {{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[تحسين الذاكرة أثناء العمل مع مجموعات البيانات الكبيرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
