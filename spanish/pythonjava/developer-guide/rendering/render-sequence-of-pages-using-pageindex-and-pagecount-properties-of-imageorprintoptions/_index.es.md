---
title: Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions
type: docs
weight: 10
url: /es/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**
Puede renderizar una secuencia de páginas de su archivo de Excel a imágenes utilizando Aspose.Cells con las propiedades [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) y [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Estas propiedades son útiles cuando hay muchas páginas, por ejemplo, miles de páginas en su hoja de cálculo, pero solo desea renderizar algunas de ellas. Esto no solo ahorrará tiempo de procesamiento, sino que también ahorrará el consumo de memoria del proceso de renderizado.

El siguiente código de muestra carga el archivo de Excel de muestra y renderiza solo las páginas 4, 5, 6 y 7 utilizando las propiedades [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) y [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Las siguientes son las imágenes de las páginas renderizadas generadas por el código de muestra.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
