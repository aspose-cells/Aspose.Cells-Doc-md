---
title: وضع صيغة لنطاق مسمى
type: docs
weight: 20
url: /ar/python-net/setting-formula-for-named-range/
---

## **وضع صيغة لنطاق مسمى**
مثل تطبيق Excel، توفر واجهات برمجة تطبيقات Aspose.Cells for Python via .NET القدرة على تحديد صيغة لنطاق مسمى أثناء استخدام خاصية [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to). قد يكون هناك العديد من سيناريوهات الاستخدام لهذه الميزة، منها ما هو مفصل أدناه.
### **وضع صيغة بسيطة لنطاق مسمى**
يمكن أن تكون الصيغة البسيطة إشارة إلى خلية أخرى في نفس جدول العمل (أو جداول عمل مختلفة). ينشئ المثال التالي نطاقًا مسمى في جدول بيانات جديد ويحدد إشارته إلى خلية أخرى.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **وضع صيغة معقدة لنطاق مسمى**
يمكن أن تكون الصيغة المعقدة أي شيء مثل نطاق ديناميكي أو صيغة تمتد عبر عدة خلايا في جداول عمل مختلفة. ينشئ المثال التالي نطاقًا ديناميكيًا باستخدام وظيفة INDEX للحصول على القيمة من قائمة استنادًا إلى موقعها.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



هنا مثال آخر يستخدم نطاقًا مسمى لجمع القيم من 2 خليتين في جداول عمل مختلفة.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
