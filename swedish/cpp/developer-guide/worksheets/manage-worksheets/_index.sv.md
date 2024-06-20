---
title: Hantera kalkylblad 
type: docs
weight: 20
url: /sv/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Detta ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}} 

Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en samling [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som tillåter åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad.
## **Lägga till kalkylblad i en ny Excelfil**
För att skapa en ny Excel-fil programmatiskt:

1. Skapa ett objekt av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
1. Anropa metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) i samlingen [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). Ett tomt kalkylblad läggs automatiskt till Excel-filen. Det kan refereras genom att skicka det nya kalkylbladets index till samlingen [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
1. Få en referens till ett kalkylblad.
1. Arbeta med kalkylbladen.
1. Spara den nya Excel-filen med nya kalkylblad genom att anropa metoden [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) i klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Åtkomst till kalkylblad med hjälp av kalkylbladsindex**
Följande exempelkod visar hur man får åtkomst till eller hämtar ett kalkylblad genom att ange dess index.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Ta bort kalkylblad med hjälp av kalkylbladsindex**
Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av metoden [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) som tar kalkylbladets index istället för dess namn.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
