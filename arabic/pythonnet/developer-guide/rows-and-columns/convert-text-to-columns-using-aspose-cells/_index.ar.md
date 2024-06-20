---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/python-net/convert-text-to-columns-using-aspose-cells/
description: توضح هذه المقالة كيفية تحويل النص إلى أعمدة باستخدام Aspose.Cells لـ Python via .NET API.
keywords: مكتبة Python Excel، تحويل النص إلى أعمدة باستخدام Python، تحويل النص إلى أعمدة في Python.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحويل نصك إلى أعمدة باستخدام Microsoft Excel. هذه الميزة متوفرة من خلال *أدوات البيانات* تحت علامة *البيانات*. من أجل تقسيم محتويات العمود إلى عمودين أو أكثر، يجب أن يحتوي البيانات على فاصل محدد مثل فاصلة (أو أي حرف آخر) بناءً على الذي يقسم Microsoft Excel محتويات الخلية إلى خلايا متعددة. توفر أيضًا Aspose.Cells لـ Python via .NET هذه الميزة عبر الطريقة [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/).

## **تحويل النص إلى أعمدة باستخدام Aspose.Cells لمكتبات Python Excel**

يشرح الكود النموذجي التالي استخدام الطريقة [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/). يضيف الكود أولاً بعض أسماء الأشخاص في العمود A من الورقة العمل الأولى. ثم يطبق الطريقة [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) على العمود A ويحفظه كملف إكسل مخرج. إذا فتحت [ملف Excel الناتج](25395213.xlsx), سترى أن الأسماء الأولى في العمود A بينما الأسماء الأخيرة في العمود B كما هو موضح في هذا اللقطة.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
