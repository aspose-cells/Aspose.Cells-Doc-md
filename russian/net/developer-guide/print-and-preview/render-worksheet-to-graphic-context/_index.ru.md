---
title: Отобразить Рабочий лист на графический контекст
type: docs
weight: 300
url: /ru/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Теперь Aspose.Cells может воспроизводить рабочий лист в графическом контексте. Графический контекст может быть чем угодно, например, файлом изображения, экраном или принтером и т. д. Пожалуйста, используйте один из следующих двух методов для воспроизведения рабочего листа в графическом контексте.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

Следующий код показывает, как использовать Aspose.Cells для воспроизведения рабочего листа в графическом контексте. После выполнения кода он напечатает весь рабочий лист и заполнит оставшееся пустое место синим цветом в графическом контексте и сохранит изображение как файл **OutputImage_out_.png**. Вы можете использовать любой исходный файл Excel для проверки этого кода. Пожалуйста, также прочитайте комментарии внутри кода для лучшего понимания.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
{{< app/cells/assistant language="csharp" >}}
