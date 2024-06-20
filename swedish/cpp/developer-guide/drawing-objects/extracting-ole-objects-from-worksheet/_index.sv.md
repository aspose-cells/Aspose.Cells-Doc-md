---
title: Extrahera OLE objekt från arbetsbladet
type: docs
weight: 10
url: /sv/cpp/extracting-ole-objects-from-worksheet/
---

## **Möjliga användningsscenario**
Aspose.Cells gör att du kan extrahera alla typer av OLE-objekt från arbetsbladet. Använd [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) metoden för att komma åt alla OLE-objekt inne i arbetsbladet. Varje OLE-objekt har [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) och [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) egenskaper som kan hjälpa dig att identifiera typen av OLE-objekt och extrahera det framgångsrikt.
## **Extrahera OLE-objekt från arbetsbladet**
Följande exempelkod laddar den [exempelfil i Excel](66519077.xlsx) som har tre OLE-objekt. Koden identifierar typerna av OLE-objekt och extraherar dem en efter en som följande filer.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
