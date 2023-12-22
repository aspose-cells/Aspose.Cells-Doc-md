---
title: Extracción de objetos OLE de la hoja de trabajo
type: docs
weight: 10
url: /es/cpp/extracting-ole-objects-from-worksheet/
---
##  **Posibles escenarios de uso**
 Aspose.Cells le permite extraer todo tipo de objetos OLE de la hoja de trabajo. Por favor use[Hoja de trabajo->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) método para acceder a todos los objetos OLE dentro de la hoja de trabajo. Cada objeto OLE tiene[ID de programa](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) y[Datos de objeto](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)propiedades que pueden ayudarle a identificar el tipo de objeto OLE y extraerlo correctamente.
##  **Extracción de objetos OLE de la hoja de trabajo**
 El siguiente código de muestra carga el[archivo de Excel de muestra](66519077.xlsx) que tiene tres objetos OLE. El código identifica los tipos de objetos OLE y los extrae uno por uno como los siguientes archivos.

- [salidaExtractOleObject.pptx](66519080.pptx)
- [salidaExtractOleObject.pdf](66519079.pdf)
- [salidaExtractOleObject.docx](66519078.docx)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
