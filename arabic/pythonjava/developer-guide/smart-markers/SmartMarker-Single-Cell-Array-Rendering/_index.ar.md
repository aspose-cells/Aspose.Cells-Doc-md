---
title: عرض مصفوفة خلية واحدة في SmartMarker | Aspose.Cells Python عبر Java
linktitle: عرض مصفوفة خلية واحدة في SmartMarker | Aspose.Cells Python عبر Java
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle و ExtraDelimiter في Smart Markers مع Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, مكتبة Python عبر Java, جدول البيانات, Smart Markers, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفة, القالب
type: docs
weight: 195
url: /ar/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر Smart Markers. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.
{{% /alert %}}

## **Introduction**
تُعد Smart Markers في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جداول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. يتم وضع العلامة في مصنف المصمم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، يتم استبدال العلامات بقيم من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة Smart Marker إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ويضع كل عنصر في خلية منفصلة مجاورة — إما أفقيًا عبر صف أو رأسيًا أسفل عمود. على الرغم من أن هذا السلوك مناسب في العديد من السيناريوهات، إلا أن هناك مواقف قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع ربط العناصر وفصلها بمحدد من اختيارك.
تعالج سمتا `ArrayAsSingle` و `ExtraDelimiter`، المستخدمتان معًا داخل علامة Smart Marker، هذا المتطلب بالتحديد. تسمحان لك بالحفاظ على تخطيطات التقارير مضغوطة وقابلة للتنبؤ مع الاستمرار في العمل أصلاً مع مصادر بيانات المصفوفات.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
عندما تشير علامة Smart Marker إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` مقابل `string[]` تحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر إلى الخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **Use Case Limitations**
توجد العديد من السيناريوهات العملية التي يكون فيها سلوك النشر الافتراضي غير مرغوب فيه:
- **تقارير بنمط الملخص** التي تحتاج إلى تخطيط مضغوط من صف واحد لكل سجل.
- **قوائم العلامات أو التسميات أو الكلمات المفتاحية** التي يجب عرضها كقيم مفصولة بفواصل أو أنابيب داخل خلية واحدة.
- **رقاقات التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر المنصات**، حيث لا يمكن لبعض المستهلكين التعامل مع المصفوفات التي تنتشر عبر خلايا متعددة.

### **The Gap It Fills**
بدون آلية مدمجة، سيكون المطورون مجبرين على معالجة البيانات مسبقًا في Python — دمج المصفوفات في سلاسل مفصولة قبل ربطها بمصمم المصنف. يضاعف هذا المنطق، ويعقد نماذج البيانات، ويزيد من فرص حدوث الأخطاء. تلغي سمتا `ArrayAsSingle` و `ExtraDelimiter` هذا الحل البديل من خلال معالجة التنسيق بشكل وصفي داخل Smart Marker نفسه.

## **Feature Benefits**
يوفر استخدام سمتي `ArrayAsSingle` و `ExtraDelimiter` في Smart Markers الخاصة بك العديد من المزايا:
- **الاحتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مضغوطة وقابلة للتنبؤ.
- **التحكم في المحدد المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، شرطة، أنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القالب**: لا يلزم وجود كود إضافي لمعالجة البيانات مسبقًا؛ توجد قواعد التنسيق داخل علامة Smart Marker.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل النصية والأرقام والتواريخ وأي نوع بيانات آخر يمكن ربطه بمحدد.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك النشر الأصلي، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **How to Use This Feature**

### **Smart Marker Syntax**
يتم تمرير سمتي `ArrayAsSingle` و `ExtraDelimiter` كأزواج مفتاح-قيمة داخل أقواس Smart Marker القياسي. الصياغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — Smart Marker القياسي الذي يشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة أو حرفًا واحدًا أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}
تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك المحددات متعددة الأحرف أو النص المخصص أو تسلسلات الهروب مثل `\n` للإخراج المفصول بسطر جديد. إذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.
{{% /alert %}}

### **Step-by-Step Workflow**
يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام Smart Markers.
1. **إعداد مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن أن تُرجع الخاصية `string[]` أو `int[]` أو أي نوع مصفوفة مدعوم آخر.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية Smart Marker تشير إلى خاصية المصفوفة مع سمتي `arrayasSingle` و `extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصنف المصمم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `set_data_source`.
4. **معالجة العلامات**: استدعِ طريقة `WorkbookDesigner.process()` لتوسيع Smart Markers وتعبئة المصنف بالبيانات الحقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف مدعوم آخر.

### **Code Example 1 — Basic String Array Rendering**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags
product = Product(["C#", "Aspose", "SmartMarker", "Excel"])
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")
designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()
workbook.save("output_arraySingle.xlsx")
jpype.shutdownJVM()
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Define Student class
class Student:
    def __init__(self):
        self.Scores = []
student = Student()
student.Scores = [95, 88, 76, 100, 67]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))
workbook.save("output_numericArray.xlsx")
jpype.shutdownJVM()
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
# Define the data source as a dictionary (equivalent to the Order class)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Section 1: Default Smart Marker - values spread horizontally across cells
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")
# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")
# Bind the data source and process Smart Markers
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()
# Save the resulting workbook
workbook.save("output_comparison.xlsx")
jpype.shutdownJVM()
```

### **Notes & Best Practices**
ضع النقاط التالية في اعتبارك عند العمل مع سمتي `ArrayAsSingle` و `ExtraDelimiter`:
- تُعامل قيمة `extraDelimiter` على أنها سلسلة حرفية؛ قم بإفلات أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` يؤدي إلى سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك النشر الافتراضي.
- إذا كانت المصفوفة فارغة أو null، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة اعتمادًا على نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات بالإضافة إلى مصادر `DataSet` و `DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للحصول على إخراج مفصول بسطر جديد، يمكنك استخدام `\n` أو ثابت سطر الجديد الخاص بالمنصة كقيمة للمحدد.
- ضع Smart Marker في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، قد يتجاوز المحتوى بصريًا إلى الخلايا المجاورة اعتمادًا على التنسيق.

## Related Articles
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Python عبر Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python عبر Java](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/python-java/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python عبر Java](/cells/ar/python-java/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}