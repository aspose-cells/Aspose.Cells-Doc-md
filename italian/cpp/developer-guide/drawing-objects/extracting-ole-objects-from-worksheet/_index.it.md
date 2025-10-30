---
title: Estrazione di Oggetti OLE dal Foglio di Lavoro
type: docs
weight: 10
url: /it/cpp/extracting-ole-objects-from-worksheet/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells consente di estrarre tutti i tipi di oggetti OLE dal foglio di lavoro. Si prega di utilizzare il metodo [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) per accedere a tutti gli oggetti OLE all'interno del foglio di lavoro. Ogni oggetto OLE ha le proprietà [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) e [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) che possono aiutarti a identificare il tipo di oggetto OLE ed estrarlo con successo.
## **Estrazione di Oggetti OLE dal Foglio di Lavoro**
Il seguente codice di esempio carica il [file Excel di esempio](66519077.xlsx) che contiene tre oggetti OLE. Il codice identifica i tipi di oggetti OLE e li estrae uno per uno come i seguenti file.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
