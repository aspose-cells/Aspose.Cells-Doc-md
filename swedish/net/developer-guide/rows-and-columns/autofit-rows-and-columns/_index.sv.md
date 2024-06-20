---
title: Automatisk anpassning av rader och kolumner
type: docs
weight: 20
url: /sv/net/autofit-rows-and-columns/
description: Den här artikeln visar hur man automatiskt anpassar rader, kolumner, rader i sammanslagna celler och rad i en cellintervall med hjälp av Aspose.Cells for .NET API.
keywords: Autostorlek för rader, autostorlek för kolumner, autostorlek för rad i en cellintervall, autostorlek för rader i sammanslagna celler
---

{{% alert color="primary" %}}

Microsoft Excel låter användare automatiskt anpassa bredd och höjd på celler enligt dess innehåll. Denna funktion är också tillgänglig genom Aspose.Cells så att utvecklare kan automatiskt anpassa dimensionerna på en cell under körning.

{{% /alert %}}

## **Autostorlek**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-kollektion som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för hantering av ett kalkylblad. Den här artikeln tittar på användningen av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen för att automatiskt anpassa rader eller kolumner.

### **AutoFit Row - Enkelt**

Det mest raka tillvägagångssättet för att automatiskt justera bredd och höjd för en rad är att anropa klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) metoden [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index). Metoden [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) tar en radindex (av raden som ska ändras) som parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Hur man Autofitrad i ett område av celler**

En rad består av många kolumner. Aspose.Cells tillåter utvecklare att automatiskt justera en rad baserad på innehållet i en rad av celler genom att anropa en överlagrad version av metoden [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1). Den tar följande parametrar:

- **Radindex**, index för raden som ska autofit.
- **Första kolumnindex**, index för radens första kolumn.
- **Sista kolumnindex**, index för radens sista kolumn.

Metoden [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) kontrollerar innehållet i alla kolumner i raden och anpassar sedan raden automatiskt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Hur man Autofittar kolumn i ett område av celler**

En kolumn består av många rader. Det är möjligt att automatiskt justera en kolumn baserad på innehållet i ett område av celler i kolumnen genom att anropa en överlagrad version av metoden [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) som tar följande parametrar:

- **Kolumnindex**, index för kolumnen som ska autofit.
- **Första radindex**, index för kolumnens första rad.
- **Sista radindex**, index för kolumnens sista rad.

Metoden [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) kontrollerar innehållet i alla rader i kolumnen och anpassar sedan kolumnen automatiskt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Hur man Autofittar rader för sammanfogade celler**

Med Aspose.Cells är det möjligt att automatisera rader även för celler som har sammanfogats med hjälp av [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) klass tillhandahåller [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) egenskap som kan användas för att automatisera rader för sammanfogade celler. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) accepterar [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) uppräkneligt som har följande medlemmar.

- Ingen: Ignorera sammanfogade celler.
- FörstaLinje: Endast expanderar höjden på första raden.
- SistaLinje: Endast expanderar höjden på sista raden.
- VarjeLinje: Endast expanderar höjden på varje rad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

Du kan även försöka att använda de överlagrade versionerna av [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) och [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) metoder som accepterar ett område av rader/kolumner och en instans av [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) för att automatiskt anpassa de valda raderna/kolumnerna med din önskade  [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) i enlighet.

Signaturerna för ovanstående metoder är som följer:

1. AutoFitRows(int startRad, int slutRad, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) alternativ)
1. AutoFitColumns(int förstaKolumn, int sistaKolumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) alternativ)

{{% /alert %}}

## **Viktigt att veta**

{{% alert color="primary" %}}

Om en cell är sammanfogad kommer inte AutoFit-metoderna att appliceras, vilket är samma beteende som i Microsoft Excel. Du kan komma runt detta genom att använda auto filter API. Dessutom, om texten i en cell är radbryten, kommer inte metoden [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) att tillämpas heller. En annan sak du behöver veta är att *AutoFit*-metoderna tar lång tid. Så, du bör anropa dessa metoder så sällan som möjligt för att säkerställa effektiviteten i din applikation.

{{% /alert %}}

## **Fortsatta ämnen**
- [Automatisk justering av rader för sammanfogade celler](/cells/sv/net/autofit-rows-for-merged-cells/)
