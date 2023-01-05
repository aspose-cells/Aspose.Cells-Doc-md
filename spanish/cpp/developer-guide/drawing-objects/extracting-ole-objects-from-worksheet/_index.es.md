---
title: Extracción de objetos OLE de la hoja de trabajo
type: docs
weight: 10
url: /es/cpp/extracting-ole-objects-from-worksheet/
---
## **Posibles escenarios de uso**
 Aspose.Cells le permite extraer todo tipo de objetos OLE de la hoja de trabajo. Por favor use[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) método para acceder a todos los objetos OLE dentro de la hoja de trabajo. Cada objeto OLE tiene[ID de programa](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) y[ObjetoDatos](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)propiedades que pueden ayudarlo a identificar el tipo de objeto OLE y extraerlo con éxito.
## **Extracción de objetos OLE de la hoja de trabajo**
 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](66519077.xlsx) que tiene tres objetos OLE. El código identifica los tipos de objetos OLE y los extrae uno por uno como los siguientes archivos.

- [salidaExtraerOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
