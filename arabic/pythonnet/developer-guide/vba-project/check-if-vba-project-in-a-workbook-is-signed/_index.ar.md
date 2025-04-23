---
title: التحقق مما إذا كان مشروع VBA في كتاب عمل موقع بالتوقيع
type: docs
weight: 70
url: /ar/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

يمكنك التحقق مما إذا كان مشروع VBA الخاص بك موقّعًا أم لا باستخدام ميكروسوفت إكسل عبر أمر القائمة **Tools > Digital Signatures...**. بالمثل، يمكنك التحقق منه برمجياً باستخدام خاصية [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) من Aspose.Cells لبايثون via .NET.

{{% /alert %}}

## **التحقق مما إذا كان مشروع VBA في ملف عمل موقعًا في بايثون**

الكود التالي يحمل الكتاب ويتحقق مما إذا كان مشروع VBA الخاص به موقع بالتوقيع باستخدام خاصية [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). ستعيد الخاصية **true** إذا كان المشروع موقع بالتوقيع وإلا ستعيد **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

