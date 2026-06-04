---
title: عرض مصفوفة خلية واحدة في SmartMarker | Aspose.Cells .NET
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle وExtraDelimiter في العلامات الذكية مع Aspose.Cells لـ .NET.
keywords: Aspose.Cells, مكتبة .NET, جدول بيانات, علامات ذكية, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفات, قالب
type: docs
weight: 195
url: /ar/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر العلامات الذكية. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.

{{% /alert %}}

## **المقدمة**

تعد العلامات الذكية في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جداول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. يتم وضع العلامة في مصنف التصميم، وعندما يقوم `WorkbookDesigner` بمعالجة القالب، يتم استبدال العلامات بقيم من مصدر البيانات المقدم.

افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، فإن المحرك يوسع المصفوفة ويضع كل عنصر في خلية منفصلة متجاورة — إما أفقيًا عبر صف أو رأسيًا على طول عمود. على الرغم من أن هذا السلوك مناسب في العديد من السيناريوهات، إلا أن هناك حالات قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع تسلسل العناصر وفصلها بواسطة فاصل من اختيارك.

تعالج سمتي `ArrayAsSingle` و`ExtraDelimiter`، المستخدمتين معًا داخل علامة ذكية، هذا المتطلب بالتحديد. تسمحان لك بالحفاظ على تخطيطات التقارير مدمجة ويمكن التنبؤ بها مع الاستمرار في العمل أصلاً مع مصادر بيانات المصفوفات.

## **سبب الحاجة إلى هذه الميزة**

### **سلوك انتشار المصفوفة الافتراضي**

عندما تشير علامة ذكية إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` يحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر للخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

هناك العديد من السيناريوهات العملية التي يكون فيها سلوك الانتشار الافتراضي غير مرغوب فيه:

- **تقارير بنمط الملخص** التي تحتاج إلى تخطيط مدمج من صف واحد لكل سجل.
- **قوائم العلامات أو التسميات أو الكلمات المفتاحية** التي تحتاج إلى عرضها كقيم مفصولة بفاصلات أو أنابيب داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا يمكن لبعض المستهلكين تحمل المصفوفات التي تنتشر عبر خلايا متعددة.

### **الفجوة التي تسدها**

بدون آلية مدمجة، سيُجبر المطورون على معالجة البيانات مسبقًا في C# أو VB.NET — ضم المصفوفات في سلاسل مفصولة قبل ربطها بمصمم المصنف. هذا يضاعف المنطق، ويعقد نماذج البيانات، ويزيد من احتمال الأخطاء. تلغي سمتي `ArrayAsSingle` و`ExtraDelimiter` هذا الحل البديل من خلال التعامل مع التنسيق بشكل تصريحي داخل العلامة الذكية نفسها.

## **فوائد الميزة**

يوفر استخدام سمتي `ArrayAsSingle` و`ExtraDelimiter` في العلامات الذكية العديد من المزايا:

- **احتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مدمجة ويمكن التنبؤ بها.
- **التحكم في الفاصل المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، شرطة، أنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القالب**: لا يلزم وجود كود إضافي لمعالجة البيانات مسبقًا؛ تعيش قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل والأرقام والتواريخ وأي نوع بيانات آخر يمكن ضمه بفاصل.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك الانتشار الأصلي، لذلك تستمر القوالب الموجودة في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة العلامة الذكية**

يتم تمرير سمتي `ArrayAsSingle` و`ExtraDelimiter` كأزواج مفتاح-قيمة داخل أقواس العلامة الذكية القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:

- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى تشغيل سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة أو حرفًا واحدًا أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}

تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك الفواصل متعددة الأحرف أو النص المخصص أو تسلسلات الهروب مثل `\n` للإخراج المفصول بأسطر جديدة. إذا كانت المصفوفة فارغة، فستترك الخلية الناتجة فارغة.

{{% /alert %}}

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.

1. **تحضير مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن للخاصية إرجاع `string[]` أو `int[]` أو أي نوع مصفوفة مدعوم آخر.
2. **إنشاء مصنف التصميم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية علامة ذكية تشير إلى خاصية المصفوفة بسمتي `arrayasSingle` و`extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، واربط مصنف التصميم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `SetDataSource`.
4. **معالجة العلامات**: استدعِ طريقة `WorkbookDesigner.Process()` لتوسيع العلامات الذكية وتعبئة المصنف بالبيانات الحقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي صيغة ملف مدعومة أخرى.

### **مثال على الكود 1 — عرض مصفوفة سلسلة أساسية**

```csharp
using System;
using Aspose.Cells;

class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }

    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();

        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **مثال على الكود 2 — مصفوفة رقمية بفاصل مخصص**

```csharp
using System;
using Aspose.Cells;

public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

        var designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Student", student);
        designer.Process();

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **مثال على الكود 3 — مقارنة السلوك الافتراضي بسلوك ArrayAsSingle**

```csharp
using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // القسم 1: العلامة الذكية الافتراضية - القيم تنتشر أفقياً عبر الخلايا
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // القسم 2: عرض الخلية الواحدة الجديد باستخدام arrayasSingle و extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // ربط مصدر البيانات ومعالجة العلامات الذكية
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // حفظ المصنف الناتج
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في اعتبارك عند العمل مع سمتي `ArrayAsSingle` و`ExtraDelimiter`:

- يتم التعامل مع قيمة `extraDelimiter` كسلسلة حرفية؛ قم بتهرب من أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` تؤدي إلى تشغيل سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك الانتشار الافتراضي.
- إذا كانت المصفوفة فارغة أو null، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة اعتمادًا على نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات بالإضافة إلى مصادر `DataSet` و`DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بأسطر جديدة، يمكنك استخدام `\n` أو `Environment.NewLine` كقيمة فاصل.
- ضع العلامة الذكية في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، قد يفيض المحتوى بصريًا إلى الخلايا المجاورة اعتمادًا على التنسيق.

## **مقالات ذات صلة**

- [العلامات الذكية](/cells/ar/net/smart-markers/)
- [دمج الخلايا وفك دمجها](/cells/ar/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}