---
title: Рендеринг рабочего листа в графическом контексте
type: docs
weight: 300
url: /ru/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells теперь может отображать рабочий лист в графическом контексте. Графический контекст может быть чем угодно, например, файлом изображения, экраном, принтером и т. д. Используйте один из следующих двух методов для преобразования рабочего листа в графический контекст.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage (int pageIndex, Graphics g, float x, float y, ширина float, высота float)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 В следующем коде показано, как использовать Aspose.Cells для отображения рабочего листа в графическом контексте. Как только вы выполните код, он распечатает весь рабочий лист и заполнит оставшееся пустое пространство синим цветом в графическом контексте и сохранит изображение как**Выходное изображение_out_.png** файл. Вы можете использовать любой исходный файл Excel, чтобы попробовать этот код. Также прочитайте комментарии внутри кода для лучшего понимания.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
