---
title: تعيين خصائص ScaleCrop و LinksUpToDate للخصائص المدمجة للمستند باستخدام Golang عبر C++
linktitle: تعيين خصائص ScaleCrop وLinksUpToDate
type: docs
weight: 320
url: /ar/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: تعلم كيفية تعيين خصائص ScaleCrop وLinksUpToDate لخصائص المستند المدمجة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) و [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) هما خاصيتان موسعتان مدمجتان من خصائص المستندات، معرفتان داخل تنسيق OpenXml. الغرض من هذه الخصائص هو كما يلي:

## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **تعيين خصائص ScaleCrop وLinksUpToDate لخصائص المستند المدمجة**
يوضح المثال التالي كيف تقوم بضبط خصائص المستند الموسعة [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) و [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) للملف المسمى. يرجى التحقق من ملف الإكسل الناتج [ملف الإخراج](5115500.xlsx) الذي تم إنشاؤه بواسطة هذا الكود، غيّره إلى الامتداد .zip واستخرج محتوياته واطلع على ملف app.xml كما في الصورة أعلاه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
