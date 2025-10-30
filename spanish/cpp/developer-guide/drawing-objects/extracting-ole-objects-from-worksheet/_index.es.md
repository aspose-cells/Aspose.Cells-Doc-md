---
title: Extracción de objetos OLE de la hoja de cálculo
type: docs
weight: 10
url: /es/cpp/extracting-ole-objects-from-worksheet/
---

## **Escenarios de uso posibles**
Aspose.Cells le permite extraer todo tipo de objetos OLE de la hoja de cálculo. Utilice el método [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) para acceder a todos los objetos OLE dentro de la hoja de cálculo. Cada objeto OLE tiene las propiedades [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) y [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) que pueden ayudarle a identificar el tipo de objeto OLE y extraerlo con éxito.
## **Extracción de objetos OLE de la hoja de cálculo**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](66519077.xlsx) que tiene tres objetos OLE. El código identifica los tipos de objetos OLE y los extrae uno por uno como los siguientes archivos.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
