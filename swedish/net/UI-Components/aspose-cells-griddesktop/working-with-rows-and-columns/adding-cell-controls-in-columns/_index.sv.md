---
title: Lägger till Cell kontroller i kolumner
type: docs
weight: 90
url: /sv/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

våra senare diskussioner har vi diskuterat om att lägga till och hantera cellkontroller i kalkylbladet. Men med dessa metoder kan vi lägga till cellkontroller till enstaka celler en efter en. Vad händer om någon skulle vilja lägga till cellkontroller till alla celler i en eller flera kolumner? I sådana fall, för att minska utvecklarnas ansträngningar, tillhandahåller Aspose.Cells.GridDesktop funktionen att lägga till cellkontroller per kolumnbasis. Det betyder att utvecklare bara kan välja en önskad kolumn och ange valfri cellkontroll. Den angivna cellkontrollen kommer att läggas till i alla celler i den angivna kolumnen. Låt oss se hur vi kan använda den här funktionen.

{{% /alert %}} 
## **Introduktion**
För närvarande stöder Aspose.Cells.GridDesktop att lägga till tre typer av cellkontroller, som inkluderar följande:

- **Knapp**
- **Kryssruta**
- **Kombinationsrutan**

 Alla dessa kontroller är härledda från en abstrakt klass,**CellControl**.

**VIKTIG:** Om du vill lägga till cellkontroller till en enskild cell istället för hela kolumnen kan du referera till[Lägger till Cell kontroller i kalkylblad.](/cells/sv/net/adding-cell-controls-in-worksheets/)
### **Lägga till knapp**
För att lägga till knappar i en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Knapp** till någon specificerad**Kolumn** av**Arbetsblad**

**NOTERA:** Medan du lägger till**Knapp**, kan vi ange knappens bredd, höjd och bildtext.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 Ovan kodavsnitt lägger till knappar till alla celler i den angivna kolumnen. Närhelst någon cell i den specifika kolumnen väljs, blir en knapp synlig. För mer information om händelsehantering av knappar, se[Händelsehantering av en knappkontroll.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Lägger till kryssruta**
För att lägga till kryssrutor i en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Kryssruta** till någon specificerad**Kolumn** av**Arbetsblad**

**NOTERA:** Medan du lägger till**Kryssruta**, kan vi också ange status för kryssrutan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 Ovan kodavsnitt lägger till kryssrutor i alla celler i den angivna kolumnen. För mer information om händelsehantering av kryssrutor, se[Händelsehantering av en CheckBox-kontroll.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Lägger till ComboBox**
För att lägga till kombinationsrutor i en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Skapa en uppsättning objekt (eller värden) som kommer att läggas till**Kombinationsrutan**
-  Lägg till**Kombinationsrutan** (innehåller föremål eller värden) till någon specificerad**Kolumn** av**Arbetsblad**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 Ovan kodavsnitt lägger till kombinationsrutor till alla celler i den angivna kolumnen. När en cell i den specifika kolumnen markeras, blir en kombinationsruta synlig. För mer information om evenemangshantering av comboboxar, se[Händelsehantering av en ComboBox-kontroll.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
