---
title: الاستعلام Cell مناطق مناوبة لمسار مخطط XML باستخدام طريقة Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ar/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك الاستعلام عن مناطق الخلايا مناظرة لمسار مخطط XML باستخدام Aspose.Cells باستخدام[**Worksheet.XmlMapQuery ()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)طريقة. إذا كان المسار موجودًا ، فسيعيد قائمة مناطق الخلايا المتعلقة بهذا المسار داخل خريطة XML. المعلمة الأولى من[**Worksheet.XmlMapQuery ()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)تحدد الطريقة مسار عنصر XML وتحدد المعلمة الثانية مخطط XML الذي تريد الاستعلام عنه.

## **الاستعلام Cell مناطق مناوبة لمسار مخطط XML باستخدام طريقة Worksheet.XmlMapQuery**

 توضح لقطة الشاشة التالية Microsoft Excel الذي يعرض خريطة XML داخل ملف[نموذج لملف Excel](55541790.xlsx) المستخدمة في الكود. يستعلم الرمز عن مخطط XML مرتين ويطبع قائمة مناطق الخلايا التي تم إرجاعها بواسطة ملف[**Worksheet.XmlMapQuery ()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)الطريقة على وحدة التحكم كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **إخراج وحدة التحكم**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **احصل على مسار XML من قائمة كائن / جدول**

يمكن استيراد بيانات XML إلى أوراق العمل. أحيانًا يكون مسار XML مطلوبًا من ListObjects في ورقة العمل. تتوفر هذه الميزة في Excel باستخدام تعبير مثل Sheet1.ListObjects (1) .XmlMap.DataBinding. تتوفر نفس الميزة في Aspose.Cells عن طريق الاتصال[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). يوضح المثال التالي هذه الميزة. يمكن تنزيل ملف النموذج وملفات المصدر الأخرى من الروابط التالية:

1. [XML Data.xlsx](72417285.xlsx)
1. [قائمة الدول. xml](72417287.xml)
1. [قائمة الطعام. xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
