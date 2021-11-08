---
title: Extracting OLE Objects from Worksheet
type: docs
weight: 10
url: /cpp/extracting-ole-objects-from-worksheet/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to extract all types of OLE objects from the worksheet. Please use [IWorksheet->GetIOleObjects()](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) method to access all the OLE objects inside the worksheet. Each OLE object has [ProgID](https://apireference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) and [ObjectData](https://apireference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70) properties that can help you identify the type of OLE object and extract it successfully.
## **Extracting OLE Objects from Worksheet**
The following sample code loads the [sample Excel file](66519077.xlsx) which has three OLE objects. The code identifies the types of OLE objects and extracts them one by one as the following files.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
