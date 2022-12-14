---
title: أضف أجزاء XML المخصصة وحددها حسب المعرف
type: docs
weight: 10
url: /ar/java/add-custom-xml-parts-and-select-them-by-id/
---
## **سيناريوهات الاستخدام الممكنة**

أجزاء XML المخصصة هي بيانات XML المخزنة داخل مستندات Excel Microsoft وتستخدم من قبل التطبيقات التي تتعامل معها. لا توجد طريقة مباشرة لإضافتها باستخدام Microsoft Excel UI في الوقت الحالي. ومع ذلك ، يمكنك إضافتها برمجيًا بطرق مختلفة ، مثل استخدام ملفات*VSTO*، استخدام*Aspose.Cells*الخ. الرجاء استخدام[**Workbook.getCustomXmlParts (). add ()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) إذا كنت تريد إضافة جزء XML مخصص باستخدام Aspose.Cells API. يمكنك أيضًا تعيين معرفه ، باستخدام[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)منشأه. وبالمثل ، إذا كنت تريد تحديد جزء XML مخصص حسب المعرف ، فيمكنك استخدام[**Workbook.getCustomXmlParts (). selectByID ()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) طريقة.

## **أضف أجزاء XML المخصصة وحددها حسب المعرف**

يضيف نموذج التعليمات البرمجية التالي أولاً أربعة أجزاء مخصصة لـ XML باستخدام[**Workbook.getCustomXmlParts (). add ()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) طريقة. ثم يقوم بتعيين معرفاتهم باستخدام[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)منشأه. أخيرًا ، يقوم بالبحث عن أحد أجزاء XML المخصصة المضافة أو تحديده باستخدام[**Workbook.getCustomXmlParts (). selectByID ()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) طريقة. يرجى أيضًا الاطلاع على إخراج وحدة التحكم للرمز الوارد أدناه كمرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
