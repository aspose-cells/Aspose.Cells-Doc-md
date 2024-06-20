---
title: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions
type: docs
weight: 100
url: /es/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Escenarios de uso posibles**

Puede renderizar una secuencia de páginas de su archivo de Excel a imágenes utilizando Aspose.Cells con las propiedades [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) y [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Estas propiedades son útiles cuando hay muchas, por ejemplo, miles de páginas en su hoja de cálculo pero solo desea renderizar algunas de ellas. Esto no solo ahorrará tiempo de procesamiento, sino que también reducirá el consumo de memoria del proceso de renderizado.

## **Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](55541812.xlsx) y renderiza solo las páginas 4, 5, 6 y 7 utilizando las propiedades [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) y [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Aquí están las páginas renderizadas generadas por el código.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}
