---
title: الوصول إلى أجزاء النص المنسق لـ Cell وتحديثها
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/net/access-and-update-the-portions-of-rich-text-of-cell/
description: تعرف على كيفية الوصول إلى أجزاء النص المنسق وتحديثها من Cell من خلال Aspose.Cells for .NET API.
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells يسمح لك بالوصول إلى أجزاء النص الغني للخلية وتحديثها. لهذا الغرض، يمكنك استخدام[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طُرق. ستعود هذه الأساليب وتقبل مجموعة من[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)الكائنات التي يمكنك استخدامها للوصول إلى خصائص الخط المختلفة وتحديثها مثل اسم الخط ولون الخط والخط الغامق وما إلى ذلك.

{{% /alert %}}

##  **الوصول إلى أجزاء النص المنسق لـ Cell وتحديثها**

 الكود التالي يوضح استخدام[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طريقة باستخدام[ملف اكسيل المصدر](5112369.xlsx) والتي يمكنك تنزيلها من الرابط المقدم. يحتوي ملف Excel المصدر على نص منسق في الخلية A1. يحتوي على 3 أجزاء وكل جزء له خط مختلف. يصل مقتطف التعليمات البرمجية التالي إلى هذه الأجزاء ويقوم بتحديث الجزء الأول باسم خط جديد. وأخيرا، فإنه يحفظ المصنف باسم[إخراج ملف إكسل](5112366.xlsx). عندما تفتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى *"Arial"**.

###  رمز C# للوصول إلى أجزاء النص المنسق لـ Cell وتحديثها

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### إخراج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

 فيما يلي إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه باستخدام ملف[ملف اكسيل المصدر](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

