---
title: Extracting OLE Objects from Worksheet
type: docs
weight: 10
url: /cpp/extracting-ole-objects-from-worksheet/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to extract all types of OLE objects from the worksheet. Please use [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) method to access all the OLE objects inside the worksheet. Each OLE object has [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) and [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) properties that can help you identify the type of OLE object and extract it successfully.
## **Extracting OLE Objects from Worksheet**
The following sample code loads the [sample Excel file](66519077.xlsx) which has three OLE objects. The code identifies the types of OLE objects and extracts them one by one as the following files.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
