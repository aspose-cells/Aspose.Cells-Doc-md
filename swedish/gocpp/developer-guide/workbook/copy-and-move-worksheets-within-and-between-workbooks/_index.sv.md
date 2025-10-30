---
title: Kopiera och flytta kalkylblad inom och mellan arbetsböcker med Golang via C++
linktitle: Kopiera och flytta arbetsblad
type: docs
weight: 80
url: /sv/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Lär dig hur du kopierar och flyttar arbetsblad inom och mellan Excel arbetsböcker med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver du flera arbetsblad med gemensam formatering och datainmatning. Till exempel, om du arbetar med kvartalsbudgeten, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det flera gånger.

Aspose.Cells stöder att kopiera eller flytta arbetsblad inom eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta noggrannhet.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

### **Kopiera ett arbetsblad inom en arbetsbok**

De initiala stegen är desamma för alla exempel:

1. Skapa två arbetsböcker med viss data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in viss data i arbetsbladen:
   - FirstWorkbook.xlsx (3 arbetsblad)
   - SecondWorkbook.xlsx (1 arbetsblad)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Installera den på din utvecklingsdator

1. Skapa ett projekt:
   1. Skapa ett nytt C++-projekt i din föredragna IDE

1. Lägg till referenser:
   1. Lägg till Aspose.Cells for C++-biblioteket i ditt projekt

1. Kopiera kalkylbladet inom en arbetsbok
   Det första exemplet kopierar det första kalkylbladet (Kopiera) inom FirstWorkbook.xlsx.

När koden körs kopieras kalkylbladet med namnet Kopiera inom FirstWorkbook.xlsx med namnet Sista blad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Flytta ett blad inom en arbetsbok**

Koden nedan visar hur man flyttar ett blad från en position i en arbetsbok till en annan. Utförande av koden flyttar bladet som kallas Flytta från index 1 till index 2 i FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Kopiera ett kalkylblad mellan arbetsböcker**

När koden körs kopierar den arbetsbladet som heter Copy till SecondWorkbook.xlsx med namnet Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas bladet med namnet Flytta från FirstWorkbook.xlsx till SecondWorkbook.xlsx med namnet Sheet3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
