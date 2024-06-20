---
title: ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 320
url: /ar/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **سيناريوهات الاستخدام المحتملة**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) و [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) هما خاصيتان مضمنتان موسعتان تم تعريفهما داخل تنسيق OpenXml. الغرض من هاتين الخاصيتين هو التالي
## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
الكود النموذجي التالي يقوم بتعيين [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) و [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) خصائص المستند المضمنة للفصل. يرجى التحقق من ملف الإكسل الناتج [ملف الإكسل الناتج](5115500.xlsx) باستخدام هذا الكود، قم بتغيير امتداده إلى .zip واستخراج محتوياته وعرض app.xml كما هو موضح في اللقطة المصورة أعلاه.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
