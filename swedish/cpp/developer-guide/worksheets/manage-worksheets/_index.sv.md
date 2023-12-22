---
title: Hantera arbetsblad
type: docs
weight: 20
url: /sv/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med Aspose.Cells flexibel API. Det här avsnittet beskriver metoder för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}} 

 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i Excel-filen.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad.
##  **Lägga till arbetsblad i en ny Excel-fil**
Så här skapar du en ny Excel-fil programmatiskt:

1.  Skapa ett objekt av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass.
1.  Ring[Lägg till](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) metod för[Arbetsbladssamling](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling. Ett tomt kalkylblad läggs automatiskt till i Excel-filen. Det kan refereras till genom att skicka arkindexet för det nya kalkylbladet till[Arbetsbladssamling](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling.
1. Skaffa en kalkylbladsreferens.
1. Utför arbete på arbetsbladen.
1. Spara den nya Excel-filen med nya kalkylblad genom att anropa[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Få åtkomst till arbetsblad med Sheet Index**
Följande exempelkod visar hur du kommer åt eller får ett kalkylblad genom att ange dess index.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Ta bort kalkylblad med Sheet Index**
 Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av[Ta bortAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)metod som tar kalkylbladets arkindex istället för dess arknamn.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
