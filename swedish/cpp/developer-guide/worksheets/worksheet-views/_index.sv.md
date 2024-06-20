---
title: Arbetsboks vy
type: docs
weight: 40
url: /sv/cpp/worksheet-views/
---

## **Sidbrytning Förhandsgranskning**
Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normal visning är ett kalkylblads standardvisning. Sidbrytningsgranskning är en redigeringsvisning som visar ett kalkylblad som det kommer att skrivas ut. Sidbrytningsgranskning visar vilka data som kommer att placeras på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Med Aspose.Cells kan utvecklare aktivera normal visning eller sidbrytningsgranskningsläge.
### **Styra vynlägen**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en samling [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att aktivera normal eller sidbrytningsgranskningslägen, använd metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) returnerar ett bool-värde, vilket innebär att det endast kan lagra ett **true** eller **false**-värde.
#### **Aktivera normal vy**
Ange ett kalkylblad till normal visning genom att ange metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) till **false**.
#### **Aktivera sidbrytningsvy**
Ange valfritt kalkylblad till sidbrytningsgranskning genom att ange metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) till **true**. På så sätt växlar kalkylarket från normal visning till sidbrytningsgranskningsläge.

Ett komplett exempel ges nedan som visar hur man använder metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) för att aktivera sidbrytningsgranskningsläge för det första kalkylbladet i en Excel-fil.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Zoomfaktor**
### **Använda Microsoft Excel**
Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.
### **Aspose.Cells och Zoom Faktor**
Aspose.Cells tillåter också utvecklare att ange kalkylbladets zoomfaktor. Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att ange en kalkylblads zoomfaktor, använd  metoden [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Zoomfaktorn anges genom att tilldela ett numeriskt (heltal) värde till metoden [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/).

Ett komplett exempel ges nedan som visar hur man använder metoden [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) för att ange zoomfaktorn för det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Frys Fönsterpaneler**
### **Använda Microsoft Excel**
Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.
### **Aspose.Cells och Frysa rutor**
Aspose.Cells tillåter även utvecklare att tillämpa fryspunkter på kalkylblad vid körning. Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att konfigurera fryspunkter, anropa metoden [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frusna kolumner**, antalet synliga kolumner i vänstra fönstret.

Ett komplett exempel ges nedan som visar hur man använder metoden [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) för att frysa rader och kolumner (från C4, representerad av 4:e raden och 3:e kolumnen, där raderna och kolumnerna börjar från index 0) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Dela rutor**
Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.
### **Sätta på och Ta bort Delade paneler**
#### **Dela Fönster**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) tillhandahåller ett brett utbud av metoder för att hantera en Excel-fil. För att implementera splitvyer, använd metoden [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). För att ta bort splitfönstren, använd metoden [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Ta bort rutor**
Ta bort splitfönster med hjälp av [mRemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) metoden.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
