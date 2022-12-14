---
title: Hantera hyperlänkar i kalkylblad
type: docs
weight: 100
url: /sv/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar vilka typer av hyperlänkar som stöds i Aspose.Cells.GridWeb och hur man hanterar dem programmatiskt. Hyperlänkar kan användas för att antingen skapa länkar till webbadresser eller för att utföra återsändning till en server.

{{% /alert %}} 
## **Arbeta med hyperlänkar**
### **Typer av hyperlänkar**
I allmänhet stöds följande hyperlänkar av Aspose.Cells.GridWeb:

- [URL-hyperlänkar](/cells/sv/net/manage-hyperlinks-in-worksheet/), hyperlänkar som kan länkas till webbadresser.
- [Text hyperlänkar](/cells/sv/net/manage-hyperlinks-in-worksheet/), URL-hyperlänkar tillämpas på text.
- [Bild hyperlänkar](/cells/sv/net/manage-hyperlinks-in-worksheet/), URL-hyperlänkar tillämpas på bilder.
- [Cell kommandohyperlänkar](/cells/sv/net/manage-hyperlinks-in-worksheet/), hyperlänkar som skickar data till en server. Sådana hyperlänkar fungerar mer som en knapp som utlöser en händelse på serversidan när den klickas.

Avsnitten nedan beskriver användningen av alla typer av hyperlänkar i detalj. Den diskuterar också hur man kommer åt eller tar bort länkar.
### **Lägga till hyperlänkar**

#### **URL-hyperlänkar**
URL-hyperlänkar ser mer ut som enkla hyperlänkar som du normalt ser på webbplatser. En URL-hyperlänk fungerar som ett ankare i en cell. När du klickar på den navigerar den till en webbsida eller öppnar ett nytt webbläsarfönster.

Det finns olika typer av URL-hyperlänkar:

- Text hyperlänkar.
- Bild hyperlänkar.

Utvecklare kan ange en bild för hyperlänken. Om en bild inte anges skapas en texthyperlänk; annars skapas en bildhyperlänk.


##### **Text hyperlänkar**
Så här lägger du till en texthyperlänk till ett kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Få tillgång till ett arbetsblad.
1. Lägg till en hyperlänk till en cell i kalkylbladet.
1. Ställ in texten som ska visas i cellen.
1. Ställ in hyperlänkens URL.
1. Ställ in hyperlänkens mål, om så önskas.
1. Ställ in ett verktygstips om så önskas.

{{% alert color="primary" %}} 

 OBS: Hyperlänksmålet kan ställas in på_ själv,_top eller _parent för att öppna webbadresser i ett nytt, det aktuella respektive det översta fönstret.

{{% /alert %}} 

Exemplet nedan lägger till två hyperlänkar till ett kalkylblad. Den ena har inget mål medan den andra är inställd på _parent.

**Utdata: texthyperlänkar läggs till i kalkylbladet** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Bildhyperlänkar**
Så här lägger du till en bildhyperlänk:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Få tillgång till ett arbetsblad.
1. Lägg till en hyperlänk till en cell.
1. Ställ in webbadressen till bilden som ska visas som hyperlänk.
1. Ställ in hyperlänkens URL.
1. Ställ in ett verktygstips om så önskas.
1. Ställ in hyperlänkstexten om så önskas.

**Utdata: bildhyperlänkar har lagts till i kalkylbladet** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 Att ställa in bildens hyperlänks AltText fyller en liknande funktion som att ställa in en<ALT> taggen i HTML. Texten visas endast om den hyperlänkade bilden inte visas. (Till exempel om bilden inte finns på den angivna platsen.) Om bilden av den andra hyperlänken inte hittas, skulle utdata från kodavsnittet nedan se ut som följer.

**Det gick inte att hitta bilden för bildens webbadress** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Kommandohyperlänkar**
En cellkommandohyperlänk är en speciell typ av hyperlänk som utlöser en händelse på serversidan istället för att öppna en webbsida. Utvecklare kan lägga till kod till händelsen på serversidan och utföra valfri uppgift när hyperlänken klickas. Denna funktion gör det möjligt för utvecklare att skapa mer interaktiva applikationer.

Så här lägger du till en hyperlänk för ett cellkommando:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Få tillgång till ett arbetsblad.
1. Lägg till en hyperlänk till en cell.
1. Ställ in hyperlänkens kommando till valfritt värde.
 Värdet används av hyperlänkens händelsehanterare för att känna igen det.
1. Ställ in ett verktygstips om så önskas.
1. Ställ in URL:en för bilden som ska visas som en hyperlänk.

**En cellkommandohyperlänk har lagts till i kalkylbladet** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Händelsehantering av Cell kommandohyperlänkar**
Utvecklare måste skapa en händelsehanterare för GridWeb-kontrollens CellCommand-händelse för att utföra specifika uppgifter när en specifik cellkommandohyperlänk klickas. CellCommand-händelsens händelsehanterare tillhandahåller ett objekt av typen CellEventArgs som erbjuder egenskapen Argument. Använd egenskapen Argument för att identifiera en specifik hyperlänk genom att jämföra dess CellCommand-värde.

Exemplet nedan skapar en händelsehanterare för cellkommandot hyperlänk skapad i koden ovan. Hyperlänkens CellCommand var inställd på Click. Så, i händelsehanteraren, kontrollera först den och lägg sedan till kod som visar ett meddelande i A6-cellen.

Händelsehanteraren anropas när hyperlänken klickas.

**Utdata: text läggs till i A6-cellen när hyperlänken klickas** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Åtkomst till hyperlänkar**
För att komma åt en befintlig hyperlänk:

1. Gå till cellen som innehåller den.
1. Hämta cellreferensen.
1. Skicka referensen till Hyperlinks-samlingens GetHyperlink-metod för att komma åt hyperlänken.
1. Ändra hyperlänkens egenskaper.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Ta bort hyperlänkar**
Så här tar du bort en hyperlänk:

1. Öppna det aktiva arbetsbladet.
1. Ta bort en hyperlänk med hjälp av Hyperlinks-samlingens Remove-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
