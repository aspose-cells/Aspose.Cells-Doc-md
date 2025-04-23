---
title: ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 1050
url: /ar/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **سيناريوهات الاستخدام المحتملة**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) و [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) هما خاصيتان مدمجتان موسعتان محددتان داخل تنسيق OpenXml. الغرض من هذه الخصائص هو ما يلي
## **1) ScaleCrop**
يُشير هذا العنصر إلى وضع عرض صورة مصغرة المستند. قم بتعيين هذا العنصر إلى **صحيح** لتمكين تكبير صورة مصغرة المستند للعرض. قم بتعيين هذا العنصر إلى **خطأ** لتمكين قص الصورة المصغرة لعرض أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **2) LinksUpToDate**
يُشير هذا العنصر ما إذا كانت الروابط في مستند مُحدّثة. قم بتعيين هذا العنصر إلى **صحيح** للإشارة إلى أن الروابط محدّثة. قم بتعيين هذا العنصر إلى **خطأ** للإشارة إلى أن الروابط قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.
## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
يُعين الرمز النموذجي التالي [ScaleCrop] (https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) و [LinksUpToDate] (https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) خصائص المستند المدمجة المُمتدة في سجل العمل. يُرجى التحقق من [ملف الإكسل الناتج] (5472494.xlsx) المتولد بهذا الرمز، قم بتغيير الامتداد الخاص به إلى .zip واستخرج محتوياته وعرض aap.xml كما هو موضح في اللقطة أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
{{< app/cells/assistant language="java" >}}
