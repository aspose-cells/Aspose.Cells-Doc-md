---
title: عرض مصفوفة خلية واحدة باستخدام SmartMarker | Aspose.Cells Java
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمات arrayassingle وarraydelimiter للعلامة الذكية في Aspose.Cells for Java.
linktitle: عرض مصفوفة خلية واحدة باستخدام SmartMarker | Aspose.Cells
url: /ar/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, مكتبة Java, جدول بيانات, العلامات الذكية, arrayassingle, arraydelimiter, مصفوفة خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يمكن لـ Aspose.Cells عرض مصدر بيانات من نوع مصفوفة في خلية واحدة من خلال العلامات الذكية. تعطّل السمة `arrayassingle` التوزيع الافتراضي عنصرًا تلو الآخر، وتحدّد السمة `arraydelimiter` الفاصل الموضوع بين العناصر المدمجة — الفاصلة افتراضيًا، أو أي حرف واحد أو سلسلة متعددة الأحرف بين علامتَي اقتباس تحدّدها.
{{% /alert %}}

## **مقدمة**

العلامات الذكية في Aspose.Cells هي ميزة قائمة على القوالب تملأ بيانات جدول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. تُوضع العلامة في مصنف مصمم، وعندما يعالج `WorkbookDesigner` القالب، تُستبدل العلامات بالقيم من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة (على سبيل المثال، `&=Product.Tags` مرتبطة بمصفوفة `String[]` تضم أربع قيم)، يوسّع المحرك المصفوفة ويضع كل عنصر في خلية خاصة به، موزعًا القيم عموديًا داخل العمود الموجود أسفل العلامة. ورغم أن هذا السلوك مريح في سيناريوهات كثيرة، هناك حالات تفضّل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج عناصرها وفصلها بفاصل تختاره.
تلبّي السمتان `arrayassingle` و`arraydelimiter`، المكتوبتان داخل أقواس العلامة الذكية بصيغة `name:value`، هذا المتطلب تحديدًا. تتيحان لك إبقاء تخطيطات التقارير مضغوطة ومتوقعة مع الاستمرار في العمل أصلًا مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك توزيع المصفوفات الافتراضي**

عندما تشير علامة ذكية إلى خاصية مصفوفة، يوسّع Aspose.Cells المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، توضع علامة مثل `&=Product.Tags` مقابل `String[]` تحتوي على أربع قيم في خلية خاصة بكل قيمة أسفل العلامة، مما يدفع بقية محتوى القالب إلى الخارج وقد يعطّل تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

