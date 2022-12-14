---
title: Aspose.Cells for Java 16.10.0 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/java/aspose-cells-for-java-16-10-0-release-notes/
---
## **1) Aspose.Cells**

|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-41974 | لا يعمل تحديث PivotTable في ملف PDF المعروض| حشرة|
|CELLSJAVA-41900 | يتلف XLSM عن طريق التحميل البسيط وعملية الحفظ| حشرة|
|CELLSJAVA-41790 | الارتباطات التشعبية لا تعمل كما هو متوقع بعد تحويل جدول البيانات إلى HTML| حشرة|
|CELLSJAVA-42010 | لا يتم عرض بعض الأحرف في ملف PDF الناتج| حشرة|
|CELLSJAVA-41977 | تم تغيير ترتيب وسيلة إيضاح الرسم البياني في ملف PDF للمخطط| حشرة|
|CELLSJAVA-41972 | ترتيب Z للخطوط المرتفعة والمنخفضة غير صحيح في PDF| حشرة|
|CELLSJAVA-42015 | تلف جدول البيانات بعد إعادة الحفظ باستخدام Aspose.Cells| حشرة|
|CELLSJAVA-42005 | يتم تغيير الصيغة بعد إدراجها في خلية| حشرة|
|CELLSJAVA-41997 | سلوك غريب مع حبة بسيطة باستخدام العلامات الذكية| حشرة|
|CELLSJAVA-41993 | NullPointerException أثناء فتح ملف a7.xlsm| استثناء|
|CELLSJAVA-41992 | NullPointerException أثناء فتح ملف a6.xlsm| استثناء|
|CELLSJAVA-41991 |NullPointerException أثناء فتح ملف a5.xlsm| استثناء|
|CELLSJAVA-41990 | NullPointerException أثناء فتح ملف a4.xlsm| استثناء|
|CELLSJAVA-41989 | NullPointerException أثناء فتح ملف a3.xlsm| استثناء|
|CELLSJAVA-41988 | NullPointerException أثناء فتح ملف a2.xlsm| استثناء|
|CELLSJAVA-41987 | NullPointerException أثناء فتح ملف a1.xlsm| استثناء|
|CELLSJAVA-41968 | IndexOutOfBoundsException: الفهرس: 23 ، الحجم: 14 أثناء تحديث PivotChart| استثناء|
|CELLSJAVA-42014 | ClassCastException: لا يمكن تحويل com.aspose.cells.zadp إلى com.aspose.cells.zadq أثناء إعادة حفظ XLSX| استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية Shape.Reflection وفئة ReflectionEffect**
يمثل تأثير الانعكاس لعنصر المخطط أو شكله.
### **يضيف خصائص Shape.Glow و GlowEffect.Size و GlowEffect.Transparency**
يمثل تأثير التوهج لعنصر المخطط أو شكله.
### **يضيف LightRigType. لا يوجد تعداد**
لا يمثل أي إعداد للإضاءة.
### **يضيف خاصية Shape.ShadowEffect**
يمثل تأثير الظل لعنصر المخطط أو شكله.
### **يضيف خاصية ExternalLink.IsVisible**
يشير إلى ما إذا كان الارتباط الخارجي مرئيًا أم لا.
### **إضافة خاصية Shape.ThreeDFormat وفئة ThreeDFormat**
الحصول على تنسيق ثلاثي الأبعاد للشكل وتعيينه.
### **يضيف تعداد PresetCameraType**
يمثل طرقًا خوارزمية مختلفة لتعيين جميع خصائص الكاميرا ، بما في ذلك الموضع.
### **يضيف تعداد LightRigDirectionType**
يمثل نوع اتجاه منصة الحفر الخفيفة.
### **يضيف تعداد BevelType**
يمثل إعدادًا مسبقًا لنوع مجسم مشطوف الحواف يمكن تطبيقه على شكل ثلاثي الأبعاد.
### **يضيف طريقة XmlMapCollection.Add (سلسلة url)**
يضيف XmlMap بواسطة عنوان url / مسار ملف XML.
### **إضافة طريقة ShapeCollection.AddWordArt () وتعداد PresetWordArtStyle**
يضيف WordArt مُعدًا مسبقًا منذ MS Excel 2007.
### **يضيف أسلوب FontSettingCollection.SetWordArtStyle () وطريقة FontSetting.SetWordArtStyle ()**
يعيّن نمط WordArt المعين مسبقًا على نص الشكل.
### **يضيف Cells.LinkToXmlMap (سلسلة mapName ، int row ، int column ، string path)**
الارتباط بخريطة xml.
### **يضيف خاصية ListColumn.Formula**
الحصول على صيغة عمود القائمة وتعيينها.
### **إضافة خاصية GridWeb.CustomCalculationEngine وفئة GridAbstractCalculationEngine**
يمثل محرك الحساب المخصص للمستخدم لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells.GridWeb.
