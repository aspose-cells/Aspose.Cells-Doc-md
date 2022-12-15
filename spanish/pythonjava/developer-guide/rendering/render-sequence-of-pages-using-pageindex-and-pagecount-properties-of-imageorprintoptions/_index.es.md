---
title: Representar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions
type: docs
weight: 10
url: /es/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---
## **Representar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions**
Puede representar una secuencia de páginas de su archivo de Excel en imágenes usando Aspose.Cells con[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) y[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) propiedades. Estas propiedades son útiles cuando hay tantas, por ejemplo, miles de páginas en su hoja de trabajo, pero desea representar solo algunas de ellas. Esto no solo ahorrará tiempo de procesamiento, sino que también ahorrará el consumo de memoria del proceso de renderizado.

El siguiente código de muestra carga el archivo de muestra de Excel y representa solo las páginas 4, 5, 6 y 7 usando el[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex)y[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) propiedades. Las siguientes son las imágenes de las páginas renderizadas generadas por el código de muestra.

|![todo:imagen_alternativa_texto](outputImage-4.png)|![todo:imagen_alternativa_texto](outputImage-5.png)|
|:- |:- |
|![todo:imagen_alternativa_texto](outputImage-6.png)|![todo:imagen_alternativa_texto](outputImage-7.png)|



## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
