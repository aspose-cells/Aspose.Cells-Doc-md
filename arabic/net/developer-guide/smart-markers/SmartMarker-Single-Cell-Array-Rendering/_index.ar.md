---
title: عرض المصفوفات في خلية واحدة باستخدام SmartMarker | Aspose.Cells .NET
description: تعلَّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتَي `arrayassingle` و`arraydelimiter` الخاصتين بالعلامة الذكية في Aspose.Cells for .Net.
linktitle: عرض SmartMarker في خلية واحدة | Aspose.Cells
url: /ar/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, مكتبة .NET, جدول بيانات, العلامات الذكية, arrayassingle, arraydelimiter, مصفوفة في خلية واحدة, عرض المصفوفات, قالب
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يمكن لـ Aspose.Cells عرض مصدر بيانات من نوع مصفوفة في خلية واحدة عبر العلامات الذكية. تعطّل السمة `arrayassingle` سلوك التوزيع الافتراضي عنصرًا تلو الآخر، وتحدد السمة `arraydelimiter` الفاصل الموضوع بين العناصر المدمجة — بفاصلة افتراضيًا، أو بأي حرف واحد أو سلسلة متعددة الأحرف بين علامتَي اقتباس تحددها.
{{% /alert %}}

## **مقدمة**

تمثل العلامات الذكية في Aspose.Cells ميزة قائمة على القوالب تملأ بيانات جداول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. تُوضع العلامة في مصنف التصميم، وعند معالجة القالب بواسطة `WorkbookDesigner`، تُستبدل العلامات بالقيم من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة، مثل `&=Product.Tags` المرتبطة بمصفوفة `string[]` من أربع قيم، يوسّع المحرك المصفوفة ويضع كل عنصر في خلية خاصة به، فتتوزع القيم رأسيًا في العمود تحت العلامة. على الرغم من أن هذا السلوك ملائم في العديد من السيناريوهات، هناك حالات تفضّل فيها عرض المصفوفة بأكملها في خلية واحدة، مع ربط عناصرها متتالية وفصلها بفاصل من اختيارك.
تتعامل سمتا `arrayassingle` و`arraydelimiter`، المكتوبتان داخل أقواس العلامة الذكية بصيغة `name:value`، مع هذا المتطلب تحديدًا. تتيح لك الحفاظ على تخطيطات التقارير مضغوطة ومتوقعة، مع الاستمرار في العمل مباشرةً مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك توزيع المصفوفات الافتراضي**

عندما تشير علامة ذكية إلى خاصية مصفوفة، يمدّ Aspose.Cells المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، إذا كانت العلامة `&=Product.Tags` مرتبطة بمصفوفة `string[]` تحتوي على أربع قيم، تضع كل قيمة في خلية خاصة بها أسفل العلامة، مما يزيح بقية محتوى القالب إلى مواضع أخرى وقد يعطل تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

توجد العديد من السيناريوهات العملية التي يكون فيها سلوك التوزيع الافتراضي غير مرغوب فيه:
- **تقارير بأسلوب ملخصي** تحتاج إلى تخطيط مختصر بسجل واحد لكل صف.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية** التي يلزم عرضها كقيم مفصولة بفواصل أو بالشرطة العمودية داخل خلية واحدة.
- **وسوم التصفية أو مؤشرات الحالة** التي تجمع عدة قيم في موضع واحد لتسهيل القراءة.
- **خطوط المعالجة اللاحقة** (تصدير CSV، وعرض PDF، ودمج المراسلات) التي تتوقع قيمة موحدة واحدة لكل خلية بدلًا من نطاق موسّع.
- **التوافق عبر المنصات**، حيث لا تتحمل بعض الجهات المستهلكة المصفوفات الممتدة عبر خلايا متعددة.

### **الفجوة التي تعالجها**

بدون آلية مدمجة، سيضطر المطورون إلى معالجة البيانات مسبقًا في C# أو VB.NET — بدمج المصفوفات في سلاسل مفصولة قبل ربطها بمصمم المصنف. يكرر هذا المنطق، ويصعّب نماذج البيانات، ويزيد احتمال وقوع الأخطاء. تلغي سمتا `arrayassingle` و`arraydelimiter` هذا الالتفاف عبر التعامل مع التنسيق تعريفًا داخل العلامة الذكية نفسها.

## **مزايا الميزة**

