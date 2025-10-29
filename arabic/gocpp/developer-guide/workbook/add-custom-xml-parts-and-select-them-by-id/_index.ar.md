---
title: إضافة أجزاء XML مخصصة واختيارها بواسطة المعرف باستخدام Golang عبر C++
linktitle: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 70
url: /ar/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: تعلم كيفية إضافة واختيار أجزاء XML مخصصة في ملفات Excel باستخدام Aspose.Cells مع Golang عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

أجزاء XML مخصصة هي بيانات XML مخزنة داخل مستندات Microsoft Excel وتستخدمها التطبيقات التي تتفاعل معها. لا توجد طريقة مباشرة لإضافتها باستخدام واجهة مستخدم Microsoft Excel في الوقت الحالي. ومع ذلك، يمكنك إضافتها برمجياً بطرق مختلفة، مثل استخدام VSTO أو Aspose.Cells. استخدم طريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) لإضافة جزء XML مخصص باستخدام واجهة برمجة تطبيقات Aspose.Cells. يمكنك أيضًا تعيين معرفها باستخدام الخاصية [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). بالمثل، إذا كنت تريد تحديد جزء XML مخصص باستخدام المعرف، يمكنك استخدام طريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**

في المثال التالي، تضاف أولاً أربعة أجزاء XML مخصصة باستخدام طريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/). ثم يتم تعيين معرفاتها باستخدام الخاصية [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). أخيرًا، يتم العثور على أحد أجزاء XML المخصصة المضافة أو تحديده باستخدام طريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). يرجى أيضًا الاطلاع على مخرجات وحدة التحكم للكود المقدم أدناه للمرجعية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
