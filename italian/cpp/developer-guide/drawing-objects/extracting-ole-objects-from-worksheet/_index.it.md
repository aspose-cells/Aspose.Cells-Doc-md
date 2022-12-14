---
title: Estrazione di oggetti OLE dal foglio di lavoro
type: docs
weight: 10
url: /it/cpp/extracting-ole-objects-from-worksheet/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells consente di estrarre tutti i tipi di oggetti OLE dal foglio di lavoro. Si prega di utilizzare[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) metodo per accedere a tutti gli oggetti OLE all'interno del foglio di lavoro. Ogni oggetto OLE ha[ProgID](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) e[ObjectData](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)proprietà che consentono di identificare il tipo di oggetto OLE ed estrarlo correttamente.
## **Estrazione di oggetti OLE dal foglio di lavoro**
 Il codice di esempio seguente carica il file[esempio di file Excel](66519077.xlsx) che ha tre oggetti OLE. Il codice identifica i tipi di oggetti OLE e li estrae uno per uno come i seguenti file.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