يوفر استخدام سمتَي `arrayassingle` و`arraydelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء داخل خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على تخطيطات مضغوطة ومتوقعة.
- **التحكم المخصص في الفاصل**: حدّد الفاصل الذي تريده — الفاصلة الافتراضية، أو فاصلة منقوطة، أو شرطة، أو شرطة عمودية، أو سلسلة متعددة الأحرف محاطة بعلامتَي اقتباس مثل `" | "`.
- **التنسيق المستند إلى القالب**: لا يلزم كتابة أي كود إضافي لمعالجة البيانات مسبقًا؛ وتقع قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع بمحتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات مرنة**: تعمل مع المصفوفات النصية والرقمية من مصادر بيانات كائن.
- **التوافق مع الإصدارات الأقدم**: عند حذف السمتين، يبقى سلوك التوزيع الأصلي كما هو، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة العلامة الذكية**

تستخدم سمتا `arrayassingle` و`arraydelimiter` قواعد سمات `name:value` في Aspose.Cells داخل أقواس علامة ذكية قياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

يتكوّن العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayassingle:true` — يوجّه المحرك إلى عرض المصفوفة بأكملها في خلية واحدة بدلًا من توزيع عناصرها.
- `arraydelimiter:;` — اختيارية؛ تحدد الفاصل الموضوع بين عناصر المصفوفة. عند حذفها، تُستخدم الفاصلة.

{{% alert color="warning" %}}
اكتب السمات بصيغة `name:value` (نقطتان، لا علامة يساوي) وافصل بين السمات المتعددة بفاصلة **دون مسافات**. فالمسافة بعد الفاصلة تزيح القيمة التي تم تحليلها بمقدار حرف واحد — إذ سيؤدي `(arrayassingle:true, arraydelimiter:;)` إلى الدمج باستخدام الفاصل الخاطئ `:;` بدلًا من `;`.
{{% /alert %}}

### **أشكال الفاصل**

- حرف واحد يوضع مباشرةً بعد النقطتين: `arraydelimiter:;`، `arraydelimiter:-`، `arraydelimiter:*`.
- يُكتب الفاصل متعدد الأحرف بين علامتَي اقتباس مزدوجتين: `arraydelimiter:" | "`، `arraydelimiter:" - "`.

### **سير العمل خطوة بخطوة**

يوضح سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تجهيز مصدر البيانات**: أنشئ فئة تكشف خاصية تُعيد مصفوفة، مثل `string[]` أو `int[]`، واربط `List<T>` من هذه الفئة حتى يقرأ المحرك سجلًا واحدًا لكل صف.
2. **إنشاء مصنف تصميم**: أنشئ `Workbook` جديدًا، وأضف صف عناوين، وضع خلية علامة ذكية تشير إلى خاصية المصفوفة مع السمة `arrayassingle` (و`arraydelimiter` عند الحاجة إلى فاصل مخصص).
3. **إنشاء WorkbookDesigner**: أنشئ كائن `WorkbookDesigner` حول المصنف واربط مصدر البيانات باستخدام `SetDataSource`.
4. **معالجة العلامات**: استدعِ أسلوب `WorkbookDesigner.Process()` لتوسيع العلامات الذكية وملء المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي صيغة ملف مدعومة أخرى.

### **مثال برمجي 1 — العرض الأساسي لمصفوفة نصية**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

يطبع المثال القيمة المدمجة للمصفوفة بأكملها. تنتهي الوسوم الأربعة في خلية واحدة، مفصولة بفاصلة افتراضية:

```
C#,Aspose,SmartMarker,Excel
```

### **مثال برمجي 2 — مصفوفة رقمية بفاصل مخصص**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

تدمج المصفوفات الرقمية تمامًا مثل المصفوفات النصية — يحتفظ كل عنصر بنصه الرقمي البسيط:

```
95-88-76-100-67
```

### **مثال برمجي 3 — مقارنة بين العرض الافتراضي والعرض في خلية واحدة**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

تملأ العلامة الافتراضية خلية واحدة لكل عنصر أسفل العمود B، بينما تجمع العلامة التي تستخدم `arrayassingle` المصفوفة نفسها في خلية واحدة في العمود C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في الاعتبار عند العمل مع سمتَي `arrayassingle` و`arraydelimiter`:
- تتبع قيم السمات صيغة `name:value`. لا يتم التعرف على صيغة علامة يساوي مثل `arrayassingle=true`، فيلجأ التطبيق بصمت إلى سلوك التوزيع الافتراضي.
- افصل السمات بفاصلة ودون مسافات؛ فالمسافة بعد الفاصلة تزيح قيمة الفاصل بمقدار حرف واحد، كما ورد في التحذير أعلاه.
- يمكن أن تكون قيمة `arraydelimiter` حرفًا واحدًا مكتوبًا مباشرةً بعد النقطتين، أو سلسلة متعددة الأحرف محاطة بعلامتَي اقتباس مزدوجتين.
- عند حذف `arraydelimiter`، تُدمج العناصر بفاصلة.
- يجب أن يسمح مصدر البيانات للمحرك بتعداد السجلات: اربط `List<T>` أو مجموعة أخرى يكشف نوع عنصرها خاصية المصفوفة. أما ربط كائن واحد فيترك علامات المحتوى دون حل.
- تعمل السمات نفسها مع المصفوفات النصية والرقمية؛ ويُعرض كل عنصر بنص قيمته العادي.

## المقالات ذات الصلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/net/change-page-field-layout/)
- [تحويل سباركلاين إلى صورة وHTML في Aspose.Cells for .NET](/cells/ar/net/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}