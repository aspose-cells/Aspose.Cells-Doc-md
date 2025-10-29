---
title: نسخ مصمم مستخدم النموذج التقديمي للماكرو VBA من القالب إلى كتاب العمل الهدف
type: docs
weight: 130
url: /ar/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لبايثون via .NET بنسخ مشروع VBA من ملف إكسل إلى آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات النمطية، مثل المستند، الإجرائية، المصمم، وغيرها. يمكن نسخ جميع الوحدات بسهولة باستخدام كود بسيط، ولكن بالنسبة لوحدة المصمم، هناك بعض البيانات الإضافية تسمى تخزين المصمم والتي تحتاج إلى الوصول إليها أو نسخها. تتعامل الطريقتان التاليتان مع تخزين المصمم.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف**

يرجى الاطلاع على الكود العيني التالي. يقوم بنسخ مشروع VBA من [ملف Excel القالب](50528345.xlsm) إلى دفتر عمل فارغ ويحفظه باسم [ملف Excel الناتج](50528346.xlsm). إذا فتحت مشروع VBA داخل ملف Excel القالب، سترى استوديو المستخدم كما هو مبين أدناه. يتكون استوديو المستخدم من تصميم الاستوديو الذي سيتم نسخه باستخدام الأساليب [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) و [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

تُظهر اللقطة الشاشية التالية ملف Excel الناتج ومحتوياته التي تم نسخها من ملف Excel القالب. عند النقر فوق الزر 1، يفتح استوديو المستخدم VBA الذي بحد ذاته يحتوي على زر أمر يعرض صندوق رسائل عند النقر عليه.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
