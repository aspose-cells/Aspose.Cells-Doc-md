---
title: قراءة وكتابة ملفات DBF
linktitle: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة Python عبر Java للعمل مع ملفات جداول البيانات، وتدعم قراءة وكتابة ملفات dBASE III وIV (DBF). توضح هذه المقالة كيفية استيراد البيانات من ملفات DBF وتصديرها إليها باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة وأمثلة خطوة بخطوة.
keywords: Aspose.Cells, مكتبة Python عبر Java, DBF, dBASE, قراءة DBF, كتابة DBF, استيراد DBF, تصدير DBF, تنسيق الملف, .dbf
type: docs
weight: 200
url: /ar/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells دعمًا كاملًا لقراءة ملفات DBF (dBASE) وكتابتها. يمكنك تحميل ملفات dBASE III وdBASE IV الموجودة إلى كائن Workbook، ومعالجة البيانات باستخدام واجهة Aspose.Cells API ذات الإمكانات الشاملة، ثم حفظ المصنف مجددًا بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.
{{% /alert %}}

## **مقدمة**
تنسيق DBF (ملف قاعدة بيانات) هو تنسيق ملف قديم لقواعد البيانات، ظهر أول مرة مع dBASE في مطلع الثمانينيات. على الرغم من عمر هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في كثير من الصناعات لتخزين البيانات المنظمة، ولا سيما في المحاسبة ونظم المعلومات الجغرافية (GIS) والتطبيقات المتخصصة الأخرى. يتيح Aspose.Cells إدماج هذه الملفات القديمة بسلاسة ضمن مسارات عمل جداول البيانات الحديثة عبر Python باستخدام Java.
تدعم المكتبة القراءة والكتابة لملفات DBF، مما يمنحك القدرة على:
- استيراد البيانات من ملفات DBF الحالية إلى كائنات Workbook في Aspose.Cells من أجل المعالجة الإضافية أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو عن طريق تحويل البيانات من تنسيقات جداول بيانات أخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وهياكل السجلات عند نقل البيانات من تنسيق DBF وإليه.
يمكن أيضًا فتح ملفات DBF مباشرةً في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا مريحًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات تنسيق DBF والميزات المدعومة**
يدعم Aspose.Cells إصدارات تنسيق DBF التالية:
- **dBASE III** — النوع الأصلي والأكثر دعمًا لتنسيق DBF.
- **dBASE IV** — إصدار موسع يدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة
توفر المكتبة دعمًا شاملًا للعمليات التالية:
- قراءة بيانات DBF في كائن Workbook، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مجددًا بتنسيق DBF لتصديرها إلى تطبيقات متوافقة مع dBASE.
- معالجة أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول النصية والرقمية والتاريخية والمنطقية.
- الحفاظ على تعريفات الحقول، مثل اسم الحقل ونوعه وطوله، أثناء عمليات القراءة والكتابة.

### القيود والاعتبارات
عند العمل مع ملفات DBF، ضع القيود التالية في اعتبارك:
- الحد الأقصى لعدد الحقول في كل ملف هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- تقتصر أسماء الحقول على **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق المصدر، ويكون عادةً Windows-1252 أو صفحات ترميز OEM.

## **قراءة ملف DBF**
يتيح لك Aspose.Cells تحميل البيانات بسهولة من ملف DBF إلى كائن Workbook. تستخدم المكتبة فئة `LoadOptions` لتحديد التنسيق المصدر، مما يضمن تفسير البيانات على نحو صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells
لقراءة ملف DBF، تحتاج إلى إنشاء مثيل من `LoadOptions`، وتعيين الخاصية `LoadFormat` إلى `LoadFormat.DBF`، ثم تمريرها إلى مُنشئ `Workbook` مع مسار الملف. بعد التحميل، تصبح البيانات متاحة عبر مجموعة `Worksheets`، حيث يمكنك التنقل بين الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.
يوضح المثال التالي كيفية تحميل ملف DBF موجود إلى Aspose.Cells، والوصول إلى ورقة العمل الأولى، وقراءة قيم الخلايا.

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat
dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")
loadOptions = LoadOptions(LoadFormat.DBF)
workbook = Workbook(filePath, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
sb = []
maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()
for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")
print("".join(sb))
outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.XLSX)
print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
يمكنك فتح ملفات DBF مباشرةً في Microsoft Excel بتحديد الملف في مربع حوار الفتح. سيتعامل Excel مع ملف DBF كجدول بيانات، ويعرض سجلاته في تخطيط جدولي. يكون هذا مفيدًا للتحقق بسرعة من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.
{{% /alert %}}

