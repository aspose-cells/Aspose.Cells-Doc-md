---
title: التحقق مما إذا كان كود VBA موقع بالتوقيع
type: docs
weight: 100
url: /ar/python-net/check-if-vba-code-is-signed/
---

{{% alert color="primary" %}}

يتيح Aspose.Cells لبايثون via .NET للمستخدم التحقق مما إذا كان مشروع شفرة VBA موقّعًا أم لا باستخدام الخاصية [**VbaProject.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed).

{{% /alert %}}

الكود التالي يوضح كيفية التحقق مما إذا كان كود VBA موقع بالتوقيع أم لا باستخدام خاصية [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). يمكنك استخدام أي من ملفات Excel الخاصة بك لاختبار هذا الكود. لأغراض الاختبار، يمكنك استخدام [هذا الملف Excel المستخدم في الكود](5115032.xlsm).

## **تحقق مما إذا كانت شفرة VBA موقعة في بايثون**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaCodeIsSigned.py" >}}

## مخرج الكونسول

أدناه مخرج الكونسول للكود أعلاه باستخدام [ملف Excel عينة](5115032.xlsm) المقدم من خلال الرابط.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
