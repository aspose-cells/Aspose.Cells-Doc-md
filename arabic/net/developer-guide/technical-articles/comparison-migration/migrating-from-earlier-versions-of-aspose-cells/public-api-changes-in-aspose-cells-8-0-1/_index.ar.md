---
title: تغييرات API العامة في Aspose.Cells 8.0.1
type: docs
weight: 20
url: /ar/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

تشمل هذه الصفحة قائمة التغييرات العامة التي تم إدخالها في Aspose.Cells 8.0.1. وتتضمن ليس فقط الطرق العامة الجديدة والمهجورة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الكامنة في Aspose.Cells التي قد تؤثر على الرمز الموجود. أي سلوك يُعتبر تقديمًا ويُطلق عليه النحو الشكلي ويُعد تحديثًا لسلوك موجود بالذات مهمًا وموجود هنا.

{{% /alert %}} 
## **تمت إضافة خاصية MemorySetting إلى فئة Cells**
تمتك فئة Cells تعريض خاصية MemorySetting التي يمكن استخدامها لتحسين استخدام الذاكرة لبيانات الخلايا، وبالتالي تقليل تكلفة الذاكرة الكلية. يُظهر المثال التالي كيفية كتابة بيانات كبيرة إلى ورقة البيانات بوضع محسن.

**C#**

{{< highlight csharp >}}

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

لن تعمل إعدادات الذاكرة للورقة الافتراضية التي تم إنشاؤها تلقائيًا بواسطة كائن Workbook. من أجل تغيير إعدادات الذاكرة للصفحات الحالية، يرجى تطبيق إعداد الذاكرة يدويًا قبل أداء أي عمليات تلاعب بالبيانات.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [تحسين استخدام الذاكرة أثناء العمل مع مجموعات بيانات كبيرة](/cells/ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
