---
title: قم بالوصول إلى أجزاء النص المنسق وتحديثها في Cell
linktitle: نص منسق
type: docs
weight: 40
url: /ar/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells يسمح لك بالتوصل وتحديث أجزاء النص المنسق للخانة. لهذا الغرض ، يمكنك استخدام[**Cell. احصل على الأحرف ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و[**مجموعة الأحرف ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) أساليب. ستعود هذه التوابع وتقبل مصفوفة[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)العناصر التي يمكنك استخدامها للوصول إلى الخصائص المختلفة للخط وتحديثها مثل اسم الخط ولون الخط والجرأة وما إلى ذلك.

{{% /alert %}}

## **قم بالوصول إلى أجزاء النص المنسق وتحديثها في Cell**

 يوضح الكود التالي استخدام[**Cell. احصل على الأحرف ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و[**مجموعة الأحرف ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طريقة استخدام[ملف اكسل المصدر](5112369.xlsx)والتي يمكنك تنزيلها من الرابط المقدم. يحتوي ملف Excel المصدر على نص منسق في الخلية A1. يحتوي على 3 أجزاء ولكل جزء خط مختلف. يصل مقتطف التعليمات البرمجية التالي إلى هذه الأجزاء ويقوم بتحديث الجزء الأول باسم خط جديد. أخيرًا ، يحفظ المصنف باسم[ملف اكسل الناتج](5112366.xlsx) . عندما تفتحه ، ستجد أن خط الجزء الأول من النص قد تغير إلى**"اريال"**.

### C# كود للوصول إلى أجزاء نص منسق وتحديثها من Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### ناتج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه باستخدام[ملف اكسل المصدر](5112369.xlsx).

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

