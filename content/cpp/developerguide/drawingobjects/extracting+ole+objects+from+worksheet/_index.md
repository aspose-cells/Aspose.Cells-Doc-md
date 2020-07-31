---
title : "Extracting OLE Objects from Worksheet" 
description : "" 
weight : 12067 
toc : false
type: docs
url: /cpp/developerguide/drawingobjects/extracting+ole+objects+from+worksheet/
---

# Aspose.Cells for C++ : Extracting OLE Objects from Worksheet


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Extracting OLE Objects from Worksheet](#extracting-ole-objects-from-worksheet)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells allows you to extract all types of OLE objects from the worksheet. Please use [IWorksheet->GetIOleObjects()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/#a4c59d95cdd871ecfe18274480831a728) method to access all the OLE objects inside the worksheet. Each OLE object has [ProgID](https://apireference.aspose.com/cpp/cells/class/aspose.cells.drawing.i_ole_object/#abb2ea6872025fe4724d9613cd6b81752) and [ObjectData](https://apireference.aspose.com/cpp/cells/class/aspose.cells.drawing.i_ole_object/#a4a200a03478d3553798360cd6a911d70) properties that can help you identify the type of OLE object and extract it successfully.

## Extracting OLE Objects from Worksheet

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/cpp/attachments/66257169/66519077.xlsx) which has three OLE objects. The code identifies the types of OLE objects and extracts them one by one as the following files.

*   [outputExtractOleObject.pptx](https://docs2.aspose.com/cells/cpp/attachments/66257169/66519080.pptx)
*   [outputExtractOleObject.pdf](https://docs2.aspose.com/cells/cpp/attachments/66257169/66519079.pdf)
*   [outputExtractOleObject.docx](https://docs2.aspose.com/cells/cpp/attachments/66257169/66519078.docx)

## Sample Code

