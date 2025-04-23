---
title: Renderizar hoja de cálculo en contexto gráfico
type: docs
weight: 300
url: /es/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells ahora puede renderizar la hoja de cálculo al contexto gráfico. El contexto gráfico puede ser cualquier cosa como un archivo de imagen, pantalla o impresora, etc. Utilice uno de los siguientes dos métodos para renderizar la hoja de cálculo al contexto gráfico.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

El siguiente código ilustra cómo utilizar Aspose.Cells para renderizar la hoja de cálculo al contexto gráfico. Una vez que ejecutes el código, imprimirá la hoja de cálculo completa y rellenará el espacio vacío restante con color azul en el contexto gráfico y guardará la imagen como archivo **OutputImage_out_.png**. Puedes probar este código con cualquier archivo de Excel de origen. Por favor, también lee los comentarios dentro del código para una mejor comprensión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
{{< app/cells/assistant language="csharp" >}}
