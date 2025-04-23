---
title: Kopiera och Flytta Kalkylblad
type: docs
weight: 10
url: /sv/go-cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Ett kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta möjliga precision.

{{% /alert %}}

## **Flytta eller Kopiera Blad med Microsoft Excel**

Följande är stegen för att kopiera och flytta kalkylblad inom eller mellan arbetsböcker i Microsoft Excel.

1. För att flytta eller kopiera blad till en annan arbetsbok, öppna arbetsboken som kommer ta emot bladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I dialogrutan **Till bok** klicka på arbetsboken som ska ta emot sidorna.
1. För att flytta eller kopiera de valda sidorna till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera bladen istället för att flytta dem, markera kryssrutan **Skapa en kopia**.

### **Kopiera Arksidor inom en Arbetsbok med Aspose.Cells**

Aspose.Cells tillhandahåller en överlagrad metod [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/) som används för att lägga till ett arbetsblad till samlingen och kopiera data från ett befintligt arbetsblad. En version av metoden tar källarbetsbladets index som parameter. Den andra versionen tar namnet på källarbetsbladet. Följande exempel visar hur man kopierar ett befintligt arbetsblad inom en arbetsbok.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Flytta Kalkylblad inom en Arbetsbok**

Aspose.Cells tillhandahåller en metod [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/) som används för att flytta ett kalkylblad till en annan plats i samma kalkblad. Metoden tar målkistelindexet som parameter. Följande exempel visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
