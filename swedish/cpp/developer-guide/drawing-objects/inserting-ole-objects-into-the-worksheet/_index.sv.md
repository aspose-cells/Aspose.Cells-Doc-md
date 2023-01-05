---
title: Infoga OLE-objekt i arbetsbladet
type: docs
weight: 20
url: /sv/cpp/inserting-ole-objects-into-the-worksheet/
---
## **Möjliga användningsscenarier**
 Aspose.Cells låter dig infoga ett OLE-objekt i kalkylbladet. Snälla använd[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)metod för detta ändamål. Du behöver en bildbyte-array som kommer att användas för att infoga OLE-objektet i kalkylbladet och Ole-objektdatabytes som kommer att vara ditt faktiska objekt. för att infoga Ole-objektet i kalkylbladet.
## **Infoga OLE-objekt i arbetsbladet**
 Följande exempelkod skapar arbetsboksobjektet och infogar Ole-objektet i det första kalkylbladet och sparar det som[utdata Excel-fil](66519074.xlsx) . Vänligen se[Aspose Logotyp](66519075.png) används som bildbyte och[mata in Excel-fil](66519081.xlsx) används som Ole-objektdata inuti koden för referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
