---
title: Hur man lägger till textbaserad villkorsstyrd formatering
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa textbaserad villkorsstyrd formatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Textvillkorsstyrd formatering, C#, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/net/how-to-add-text-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda textbaserad villkorsstyrd formatering i kalkylblad är användbart för att markera celler som uppfyller specifika textkrav. Detta kan förbättra dataanalys och göra det lättare att hitta nyckelinformation i en stor datamängd. Här är några anledningar till att använda textbaserad villkorsstyrd formatering:

1. Markera särskild text: Du kan tillämpa formatering baserat på specifika ord, fraser eller tecken. Till exempel kan du vilja markera alla celler som innehåller ordet "Brådskande" eller "Avslutad" för att enkelt särskilja uppgifter i ett projekt.
1. Identifiera mönster eller trender: Om du arbetar med kategorier eller statusar (som "Hög", "Medium", "Låg") kan textbaserad villkorsstyrd formatering visuellt skilja mellan dem, vilket gör det lättare att följa framsteg eller prioritera uppgifter.
1. Fel- eller dataregistreringsvarningar: Textformatering kan flagga inkonsekventa eller felaktiga inmatningar, som stavfel, ofullständig text eller felaktiga värden. Detta är särskilt användbart i dataset med mycket textinmatning.
1. Förbättrad läsbarhet: Färgmärkning av text eller ändring av stil (fet, kursiv osv.) hjälper till att framhäva viktig information, vilket förbättrar det övergripande läsbarheten.
1. Dynaisk feedback: Du kan skapa regler som automatiskt justerar formateringen när text matchar vissa villkor. Detta innebär att du inte behöver uppdatera formateringen manuellt när data ändras.

Kort sagt hjälper textbaserad villkorsstyrd formatering dig att snabbt upptäcka relevant information, fel och trender, vilket gör det till ett kraftfullt verktyg för att hantera och tolka textuell data.

## **Hur man lägger till textvillkorsstyrd formatering med Excel**
För att lägga till textbaserad villkorsstyrd formatering i Excel, följ dessa steg:

1. Markera cellområdet: Markera de celler där du vill tillämpa villkorsstyrd formatering.
1. Öppna menyn Villkorsstyrd formatering: Gå till fliken Start i Excel-rollen. Klicka på Villkorsstyrd formatering i "Stilar"-gruppen.
1. Välj "Nytt regel": Från rullgardinsmenyn, välj Ny regel.
1. Välj "Formatera endast celler som innehåller": I dialogrutan Ny formatregel, välj Formatera endast celler som innehåller under avsnittet "Välj regeltyp".
1. Ange regelkriterier: I avsnittet "Formatera celler med", välj Specifik text från rullgardinen. Välj antingen innehåller, börjar med eller slutar med, beroende på villkoret du vill tillämpa. Ange den text du vill formatera (t.ex. ett specifikt ord som "Brådskande" eller "Avslutad").
1. Välj formateringen: Klicka på knappen Formatera. I dialogrutan Formatera celler kan du välja teckensfärg, fyllnadsfärg eller andra formateringsalternativ.
1. Tillämpa regeln: När du har ställt in önskad formatering klickar du OK för att tillämpa regeln. Klicka på OK igen i dialogrutan Ny formatregel för att stänga den.
1. Visa resultaten: Cellerna som innehåller den angivna texten kommer nu att ha den tillämpliga formateringen, vilket gör det enkelt att hitta relevant information.


## **Hur man lägger till textvillkorsstyrd formatering med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut den villkorsstyrda formatering som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på cellnivå i realtid. Detta exempel demonstration för avancerade typer av villkorsstyrd formatering inklusive Börjar med, Innehåller tomt, Innehåller text och så vidare.

### **Formatera cell när värdet börjar med specifik text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Formatera cell när värdet innehåller tomt**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Formatera cell när värdet innehåller fel**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Formatera cell när värdet innehåller angiven text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Formatera cell när värdet innehåller dubbletter**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Formatera cell när värdet slutar med specificerad text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Formatera cell när värdet inte innehåller tomt**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Formatera cell när värdet inte innehåller fel**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Formatera cell när värdet inte innehåller specificerad text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Formatera cell när värdet innehåller unika värden**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
