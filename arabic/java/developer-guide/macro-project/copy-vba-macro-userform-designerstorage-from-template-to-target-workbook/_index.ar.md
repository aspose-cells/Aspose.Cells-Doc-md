---
title: نسخ مصمم مستخدم النموذج التقديمي للماكرو VBA من القالب إلى كتاب العمل الهدف
type: docs
weight: 60
url: /ar/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

تسمح Aspose.Cells لك بنسخ مشروع VBA من ملف Excel واحد إلى ملف Excel آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات مثل المستند والوظيفة والمصمم وما إلى ذلك. يمكن نسخ جميع الوحدات بكود بسيط ولكن بالنسبة لوحدة المصمم، هناك بعض البيانات الإضافية تسمى تخزين المصمم التي يجب الوصول إليها أو نسخها. تتعامل الطرقتان التاليتان مع تخزين المصمم.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف**

يرجى الاطلاع على الشفرة النموذجية التالية. تقوم بنسخ مشروع VBA من [ملف Excel النموذجي](50528367.xlsm) إلى مصنف فارغ وتحفظه كـ [ملف Excel الناتج](50528366.xlsm). إذا فتحت المشروع VBA داخل ملف Excel النموذجي، سترى نموذج مستخدم كما هو موضح أدناه. يتألف نموذج المستخدم من مخزن المصمم، لذا سيتم نسخه باستخدام الطرق [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) و [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-).

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

تُظهر الصورة الشاشية التالية ملف Excel الناتج ومحتوياته التي تم نسخها من ملف Excel النموذجي. عند النقر فوق Button 1 ، يفتح نافذة المشروع الماكرو VBA التي تحتوي بدورها على زر أمر يعرض مربع رسالة عند النقر.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
