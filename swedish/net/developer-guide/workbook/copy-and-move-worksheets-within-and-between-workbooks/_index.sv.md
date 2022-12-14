---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker
type: docs
weight: 80
url: /sv/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med vanlig formatering och datainmatning. Om du till exempel arbetar med kvartalsbudgetar kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett ark och sedan kopiera det tre gånger.

Aspose.Cells stöder kopiering eller flyttning av kalkylblad i eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta precision.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

### **Kopiera ett arbetsblad i en arbetsbok**

De första stegen är desamma för alla exempel.

1. Skapa två arbetsböcker med lite data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in en del data i kalkylbladen.

- FirstWorkbook.xlsx (3 kalkylblad).
- SecondWorkbook.xlsx (1 kalkylblad).

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells för .NET](https://downloads.aspose.com/cells/net).
 1. Installera det på din utvecklingsdator.
 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. Skapa ett projekt:
 1. Starta Visual Studio.Net.
 1. Skapa en ny konsolapplikation.
1. Lägg till referenser:
 1. Lägg till en referens till Aspose.Cells till projektet.
 Lägg till exempel till en referens till ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Kopiera kalkylbladet i en arbetsbok
 Det första exemplet kopierar det första kalkylbladet (Copy) i FirstWorkbook.xlsx.

När koden körs kopieras arbetsbladet med namnet Copy i FirstWorkbook.xlsx med namnet Last Sheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Flytta ett kalkylblad i en arbetsbok**

Koden nedan visar hur man flyttar ett kalkylblad från en position i en arbetsbok till en annan. Genom att köra koden flyttas kalkylbladet som heter Flytta från index 1 till index 2 i FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Kopiera ett arbetsblad mellan arbetsböcker**

När du kör koden kopieras arbetsbladet med namnet Copy till SecondWorkbook.xlsx med namnet Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas kalkylbladet med namnet Move från FirstWorkbook.xlsx till SecondWorkbook.xlsx med namnet Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
