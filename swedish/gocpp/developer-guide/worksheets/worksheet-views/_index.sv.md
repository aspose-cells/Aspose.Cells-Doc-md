---
title: Arbetsboks vy
type: docs
weight: 40
url: /sv/go-cpp/worksheet-views/
---

## **Sidbrytning Förhandsgranskning**

Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normal visning är ett kalkylblads standardvisning. Sidbrytningsgranskning är en redigeringsvisning som visar ett kalkylblad som det kommer att skrivas ut. Sidbrytningsgranskning visar vilka data som kommer att placeras på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Med Aspose.Cells kan utvecklare aktivera normal visning eller sidbrytningsgranskningsläge.

### **Styra vynlägen**

Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som ger tillgång till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) erbjuder ett brett utbud av metoder för att hantera kalkylblad. För att aktivera normala eller sidbrytningsförhandsgranskningslägen, använd metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) returnerar ett booleskt värde, vilket betyder att det bara kan lagra ett **true** eller **false** värde.

#### **Aktivera normal vy**

Ställ in ett kalkylblad till normalt läge genom att ställa in metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) för klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) till **false**.

#### **Aktivera sidbrytningsvy**

Ställ in något kalkylblad till sidbrytningsförhandsgranskningsläge genom att ställa in metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) för klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) till **true**. Detta växlar kalkylbladet från normalt läge till sidbrytningsförhandsgranskning.

Ett fullständigt exempel är nedan som visar hur man använder metoden [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) för att aktivera sidbrytningsförhandsgranskningsläge för det första kalkylbladet i en Excel-fil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Zoomfaktor**

### **Använda Microsoft Excel**

Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

### **Aspose.Cells och Zoom Faktor**

Aspose.Cells ger också utvecklare möjlighet att ställa in kalkylbladets zoomfaktor. Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som ger tillgång till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) erbjuder ett brett utbud av metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd metoden [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Zoomfaktorn anges genom att tilldela ett numeriskt (heltal) värde till [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

Ett fullständigt exempel är nedan som visar hur man använder metoden [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) för att ställa in zoomfaktorn för det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Frys Fönsterpaneler**

### **Använda Microsoft Excel**

Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

### **Aspose.Cells och Frysa rutor**

Aspose.Cells ger också utvecklare möjlighet att tillämpa låsade fönster på kalkylblad vid körning. Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som ger tillgång till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) erbjuder ett brett utbud av metoder för att hantera kalkylblad. För att konfigurera låsta fönster, anropa metoden [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Metoden [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frusna kolumner**, antalet synliga kolumner i vänstra fönstret.

Ett fullständigt exempel visas nedan som visar hur man använder metoden [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) för att låsa rader och kolumner (från C4, representerad av den 4:e raden och den 3:e kolumnen, där rader och kolumner börjar från index 0) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Dela rutor**

Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.

### **Sätta på och Ta bort Delade paneler**

#### **Dela Fönster**

Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) erbjuder ett brett utbud av metoder för att hantera en Excel-fil. För att implementera delade vyer, använd metoden [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). För att ta bort de delade fönstren, använd metoden [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Ta bort rutor**

Ta bort delade fönster med metoden [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
