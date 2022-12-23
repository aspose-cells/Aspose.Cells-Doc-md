---
title: أضف أجزاء XML المخصصة وحددها حسب المعرف
type: docs
weight: 70
url: /ar/net/add-custom-xml-parts-and-select-them-by-id/
---
## **سيناريوهات الاستخدام الممكنة**

أجزاء XML المخصصة هي بيانات XML المخزنة داخل مستندات Excel Microsoft وتستخدم من قبل التطبيقات التي تتعامل معها. لا توجد طريقة مباشرة لإضافتها باستخدام Microsoft Excel UI في الوقت الحالي. ومع ذلك ، يمكنك إضافتها برمجيًا بعدة طرق ، مثل استخدام VSTO ، باستخدام Aspose.Cells وما إلى ذلك. يرجى استخدام[**المصنف. CustomXmlParts.Add ()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)الطريقة إذا كنت تريد إضافة جزء XML مخصص باستخدام Aspose.Cells API. يمكنك أيضًا تعيين معرفه ، باستخدام[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)خاصية. وبالمثل ، إذا كنت تريد تحديد جزء XML مخصص حسب المعرف ، فيمكنك استخدام[**المصنف. CustomXmlParts.SelectByID ()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)طريقة.

## **أضف أجزاء XML المخصصة وحددها حسب المعرف**

يضيف نموذج التعليمات البرمجية التالي أولاً أربعة أجزاء مخصصة لـ XML باستخدام[**المصنف. CustomXmlParts.Add ()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)طريقة. ثم يقوم بتعيين معرفاتهم باستخدام[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) خاصية. أخيرًا ، يقوم بالبحث عن أحد أجزاء XML المخصصة المضافة أو تحديده باستخدام[**المصنف. CustomXmlParts.SelectByID ()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)طريقة. يرجى أيضًا الاطلاع على إخراج وحدة التحكم للرمز الوارد أدناه للرجوع إليه.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
