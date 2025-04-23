---
title: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 70
url: /ar/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **سيناريوهات الاستخدام المحتملة**

الأجزاء XML المخصصة هي بيانات XML مخزنة داخل مستندات Microsoft Excel وتستخدمها التطبيقات التي تتعامل معها. لا توجد طريقة مباشرة لإضافتها باستخدام واجهة مستخدم Microsoft Excel حاليًا. ومع ذلك، يمكنك إضافتها برمجيًا بعدة طرق، مثل باستخدام VSTO، أو باستخدام Aspose.Cells، وغيرها. يرجى استخدام الطريقة [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) إذا كنت ترغب في إضافة جزء XML مخصص باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET. يمكنك أيضًا تعيين معرفه باستخدام الخاصية [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). بالمثل، إذا كنت ترغب في تحديد جزء XML مخصص بواسطة المعرف، يمكنك استخدام الطريقة [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str).

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**

يضيف الرمز العيني التالي أولاً أربعة أجزاء XML مخصصة باستخدام الطريقة [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes). ثم يعين معرفاتها باستخدام الخاصية [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). أخيرًا، يجد أو يحدد واحدًا من الأجزاء XML المخصصة المضافة باستخدام الطريقة [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). يُرجى أيضًا الرجوع إلى إخراج الصفحة الخارجية للرمز العيني الذي يلى للإشارة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

