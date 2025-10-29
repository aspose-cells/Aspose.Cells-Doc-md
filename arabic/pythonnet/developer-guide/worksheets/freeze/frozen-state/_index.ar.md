---
title: كيفية التحقق من حالة التعليق دون إكسل.
linktitle: الحالة المجمدة
type: docs
weight: 190
url: /ar/python-net/how-to-check-frozen-state-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية التحقق من حالة التجميد لورقة عمل إكسل برمجياً باستخدام Aspose.Cells لـ Python via .NET APIs.
keywords: مكتبة إكسل بايثون، بايثون كيفية التحقق من الحالة دون إكسل، التحقق من الحالة دون إكسل في بايثون.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية التحقق من حالة التجميد لورقة عمل إكسل برمجياً. يمكننا ببساطة معرفة ما إذا كانت الورقة مجمدة أم مقسمة في MS Excel. لكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أو مقسمة باستخدام CSharp. يمكننا ببساطة القيام بذلك باستخدام Aspose.Cells لـ Python via .NET.

## **كيفية التحقق من الحالة المجمدة**
باستخدام Aspose.Cells لـ Python via .NET، يمكننا التحقق مما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة المقفلة.

يرجى استخدام الخاصية [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) لفحص حالة النوافذ 
والحصول على الصفوف والأعمدة المقفلة باستخدام الطريقة [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. إنشاء سجل العمل لفتح الملف.
2. التحقق ما إذا كانت ورقة العمل مجمدة.
3. الحصول على الصفوف والأعمدة المقفلة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
