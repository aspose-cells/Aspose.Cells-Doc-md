---
title: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة لـ Python عبر .NET للعمل مع ملفات جداول البيانات، تدعم قراءة وكتابة ملفات dBASE III و IV (DBF). تشرح هذه المقالة كيفية استيراد البيانات من وتصدير البيانات إلى ملفات DBF باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة وأمثلة خطوة بخطوة.
keywords: Aspose.Cells, Python via .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ar/python-net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

توفر Aspose.Cells دعمًا كاملاً لقراءة وكتابة ملفات DBF (dBASE). يمكنك تحميل ملفات dBASE III و dBASE IV الموجودة في كائن Workbook، ومعالجة البيانات باستخدام واجهة برمجة التطبيقات الغنية لـ Aspose.Cells، ثم حفظ المصنف مرة أخرى بتنسيق DBF للاستخدام مع تطبيقات قواعد البيانات القديمة.

{{% /alert %}}

## **مقدمة**

DBF (ملف قاعدة البيانات) هو تنسيق ملف قاعدة بيانات قديم تم تقديمه في الأصل بواسطة dBASE في أوائل الثمانينيات. على الرغم من قدم هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في العديد من الصناعات لتخزين البيانات المنظمة، لا سيما في المحاسبة ونظم المعلومات الجغرافية والتطبيقات المتخصصة الأخرى. تتيح لك Aspose.Cells دمج هذه الملفات القديمة في سير عمل جداول البيانات الحديثة لـ Python عبر .NET بسلاسة.

تدعم المكتبة كلاً من قراءة وكتابة ملفات DBF، مما يمنحك القدرة على:

- استيراد البيانات من ملفات DBF الموجودة إلى كائنات Workbook الخاصة بـ Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من البداية أو عن طريق تحويل البيانات من تنسيقات جداول بيانات أخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وهياكل السجلات عند نقل البيانات من وإلى تنسيق DBF.

يمكن أيضًا فتح ملفات DBF مباشرة في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا مناسبًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات وميزات DBF المدعومة**

تدعم Aspose.Cells إصدارات تنسيق DBF التالية:

- **dBASE III** — النسخة الأصلية والأكثر دعمًا على نطاق واسع من تنسيق DBF.
- **dBASE IV** — نسخة موسعة تدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة

توفر المكتبة دعمًا شاملاً للعمليات التالية:

- قراءة بيانات DBF في كائن Workbook، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مرة أخرى بتنسيق DBF للتصدير إلى التطبيقات المتوافقة مع dBASE.
- التعامل مع أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول النصية والرقمية والتاريخ والمنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة/الكتابة.

### القيود والاعتبارات

عند العمل مع ملفات DBF، يجب مراعاة القيود التالية:

- الحد الأقصى لعدد الحقول في الملف الواحد هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- أسماء الحقول محدودة بـ **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف اعتمادًا على التطبيق المصدر (عادةً Windows-1252 أو صفحات رموز OEM).

## **قراءة ملف DBF**

تجعل Aspose.Cells من السهل تحميل البيانات من ملف DBF في كائن Workbook. تستخدم المكتبة الفئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بشكل صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells

لقراءة ملف DBF، تحتاج إلى إنشاء مثيل من `LoadOptions`، وتعيين خاصية `load_format` الخاصة به إلى `LoadFormat.DBF`، وتمريرها إلى منشئ `Workbook` مع مسار الملف. بمجرد التحميل، تصبح البيانات قابلة للوصول من خلال مجموعة `worksheets`، حيث يمكنك التنقل عبر الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.

يوضح المثال التالي كيفية تحميل ملف DBF موجود في Aspose.Cells، والوصول إلى ورقة العمل الأولى، وقراءة قيم الخلايا.

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

يمكنك فتح ملفات DBF مباشرة في Microsoft Excel عن طريق تحديد الملف في مربع الحوار فتح. سيعامل Excel ملف DBF كجدول بيانات، ويعرض سجلاته في تخطيط جدولي. يكون هذا مفيدًا للتحقق السريع من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.

