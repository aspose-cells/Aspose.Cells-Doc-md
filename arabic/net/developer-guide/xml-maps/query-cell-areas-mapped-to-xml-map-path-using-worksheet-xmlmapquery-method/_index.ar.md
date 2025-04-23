---
title: الاستعلام عن مناطق الخلايا المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ar/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك استعلام مناطق الخلية المرتبطة بمسار خريطة XML باستخدام الأسلوب [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) في Aspose.Cells. إذا كان المسار موجودًا، فسيقوم بإرجاع قائمة مناطق الخلايا المتعلقة بهذا المسار داخل خريطة XML. يحدد المعامل الأول في الأسلوب [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) مسار العنصر XML والمعامل الثاني يحدد الخريطة النصية التي ترغب في استعلامها.

## **استعلام عن مجالات الخلية المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery**

اللقطة الشاشية التالية توضح Microsoft Excel يعرض خريطة XML داخل [ملف إكسل عيني](55541790.xlsx) المستخدم في الكود. يقوم الكود باستعلام خريطة XML مرتين ويطبع قائمة مناطق الخلايا التي يتم إرجاعها بواسطة الأسلوب [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) على وحدة التحكم كما هو موضح أدناه.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **الحصول على مسار XML من جدول الكائن/الجدول**

بيانات XML يمكن استيرادها إلى أوراق العمل. في بعض الأحيان يُطلب مسار XML من ListObjects/جداول الورقة. تتوفر هذه الميزة في Excel عن طريق استخدام تعبير مثل Sheet1.ListObjects (1) .XmlMap.DataBinding. نفس الميزة متاحة في Aspose.Cells عن طريق استدعاء [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). يوضح المثال التالي هذه الميزة. يمكن تنزيل ملف القالب وملفات المصدر الأخرى من الروابط التالية:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
{{< app/cells/assistant language="csharp" >}}
