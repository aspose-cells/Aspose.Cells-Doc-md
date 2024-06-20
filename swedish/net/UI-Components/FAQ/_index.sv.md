---
title: Frågor och svar
type: docs
weight: 400
url: /sv/net/grid-faq/
---

## **Finns det några begränsningar i utvärderingsversionen av Aspose.Cells Gridkontroller?**
Nej, det finns inga begränsningar av funktioner i utvärderingsversionen av dessa kontroller.

Utvärderingsversionen tillhandahåller alla funktioner i den licensierade versionen förutom att den lägger till en extra kalkylblad (innehållande **Varning för utvärderingsupphovsrätt** ) till utdatafilerna.


## **Det finns så många Grid-kontroller tillgängliga på marknaden. Varför bör jag köpa Aspose.Cells Gridkontroller?**
Nåväl, Aspose.Cells Gridkontroller är mycket väl prissatta för att vara överkomliga för alla typer av användare. Till ett mycket rimligt pris,

ger det dig en svit av två kontroller att arbeta på Windows & Web Applications. 

Dessutom är det inte bara en enkel tabell, det är din **Kalkylbladsvisare, redaktör & skapare** samtidigt. 

Du kan inte bara binda det med alla typer av datakällor (som normala Gridkontroller) men också skapa & hantera Excel-filer. Det tillhandahåller också en kraftfull & rik **Formelberäkningsmotor** för att beräkna inte bara inbyggda funktioner (som stöds av Aspose.Cells Gridkontroller) utan också anpassade formler definierade av dig. Det finns mycket fler funktioner i Aspose.Cells Grid-sviten som inte kan täckas här, vänligen se sidan för Editionstyper för en mer detaljerad lista över funktioner.

## **Jag har nyligen köpt min licens för Aspose.Cells Gridkontroller. Hur kan jag använda den licensen i min applikation med Aspose.Cells Gridkontroll?**
Vänligen se på [Licensiering](/cells/sv/net/licensing/) sidan för Aspose.Cells Gridkontroller. 

Den ger fullständiga detaljer om hur man använder licensen med Aspose.Cells Gridkontroller i dina applikationer.



## **Hur kan jag distribuera mitt Aspose.Cells.GridWeb-baserade webbprojekt/lösning på servern?**
Om du behöver distribuera webbapplikationen med GridWeb-kontrollen skulle du kopiera katalogen "acw_client" in i din projektmapp minst din webbapplikation (distribuerad över servern) kan inte hitta den.

Du kan alltid specificera skripvag genom att lägga till följande rader kod i konfigurationsavsnittet (t.ex. i webbkonfigurationsfilen i ditt VS.NET-projekt). "acw_client" är en mapp som innehåller filer och Aspose.Cells.GridWeb använder denna mapp för att hantera sin interna konfiguration, den har skriptfiler, bildfiler och andra filer för att specificera GridWebs beteende och ställa in andra operationer. Konfigurationsfilen används för att förhindra kontrollen från att använda inbäddade klientresurser (bilder, skript osv.) vilket är användbart i vissa fall/scenarier.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Sökvägen är alltid relaterad till projektets katalog. Du bör inte använda någon katalog som ligger utanför projektets katalog. Så det är nödvändigt att kopiera katalogen "acw_client" (@ din GridWeb-installationsmapp) in i projektets katalog.

{{% /alert %}} 
## **Kör Aspose.Cell.GridWeb i Internet Explorer**
För närvarande stöder inte Aspose.Cells.GridWeb Internet Explorer längre, det är en alltför gammal webbläsare. 
Vi stöder Chrome, Edge, Firefox, Safari, Opera



