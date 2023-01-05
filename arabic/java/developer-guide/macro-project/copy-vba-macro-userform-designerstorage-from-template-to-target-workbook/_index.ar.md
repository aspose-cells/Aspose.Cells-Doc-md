---
title: نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف
type: docs
weight: 60
url: /ar/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

يسمح لك Aspose.Cells بنسخ مشروع VBA من ملف Excel إلى ملف Excel آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات ، مثل مستند ، إجرائي ، مصمم إلخ. يمكن نسخ جميع الوحدات برمز بسيط ولكن بالنسبة لوحدة المصمم ، هناك بعض البيانات الإضافية التي تسمى التخزين المصمم والتي تحتاج إلى الوصول إليها أو نسخها. تتعامل الطريقتان التاليتان مع Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف**

يرجى الاطلاع على نموذج التعليمات البرمجية التالي. يقوم بنسخ مشروع VBA من ملف[نموذج ملف Excel](50528367.xlsm)في مصنف فارغ ويحفظه كملف[إخراج ملف Excel](50528366.xlsm). إذا فتحت مشروع VBA داخل ملف Excel النموذجي ، فسترى نموذج مستخدم كما هو موضح أدناه. يتكون نموذج المستخدم من Designer Storage ، لذا سيتم نسخه باستخدام[**VbaModuleCollection.GetDesignerStorage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) و[**VbaModuleCollection.AddDesignerStorage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) أساليب.

![ما يجب القيام به: image_بديل_نص](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

تُظهر لقطة الشاشة التالية ملف Excel الناتج ومحتوياته التي تم نسخها من ملف Excel النموذجي. عند النقر فوق الزر 1 ، فإنه يفتح نموذج مستخدم VBA الذي يحتوي في حد ذاته على زر أمر يعرض مربع رسالة عند النقر عليه.

![ما يجب القيام به: image_بديل_نص](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
