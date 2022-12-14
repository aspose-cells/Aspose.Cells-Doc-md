---
title: Hantera arbetsblad
type: docs
weight: 20
url: /sv/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibelt API. Det här avsnittet beskriver metoder för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}} 

 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad.
## **Lägga till arbetsblad i en ny Excel-fil**
Så här skapar du en ny Excel-fil programmatiskt:

1.  Skapa ett objekt av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)klass.
1.  Ring[Lägg till](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) metod för[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) samling. Ett tomt kalkylblad läggs automatiskt till i Excel-filen. Det kan refereras till genom att skicka arkindexet för det nya kalkylbladet till[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling.
1. Skaffa en kalkylbladsreferens.
1. Utför arbete på arbetsbladen.
1.  Spara den nya Excel-filen med nya kalkylblad genom att anropa[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Få åtkomst till arbetsblad med Sheet Index**
Följande exempelkod visar hur du kommer åt eller får ett kalkylblad genom att ange dess index.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Ta bort kalkylblad med Sheet Index**
 Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av[Ta bortAt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)metod som tar kalkylbladets arkindex istället för dess arknamn.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
