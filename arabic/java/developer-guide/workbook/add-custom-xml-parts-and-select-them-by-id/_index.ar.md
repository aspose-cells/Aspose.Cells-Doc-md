---
title: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 10
url: /ar/java/add-custom-xml-parts-and-select-them-by-id/
---

## **سيناريوهات الاستخدام المحتملة**

أجزاء XML المخصصة هي البيانات الـ XML التي يتم تخزينها داخل مستندات Microsoft Excel وتُستخدم من قبل التطبيقات التي تتعامل معها. ليس هناك طريقة مباشرة لإضافتها باستخدام واجهة المستخدم في Microsoft Excel في الوقت الحالي. ومع ذلك، يمكنك إضافتها برمجياً بطرق مختلفة على سبيل المثال باستخدام VSTO، أو باستخدام Aspose.Cells وما إلى ذلك. يُرجى استخدام الـ [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) إذا كنت ترغب في إضافة جزء XML مخصص باستخدام واجهة برمجة التطبيقات API لـ Aspose.Cells. كما يمكنك أيضاً تعيين هويتها باستخدام الخاصية [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). بالمثل، إذا أردت تحديد جزء XML مخصص باستخدام الهوية، فيمكنك استخدام الـ [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-).

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**

يقوم الكود النموذجي التالي أولاً بإضافة أربعة أجزاء XML مخصصة باستخدام الـ [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-). ثم يعين هويتها باستخدام الخاصية [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). في النهاية، يجد أو يُحدد واحدًا من الأجزاء XML المخصصة التي تمت إضافتها باستخدام الـ [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-). يُرجى أيضاً رؤية إخراج واجهة السطر للكود المعطى أدناه كمرجع له.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
