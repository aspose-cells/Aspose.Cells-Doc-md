---
title: نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف
type: docs
weight: 130
url: /ar/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

يسمح لك Aspose.Cells بنسخ مشروع VBA من ملف Excel إلى ملف Excel آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات ، مثل مستند ، إجرائي ، مصمم ، إلخ. يمكن نسخ جميع الوحدات النمطية برمز بسيط ولكن بالنسبة لوحدة المصمم ، هناك بعض البيانات الإضافية التي تسمى التخزين المصمم والتي تحتاج إلى الوصول إليها أو نسخها. تتعامل الطريقتان التاليتان مع Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage ()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage ()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف**

يرجى الاطلاع على نموذج التعليمات البرمجية التالي. يقوم بنسخ مشروع VBA من ملف[نموذج ملف Excel](50528345.xlsm) في مصنف فارغ ويحفظه كملف[إخراج ملف Excel](50528346.xlsm). إذا فتحت مشروع VBA داخل ملف Excel النموذجي ، فسترى نموذج مستخدم كما هو موضح أدناه. يتكون نموذج المستخدم من Designer Storage ، لذا سيتم نسخه باستخدام[**VbaModuleCollection.GetDesignerStorage ()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)و[**VbaModuleCollection.AddDesignerStorage ()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)طُرق.

**! [todo: image_alt_text] (copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

تُظهر لقطة الشاشة التالية ملف Excel الناتج ومحتوياته التي تم نسخها من ملف Excel النموذجي. عند النقر فوق الزر 1 ، فإنه يفتح نموذج مستخدم VBA الذي يحتوي في حد ذاته على زر أمر يعرض مربع رسالة عند النقر عليه.

**! [todo: image_alt_text] (copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
