---
title: Aspose.Cells for Java 7.0.0 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-7-0-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 7.0.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.0.0/)

{{% /alert %}} 

 Introduktion

Vi är glada att kunna meddela Aspose.Cells for Java v7.0.0 för användarna. Detta är den första utgåvan där vi automatiskt har porterat från vår .NET-kod och därför kan den innehålla många funktioner som saknades i de tidigare Aspose.Cells for Java-versionerna. Den här utgåvan är en stor milstolpe eftersom vi från och med nu kan arbeta mer effektivt och det betyder helt enkelt ett mycket bättre Aspose.Cells for Java för dig. Anledningen till detta är att vi nu kan underhålla två produkter Aspose.Cells for Java och Aspose.Cells for .NET från en enda källkodsbas. Från och med nu innehåller de två produkterna nästan samma uppsättning funktioner, korrigeringar och släpps samma dag.

 Översikt över ändringarna

 Det är inte vanligt att vi gör brytande ändringar i API och vi försöker alltid undvika detta när det är möjligt, men ibland är det nödvändigt. I det här fallet sker ändringarna i den nya versionen på grund av:

- Ett steg mot att använda Aspose Unified Framework som dikterar en förbättrad API för att ladda och spara. Detta gör att en mer organiserad och konsekvent API kan användas för alla Aspose-produkter.
- Källkoden från .NET-plattformen kommer nu automatiskt att porteras till Java-plattformen. Detta gör att Aspose.Cells for Java matchar Aspose.Cells for .NET funktion för funktion.

 Nya funktioner/förbättringar



 Det finns några funktioner som ingår/förbättras nu.

-  Separata kompilerade versioner av produkten för olika JDK, t.ex. 1.4, 1.5, 1.6
 Ställ in formler med externa referenser
 Stöd ListObjects / Tabeller
 Stöd AutoShapes-objekt
 Förbättringar görs för Shape-to-Image-funktionen
 Förbättringar görs för diagram-till-bild-funktionen
 Förbättringar görs för ark-till-bild-funktionen
 Förbättringar görs för Excel-to-PDF-funktionen
 Förbättringar görs för funktionen Autopassa rader/kolumner

Kända problem/begränsningar



 Det finns ett antal kända begränsningar i den här utgåvan. Det finns några funktioner som kanske inte stöds i v7.0.0 som faktiskt stöddes i de äldre versionerna:

- Använder LightCells API:er
 Läser HTML filer
 Läsa/spara diagram/former för ODS-filer
 Bevara makron när du läser filen ODS och spara makron tillbaka till filen ODS



 Anmärkningsvärda förändringar för de befintliga användarna



 den här utgåvan (Aspose.Cells for Java v7.0.0) har vi bytt namn på vissa API:er som är inställda på att rensa strukturen API för att matcha den med Aspose.Cells for .NET. Vi har några samlingsklasser men deras namn motiverar dem inte enligt standarden 0761334871. Så vi har beslutat att ändra namnen på vissa klasser och andra medlemmar i enlighet med detta. På grund av dessa ändringar kan du behöva fixa vissa delar av dina befintliga kodsegment när du uppgraderar från din tidigare version av Aspose.Cells for Java. Om du inte använder någon av medlemmarna som anges nedan behöver du troligen inte göra några ändringar eftersom din kod redan kommer att kompileras med den nya versionen. All samma funktionalitet förblir intakt, endast åtkomst till vissa medlemmar har flyttats, bytt namn eller slagits samman med andra metoder.

Obs: Vi har försökt vårt bästa, det borde inte gå förlorad funktionalitet från de tidigare versionerna/fixarna genom omstruktureringen av API, men jag är rädd att du kan hitta vissa problem och den här versionen kanske inte klarar alla testfall. Vi arbetar kontinuerligt med att förbättra den för att se till att den nya versionen fungerar 100 % bra med alla tidigare problem (som fixades i de tidigare versionerna/fixarna av produkten). Vi behöver mer tid för att utvärdera dem alla och göra produkten mer robust. Vi uppmuntrar även er alla att utvärdera era tidigare problem med denna nya version i era olika miljöer. Var snäll och meddela oss alla problem via Aspose.Cells-forumet. Ditt samarbete i detta avseende är mycket uppskattat.
