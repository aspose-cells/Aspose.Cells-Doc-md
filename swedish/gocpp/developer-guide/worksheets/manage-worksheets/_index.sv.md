---
title: Hantera kalkylblad 
type: docs
weight: 20
url: /sv/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Detta ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}}

Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som ger tillgång till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) erbjuder ett brett utbud av metoder för att hantera kalkylblad.

## **Lägga till kalkylblad i en ny Excelfil**

För att skapa en ny Excel-fil programmatiskt:

1. Skapa ett objekt av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. Anropa metoden [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) för [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). Ett tomt kalkylblad läggs automatiskt till i Excel-filen. Det kan refereras till genom att passera bladets index för det nya kalkylbladet till [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
1. Få en referens till ett kalkylblad.
1. Arbeta med kalkylbladen.
1. Spara den nya Excel-filen med nya kalkylblad genom att anropa metoden [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) för klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Åtkomst till kalkylblad med hjälp av kalkylbladsindex**

Följande exempelkod visar hur man får åtkomst till eller hämtar ett kalkylblad genom att ange dess index.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Ta bort kalkylblad med hjälp av kalkylbladsindex**

Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte vet kalkylbladets namn, använd en överlagrad version av metoden [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) som tar bladets index i stället för dess namn.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
