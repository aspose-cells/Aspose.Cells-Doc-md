---
title: تغييرات API العامة في Aspose.Cells 8.0.1
type: docs
weight: 30
url: /ar/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

تشمل هذه الصفحة قائمة التغييرات العامة التي تم إدخالها في Aspose.Cells 8.0.1. وتتضمن ليس فقط الطرق العامة الجديدة والمهجورة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الكامنة في Aspose.Cells التي قد تؤثر على الرمز الموجود. أي سلوك يُعتبر تقديمًا ويُطلق عليه النحو الشكلي ويُعد تحديثًا لسلوك موجود بالذات مهمًا وموجود هنا.

{{% /alert %}} 
## **تمت إضافة خاصية MemorySetting إلى فئة Cells**
يتضمن فصيل الخلايا طرقًا معرضة لـتعيين الذاكرة والحصول عليها، والتي يمكن استخدامها لتحسين استخدام الذاكرة لبيانات الخلايا، وبالتالي تقليل تكلفة الذاكرة الإجمالية. يوضح المثال التالي كيفية كتابة بيانات كبيرة إلى ورقة عمل في وضع محسن.

**Java**

{{< highlight csharp >}}

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

لن يعمل إعداد الذاكرة تلقائيًا للورقة الافتراضية التي تم إنشاؤها بواسطة المصنف. من أجل تغيير إعدادات الذاكرة للأوراق الموجودة، يرجى تطبيق إعدادات الذاكرة يدويًا قبل القيام بأي عمليات تلاعب بالبيانات. 

{{% /alert %}} {{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [تحسين استخدام الذاكرة أثناء العمل مع مجموعات بيانات كبيرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
