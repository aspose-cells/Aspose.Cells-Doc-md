---
title: الاستعلام Cell مناطق مناوبة لمسار مخطط XML باستخدام طريقة Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ar/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك الاستعلام عن مناطق الخلايا التي تم تعيينها إلى مسار مخطط XML باستخدام Aspose.Cells باستخدام[**Worksheet.xmlMapQuery ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) طريقة. إذا كان المسار موجودًا ، فسيعيد قائمة مناطق الخلايا المتعلقة بهذا المسار داخل خريطة XML. المعلمة الأولى من[**Worksheet.xmlMapQuery ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) طريقة تحديد مسار عنصر XML وتحدد المعلمة الثانية مخطط XML الذي تريد الاستعلام عنه.

## **الاستعلام Cell مناطق مناوبة لمسار مخطط XML باستخدام طريقة Worksheet.XmlMapQuery**

توضح لقطة الشاشة التالية Microsoft Excel الذي يعرض خريطة XML داخل ملف[نموذج لملف Excel](55541818.xlsx)المستخدمة في الكود. يستعلم الرمز عن مخطط XML مرتين ويطبع قائمة مناطق الخلايا التي تم إرجاعها بواسطة ملف[**Worksheet.xmlMapQuery ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) على وحدة التحكم كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **احصل على مسار XML من قائمة كائن / جدول**

يمكن استيراد بيانات XML إلى أوراق العمل. أحيانًا يكون مسار XML مطلوبًا من ListObjects في ورقة العمل. تتوفر هذه الميزة في Excel باستخدام تعبير مثل Sheet1.ListObjects (1) .XmlMap.DataBinding. تتوفر نفس الميزة في Aspose.Cells عن طريق الاتصال[**ListObject.getXmlMap (). getDataBinding (). getUrl ()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). المثال التالي يوضح هذه الميزة. يمكن تنزيل ملف النموذج وملفات المصدر الأخرى من الروابط التالية:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
