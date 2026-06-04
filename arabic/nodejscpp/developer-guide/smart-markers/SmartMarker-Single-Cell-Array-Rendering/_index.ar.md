---
title: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells for Node.js via C++
description: تعرف على كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمات ArrayAsSingle و ExtraDelimiter في Smart Markers مع Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, مكتبة Node.js, جدول بيانات, Smart Markers, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
url: /ar/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر Smart Markers. باستخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.

{{% /alert %}}

## **المقدمة**

تُعد Smart Markers في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك ملء بيانات جدول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. يتم وضع العلامة في مصنف المصمم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، يتم استبدال العلامات بقيم من مصدر البيانات المقدم.

افتراضيًا، عندما تشير علامة Smart Marker إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ووضع كل عنصر في خلية منفصلة مجاورة — إما أفقيًا عبر صف أو عموديًا لأسفل عمود. على الرغم من أن هذا السلوك مناسب في العديد من السيناريوهات، إلا أن هناك مواقف قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع ربط العناصر وفصلها بفاصل من اختيارك.

تعالج سمات `ArrayAsSingle` و `ExtraDelimiter`، المستخدمة معًا داخل علامة Smart Marker، هذا المتطلب بالتحديد. فهي تسمح لك بالحفاظ على تخطيطات التقارير مضغوطة ويمكن التنبؤ بها مع الاستمرار في العمل بشكل أصلي مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك انتشار المصفوفة الافتراضي**

عندما تشير علامة Smart Marker إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` تحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر إلى الخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

هناك العديد من السيناريوهات العملية التي يكون فيها سلوك الانتشار الافتراضي غير مرغوب فيه:

- **تقارير بنمط الملخص** التي تحتاج إلى تخطيط مضغوط بسجل واحد لكل صف.
- **قوائم العلامات أو التسميات أو الكلمات المفتاحية** التي تحتاج إلى عرضها كقيم مفصولة بفواصل أو أنابيب داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط أنابيب المصب** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا يمكن لبعض المستهلكين تحمل المصفوفات التي تنتشر عبر خلايا متعددة.

### **الفجوة التي تسدها**

بدون آلية مدمجة، سيكون المطورون مجبرين على معالجة البيانات مسبقًا في JavaScript — دمج المصفوفات في سلاسل مفصولة قبل ربطها بمصمم المصنف. يكرر هذا المنطق، ويعقد نماذج البيانات، ويزيد من فرص الأخطاء. تلغي سمات `ArrayAsSingle` و `ExtraDelimiter` هذا الحل البديل من خلال معالجة التنسيق بشكل وصفي داخل Smart Marker نفسه.

## **فوائد الميزة**

يوفر استخدام سمات `ArrayAsSingle` و `ExtraDelimiter` في Smart Markers عدة مزايا:

- **احتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مضغوطة ويمكن التنبؤ بها.
- **التحكم في الفاصل المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، واصلة، أنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القوالب**: لا يلزم كود إضافي لمعالجة البيانات مسبقًا؛ تعيش قواعد التنسيق داخل علامة Smart Marker.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: يعمل مع السلاسل والأرقام والتواريخ وأي نوع بيانات آخر يمكن دمجه مع فاصل.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك الانتشار الأصلي، لذا تستمر القوالب الموجودة في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة Smart Marker**

يتم تمرير سمات `ArrayAsSingle` و `ExtraDelimiter` كأزواج قيمة-مفتاح داخل أقواس Smart Marker القياسي. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:

- `&=DataSource.ArrayProperty` — Smart Marker القياسي الذي يشير إلى خاصية المصفوفة على مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة، أو حرفًا واحدًا، أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}

تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك فواصل متعددة الأحرف، أو نص مخصص، أو تسلسلات هروب مثل `\n` للإخراج المفصول بسطر جديد. إذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.

{{% /alert %}}

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام Smart Markers.

1. **تحضير مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن للخاصية إرجاع `string[]`، أو `int[]`، أو أي نوع مصفوفة آخر مدعوم.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية Smart Marker تشير إلى خاصية المصفوفة مع سمات `arrayasSingle` و `extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصنف المصمم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `setDataSource`.
4. **معالجة العلامات**: استدعِ طريقة `workbookDesigner.process()` لتوسيع Smart Markers وملء المصنف ببيانات حقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف آخر مدعوم.

### **مثال الكود 1 — عرض مصفوفة سلاسل أساسية**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **مثال الكود 2 — مصفوفة رقمية مع فاصل مخصص**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **مثال الكود 3 — مقارنة السلوك الافتراضي بسلوك ArrayAsSingle**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// القسم 1: العلامة الذكية الافتراضية - تنتشر القيم أفقياً عبر الخلايا
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// القسم 2: عرض خلية واحدة جديد باستخدام arrayasSingle و extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// ربط مصدر البيانات ومعالجة العلامات الذكية
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// حفظ المصنف الناتج
workbook.save("output_comparison.xlsx");
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في اعتبارك عند العمل مع سمات `ArrayAsSingle` و `ExtraDelimiter`:

- تُعامل قيمة `extraDelimiter` كسلسلة حرفية؛ قم بإلغاء تأثير أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` يؤدي إلى سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك الانتشار الافتراضي.
- إذا كانت المصفوفة فارغة أو null، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة اعتمادًا على نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات وكذلك مصادر `DataSet` و `DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بسطر جديد، يمكنك استخدام `\n` أو `os.EOL` كقيمة فاصل.
- ضع Smart Marker في خلية ذات عرض كافٍ لعرض السلسلة المدمجة الناتجة؛ وإلا، قد يتجاوز المحتوى بصريًا إلى الخلايا المجاورة اعتمادًا على التنسيق.

## **مقالات ذات صلة**

- [دمج وإلغاء دمج الخلايا](/cells/ar/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}