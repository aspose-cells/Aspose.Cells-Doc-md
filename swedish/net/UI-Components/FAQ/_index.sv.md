---
title: FAQ
type: docs
weight: 400
url: /sv/net/grid-faq/
---
## **Finns det någon begränsning i utvärderingsversionen av Aspose.Cells Grid Controls?**
 Nej, det finns ingen begränsning av funktionerna i utvärderingsversionen av Aspose.Cells Grid Controls. Utvärderingsversionen innehåller alla funktioner i den licensierade versionen förutom att den lägger till ett extra kalkylblad (som innehåller**Utvärdering Copyright Varning** ) till utdatafilerna.
## **Det finns så många Grid-kontroller tillgängliga på marknaden. Varför ska jag köpa Aspose.Cells Grid Controls?**
 Tja, Aspose.Cells Grid Controls är mycket bra prissatta för att vara överkomliga för alla typer av användare. Till ett mycket rimligt pris ger det dig en svit med två kontroller för att fungera på Windows och webbapplikationer. Dessutom är det inte bara ett enkelt Grid, det är ditt**Kalkylarksvisare, redaktör och skapare** på samma gång. Du kan inte bara binda den med någon form av datakälla (som vanliga Grid-kontroller) utan också skapa och hantera Excel-filer. Det ger också en stark & rik**Formelberäkningsmotor** för att beräkna inte bara inbyggda funktioner (stöds av Aspose.Cells Grid Controls) utan även anpassade formler definierade av dig. Det finns mycket fler funktioner i Aspose.Cells Grid-sviten som inte kan täckas här, se sidan Edition Types för en mer detaljerad funktionslista.
## **Jag har nyligen köpt min licens för Aspose.Cells Grid Controls. Hur kan jag använda den licensen i min applikation med Aspose.Cells Grid Control?**
Vänligen se[Licensiering](/cells/sv/net/licensing/) sida av Aspose.Cells Grid Controls. Den ger fullständig information om hur du använder licensen med Aspose.Cells Grid Controls i dina applikationer.
## **Stöds Aspose.Cells Grid Controls på Visual Studio.NET 2005?**
Ja, Aspose.Cells Grid Controls stöds fullt ut på Visual Studio.NET 2005 och senare versioner.
## **Jag använder Aspose.Cells.GridWeb-kontroll på min webbplats med Visual Studio.NET 2005. Men det fungerar inte alls. Vad är problemet?**
 Aspose.Cells.GridWeb stöder båda**Filsystem** och**HTTP** lägen i Visual Studio.NET 2005. Om du fortfarande är förvirrad, ta en titt på en steg-för-steg-guide för att arbeta med Aspose.Cells.GridWeb med Visual Studio.NET 2005.
## **Hur kan jag distribuera mitt Aspose.Cells.GridWeb-baserade webbprojekt/lösning på servern?**
Om du behöver distribuera webbapplikationen med GridWeb-kontroll, kopierar du "acw_client"-katalogen till din projektmapp åtminstone kunde din webbapplikation (utplacerad över servern) inte hitta den. Du kan alltid ange skriptsökvägen genom att lägga till följande kodrader i konfigurationssektionen (t.ex. i web.config-filen i din VS.NET-projektet). "acw_klient" är en mapp som innehåller filer och Aspose.Cells. GridWeb använder den här mappen för att hantera sin interna konfiguration, den har skriptfiler, bildfiler och andra filer för att specificera GridWebs beteende och ställa in andra operationer. Konfigurationsfilen används för att förhindra kontrollen från använda de inbäddade klientresurserna (bilder, skript, etc.) vilket är användbart i vissa fall/scenarier.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Sökvägen är alltid relaterad till projektets katalog. Du bör inte använda någon katalog som ligger utanför projektets katalog. Så det är nödvändigt att kopiera "acw_client"-katalogen (@ din GridWeb-installationsmapp) till projektets katalog.

{{% /alert %}} 
## **Kör Aspose.Cell.GridWeb i Internet Explorer 10 eller 11**
 För närvarande fungerar Aspose.Cells.GridWeb inte särskilt bra på Internet Explorer 10 eller 11, så du måste använda kompatibilitetsläget för IE8/9 för att arbeta med det på webbläsartyp IE10/11. Du bör lägga till följande rad av**<meta>** tag i rubriken i**.aspx** sida:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

