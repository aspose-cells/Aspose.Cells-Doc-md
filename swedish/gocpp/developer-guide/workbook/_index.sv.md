---
title: Hantera arbetsbok med Golang via C++
linktitle: Arbetsbok
type: docs
weight: 60
url: /sv/go-cpp/managing-workbooks-and-worksheets/
description: Lär dig hur du hanterar arbetsboken via API erna Aspose.Cells for C++.
keywords: Hur man hanterar arbetsbok i C++, hantera arbetsbok och blad med C++, operera arbetsbok och blad i C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ tillhandahåller ett kraftfullt och flexibelt API för att hantera arbetsböcker och blad. Denna sektion förklarar hur man skapar, öppnar och manipulerar arbetsböcker och blad programmatiskt.

{{% /alert %}}

## **Skapa en ny arbetsbok**
För att skapa en ny arbetsbok:

1. Skapa en instans av [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen.
2. Lägg till arbetsblad i arbetsboken med [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) klassen.
3. Spara arbetsboken med hjälp av metoden [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Öppna en befintlig arbetsbok**
För att öppna en befintlig arbetsbok:

1. Skapa en instans av [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen och spara filvägen i konstruktorn.
2. Få åtkomst till arbetsbladen med [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) klassen.
3. Ändra arbetsboken vid behov.
4. Spara arbetsboken med hjälp av [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) metoden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Hantera blad**
Aspose.Cells for C++ erbjuder ett brett utbud av metoder för att hantera blad, inklusive att lägga till, ta bort och byta namn på blad.

### **Lägga till ett arbetsblad**
Lägga till ett nytt kalkblad:

1. Få åtkomst till [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) från arbetsboken.
2. Använd [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) metoden för att lägga till ett nytt arbetsblad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Ta bort ett Arbetsblad**
För att ta bort ett kalkblad:

1. Få åtkomst till [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) från arbetsboken.
2. Använd [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) metoden för att ta bort ett arbetsblad efter index.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Byta namn på ett Arbetsblad**
För att byta namn på ett kalkblad:

1. Få åtkomst till [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen från arbetsboken.
2. Använd [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) metoden för att byta namn på arbetsbladet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Slutsats**
Aspose.Cells for C++ ger ett omfattande set verktyg för att hantera arbetsböcker och kalkblad. Oavsett om du behöver skapa en ny arbetsbok, öppna en befintlig eller manipulera kalkblad, gör Aspose.Cells det enkelt att arbeta med Excel-filer programmässigt.
