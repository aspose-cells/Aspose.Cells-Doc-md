---
title: تحديث الجداول المحورية في Aspose.Cells for Python via Java
linktitle: تحديث الجداول المحورية في Aspose.Cells for Python via Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Python via Java باستخدام واجهة برمجة التطبيقات للتحديث في الإصدار v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Python via Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---




{{% alert color="primary" %}}

توفر Aspose.Cells واجهة برمجة تطبيقات تحديث متطبقة تتيح لك إعادة تحميل بيانات الجدول المحوري ضمن أربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Python via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.refreshData()` كطريقة قديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)

# إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refreshAll()

# حفظ المصنف
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **تحديث جميع الجداول المحورية في ورقة عمل واحدة**

في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة ولا يجب لمسها. لهذه الحالة، توفر Aspose.Cells `Worksheet.refreshPivotTables()`، التي تكون محدودة النطاق بمثيل `Worksheet` واحد.

هذه الطريقة أكثر انتقائية من `Workbook.refreshAll()`: يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون تغيير.

يملأ المثال التالي بيانات المصدر Fruit/Year/Amount نفسها، ويضيف جدولًا محوريًا في ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يقوم بتحديث الجداول المحورية في تلك الورقة فقط.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)

pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)

worksheet.refreshPivotTables()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **تحديث جدول محوري واحد**

عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### **تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`**

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. تعيد هذه الاستدعاءة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تشترك في مثيل واحد من `PivotCache`، فإن استدعاء `PivotCache.refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا شارك جدولان محوريان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يحدّث كليهما.

{{% /alert %}}

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لإثبات سلوك ذاكرة التخزين المؤقت المشتركة هذا، ويُعدّل بعض قيم المصدر، ثم يحدث من خلال مرجع ذاكرة تخزين مؤقت واحد.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة حوالي 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# إضافة جدول محوري أول "Pivot1" مثبت عند الخلية E3، نطاق المصدر A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# إضافة جدول محوري ثاني "Pivot2" مثبت عند E15 باستخدام نفس نطاق المصدر A1:C9
# يتشارك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقت واحدة للجدول المحوري لأن نطاق المصدر متطابق.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# تعديل عدة قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير في البيانات
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# تحديث ذاكرة التخزين المؤقت المشتركة للجدول المحوري.
# نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقت للجدول المحوري، فإن هذه المكالمة الواحدة
# تحدث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدث.
pivotTable1.getPivotCache().refresh()

# حفظ المصنف
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### **تغير العرض/التخطيط فقط — استخدم `calculateData()`**

إذا **لم** تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، `pivotTable.calculateData()` هو الخيار الصحيح.

يتجنب ذلك جلب المصدر غير الضروري وهو أسرع بكثير عندما تشترك جداول محورية متعددة في نفس ذاكرة التخزين المؤقت.

يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة 8 صفوف من البيانات (الصفوف 2-9، لتتناسب مع نطاق المصدر A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)

# إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ومصدره من A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# تعيين الحقول: الفاكهة إلى الصف، والسنة إلى العمود، والمبلغ إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# تعديل خاصية عرض/تخطيط — هذا تغيير على العرض فقط،
# لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من
# البيانات المخزنة بالفعل في PivotCache. نظراً لأن بيانات المصدر لم تتغير،
# لا يتم تنفيذ أي رحلة ذهاب وإياب إلى المصدر — فقط يتم إعادة حساب القيم المخزنة مؤقتاً
# في خلايا ورقة العمل.
pivotTable.calculateData()

# حفظ المصنف على القرص
workbook.save("output.xlsx")

jpype.shutdownJVM()python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# الكود المنقول هنا
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (الترويسة + 9 صفوف) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- إضافة الجدول المحوري الأول (Pivot1) عند الخلية الوجهة E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
# يتشارك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقتة محورية واحدة أساسية.
# هذا هو بالضبط السيناريو الذي تصبح فيه طريقة RefreshData() القديمة لكل جدول
# غير فعالة: تحديث جدول واحد يعيد جلب كامل
# الذاكرة المؤقتة المشتركة، لذلك تحديث N جداول يقوم بنفس الجلب المكلف N مرات.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000)   # عنب 2020
sheet.getCells().get("C5").putValue(7500)   # كرز 2020
sheet.getCells().get("C9").putValue(9500)   # كرز 2021

# --- النمط المهجور (قبل 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // يعيد الجلب من المصدر، يحدث كامل الذاكرة المؤقتة
# pivotTable2.RefreshData();  // يعيد الجلب مرة أخرى — الذاكرة المؤقتة حديثة بالفعل!
# كل استدعاء يعيد بناء الذاكرة المؤقتة المشتركة، لذلك N جداول = N جلب متكرر.

# --- النمط الجديد v26.7+: حدث الذاكرة المؤقتة مرة واحدة، ثم أعد العرض حسب الحاجة ---
# استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى الذاكرة
# المؤقتة المشتركة ويعيد حساب عرض كل جدول محوري يشير إليها.
# لأن Pivot1 و Pivot2 يتشاركان ذاكرة تخزين مؤقتة محورية واحدة، هذا الاستدعاء الواحد يحدث
# كلا الجدولين — لا حاجة لذهاب وإياب ثانٍ إلى المصدر.
pivotTable1.getPivotCache().refresh()

# CalculateData() يعيد فقط عرض الجدول المحوري (البيانات + النمط)
# من البيانات الموجودة بالفعل في الذاكرة المؤقتة — ولا يلمس المصدر.
# نستدعيه على Pivot2 هنا فقط لتوضيح الواجهة البرمجية: بعد تحديث الذاكرة
# المؤقتة مرة واحدة، يمكن إعادة عرض أي جدول تابع دون
# العودة إلى المصدر. استخدم CalculateData() بمفردها عندما تتغير فقط
# إعدادات عرض/تخطيط الجدول المحوري وتكون الذاكرة المؤقتة حالية.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟**

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | استدعاء واحد؛ يغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.refreshPivotTables()` | محدودة النطاق بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدّث **جميع** الجداول المحورية على تلك ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتجاوز رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمه للتعداد قبل التحديث المجمع. |

عمليًا، أعطِ الأولوية لواجهات برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت على `refreshData()` القديمة لكل جدول. إنها مدركة لذاكرة التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المكررة، وتتيح لك اختيار أصغر نطاق يلبي متطلب التحديث لديك.

## **مقالات ذات صلة**

- [إدراج صورة في خلية](/cells/ar/python-java/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/python-java/dbf/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/python-java/splitting-excel-files-into-multiple-files/)
- [الخطوط البيانية المصغرة في Aspose.Cells for Python via Java](/cells/ar/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}
