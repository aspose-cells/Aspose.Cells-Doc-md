---
title: ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 320
url: /ar/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **سيناريوهات الاستخدام المحتملة**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) و [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) هما خاصيتان موسعتان مدمجتان داخل تنسيق OpenXml. الغرض من هذه الخصائص هو:
## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
يعين الكود التالي المثال الخاص بكافة خصائص المستند الموسعة المدمجة التي تشمل [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) و [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) في ملف العمل. يرجى فحص الملف الموجه الناتج [excel](5115500.xlsx)، وتغيير امتداده إلى .zip وفك ضغط محتواه، ثم مشاهدة الملف app.xml كما في الصورة أعلاه.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
