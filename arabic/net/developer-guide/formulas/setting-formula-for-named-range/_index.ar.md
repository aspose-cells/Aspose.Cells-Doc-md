---
title: إعداد الصيغة لنطاق مسمى
type: docs
weight: 20
url: /ar/net/setting-formula-for-named-range/
---
## **إعداد الصيغة لنطاق مسمى**
 مثل تطبيق Excel ، توفر واجهات برمجة تطبيقات Aspose.Cells القدرة على تحديد صيغة لنطاق مسمى أثناء استخدام[يعود الى](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)منشأه. يمكن أن يكون هناك العديد من سيناريوهات الاستخدام لهذه الميزة ، بعضها مفصل على النحو التالي.
### **تعيين صيغة بسيطة لنطاق مسمى**
يمكن أن تكون الصيغة البسيطة مرجعاً لخلية أخرى في نفس ورقة العمل (أو ورقة مختلفة). يقوم المثال التالي بإنشاء نطاق مسمى في جدول بيانات جديد وتعيين مرجعه إلى خلية أخرى.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **تعيين صيغة معقدة لنطاق مسمى**
يمكن أن تكون الصيغة المعقدة أي شيء مثل نطاق ديناميكي أو صيغة تمتد عبر خلايا متعددة في أوراق عمل مختلفة. ينشئ المثال التالي نطاقًا ديناميكيًا باستخدام الدالة INDEX للحصول على القيمة من قائمة بناءً على موقعها.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



فيما يلي مثال آخر يستخدم نطاقًا مسمىًا لجمع القيم من خليتين في أوراق عمل مختلفة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
