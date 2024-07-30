---
title: كيفية التحقق من حالة التجميد دون استخدام Excel.
linktitle: الحالة المجمدة
type: docs
weight: 190
url: /ar/python-net/how-to-check-frozen-state-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية فحص حالة تجميد ورقة العمل في Excel بشكل برمجي باستخدام Aspose.Cells for Python via .NET.
keywords: مكتبة Excel بالبايثون, كيفية التحقق من حالة التجميد بدون Excel, التحقق من حالة التجميد بدون Excel بالبايثون.
---

## **مقدمة**

في هذه المقالة، سنتعلم كيفية فحص حالة تجميد ورقة العمل في Excel بشكل برمجي. يمكننا ببساطة معرفة ما إذا كانت ورقة العمل مجمدة أم مقسمة في MS Excel. ولكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أم مقسمة باستخدام CSharp. يمكننا ببساطة القيام بذلك باستخدام Aspose.Cells for Python via .NET.

## **كيفية التحقق من حالة التجميد**
مع Aspose.Cells for Python via .NET، يمكننا التحقق مما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة المقفلة.

يرجى استخدام الخاصية [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) لفحص حالة النوافذ 
والحصول على الصفوف والأعمدة المقفلة باستخدام الطريقة [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. إنشاء سجل العمل لفتح الملف.
2. التحقق ما إذا كانت ورقة العمل مجمدة.
3. الحصول على الصفوف والأعمدة المقفلة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
