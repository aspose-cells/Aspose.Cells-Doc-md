---
title: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions
type: docs
weight: 110
url: /es/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Escenarios de uso posibles**

Puede renderizar una secuencia de páginas de su archivo de Excel a imágenes utilizando Aspose.Cells con las propiedades [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) y [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount). Estas propiedades son útiles cuando hay muchas, por ejemplo, miles de páginas en su hoja de trabajo, pero solo desea representar algunas de ellas. Esto no solo ahorrará tiempo de procesamiento, sino que también ahorrará el consumo de memoria del proceso de renderizado.

## **Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**

El siguiente código de muestra carga el [archivo de Excel de muestra](55541781.xlsx) y renderiza solo las páginas 4, 5, 6 y 7 usando las propiedades [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) y [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount). Aquí se muestran las páginas generadas por el código.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
