---
title: Aspose.Cells for .NET 20.2 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-20-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.2](https://www.nuget.org/packages/Aspose.Cells/20.2.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47113|Röravgränsad / CSV till JSON konvertering|Ny funktion|
|CELLSNET-47141|Länken mellan pivottabellen och den externa anslutningen|Ny funktion|
|CELLSNET-47135|Aspose.Cells anser inte TEXTJOIN() avancerad formel/funktion som formel|Förbättring|
|CELLSNET-47126|Aspose.Cells tar bort "volatileDependencies.xml" från filen med RTD-formler medan XLSX-filen uppdateras|Förbättring|
|CELLSNET-47159|För mycket tidskostnad för PivotTable.CalculateStyle|Prestanda|
|CELLSNET-42065|Tidigare beräknade Pivot Procent bryter efter pivot.CalculateData()|Insekt|
|CELLSNET-47102|"#" visas efter konvertering av Excel till PDF i anpassat format för negativ tid (h:mm)|Insekt|
|CELLSNET-47118|Felaktigt värde 'TRUE' hämtat från Cell istället för värdet 'FALSE'|Insekt|
|CELLSNET-47125|Mellanslag går förlorade från formeln när de hämtas med Aspose.Cells for .NET|Insekt|
|CELLSNET-47149|Formelberäkning är annorlunda i Aspose.Cells och MS Excel|Insekt|
|CELLSNET-47108|Villkorlig formatering visas inte i GridDesktop|Insekt|
|CELLSNET-47134|Att infoga kolumn tar för lång tid i Aspose.Cells.GridDesktop|Insekt|
|CELLSNET-47138|GridDesktop tar lång tid att ladda stora filer|Insekt|
|CELLSNET-47043|Det går inte att välja en cell för skyddat ark i GridDesktop|Insekt|
|CELLSNET-47117|Aspose.Cells 20.1 XAdES-typ är inte definierad vid läsning av tidigare signerade filer med XAdES-signaturer|Insekt|
|CELLSNET-47081|Återgivningsdiagram till PDF|Insekt|
|CELLSNET-47085|Diagrammet återges inte korrekt när axeletiketternas textriktning är "Stack"|Insekt|
|CELLSNET-47112|Konverteringen av diagram till bild misslyckas|Insekt|
|CELLSNET-47133|Inkonsekvens vid export till PDF|Insekt|
|CELLSNET-47107|Villkorligt formateringsobjekt ger felaktiga resultat för attributet IsAboveAverage|Insekt|
|CELLSNET-47114|Arbetsbok RemoveExternalLinks resulterar i ett trasigt dokument|Insekt|
|CELLSNET-47139|ODS fil med extern länkformel visar extra arbetsblad|Insekt|
|CELLSNET-47145|Namngivna intervall försvinner efter att ha öppnat och sparat ODS-filen|Insekt|
|CELLSNET-47146|Filen öppnas inte|Insekt|
|CELLSNET-47147|Problem med arkkodnamn|Insekt|
|CELLSNET-47153|ODS grafer ändras efter spara|Insekt|
|CELLSNET-47157|Fel antal externa länkar|Insekt|
|CELLSNET-47164|IsItalic-egenskapen upptäcktes annorlunda än MS Excel|Insekt|
|CELLSNET-47169|CategoryType.CategoryScale är inte inställd i ParetoLine-diagrammet|Insekt|
|CELLSNET-47122|Undantag "Indexa utanför intervallet" vid uppdatering av pivottabeller|Undantag|
|CELLSNET-47156|IndexOutOfRangeException vid åtkomst till ExternalLink.IsReferred eller IsVisible|Undantag|
|CELLSNET-47140|Undantag vid inläsning av ODS i GridDesktop|Undantag|
|CELLSNET-47105|Undantag vid import av XML-data där en kolumn i tabellen inte är mappad|Undantag|
|CELLSNET-47170|Undantag "Ogiltig cast från 'DateTime' to 'Double'" när du sparar en Excel-fil till PDF|Undantag|
|CELLSNET-47152|Arbetsblad.Cells.EndCellInRow ger fel för filen|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoden Workbook.ParseFormulas(bool ignoreError).**
Analyserar alla formler som inte har analyserats när de laddades eller sattes till en cell.
#### **Lägger till egenskapen PivotTable.ExternalConnectionDataSource.**
Hämtar den externa anslutningsdatakällan.
#### **Lägger till FileFormatType.Numbers35 enum.**
Representerar nummer 3.5-filer sedan office 2014. Endast för att kasta filformatet vid läsning.
#### **Lägger till egenskapen LoadOptions.CheckDataValid.**
Indikerar om data är giltiga när filerna laddas.
#### **Lägger till egenskapen GridDesktop.GridMemorySetting.**
Hämtar eller ställer in minnesalternativ för att ladda kalkylblad.
