---
title: تقديم ورقة العمل إلى السياق الرسومي
type: docs
weight: 300
url: /ar/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

يمكن الآن لـ Aspose.Cells تقديم ورقة العمل إلى السياق الرسومي. يمكن أن يكون السياق الرسومي أي شيء مثل ملف صورة أو الشاشة أو الطابعة إلخ. يرجى استخدام أحد الأساليب التاليتين لتقديم ورقة العمل إلى السياق الرسومي.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

الشفرة العينية التالية توضح كيفية استخدام Aspose.Cells لتقديم ورقة العمل إلى السياق الرسومي. بمجرد تنفيذ الشفرة، ستقوم بطباعة الورقة بأكملها وتقوم بملء المساحة الفارغة المتبقية باللون الأزرق في السياق الرسومي وحفظ الصورة باسم ملف **OutputImage_out_.png**. يمكنك استخدام أي ملف Excel مصدر لتجربة هذا الشفرة. يُرجى أيضًا قراءة التعليقات داخل الشفرة لفهم أفضل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
