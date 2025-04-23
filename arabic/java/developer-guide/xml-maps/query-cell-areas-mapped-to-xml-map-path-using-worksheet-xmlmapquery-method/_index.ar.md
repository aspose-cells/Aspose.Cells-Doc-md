---
title: الاستعلام عن مناطق الخلايا المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ar/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك استعلام مجالات الخلية المتوافقة مع مسار map XML باستخدام الـ [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-). إذا كان المسار موجودًا، فسيُعيد قائمة مجالات الخليّة المتعلقة بذلك المسار داخل خريطة XML. تحدد المعلمة الأولى للـ [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) مسار العنصر XML والمعلمة الثانية تحدد Map XML الذي تريد الاستعلام عنه.

## **استعلام عن مجالات الخلية المرتبطة بمسار خريطة XML باستخدام طريقة Worksheet.XmlMapQuery**

تُظهر اللقطة الشاشة التالية عرض Map XML داخل Microsoft Excel في [ملف الإكسل النموذجي](55541818.xlsx) المستخدم في الشفرة. تستعلم الشفرة خريطة XML مرتين وتطبع قائمة مجالات الخلية المعادة من الـ [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) على واجهة السطر كما هو مُبيَّن أدناه.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **مخرجات الوحدة**

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

يمكن استيراد البيانات الخاصة بـ XML إلى أوراق العمل. في بعض الأحيان يكون مطلوبًا مسار XML من ListObjects للورقة العمل. يتوفر هذا الميزة في Excel عن طريق استخدام تعبير مثل Sheet1.ListObjects(1).XmlMap.DataBinding. نفس الميزة متاحة في Aspose.Cells عن طريق استدعاء [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). يظهر المثال التالي هذه الميزة. يمكن تحميل ملف القالب وغيرها من ملفات المصدر من الروابط التالية:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
{{< app/cells/assistant language="java" >}}
