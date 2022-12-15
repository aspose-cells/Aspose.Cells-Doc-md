---
title: Använd avancerad villkorlig formatering
type: docs
weight: 70
url: /sv/net/apply-advanced-conditional-formatting/
---
{{% alert color="primary" %}} 

Microsoft Excel 2007 och senare versioner (2010/2013/2016) innehåller några avancerade funktioner för villkorlig formatering. Till exempel låter den dig tillämpa cellskuggning, ramar, färgade ikoner, pilar, flaggor och teckensnittsformatering, etc. som har blivit ganska sofistikerad.

{{% /alert %}} 
## **Tillämpa avancerad villkorlig formatering på Microsoft Excel-filer**
Villkorlig formatering kan:

- Lägg till skuggade datastaplar för att grafiskt förbättra de underliggande siffrorna genom att bädda in ett enkelt stapeldiagram i cellerna.
- Skugga automatiskt celler med färgskalor baserat på deras relation till värden i andra celler i området. Standardinställningarna skuggar det lägsta värdet i rött och flyttas upp till det högsta värdet i grönt.
- Använd ikonuppsättningar på samma sätt som färgskalor, men istället för att skugga cellerna lägger den till små ikoner, som pilar och trafikljus i cellerna.

Aspose.Cells stöder fullt ut den villkorliga formateringen som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler under körning. Det här exemplet visar en övning för avancerade villkorliga formateringstyper inklusive IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom och andra regler med olika uppsättningar av attribut.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
### **Beräkna färgen vald av Microsoft Excel för ColorScale villkorlig formatering**
Aspose.Cells låter dig beräkna färgen vald av Microsoft Excel när ColorScale villkorlig formatering används i en mallfil. Se exempelkoden nedan för att lära dig hur du beräknar färgen som valts av Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
