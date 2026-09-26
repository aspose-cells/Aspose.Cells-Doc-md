---  
title: Extracting OLE Objects from Worksheet  
type: docs  
weight: 10  
url: /go-cpp/extracting-ole-objects-from-worksheet/  
---  

## **Possible Usage Scenarios**  
Aspose.Cells allows you to extract all types of OLE objects from the worksheet. Please use [WorksheetGetOleObjects()](https://reference.aspose.com/cells/go-cpp/worksheet/getoleobjects/) method to access all the OLE objects inside the worksheet. Each OLE object has [ProgID](https://reference.aspose.com/cells/go-cpp/oleobject/getprogid/) and [ObjectData](https://reference.aspose.com/cells/go-cpp/oleobject/getobjectdata/) properties that can help you identify the type of OLE object and extract it successfully.  

## **Extracting OLE Objects from Worksheet**  
The following sample code loads the [sample Excel file](66519077.xlsx), which has three OLE objects. The code identifies the types of OLE objects and extracts them one by one, as the following files:  

- [outputExtractOleObject.pptx](66519080.pptx)  
- [outputExtractOleObject.pdf](66519079.pdf)  
- [outputExtractOleObject.docx](66519078.docx)  

## **Sample Code**  
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractingOleObjectsFromWorksheet.go" >}}  
{{< app/cells/assistant language="go" >}}
