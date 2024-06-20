---
title: Hur man migrerar till Aspose.Cells 7.0.0 eller högre
type: docs
weight: 10
url: /sv/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

I den här artikeln har vi delat de betydande förändringarna i API som har genomförts i Aspose.Cells for Java 7.0.0 och senare versioner jämfört med föregångarversionerna av Aspose.Cells for Java. Denna artikel kommer att hjälpa användarna att snabbt migrera från det gamla API till det nya API genom att förstå de gjorda förändringarna och genomföra dem i sina applikationer.

{{% /alert %}}

## **Betydande förändringar för befintliga användare**

Sedan släppet av Aspose.Cells for Java v7.0.0 har vi gjort vissa stora modifieringar i API och har lagt till alla de funktioner som finns i Aspose.Cells for .NET hittills. Så både Aspose.Cells for Java och .NET kommer nu att vara jämförbara när det gäller funktioner och även när det gäller metoder och egenskapsnamn.

På liknande sätt som den äldre metoden, kan du bara importera en importuttryck i din applikation för att hämta alla klasser, gränssnitt osv.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Vi har döpt om vissa API: er för att rensa API-strukturen för att matcha den med Aspose.Cells for .NET. Vi har lagt till vissa samlingsklasser nu och har ersatt dem med befintliga samlingsklasser. Som Worksheets-klassen har ersatts med **WorksheetCollection**. På liknande sätt har Shapes-klassen ersatts med **ShapeCollection**. Funktionerna i klasserna har emellertid inte påverkats utan förbättrats.

Om du vill migrera till det nya API kan du behöva genomföra följande ändringar i din applikation för att få det att fungera på din sida. Följande lista innehåller de ändringar som gjorts i klasser och deras respektive metoder också.

## **Sammanfattning av ändringarna i API**

1) Samlingar i v2.5.4 eller tidigare vars namn slutar på 's' har döpts om. I v7.0.0 eller högre heter samlingarna: 
t.ex. Shapes (Gammal) -> ShapeCollection (Ny), Worksheets (Gammal) -> WorksheetCollection (Ny), ...,osv.

2) Att hämta element från samlingen är ändrad. Till exempel, i v2.5.4 eller tidigare brukade vi göra det som getXXX(int), i v7.0.0 eller högre, gör vi det nu som get(int):
t.ex. Worksheets.getSheet(int) (Gammal) -> WorksheetCollection.get(int) (Ny), ...osv.

3) Att få storlek (elementräkning) av en samling är ändrad. I v2.5.4 eller tidigare brukade vi göra detta med size(), i v7.0.0 eller högre, gör vi det nu med getCount():
Worksheets.size() (Gammal) -> WorksheetCollection.getCount() (Ny), ...osv.

4) Booleska egenskapers hämtarmetoder i v2.5.4 eller tidigare vars namn började med 'is' har ändrats. I v7.0.0 börjar dessa med "get":
t.ex. PageSetup.isBlackAndWhite() (Gammal) -> PageSetup.getBlackAndWhite() (Ny), ...osv.
