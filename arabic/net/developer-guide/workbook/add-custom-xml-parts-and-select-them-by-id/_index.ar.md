---
title: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 70
url: /ar/net/add-custom-xml-parts-and-select-them-by-id/
---

## **سيناريوهات الاستخدام المحتملة**

تمثل أجزاء XML المخصصة البيانات XML التي يتم تخزينها داخل مستندات Microsoft Excel وتستخدمها التطبيقات التي تتعامل معها. لا يوجد طريقة مباشرة لإضافتها باستخدام واجهة المستخدم Microsoft Excel في الوقت الحالي. ومع ذلك، يمكنك إضافتها برمجيا بطرق مختلفة، مثل باستخدام VSTO، باستخدام Aspose.Cells إلخ. يرجى استخدام الطريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) إذا كنت ترغب في إضافة جزء XML مخصص باستخدام واجهة برمجية Aspose.Cells. يمكنك أيضًا تعيين ID لها، استخدام الخاصية [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). بالمثل، إذا أردت تحديد جزء XML مخصص حسب الهوية، يمكنك استخدام الطريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid).

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**

يضيف الرمز العيني التالي أولاً أربعة أجزاء XML مخصصة باستخدام الطريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add). ثم يعين معرفاتها باستخدام الخاصية [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). أخيرًا، يجد أو يحدد واحدًا من الأجزاء XML المخصصة المضافة باستخدام الطريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). يُرجى أيضًا الرجوع إلى إخراج الصفحة الخارجية للرمز العيني الذي يلى للإشارة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
