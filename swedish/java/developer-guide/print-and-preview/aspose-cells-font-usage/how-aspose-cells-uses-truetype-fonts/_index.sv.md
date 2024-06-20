---
title: Hur Aspose.Cells använder TrueType typsnitt
type: docs
weight: 10
url: /sv/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells kräver TrueType-typsnitt när du renderar kalkylblad till format som PDF, XPS och bilder.

När Aspose.Cells renderar ett kalkylblad krävs åtkomst till de TrueType-typsnitt som används i kalkylbladet. Detta är en vanlig praxis vid generering av PDF, XPS och bilder och säkerställer att det konverterade dokumentet eller bilden ser identisk ut för alla användare.

{{% /alert %}}

## **Om Typsnitt**

### **Tillgänglighet och ersättning av typsnitt**

Ett kalkylblad kan formateras med olika typsnitt som Arial, Times New Roman, Verdana och andra. När Aspose.Cells renderar ett kalkylblad försöker det välja de typsnitt som används i kalkylbladet. Det kan dock finnas situationer där det exakta typsnittet inte finns tillgängligt och då måste Aspose.Cells använda ett liknande typsnitt istället.

Nedan är processen som Aspose.Cells följer bakom kulisserna.

1. Aspose.Cells försöker hitta typsnitten på filsystemet som matchar det exakta typsnittsnamnet som används i kalkylbladet.
1. Om Aspose.Cells inte kan hitta typsnitt med exakt samma namn försöker den använda standardtypsnittet som anges under arbetsbokens DefaultStyle.Font-egenskap.
1. Om Aspose.Cells inte hittar det definierade typsnittet under arbetsbokens DefaultStyle.Font-egenskap försöker den välja de mest lämpliga typsnitten bland alla tillgängliga typsnitt.
1. Slutligen, om Aspose.Cells inte hittar några typsnitt på filsystemet renderar den kalkylbladet med Arial.

### **Var Aspose.Cells letar efter typsnitt**

Aspose.Cells försöker automatiskt hitta TrueType-typsnitt på filsystemet. I de flesta fall kan du lita på Aspose.Cells standardbeteende för att hitta TrueType-typsnitt, men ibland kan du behöva ange mappar som innehåller TrueType-typsnitt med hjälp av FontConfigs.setFontFolder-metoden.

### **Vanliga typsnittrelaterade problem och lösningar**

Den här tabellen listar några av de problem som du kan stöta på vid rendering av kalkylblad till PDF med Aspose.Cells och deras lösningar.

{{% alert color="primary" %}}

Kom ihåg att de flesta typsnitt är upphovsrättsskyddade när du kopierar några typsnitt. Hitta licensen för typsnittet i förväg och se till att de kan överföras fritt till en annan dator. 

{{% /alert %}}

|**Problem** |**Orsak** |**Lösning** |
| :- | :- | :- |
|Layouten och typsnitten i det renderade dokumentet skiljer sig från originalet. |Du använder Aspose.Cells på Linux eller Mac OS där TureType-typsnitt inte finns som standard, så Aspose.Cells kan inte hitta typsnitt på din dator. |Kopiera TrueType-typsnittsfiler från en Windows-dator eller installera ett TrueType-typsnittspaket. Använd FontConfigs.setFontFolder-metoden för att ange platsen för typsnittsfilerna. |

{{% alert color="primary" %}}

Kontrollera de detaljerade artiklarna på

- [Hur du placerar TrueType-typsnitt på Linux](/cells/sv/java/how-to-install-truetype-fonts-on-linux/).
- [Hur du specifierar platsen för TrueType-typsnitt](/cells/sv/java/how-to-specify-truetype-fonts-location/).
- [Hur du får varningar när typsnittsersättning inträffar](/cells/sv/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
