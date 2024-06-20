---
title: Hantera hyperlänkar i kalkylblad
type: docs
weight: 100
url: /sv/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, hyperlänk
description: Den här artikeln introducerar hur man arbetar med hyperlänk i GridWeb.
---

{{% alert color="primary" %}} 

Detta ämne diskuterar vilka typer av hyperlänkar som stöds i Aspose.Cells.GridWeb och hur man hanterar dem programmatiskt. Hyperlänkar kan användas antingen för att skapa länkar till webbadresser eller för att utföra återuppringning till en server.

{{% /alert %}} 
## **Arbeta med hyperlänkar**
### **Typer av hyperlänkar**
I allmänhet stöds följande hyperlänkar av Aspose.Cells.GridWeb:

- [URL-hyperlänkar](/cells/sv/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hyperlänkar som kan länkas till webbadresser.
- [Text hyperlänkar](/cells/sv/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), URL-hyperlänkar som tillämpas på text.
- [Bild hyperlänkar](/cells/sv/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), URL-hyperlänkar tillämpade på bilder.
- [Cellkommandohyperlänkar](/cells/sv/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hyperlänkar som skickar data till en server. Sådana hyperlänkar fungerar mer som en knapp som utlöser en serverhändelse när de klickas.

Nedan avsnitt beskriver användningen av alla typer av hyperlänkar i detalj. Det diskuterar också hur man får åtkomst till eller tar bort länkar.
### **Lägga till hyperlänkar**

#### **URL-hyperlänkar**
URL-hyperlänkar ser mer ut som enkla hyperlänkar som du normalt ser på webbplatser. En URL-hyperlänk fungerar som en ankarpunkt i en cell. När den klickas navigerar den till en webbsida eller öppnar ett nytt webbläsarfönster.

Det finns olika typer av URL-hyperlänkar:

- Text hyperlänkar.
- Bild hyperlänkar.

Utvecklare kan ange en bild för hyperlänken. Om en bild inte anges skapas en text hyperlänk; annars skapas en bildhyperlänk.


##### **Text Hyperlinks**
För att lägga till en text hyperlänk i ett kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
2. Hämta ett arbetsblad.
1. Lägg till en hyperlänk i en cell i kalkylarket.
1. Ange den text som ska visas i cellen.
1. Ange hyperlänkens URL.
1. Ange hyperlänkens mål, om så önskas.
1. Ange en verktygstips, om så önskas.

{{% alert color="primary" %}} 

OBS: Hyperlänkens mål kan anges som _self, _top eller _parent för att öppna webbadresser i ett nytt, det aktuella eller det översta fönstret respektive.

{{% /alert %}} 

Exemplet nedan lägger till två hyperlänkar till ett kalkylblad. En har inget mål medan den andra är inställd på _parent.

**Utmatning: text hyperlänkar tillagt i kalkylbladet** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Bild Hyperlinks**
För att lägga till en bildhyperlänk:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
2. Hämta ett arbetsblad.
1. Lägg till en hyperlänk i en cell.
1. Ange URL:en för bilden som ska visas som hyperlänk.
1. Ange hyperlänkens URL.
1. Ange en verktygstips, om så önskas.
1. Ange hyperlänkens text, om så önskas.

**Output: bildhyperlänkar tillagda i kalkylarket** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**Bilden för bild-URL:en kunde inte hittas** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cellkommandohyperlänkar**
En cellkommandohyperlänk är en speciell typ av hyperlänk som utlöser en serverhändelse istället för att öppna en webbsida. Utvecklare kan lägga till kod till serverhändelsen och utföra vilken uppgift som helst när hyperlänken klickas på. Denna funktion gör att utvecklare kan skapa mer interaktiva applikationer.

För att lägga till en cellkommandohyperlänk:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
2. Hämta ett arbetsblad.
1. Lägg till en hyperlänk i en cell.
1. Ange kommandot för hyperlänken till önskat värde.
   Värdet används av hyperlänkens händelsehanterare för att känna igen det.
1. Ange en verktygstips, om så önskas.
1. Ange URL för bilden som ska visas som en hyperlänk.

**En cellkommandohyperlänk har lagts till i kalkylbladet** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Händelsehantering av cellkommandohyperlänkar**
Utvecklare behöver skapa en händelsehanterare för GridWeb-kontrollens CellCommand-händelse för att utföra specifika uppgifter när en specifik cellkommandohyperlänk klickas på. CellCommand-händelsens händelsehanterare tillhandahåller ett objekt av typen CellEventArgs som erbjuder egenskapen Argument. Använd Argument-egenskapen för att identifiera en specifik hyperlänk genom att jämföra dess CellCommand-värde.

Exemplet nedan skapar en händelsehanterare för cellkommandohyperlänken som skapades i koden ovan. Hyperlänkens CellCommand var inställd på Klicka. Så, i händelsehanteraren, kontrollera först det och lägg sedan till kod som visar ett meddelande i cellen A6.

Händelsehanteraren aktiveras när hyperlänken klickas.

**Resultat: text tillagd i cellen A6 när hyperlänken klickas** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Åtkomst av hyperlänkar**
För att komma åt en befintlig hyperlänk:

1. Åtkomst cellen som innehåller den.
1. Hämta cellreferensen.
1. Skicka referensen till Hyperlinks-samlingens GetHyperlink-metod för att komma åt hyperlänken.
1. Ändra hyperlänkens egenskaper.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Ta bort hyperlänkar**
För att ta bort en hyperlänk:

1. Åtkomst till aktivt kalkylblad.
1. Ta bort en hyperlänk med hjälp av Remove-metoden i Hyperlinks-samlingen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
