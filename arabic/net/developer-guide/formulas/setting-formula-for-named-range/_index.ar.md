---
title: وضع صيغة لنطاق مسمى
type: docs
weight: 20
url: /ar/net/setting-formula-for-named-range/
---

## **وضع صيغة لنطاق مسمى**
مثل تطبيق Excel، توفر واجهات برمجة التطبيقات في Aspose.Cells القدرة على تحديد صيغة لنطاق مسمى أثناء استخدام خاصيتها [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto). يمكن أن تكون هناك العديد من سيناريوهات الاستخدام لهذه الميزة، ويتم تفصيل بعضها كما يلي.
### **وضع صيغة بسيطة لنطاق مسمى**
يمكن أن تكون الصيغة البسيطة إشارة إلى خلية أخرى في نفس جدول العمل (أو جداول عمل مختلفة). ينشئ المثال التالي نطاقًا مسمى في جدول بيانات جديد ويحدد إشارته إلى خلية أخرى.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **وضع صيغة معقدة لنطاق مسمى**
يمكن أن تكون الصيغة المعقدة أي شيء مثل نطاق ديناميكي أو صيغة تمتد عبر عدة خلايا في جداول عمل مختلفة. ينشئ المثال التالي نطاقًا ديناميكيًا باستخدام وظيفة INDEX للحصول على القيمة من قائمة استنادًا إلى موقعها.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



هنا مثال آخر يستخدم نطاقًا مسمى لجمع القيم من 2 خليتين في جداول عمل مختلفة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
