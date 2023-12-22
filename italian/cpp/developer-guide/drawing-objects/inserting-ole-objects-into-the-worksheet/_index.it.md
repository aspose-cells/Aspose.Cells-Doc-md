---
title: Inserimento di oggetti OLE nel foglio di lavoro
type: docs
weight: 20
url: /it/cpp/inserting-ole-objects-into-the-worksheet/
---
##  **Possibili scenari di utilizzo**
 Aspose.Cells permette di inserire un oggetto OLE all'interno del foglio di lavoro. Si prega di utilizzare[Foglio di lavoro->GetOleObjects()->Aggiungi()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/)metodo a questo scopo. Avrai bisogno di un array di byte immagine che verrà utilizzato per inserire l'oggetto OLE all'interno del foglio di lavoro e di byte di dati dell'oggetto Ole che saranno il tuo oggetto reale. Per inserire l'oggetto Ole all'interno del foglio di lavoro.
##  **Inserimento di oggetti OLE nel foglio di lavoro**
 Il codice di esempio seguente crea l'oggetto cartella di lavoro, inserisce l'oggetto Ole nel primo foglio di lavoro e lo salva con nome[file Excel di output](66519074.xlsx) . Si prega di consultare il<a href="66519075.png" download="66519075.png">AsposeLogo</a> utilizzati come byte immagine e[inserire il file Excel](66519081.xlsx)utilizzato come dati oggetto Ole all'interno del codice come riferimento.
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