توجد العديد من السيناريوهات العملية التي يكون فيها سلوك التوزيع الافتراضي غير مرغوب فيه:
- **تقارير بأسلوب الملخصات** التي تحتاج إلى تخطيط مضغوط بصف واحد لكل سجل.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية** التي يلزم عرضها كقيم مفصولة بفواصل أو بالشرطة العمودية داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في موضع واحد لتسهيل القراءة.
- **خطوط المعالجة التالية** (تصدير CSV، وعرض PDF، ودمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلًا من نطاق موسَّع.
- **التوافق عبر المنصات**، حيث لا تتحمل بعض الجهات المستهلكة المصفوفات التي تمتد عبر خلايا متعددة.

### **الفجوة التي تسدّها**

بدون آلية مدمجة، سيضطر المطوّرون إلى المعالجة المسبقة للبيانات في Java — أي دمج المصفوفات في نصوص مفصولة قبل ربطها بمصمم المصنف. وهذا يكرر المنطق، ويضيف تعقيدًا إلى نماذج البيانات، ويزيد احتمال وقوع الأخطاء. تزيل السمتان `arrayassingle` و`arraydelimiter` الحاجة إلى هذا النهج الالتفافي عبر التعامل مع التنسيق بشكل تصريحي داخل العلامة الذكية نفسها.

## **مزايا الميزة**

يوفر استخدام السمتين `arrayassingle` و`arraydelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء في خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على تخطيطات مضغوطة ومتوقعة.
- **التحكم في الفاصل المخصص**: حدد الفاصل الذي تفضّله — الفاصلة الافتراضية، أو فاصلة منقوطة، أو شرطة، أو شرطة عمودية، أو نص متعدد الأحرف بين علامتَي اقتباس مثل `" | "`.
- **التنسيق المبني على القالب**: لا يلزم أي رمز إضافي للمعالجة المسبقة للبيانات؛ reside قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات مرنة**: يعمل مع مصفوفات النصوص والقيم الرقمية المعروضة كنصوص من مصادر بيانات JavaBean.
- **التوافق الخلفي**: عند حذف السمتين، يبقى سلوك التوزيع الأصلي كما هو، لذا تواصل القوالب الحالية العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صياغة العلامة الذكية**

تستخدم السمتان `arrayassingle` و`arraydelimiter` قواعد السمات `name:value` الخاصة بـ Aspose.Cells داخل أقواس العلامة الذكية القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayassingle:true` — يوجّه المحرك إلى عرض المصفوفة بالكامل في خلية واحدة بدلًا من توزيع عناصرها.
- `arraydelimiter:;` — اختيارية؛ تحدد الفاصل الموضوع بين عناصر المصفوفة. وعند حذفها، تُستخدم الفاصلة.

{{% alert color="warning" %}}
اكتب السمات بصيغة `name:value` (نقطتان، لا علامة يساوي) وافصل بين السمات المتعددة بفاصلة **من دون مسافات**. إن أضفت مسافة بعد الفاصلة، ستتغير القيمة المحلَّلة بمقدار حرف واحد — فسيؤدي `(arrayassingle:true, arraydelimiter:;)` إلى الدمج باستخدام الفاصل الخاطئ `:;` بدلًا من `;`.
{{% /alert %}}

### **أشكال الفاصل**

- يتبع النقطتين حرف واحد مباشرة: `arraydelimiter:;`، `arraydelimiter:-`، `arraydelimiter:*`.
- يُكتب الفاصل متعدد الأحرف بين علامتَي اقتباس مزدوجتين: `arraydelimiter:" | "`، `arraydelimiter:" - "`.

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **جهّز مصدر البيانات**: أنشئ صنف JavaBean مع دالة وصول تُرجع المصفوفة، مثل `String[] getTags()`، واربط قائمة `java.util.List` من كائنات JavaBean بحيث يقرأ المحرك سجلًا واحدًا لكل صف. الحقول العامة وحدها لا تُربط — يقرأ المحرك دوال الوصول في JavaBean.
2. **أنشئ مصنفًا مصممًا**: أنشئ كائن `Workbook` جديدًا، وأضف صف عنوان، وضع خلية علامة ذكية تشير إلى خاصية المصفوفة مع السمة `arrayassingle` (و`arraydelimiter` عند الحاجة إلى فاصل مخصص).
3. **أنشئ WorkbookDesigner**: أنشئ كائن `WorkbookDesigner` حول المصنف واربط قائمتك باستخدام `setDataSource`.
4. **عالج العلامات**: استدعِ الأسلوب `WorkbookDesigner.process()` لتوسيع العلامات الذكية وملء المصنف بالبيانات الفعلية.
5. **احفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي تنسيق ملف مدعوم آخر.

### **مثال الشيفرة 1 — العرض الأساسي لمصفوفة نصوص**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

يطبع المثال القيمة المدمجة للمصفوفة بأكملها. تقع الوسوم الأربعة في خلية واحدة مفصولة بفاصلة افتراضية:

```
C#,Aspose,SmartMarker,Excel
```

### **مثال الشيفرة 2 — القيم الرقمية مع فاصل مخصص**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

تدمج القيم الرقمية تمامًا مثل النصوص عندما تُرجع خاصية المصفوفة `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
اجعل خاصية المصفوفة من النوع `String[]` في Java. فعند دمج خاصية من النوع الأولي `int[]` في خلية واحدة، يُعرض النص الناتج عن toString لكائن المصفوفة (مثل `[I@1a2b3c4d`) بدلًا من الأرقام، لأن عملية الدمج تعمل على الصيغة النصية لكل عنصر وتعد المصفوفة الأولية عنصرًا واحدًا غير شفاف.
{{% /alert %}}

### **مثال الشيفرة 3 — مقارنة العرض الافتراضي بالعرض في خلية واحدة**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

تملأ العلامة الافتراضية خلية واحدة لكل عنصر في العمود B، بينما تجمع علامة `arrayassingle` المصفوفة نفسها في خلية واحدة في العمود C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في الاعتبار عند العمل مع السمتين `arrayassingle` و`arraydelimiter`:
- تستخدم قيم السمات صيغة `name:value`. ولا يتعرف النظام على صيغة علامة يساوي مثل `arrayassingle=true`، فيلجأ بهدوء إلى سلوك التوزيع الافتراضي.
- افصل بين السمات بفاصلة ودون مسافات؛ فالمسافة بعد الفاصلة تغيّر قيمة الفاصل بمقدار حرف واحد (راجع التحذير أعلاه).
- قد تكون قيمة `arraydelimiter` حرفًا واحدًا يُكتب مباشرة بعد النقطتين، أو نصًا متعدد الأحرف ملفوفًا بعلامتَي اقتباس مزدوجتين.
- عند حذف `arraydelimiter`، تُدمج العناصر بفاصلة.
- اربط قائمة `java.util.List` من كائنات JavaBean العامة التي تحتوي على دوال وصول تُرجع مصفوفات. فكائن JavaBean منفرد أو الحقول العامة وحدها يتركان العلامات غير محلولة.
- احتفظ بخصائص المصفوفات من النوع `String[]`؛ فالمصفوفة الأولية `int[]` تعرض نص toString الخاص بها عند الدمج (راجع الملاحظة أعلاه).
- ضع العلامة الذكية في خلية ذات عرض كافٍ لعرض النص المدمج الناتج؛ وإلا، فقد يفيض المحتوى بصريًا إلى الخلايا المجاورة بحسب تنسيق الملف.

## المقالات ذات الصلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Java](/cells/ar/java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Java](/cells/ar/java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/java/change-page-field-layout/)
- [تحويل الخط المصغر إلى صورة وHTML في Aspose.Cells for Java](/cells/ar/java/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}