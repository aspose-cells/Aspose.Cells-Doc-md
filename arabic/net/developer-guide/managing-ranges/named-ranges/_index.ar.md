---
title: إنشاء نطاقات مسماة لمصنف العمل وورقة العمل
linktitle: النطاق المسمى
type: docs
weight: 40
url: /ar/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بتحديد مجالات مسماة بنطاقين مختلفين: نطاق العمل (المعروف أيضا باسم نطاق عالمي) ونطاق الورقة العمل.

- يمكن الوصول إلى مجالات مسماة ذات نطاق العمل من أي ورقة عمل ضمن هذا المصنف ببساطة عن طريق استخدام اسمها.
- تتم الوصول إلى مجالات المسميات ذات نطاق ورقة العمل باستخدام مرجع لورقة العمل المعينة التي تم إنشاء المسمى فيها.

يوفر Aspose.Cells نفس الوظائف كما في Microsoft Excel لإضافة نطاقات مسماة في نطاق كتيب أو ورق العمل. عند إنشاء نطاق بتسمية نطاق ورق العمل، يجب استخدام مرجع ورق العمل في النطاق المسمى لتحديده كنطاق مسمى بنطاق ورق العمل.

{{% /alert %}} 
## **إضافة نطاق مسمى بنطاق سجل العمل**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **إضافة نطاق مسمى بنطاق ورق العمل**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **مواضيع متقدمة**
- [إنشاء الوصول ونسخ نطاقات مسماة](/cells/ar/net/create-access-and-copy-named-ranges/)
- [تنسيق وتعديل نطاقات مسماة](/cells/ar/net/format-and-modify-named-ranges/)
- [الحصول على نطاق مع روابط خارجية](/cells/ar/net/get-range-with-external-links/)
- [تنفيذ نطاقات غير متتابعة](/cells/ar/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
