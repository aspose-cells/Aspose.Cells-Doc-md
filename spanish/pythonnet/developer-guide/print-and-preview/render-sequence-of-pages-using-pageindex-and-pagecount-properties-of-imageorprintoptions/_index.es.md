---
title: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions
type: docs
weight: 110
url: /es/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Escenarios de uso posibles**

Puedes renderizar una secuencia de páginas de tu archivo de Excel a imágenes usando Aspose.Cells para Python via .NET con las propiedades [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) y [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Estas propiedades son útiles cuando hay muchas páginas, por ejemplo, miles, en tu hoja de cálculo, pero solo quieres renderizar algunas de ellas. Esto no solo ahorra tiempo de procesamiento sino también consumo de memoria durante el proceso de renderizado.

## **Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**

El siguiente código de muestra carga el [archivo de Excel de muestra](55541781.xlsx) y renderiza solo las páginas 4, 5, 6 y 7 usando las propiedades [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) y [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Aquí se muestran las páginas generadas por el código.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
