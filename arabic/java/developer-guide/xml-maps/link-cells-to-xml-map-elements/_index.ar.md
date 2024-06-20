---
title: ربط الخلايا بعناصر خريطة XML
type: docs
weight: 50
url: /ar/java/link-cells-to-xml-map-elements/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك ربط خلاياك بعناصر Map XML باستخدام Aspose.Cells. يرجى استخدام الـ [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap(java.lang.String,%20int,%20int,%20java.lang.String)) لهذا الغرض.

## **ربط الخلايا بعناصر خريطة XML**

يقوم الكود النموذجي التالي بتحميل [ملف الإكسل المصدر](5472518.xlsx) الذي يحتوي على خريطة XML ثم يقوم بربط الخلايا A1، B2، C3، D4، E5 و F6 بعناصر الخريطة XML FIELD1، FIELD2، FIELD4، FIELD5، FIELD7 و FIELD8 على التوالي، ثم يحفظ الدفتر في [ملف الإكسل الناتج](5472517.xlsx).

إذا فتحت [ملف الإكسل الناتج](5472517.xlsx) ونقرت على زر *Developer > Source*، سترى أن الخلايا مرتبطة بعناصر خريطة XML وسيتم تظليلها أيضًا من قبل Microsoft Excel كما هو موضح في هذه الصورة.

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
