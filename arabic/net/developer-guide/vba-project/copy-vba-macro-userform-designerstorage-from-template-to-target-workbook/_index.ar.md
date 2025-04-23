---
title: نسخ مصمم مستخدم النموذج التقديمي للماكرو VBA من القالب إلى كتاب العمل الهدف
type: docs
weight: 130
url: /ar/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

تتيح Aspose.Cells لك نسخ مشروع VBA من ملف Excel إلى آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات مثل المستند والإجرائي والتصميم وما إلى ذلك. يمكن نسخ جميع الوحدات بكود بسيط ولكن بالنسبة للوحدة التصميمية، هناك بعض البيانات الإضافية تسمى تخزين المصمم التي يجب الوصول إليها أو نسخها. تدير الأساليب المطروحة التاليتان تخزين المصمم.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف**

يرجى الاطلاع على الكود العيني التالي. يقوم بنسخ مشروع VBA من [ملف Excel القالب](50528345.xlsm) إلى دفتر عمل فارغ ويحفظه باسم [ملف Excel الناتج](50528346.xlsm). إذا فتحت مشروع VBA داخل ملف Excel القالب، سترى استوديو المستخدم كما هو مبين أدناه. يتكون استوديو المستخدم من تصميم الاستوديو الذي سيتم نسخه باستخدام الأساليب [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) و [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

تُظهر اللقطة الشاشية التالية ملف Excel الناتج ومحتوياته التي تم نسخها من ملف Excel القالب. عند النقر فوق الزر 1، يفتح استوديو المستخدم VBA الذي بحد ذاته يحتوي على زر أمر يعرض صندوق رسائل عند النقر عليه.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
