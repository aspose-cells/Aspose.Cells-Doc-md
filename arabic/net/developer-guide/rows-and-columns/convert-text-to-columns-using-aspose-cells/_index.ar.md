---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/net/convert-text-to-columns-using-aspose-cells/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحويل نصك إلى أعمدة باستخدام برنامج Microsoft Excel. تتوفر هذه الميزة من خلال أدوات البيانات تحت علامة تبويب البيانات. من أجل تقسيم محتويات العمود إلى أعمدة متعددة, يجب أن يحتوي البيانات على فاصل محدد مثل الفاصلة (أو أي حرف آخر) على أساسه يقوم Microsoft Excel بتقسيم محتويات الخلية إلى خلايا متعددة. توفر Aspose.Cells أيضاً هذه الميزة من خلال الطريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns).

## **تحويل النص إلى أعمدة باستخدام Aspose.Cells**

يشرح الكود النموذجي التالي استخدام الطريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns). يضيف الكود أولاً بعض أسماء الأشخاص في العمود A من الورقة العمل الأولى. ثم يطبق الطريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) على العمود A ويحفظه كملف إكسل مخرج. إذا فتحت [ملف Excel الناتج](25395213.xlsx), سترى أن الأسماء الأولى في العمود A بينما الأسماء الأخيرة في العمود B كما هو موضح في هذا اللقطة.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
{{< app/cells/assistant language="csharp" >}}
