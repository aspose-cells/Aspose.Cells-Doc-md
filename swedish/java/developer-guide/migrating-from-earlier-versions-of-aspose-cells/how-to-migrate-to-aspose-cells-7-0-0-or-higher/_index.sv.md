---
title: Hur man migrerar till Aspose.Cells 7.0.0 eller högre
type: docs
weight: 10
url: /sv/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

den här artikeln har vi delat de anmärkningsvärda ändringarna i API:et som har genomförts i Aspose.Cells för Java 7.0.0 och senare versioner jämfört med föregångarna av Aspose.Cells för Java. Den här artikeln hjälper användarna att snabbt migrera från Gamla API till nya API genom att förstå de ändringar som gjorts och genomföra dem i deras applikationer.

{{% /alert %}}

## **Anmärkningsvärda förändringar för de befintliga användarna**

Sedan lanseringen av Aspose.Cells för Java v7.0.0 har vi gjort några större ändringar i API:t och lagt till alla de funktioner som finns i Aspose.Cells för .NET hittills. Så både Aspose.Cells för Java och .NET kommer att vara jämförbara nu när det gäller funktioner och till och med när det gäller metoder och egenskapsnamn.

I likhet med det äldre tillvägagångssättet kan du bara importera en importsats i din applikation för att hämta alla klasser, gränssnitt etc.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Vi har bytt namn på vissa API-inställningar för att rensa API-strukturen för att matcha den med Aspose.Cells för .NET. Vi har lagt till några insamlingsklasser nu och har ersatt dem med befintliga insamlingsklasser. Like Worksheets-klassen har ersatts med**Arbetsbladssamling** . På samma sätt har Shapes-klassen ersatts med**ShapeCollection**. Funktionaliteten hos klasserna har dock inte påverkats snarare förbättrats.

Om du vill migrera till ett nytt API kan du behöva utföra följande ändringar i din applikation för att få saker att fungera på din sida. Följande lista innehåller de ändringar som gjorts i klasser och deras respektive metoder också.

## **Sammanfattning av ändringarna i API**

1) Samlingar i v2.5.4 eller tidigare vars namn som slutar med 's' har bytt namn. I v7.0.0 eller senare heter samlingarna:
t.ex. Former (gammalt) -> ShapeCollection (Ny), Arbetsblad (Gammal) -> Arbetsbladssamling (Ny), ..., etc.

2) Att hämta element från samlingen ändras. Till exempel, i v2.5.4 eller tidigare brukade vi göra det som getXXX(int), i v7.0.0 eller högre, nu gör vi det som get(int):
t.ex. Worksheets.getSheet(int) (Old) -> WorksheetCollection.get(int) (New), ...etc.

3) Att få storlek (elementantal) för en samling ändras. I v2.5.4 eller tidigare gjorde vi det med size(), i v7.0.0 eller högre, nu gör vi det med getCount():
Worksheets.size() (Old) -> WorksheetCollection.getCount() (New), ...,etc.

4) Booleska egenskapers gettermetoder i v2.5.4 eller tidigare vars namn som börjar med 'är' ändras. I v7.0.0 startas dessa med "get":
t.ex. PageSetup.isBlackAndWhite() (Old) -> PageSetup.getBlackAndWhite() (New), ...,etc.
