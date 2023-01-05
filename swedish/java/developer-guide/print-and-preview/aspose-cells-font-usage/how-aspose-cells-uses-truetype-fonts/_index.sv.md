---
title: Hur Aspose.Cells använder TrueType-teckensnitt
type: docs
weight: 10
url: /sv/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells kräver TrueType-teckensnitt vid rendering av kalkylblad till format som PDF, XPS och bilder.

När Aspose.Cells renderar ett kalkylark kräver det åtkomst till TrueType-teckensnitten som används i kalkylarket. Detta är en normal praxis under PDF, XPS och bildgenerering och säkerställer att det konverterade dokumentet eller bilden ser identisk ut för alla tittare.

{{% /alert %}}

## **Om teckensnitt**

### **Tillgänglighet och ersättning av teckensnitt**

Ett kalkylblad kan formateras med olika typsnitt som Arial, Times New Roman, Verdana och andra. När Aspose.Cells renderar ett kalkylblad försöker det välja de teckensnitt som används i kalkylarket. Det finns dock situationer då det exakta typsnittet kanske inte är tillgängligt så Aspose.Cells måste ersätta ett liknande typsnitt istället.

Nedan följer processen som Aspose.Cells följer bakom scenen.

1. Aspose.Cells försöker hitta typsnitten i filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylarket.
1. Om Aspose.Cells inte kan hitta teckensnitt med exakt samma namn, försöker den använda standardteckensnittet som anges under arbetsbokens egenskap DefaultStyle.Font.
1. Om Aspose.Cells inte kan hitta teckensnittet som definierats under arbetsbokens egenskap DefaultStyle.Font, försöker den välja de mest lämpliga typsnitten från alla tillgängliga teckensnitt.
1. Slutligen, om Aspose.Cells inte kan hitta några teckensnitt i filsystemet, renderar den kalkylarket med Arial.

### **Där Aspose.Cells letar efter teckensnitt**

Aspose.Cells försöker automatiskt hitta TrueType-teckensnitt i filsystemet. För det mesta kan du lita på Aspose.Cell:s standardbeteende för att hitta TrueType-teckensnitt, men ibland kan du behöva ange mappar som innehåller TrueType-teckensnitten med FontConfigs.setFontFolder-fabriksmetoden.

### **Typiska teckensnittsrelaterade problem och lösningar**

Den här tabellen listar några av de problem som du kan stöta på när du renderar kalkylblad till PDF med Aspose.Cells och deras lösningar.

{{% alert color="primary" %}}

 Tänk på när du kopierar teckensnitt att de flesta typsnitt är upphovsrättsskyddade. Leta först upp licensen för ett teckensnitt i förväg och kontrollera att de fritt kan överföras till en annan dator.

{{% /alert %}}

|**Problem** |**Anledning** |**Lösning** |
|:- |:- |:- |
| Layouten och teckensnitten i det renderade dokumentet skiljer sig från originalet.| Du använder Aspose.Cells på Linux eller Mac OS där TureType-teckensnitt inte finns som standard så Aspose.Cells kan inte hitta teckensnitt på din dator.|Kopiera TrueType-teckensnittsfiler från en Windows-maskin eller installera ett TrueType-teckensnittspaket. Använd FontConfigs.setFontFolder fabriksmetoden för att ange platsen för teckensnittsfilerna.|

{{% alert color="primary" %}}

Kontrollera de detaljerade artiklarna om

- [Hur man placerar TrueType-teckensnitt på Linux](/cells/sv/java/how-to-install-truetype-fonts-on-linux/).
- [Så här anger du TrueType-teckensnittsplats](/cells/sv/java/how-to-specify-truetype-fonts-location/).
- [Hur man får varningar när teckensnittsersättning sker](/cells/sv/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
