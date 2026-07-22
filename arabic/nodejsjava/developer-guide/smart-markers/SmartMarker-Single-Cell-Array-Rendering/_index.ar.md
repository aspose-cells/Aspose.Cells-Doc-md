---
title: عرض مصفوفة خلية واحدة لـ SmartMarker | Aspose.Cells for Node.js via Java
linktitle: عرض مصفوفة خلية واحدة لـ SmartMarker | Aspose.Cells
description: تعلم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمات ArrayAsSingle و ExtraDelimiter في علامات Smart مع Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, مكتبة Node.js via Java, جدول بيانات, علامات Smart, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
url: /ar/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر علامات Smart. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.

{{% /alert %}}

## **المقدمة**

تعد علامات Smart في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جدول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. يتم وضع العلامة في مصنف المصمم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، يتم استبدال العلامات بقيم من مصدر البيانات المقدم.

افتراضيًا، عندما تشير علامة Smart إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ووضع كل عنصر في خلية مجاورة منفصلة - إما أفقيًا عبر صف أو رأسيًا لأسفل عمود. على الرغم من أن هذا السلوك مناسب في العديد من السيناريوهات، إلا أن هناك مواقف قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع ربط العناصر وفصلها بفاصل من اختيارك.

تلبى سمات `ArrayAsSingle` و `ExtraDelimiter`، المستخدمة معًا داخل علامة Smart، هذا المتطلب بالتحديد. تتيح لك الحفاظ على تخطيطات التقارير مدمجة وقابلة للتنبؤ مع الاستمرار في العمل بشكل أصلي مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك انتشار المصفوفة الافتراضي**

عندما تشير علامة Smart إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` تحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر للخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

هناك العديد من السيناريوهات العملية حيث يكون سلوك الانتشار الافتراضي غير مرغوب فيه:

- **تقارير بأسلوب الملخص** التي تحتاج إلى تخطيط مدمج من صف واحد لكل سجل.
- **قوائم العلامات أو التسميات أو الكلمات الرئيسية** التي تحتاج إلى عرضها كقيم مفصولة بفواصل أو أنابيب داخل خلية واحدة.
- **شرائح التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط أنابيب المصب** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا يمكن لبعض المستهلكين تحمل المصفوفات التي تنتشر عبر خلايا متعددة.

### **الفجوة التي تملأها**

بدون آلية مدمجة، سيكون المطورون مجبرين على معالجة البيانات مسبقًا في JavaScript - ربط المصفوفات في سلاسل مفصولة قبل ربطها بمصمم المصنف. يؤدي هذا إلى تكرار المنطق، وتعقيد نماذج البيانات، وزيادة فرصة الأخطاء. تقضي سمات `ArrayAsSingle` و `ExtraDelimiter` على هذا الحل البديل من خلال التعامل مع التنسيق بشكل وصفي داخل علامة Smart نفسها.

## **فوائد الميزة**

يوفر استخدام سمات `ArrayAsSingle` و `ExtraDelimiter` في علامات Smart الخاصة بك العديد من المزايا:

- **الاحتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مدمجة وقابلة للتنبؤ.
- **التحكم في الفاصل المخصص**: حدد أي سلسلة فاصل تريدها - فاصلة، فاصلة منقوطة، واصلة، أنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القوالب**: لا حاجة إلى كود إضافي لمعالجة البيانات مسبقًا؛ تعيش قواعد التنسيق داخل علامة Smart.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل والأرقام والتواريخ وأي نوع بيانات آخر يمكن ربطه بفاصل.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك الانتشار الأصلي، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة علامة Smart**

يتم تمرير سمات `ArrayAsSingle` و `ExtraDelimiter` كأزواج قيمة-مفتاح داخل أقواس علامة Smart القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:

- `&=DataSource.ArrayProperty` — علامة Smart القياسية التي تشير إلى خاصية المصفوفة على مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى تشغيل سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة أو حرفًا واحدًا أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}

تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك الفواصل متعددة الأحرف أو النص المخصص أو تسلسلات الهروب مثل `\n` للإخراج المفصول بسطر جديد. إذا كانت المصفوفة فارغة، فستترك الخلية الناتجة فارغة.

{{% /alert %}}

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام علامات Smart.

1. **إعداد مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن للخاصية إرجاع `string[]` أو `int[]` أو أي نوع مصفوفة آخر مدعوم.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية علامة Smart تشير إلى خاصية المصفوفة بسمات `arrayasSingle` و `extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصنف المصمم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `setDataSource`.
4. **معالجة العلامات**: اتصل بطريقة `workbookDesigner.process()` لتوسيع علامات Smart وتعبئة المصنف بالبيانات الحقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف مدعوم آخر.

### **مثال الكود 1 — عرض مصفوفة سلسلة أساسية**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **مثال الكود 2 — مصفوفة رقمية بفاصل مخصص**

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

### **مثال الكود 3 — مقارنة السلوك الافتراضي مقابل سلوك ArrayAsSingle**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // القسم 1: العلامة الذكية الافتراضية - يتم توزيع القيم أفقيًا عبر الخلايا
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // القسم 2: العرض الجديد في خلية واحدة باستخدام arrayasSingle و extraDelimiter
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // ربط مصدر البيانات ومعالجة العلامات الذكية
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // حفظ المصنف الناتج
    workbook.save("output_comparison.xlsx");
}

main();
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في الاعتبار عند العمل مع سمات `ArrayAsSingle` و `ExtraDelimiter`:

- تُعامل قيمة `extraDelimiter` كسلسلة حرفية؛ ضع أحرف هروب لأي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` تؤدي إلى تشغيل سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك الانتشار الافتراضي.
- إذا كانت المصفوفة فارغة أو null، فستترك الخلية فارغة (أو تحتوي على سلسلة فارغة اعتمادًا على نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات بالإضافة إلى مصادر `DataSet` و `DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بسطر جديد، يمكنك استخدام `\n` كقيمة الفاصل.
- ضع علامة Smart في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، فقد يفيض المحتوى بصريًا إلى الخلايا المجاورة اعتمادًا على التنسيق.



{{< app/cells/assistant language="javascript" >}}