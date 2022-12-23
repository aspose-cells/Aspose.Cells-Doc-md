---
title: تقديم ورقة العمل إلى سياق رسومي
type: docs
weight: 300
url: /ar/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells يمكنه الآن عرض ورقة العمل لسياق بياني. يمكن أن يكون سياق الرسوم أي شيء مثل ملف الصورة أو الشاشة أو الطابعة وما إلى ذلك. يُرجى استخدام إحدى الطريقتين التاليتين لعرض ورقة العمل في سياق رسومي.

- [**SheetRender.ToImage (int pageIndex ، Graphics g ، float x ، float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage (int pageIndex، Graphics g، float x، float y، float width، float width، float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 يوضح الكود التالي كيفية استخدام Aspose.Cells لتقديم ورقة العمل إلى سياق رسومي. بمجرد تنفيذ التعليمات البرمجية ، ستقوم بطباعة ورقة العمل بأكملها وملء المساحة الفارغة المتبقية باللون الأزرق في سياق الرسومات وحفظ الصورة باسم**OutputImage_out_.png** ملف. يمكنك استخدام أي ملف اكسل المصدر لتجربة هذا الكود. يرجى أيضًا قراءة التعليقات الموجودة داخل الكود لفهم أفضل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