{{% /alert %}}

## **كتابة ملف DBF**

تتبع كتابة البيانات إلى ملف DBF نمطًا مشابهًا لحفظ أي تنسيق جدول بيانات آخر باستخدام Aspose.Cells. يمكنك إنشاء أو تحميل Workbook، وتعبئة ورقة العمل بالبيانات، ثم استدعاء طريقة `save` مع تحديد `SaveFormat.DBF` كتنسيق الهدف.

### كتابة ملف DBF باستخدام Aspose.Cells

لإنشاء ملف DBF، اتبع الخطوات التالية:

1. أنشئ مثيلًا جديدًا من `Workbook`.
2. الوصول إلى ورقة العمل الأولى من مجموعة `worksheets`.
3. تعبئة ورقة العمل ببياناتك، بما في ذلك الرؤوس في الصف الأول والسجلات في الصفوف اللاحقة.
4. استدعاء طريقة `Workbook.save`، وتمرير مسار الملف و `SaveFormat.DBF` كمعلمات.

يوضح المثال التالي كيفية إنشاء ملف DBF جديد من البداية. حيث يقوم بتعبئة ورقة العمل ببيانات عينة تحتوي على أنواع بيانات مختلفة (نصوص وأرقام وتواريخ) لتوضيح كيفية التعامل مع أنواع الحقول عند التصدير إلى تنسيق DBF.

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# رؤوس الأعمدة
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# صف البيانات 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# صف البيانات 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# صف البيانات 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# صف البيانات 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# صف البيانات 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# تعيين عرض الأعمدة لتحسين القراءة
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

عند كتابة البيانات في ملف DBF، تأكد من أن بياناتك تتوافق مع قيود التنسيق. يجب ألا يتجاوز طول أسماء الحقول 10 أحرف ولا يجب أن تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بشكل صحيح. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.

{{% /alert %}}

## **اعتبارات نوع البيانات والتنسيق**

عند نقل البيانات بين Aspose.Cells وتنسيق DBF، فإن فهم كيفية تعيين أنواع البيانات بين النظامين يعد أمرًا مهمًا لضمان سلامة البيانات.

### أنواع الخلايا إلى أنواع حقول DBF

يتم تحويل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:

- يتم تعيين **النصوص** إلى حقول الأحرف (C).
- يتم تعيين **القيم الرقمية** (الأعداد الصحيحة والعشرية) إلى الحقول الرقمية (N).
- يتم تعيين **قيم التاريخ** إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- يتم تعيين **القيم المنطقية** إلى الحقول المنطقية (L).

### الترميز

قد تستخدم ملفات DBF ترميزات أحرف مختلفة اعتمادًا على التطبيق الذي أنشأها. تتعامل Aspose.Cells مع الترميز بشفافية في معظم الحالات، ولكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول

يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:

- الحد الأقصى للطول 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- يتم تخزينها بأحرف كبيرة بغض النظر عن الحالة المستخدمة في الإدخال.

### التحقق من المخرجات

بعد كتابة ملف DBF، يمكنك التحقق من النتيجة عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تخطيط جدولي مع أسماء الحقول كرؤوس أعمدة، والسجلات ممتلئة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**

تتمثل إحدى أكثر حالات الاستخدام العملية لقراءة وكتابة ملفات DBF باستخدام Aspose.Cells في تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX و XLS أو CSV. نظرًا لأن Aspose.Cells تدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو العكس.

على سبيل المثال، يمكنك قراءة ملف DBF، وتطبيق التنسيق أو الحسابات باستخدام واجهة برمجة تطبيقات Aspose.Cells، ثم حفظ النتيجة كملف XLSX لتوزيعها على المستخدمين الذين يعملون مع تطبيقات جداول البيانات الحديثة. وعلى العكس من ذلك، يمكنك أخذ البيانات من ملف XLSX أو CSV وتصديرها إلى تنسيق DBF للتكامل مع الأنظمة القديمة.



{{< app/cells/assistant language="python" >}}