## **كتابة ملف DBF**
تتبع كتابة البيانات إلى ملف DBF نمطًا مماثلًا لحفظ أي تنسيق آخر لجداول البيانات باستخدام Aspose.Cells. تنشئ مصنفًا أو تحمّله، ثم تملأ ورقة العمل بالبيانات، ثم تستدعي طريقة `Save` مع تحديد `SaveFormat.DBF` كتنسيق للهدف.

### كتابة ملف DBF باستخدام Aspose.Cells
لإنشاء ملف DBF، اتبع الخطوات التالية:
1. أنشئ نسخة جديدة من `Workbook`.
2. احصل على ورقة العمل الأولى من مجموعة `Worksheets`.
3. املأ ورقة العمل ببياناتك، بما في ذلك العناوين في الصف الأول والسجلات في الصفوف التالية.
4. استدعِ طريقة `Workbook.save`، مع تمرير مسار الملف و`SaveFormat.DBF` كمعلمات.
يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. يملأ ورقة العمل ببيانات نموذجية تتضمن أنواع بيانات مختلفة، مثل السلاسل النصية والأرقام والتواريخ، لتوضيح كيفية معالجة أنواع الحقول عند التصدير إلى تنسيق DBF.

```python
import jpype
import os
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju
outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")
if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# رؤوس الأعمدة
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")
# الصف الأول من البيانات
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))
# الصف الثاني من البيانات
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))
# الصف الثالث من البيانات
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))
# الصف الرابع من البيانات
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))
# الصف الخامس من البيانات
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))
# تعيين عرض الأعمدة لتحسين القراءة
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)
workbook.save(filePath, SaveFormat.DBF)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
عند كتابة البيانات إلى ملف DBF، تأكد من توافقها مع قيود التنسيق. يجب ألا يزيد طول أسماء الحقول على 10 أحرف، ويجب ألا تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بصورة صحيحة. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.
{{% /alert %}}

## **اعتبارات أنواع البيانات والتنسيق**
عند نقل البيانات بين Aspose.Cells وتنسيق DBF، من المهم فهم كيفية مطابقة أنواع البيانات بين النظامين لضمان سلامة البيانات.

### أنواع الخلايا وأنواع حقول DBF
تُحوَّل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:
- تُحوَّل **السلاسل النصية** إلى الحقول النصية (C).
- تُحوَّل **القيم الرقمية**، بما في ذلك الأعداد الصحيحة والعشرية، إلى الحقول الرقمية (N).
- تُحوَّل **قيم التاريخ** إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- تُحوَّل **القيم المنطقية** إلى الحقول المنطقية (L).

### الترميز
قد تستخدم ملفات DBF ترميزات أحرف مختلفة وفقًا للتطبيق الذي أنشأها. يتعامل Aspose.Cells مع الترميز بسلاسة في معظم الحالات، لكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول
يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:
- الحد الأقصى للطول هو 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- تُخزن بأحرف كبيرة بغض النظر عن حالة الأحرف المستخدمة في الإدخال.

### التحقق من الناتج
بعد كتابة ملف DBF، يمكنك التحقق من النتيجة بفتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. ينبغي أن تظهر البيانات في تخطيط جدولي، مع ظهور أسماء الحقول كعناوين للأعمدة، وتكون السجلات مملوءة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**
تُعدّ تحويلات البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX أو XLS أو CSV من بين أكثر حالات الاستخدام عمليةً لقراءة ملفات DBF وكتابتها باستخدام Aspose.Cells. وبما أن Aspose.Cells يدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو تنفيذ العملية في الاتجاه المعاكس.

{{< app/cells/assistant language="python" >}}