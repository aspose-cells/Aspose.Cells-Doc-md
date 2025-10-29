---
title: الاستعلام عن مناطق الخلايا المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ar/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك الاستعلام عن مناطق الخلايا المرتبطة بمسار خريطة XML باستخدام Aspose.Cells لـ بايثون via .NET عبر طريقة [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query). إذا كان المسار موجودًا، فسيُعيد قائمة بمناطق الخلايا المرتبطة بذلك المسار داخل خريطة XML. يُحدد المعامل الأول لطريقة [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) مسار العنصر XML والمعامل الثاني يحدد خريطة XML التي تريد الاستعلام عنها.

## **استعلام عن مجالات الخلية المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery**

اللقطة الشاشية التالية توضح Microsoft Excel يعرض خريطة XML داخل [ملف إكسل عيني](55541790.xlsx) المستخدم في الكود. يقوم الكود باستعلام خريطة XML مرتين ويطبع قائمة مناطق الخلايا التي يتم إرجاعها بواسطة الأسلوب [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) على وحدة التحكم كما هو موضح أدناه.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

يمكن استيراد بيانات XML إلى أوراق العمل. أحيانًا، يلزم مسار XML من كائنات ListObjects في ورقة العمل. تتوفر هذه الميزة في إكسل باستخدام تعبير مثل Sheet1.ListObjects(1).XmlMap.DataBinding. وتتوفر نفس الميزة في Aspose.Cells لـ بايثون via .NET عبر استدعاء [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url). يوضح المثال التالي هذه الميزة. يمكن تنزيل ملف النموذج والملفات المصدر الأخرى من الروابط التالية:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
