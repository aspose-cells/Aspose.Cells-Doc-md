---
title: Inserimento di oggetti OLE nel foglio di lavoro
type: docs
weight: 20
url: /it/cpp/inserting-ole-objects-into-the-worksheet/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells permette di inserire un oggetto OLE all'interno del foglio di lavoro. Si prega di utilizzare[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)metodo per questo scopo. Avrai bisogno di un array di byte dell'immagine che verrà utilizzato per inserire l'oggetto OLE all'interno del foglio di lavoro e dei byte di dati dell'oggetto Ole che saranno il tuo oggetto reale. Per inserire l'oggetto Ole all'interno del foglio di lavoro.
## **Inserimento di oggetti OLE nel foglio di lavoro**
 Il seguente codice di esempio crea l'oggetto cartella di lavoro, inserisce l'oggetto Ole all'interno del primo foglio di lavoro e lo salva con nome[file Excel di output](66519074.xlsx) . Si prega di consultare il[Aspose Logo](66519075.png) usato come byte immagine e[inserire il file Excel](66519081.xlsx) utilizzato come dati oggetto Ole all'interno del codice per riferimento.
## **Codice di esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
