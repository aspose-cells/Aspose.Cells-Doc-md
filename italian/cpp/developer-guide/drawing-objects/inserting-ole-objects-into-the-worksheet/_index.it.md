---
title: Inserimento di Oggetti OLE nel Foglio di Lavoro
type: docs
weight: 20
url: /it/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells ti consente di inserire un oggetto OLE all'interno del foglio di lavoro. Utilizzare il metodo [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) a questo scopo. Sarà necessario un array di byte dell'immagine che verrà utilizzato per inserire l'oggetto OLE all'interno del foglio di lavoro e byte di dati dell'oggetto OLE che rappresenteranno il tuo oggetto effettivo da inserire all'interno del foglio di lavoro. 
## **Inserimento di oggetti OLE nel foglio di lavoro**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Logo Aspose</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
