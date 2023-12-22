---
title: Estrazione di oggetti OLE dal foglio di lavoro
type: docs
weight: 10
url: /it/cpp/extracting-ole-objects-from-worksheet/
---
##  **Possibili scenari di utilizzo**
 Aspose.Cells consente di estrarre tutti i tipi di oggetti OLE dal foglio di lavoro. Si prega di utilizzare[Foglio di lavoro->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) metodo per accedere a tutti gli oggetti OLE all'interno del foglio di lavoro. Ogni oggetto OLE ha[ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) E[ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)proprietà che possono aiutarti a identificare il tipo di oggetto OLE ed estrarlo correttamente.
##  **Estrazione di oggetti OLE dal foglio di lavoro**
 Il codice di esempio seguente carica il file[file Excel di esempio](66519077.xlsx) che ha tre oggetti OLE. Il codice identifica i tipi di oggetti OLE e li estrae uno per uno come i seguenti file.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
