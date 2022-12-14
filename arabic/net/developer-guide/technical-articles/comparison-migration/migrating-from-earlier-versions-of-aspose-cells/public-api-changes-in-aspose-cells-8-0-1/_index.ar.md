---
title: API العام التغييرات في Aspose.Cells 8.0.1
type: docs
weight: 20
url: /ar/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

تسرد هذه الصفحات التغييرات API العامة التي تم تقديمها في Aspose.Cells 8.0.1. لا يشمل فقط الأساليب العامة الجديدة والمتقادمة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells والتي قد تؤثر على الكود الحالي. أي سلوك يتم تقديمه يمكن اعتباره انحدارًا ويقوم بتعديل السلوك الحالي له أهمية خاصة ويتم توثيقه هنا.

{{% /alert %}} 
## **تمت إضافة خاصية MemorySetting إلى Cells Class**
تعرض الفئة Cells خاصية MemorySetting التي يمكن استخدامها لتحسين استخدام الذاكرة لبيانات الخلايا ، وبالتالي تقليل التكلفة الإجمالية للذاكرة. يوضح المثال التالي كيفية كتابة بيانات كبيرة إلى ورقة عمل في الوضع الأمثل.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

لن تعمل إعدادات الذاكرة للورقة الافتراضية التي تم إنشاؤها تلقائيًا بواسطة كائن المصنف. لتغيير إعدادات الذاكرة للأوراق الموجودة ، يرجى تطبيق إعداد الذاكرة يدويًا قبل إجراء أي معالجة للبيانات.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[تحسين الذاكرة أثناء العمل مع مجموعات البيانات الكبيرة](/cells/ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
