---
title: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells .NET
linktitle: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells .NET
description: تعلم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle و ExtraDelimiter في Smart Markers مع Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template, خلية واحدة, مصفوفة
type: docs
weight: 195
url: /ar/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر Smart Markers. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.

## **المقدمة**
تُعد Smart Markers في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جدول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. توضع العلامة في مصنف المصمم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، تستبدل العلامات بقيم من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة Smart Marker إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ووضع كل عنصر في خلية منفصلة مجاورة — إما أفقيًا عبر صف أو رأسيًا عبر عمود. على الرغم من أن هذا السلوك ملائم في العديد من السيناريوهات، إلا أن هناك حالات قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج العناصر وفصلها بمحدد من اختيارك.
تعالج سمتي `ArrayAsSingle` و `ExtraDelimiter`، المستخدمتين معًا داخل علامة Smart Marker، هذا المتطلب بالتحديد. تسمحان لك بالحفاظ على تخطيطات التقارير مضغوطة وقابلة للتنبؤ مع الاستمرار في العمل أصلاً مع مصادر بيانات المصفوفات.

## **لماذا تُعد هذه الميزة ضرورية**

### **سلوك انتشار المصفوفة الافتراضي**
عندما تشير علامة Smart Marker إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة بشكل افتراضي. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` تحتوي على أربع قيم كل قيمة في خلية خاصة بها، مما يدفع محتوى القالب الآخر للخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**
توجد سيناريوهات عملية عديدة يكون فيها سلوك الانتشار الافتراضي غير مرغوب فيه:
- **تقارير بنمط الملخص** التي تحتاج إلى تخطيط مضغوط من صف واحد لكل سجل.
- **قوائم العلامات أو التسميات أو الكلمات الرئيسية** التي تحتاج إلى عرضها كقيم مفصولة بفواصل أو بخطوط عمودية داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط أنابيب المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا يستطيع بعض المستهلكين التعامل مع المصفوفات التي تنتشر عبر خلايا متعددة.

### **الفجوة التي تسدها**
بدون آلية مدمجة، سيُجبر المطورون على معالجة البيانات مسبقًا في C# أو VB.NET — دمج المصفوفات في سلاسل محددة قبل ربطها بمصمم المصنف. يؤدي ذلك إلى تكرار المنطق، وتعقيد نماذج البيانات، وزيادة فرص الأخطاء. تلغي سمتي `ArrayAsSingle` و `ExtraDelimiter` هذا الحل البديل من خلال معالجة التنسيق بشكل وصفي داخل علامة Smart Marker نفسها.

## **فوائد الميزة**
يوفر استخدام سمتي `ArrayAsSingle` و `ExtraDelimiter` في Smart Markers الخاصة بك العديد من المزايا:
- **احتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مضغوطة وقابلة للتنبؤ.
- **التحكم في المحدد المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، واصلة، خط عمودي، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القالب**: لا حاجة إلى كود إضافي لمعالجة البيانات مسبقًا؛ توجد قواعد التنسيق داخل علامة Smart Marker.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل النصية، والأرقام، والتواريخ، وأي نوع بيانات آخر يمكن ربطه بمحدد.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك الانتشار الأصلي، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة Smart Marker**
يتم تمرير سمتي `ArrayAsSingle` و `ExtraDelimiter` كأزواج مفتاح-قيمة داخل أقواس علامة Smart Marker القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — علامة Smart Marker القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المنضم.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة، أو حرفًا واحدًا، أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}
تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك المحددات متعددة الأحرف، أو النص المخصص، أو تسلسلات الهروب مثل `\n` للإخراج المفصول بأسطر جديدة. إذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.

### **سير العمل خطوة بخطوة**
يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام Smart Markers.
1. **إعداد مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن للخاصية إرجاع `string[]`، أو `int[]`، أو أي نوع مصفوفة آخر مدعوم.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية Smart Marker تشير إلى خاصية المصفوفة مع سمتي `arrayasSingle` و `extraDelimiter`.
3. **إنشاء WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصمم المصنف به، واربط مصدر البيانات باستخدام طريقة `SetDataSource`.
4. **معالجة العلامات**: استدعِ طريقة `WorkbookDesigner.Process()` لتوسيع Smart Markers وتعبئة المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف آخر مدعوم.

### **مثال الكود 1 — عرض مصفوفة السلاسل النصية الأساسي**

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

### **مثال الكود 2 — مصفوفة رقمية بمحدد مخصص**

```csharp
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
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **مثال الكود 3 — مقارنة السلوك الافتراضي مقابل ArrayAsSingle**

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
        // القسم 1: العلامة الذكية الافتراضية - القيم تنتشر أفقيًا عبر الخلايا
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // القسم 2: العرض الجديد في خلية واحدة باستخدام arrayasSingle و extraDelimiter
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
ضع النقاط التالية في الاعتبار عند العمل مع سمتي `ArrayAsSingle` و `ExtraDelimiter`:
- تُعامل قيمة `extraDelimiter` كسلسلة حرفية؛ قم بإفلات أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` تؤدي إلى سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك الانتشار الافتراضي.
- إذا كانت المصفوفة فارغة أو null، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة حسب نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات بالإضافة إلى مصادر `DataSet` و `DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بأسطر جديدة، يمكنك استخدام `\n` أو `Environment.NewLine` كقيمة المحدد.
- ضع Smart Marker في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، فقد يتجاوز المحتوى بصريًا إلى الخلايا المجاورة حسب التنسيق.
{{% /alert %}}

{{% /alert %}}

## المقالات ذات الصلة
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for .NET](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/net/change-page-field-layout/)
- [تحويل Sparkline إلى صورة و HTML في Aspose.Cells for .NET](/cells/ar/net/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}