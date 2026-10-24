---
title: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells for Python via .NET
linktitle: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells for Python via .NET
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle وExtraDelimiter في العلامات الذكية مع Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, مكتبة Python عبر .NET, جداول البيانات, العلامات الذكية, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفة, القوالب
type: docs
weight: 195
url: /ar/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر العلامات الذكية. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.
{{% /alert %}}

## **Introduction**
تعد العلامات الذكية في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جداول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. توضع العلامة في مصنف المصمم، وعندما يقوم `WorkbookDesigner` بمعالجة القالب، يتم استبدال العلامات بقيم من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ويضع كل عنصر في خلية منفصلة متجاورة — سواء أفقيًا عبر صف أو عموديًا لأسفل عمود. في حين أن هذا السلوك مناسب في العديد من السيناريوهات، إلا أن هناك مواقف قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج العناصر وفصلها بفاصل من اختيارك.
تعالج سمتا `ArrayAsSingle` و`ExtraDelimiter`، المستخدمتان معًا داخل وسم علامة ذكية، هذا المتطلب بالتحديد. تسمحان لك بالحفاظ على تخطيطات التقارير مدمجة ويمكن التنبؤ بها مع الاستمرار في العمل بشكل أصلي مع مصادر بيانات المصفوفات.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
عندما تشير علامة ذكية إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` يحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر إلى الخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **Use Case Limitations**
هناك العديد من السيناريوهات العملية التي يكون فيها سلوك الانتشار الافتراضي غير مرغوب فيه:
- **تقارير بأسلوب الملخص** التي تحتاج إلى تخطيط مدمج بصف واحد لكل سجل.
- **قوائم الوسوم أو التصنيفات أو الكلمات المفتاحية** التي تحتاج إلى عرضها كقيم مفصولة بفواصل أو أنابيب داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر المنصات**، حيث لا يمكن لبعض المستهلكين التعامل مع المصفوفات التي تنتشر عبر خلايا متعددة.

### **The Gap It Fills**
بدون آلية مدمجة، سيُجبر المطورون على معالجة البيانات مسبقًا في Python — دمج المصفوفات في سلاسل نصية مفصولة قبل ربطها بمصمم المصنف. يؤدي هذا إلى تكرار المنطق، وتعقيد نماذج البيانات، وزيادة احتمال الأخطاء. تلغي سمتا `ArrayAsSingle` و`ExtraDelimiter` هذا الحل البديل من خلال معالجة التنسيق بشكل وصفي داخل العلامة الذكية نفسها.

## **Feature Benefits**
يوفر استخدام سمتي `ArrayAsSingle` و`ExtraDelimiter` في العلامات الذكية العديد من المزايا:
- **احتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مدمجة ويمكن التنبؤ بها.
- **التحكم في الفاصل المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، شرطة، أنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القوالب**: لا حاجة إلى كود إضافي لمعالجة البيانات مسبقًا؛ توجد قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل النصية والأرقام والتواريخ وأي نوع بيانات آخر يمكن دمجه مع فاصل.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك الانتشار الأصلي، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **How to Use This Feature**

### **Smart Marker Syntax**
يتم تمرير سمتي `ArrayAsSingle` و`ExtraDelimiter` كأزواج مفتاح-قيمة داخل أقواس علامة ذكية قياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة أو حرفًا واحدًا أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}
تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك الفواصل متعددة الأحرف أو النص المخصص أو تسلسلات الهروب مثل `\n` للإخراج المفصول بسطر جديد. إذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.
{{% /alert %}}

### **Step-by-Step Workflow**
يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تجهيز مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن للخاصية إرجاع `list[str]` أو `list[int]` أو أي نوع مصفوفة مدعوم آخر.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف ترويسة، وضع خلية علامة ذكية تشير إلى خاصية المصفوفة مع سمتي `arrayasSingle` و`extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، واربط مصنف المصمم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `set_data_source`.
4. **معالجة العلامات**: استدعِ طريقة `WorkbookDesigner.process()` لتوسيع العلامات الذكية وتعبئة المصنف ببيانات حقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف آخر مدعوم.

### **Code Example 1 — Basic String Array Rendering**

```python
import aspose.cells as ac
class Product:
    def __init__(self):
        self.Tags = []
product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")
designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()
workbook.save("output_arraySingle.xlsx")
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```python
import aspose.cells as ac
class Student:
    def __init__(self):
        self.scores = []
student = Student()
student.scores = [95, 88, 76, 100, 67]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
worksheet.cells.get("A2").put_value(" - ".join(str(s) for s in student.scores))
workbook.save("output_numericArray.xlsx")
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```python
import aspose.cells as ac
class Order:
    def __init__(self, items):
        self._items = items
    @property
    def Items(self):
        return self._items
    @Items.setter
    def Items(self, value):
        self._items = value
order = Order(["Apple", "Banana", "Cherry", "Date"])
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Section 1: Default Smart Marker - values spread horizontally across cells
cells.get("A1").put_value("Default Spreading Behavior:")
cells.get("A2").put_value("&=Order.Items")
# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").put_value("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')
# Bind the data source and process Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()
# Save the resulting workbook
workbook.save("output_comparison.xlsx")
```

### **Notes & Best Practices**
ضع النقاط التالية في اعتبارك عند العمل مع سمتي `ArrayAsSingle` و`ExtraDelimiter`:
- تُعامل قيمة `extraDelimiter` كسلسلة حرفية؛ قم بإفلات أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`True` / `False`). فقط `True` تؤدي إلى سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك الانتشار الافتراضي.
- إذا كانت المصفوفة فارغة أو لا شيء، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة حسب نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات وكذلك مصادر `DataSet` و`DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بسطر جديد، يمكنك استخدام `\n` أو `os.linesep` كقيمة فاصل.
- ضع العلامة الذكية في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، قد يفيض المحتوى بصريًا إلى الخلايا المجاورة حسب التنسيق.

## Related Articles
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Python via .NET](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via .NET](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/python-net/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python via .NET](/cells/ar/python-net/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}