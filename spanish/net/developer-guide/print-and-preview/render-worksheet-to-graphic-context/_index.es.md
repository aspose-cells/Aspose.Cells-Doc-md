---
title: Renderizar la hoja de trabajo al contexto gráfico
type: docs
weight: 300
url: /es/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells ahora puede representar la hoja de trabajo en un contexto gráfico. El contexto gráfico puede ser cualquier cosa, como un archivo de imagen, una pantalla o una impresora, etc. Utilice uno de los dos métodos siguientes para convertir la hoja de trabajo en un contexto gráfico.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 El siguiente código ilustra cómo usar Aspose.Cells para representar la hoja de trabajo en un contexto gráfico. Una vez que ejecute un código, imprimirá toda la hoja de trabajo y llenará el espacio vacío sobrante con color azul en el contexto de gráficos y guardará la imagen como**OutputImage_out_.png** expediente. Puede usar cualquier archivo fuente de Excel para probar este código. Lea también los comentarios dentro del código para una mejor comprensión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
