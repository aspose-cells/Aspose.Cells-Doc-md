---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker
type: docs
weight: 80
url: /sv/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Ibland behöver du ett antal arbetsblad med gemensam formatering och datainmatning. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det tre gånger.

Aspose.Cells för Python via .NET stöder kopiering eller flytt av arbetsblad inom eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta precision.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

### **Kopiera ett arbetsblad inom en arbetsbok**

De inledande stegen är desamma för alla exemplen.

1. Skapa två arbetsböcker med lite data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in data i kalkylbladen.

- FirstWorkbook.xlsx (3 kalkylblad).
- SecondWorkbook.xlsx (1 kalkylblad).

1. Ladda ner och installera Aspose.Cells for Python via .NET:
   1. [Ladda ner Aspose.Cells för Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Installera det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.
1. Skapa ett projekt och lägg till referenser:   
1. Kopiera kalkylbladet inom en arbetsbok
   Det första exemplet kopierar det första kalkylbladet (Kopiera) inom FirstWorkbook.xlsx.

När koden körs kopieras kalkylbladet med namnet Kopiera inom FirstWorkbook.xlsx med namnet Sista blad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Flytta ett blad inom en arbetsbok**

Koden nedan visar hur man flyttar ett blad från en position i en arbetsbok till en annan. Utförande av koden flyttar bladet som kallas Flytta från index 1 till index 2 i FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Kopiera ett kalkylblad mellan arbetsböcker**

Genom att köra koden kopieras bladet med namnet Kopiera till SecondWorkbook.xlsx med namnet Sheet2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas bladet med namnet Flytta från FirstWorkbook.xlsx till SecondWorkbook.xlsx med namnet Sheet3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
