---
title: Infoga OLE objekt i arbetsbladet
type: docs
weight: 20
url: /sv/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Möjliga användningsscenario**
Aspose.Cells låter dig infoga ett OLE-objekt i arbetsbladet. Använd [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) metoden för detta ändamål. Du behöver en bildbytesarray som kommer att användas för att infoga OLE-objektet i arbetsbladet och OLE-objektets databytes som kommer att vara ditt faktiska objekt för att infoga OLE-objektet i arbetsbladet. 
## **Infoga OLE-objekt i arbetsbladet**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose logo</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
