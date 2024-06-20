---
title: Arbeta med valideringar i arbetsblad
type: docs
weight: 70
url: /sv/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop, valideringar, validering
description: Denna artikel introducerar hur man arbetar med validering i GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop stöder också att lägga till valideringar (eller valideringsregler) till cellerna i ett arbetsblad. Genom att tillämpa valideringsregler på celler kan utvecklare begränsa användare att ange data i Grid i ett specifikt format. Olika valideringstyper stöds av Aspose.Cells.GridDesktop. I detta avsnitt kommer vi inte bara att diskutera dessa valideringstyper utan också förklara manipulationen av dessa valideringar.

{{% /alert %}} 
## **Valideringstyper**
Det finns tre valideringstyper som stöds av Aspose.Cells.GridDesktop enligt följande:

- Är Obligatorisk Valideringstyp
- Reguljära Uttryck Valideringstyp
- Anpassad Valideringstyp
### **Krävs valideringsläge**
I det här valideringsläget begränsas användarna att ange värden i angivna celler. När **Is Required Validation** tillämpas på en kalkylbladscell måste användaren ange ett värde i den cellen.
### **Reguljära uttryck valideringsläge**
I det här läget tillämpas restriktioner på arbetsboksceller för att användarna ska kunna skicka in data i en specifik format. Mönstret för dataformatet tillhandahålls i form av ett **Reguljärt uttryck**.
### **Anpassat valideringsläge**
För att använda **anpassad validering** är det ett krav för utvecklare att implementera Aspose.Cells.GridDesktop.ICustomValidation interface. Gränssnittet tillhandahåller en **Validera**-metod. Denna metod returnerar true om datan är giltig annars returnerar den false.
## **Arbeta med validering i Aspose.Cells.GridDesktop**
### **Lägga till validering**
För att lägga till någon form av validering på en kalkylbladscell, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till önskad validering i **Validerings**-samlingen av **Kalkylbladet** för att ange vilken validering som ska tillämpas på vilken cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

I den ovanstående figuren har vi också nämnt valideringsreglerna framför celler där dessa valideringsregler tillämpas. Om ett ogiltigt värde (som inte är giltigt enligt den valideringsregel som är definierad för den cellen) matas in, skulle en **MessageBox** visas för att meddela användaren om det ogiltiga inträffandet.

{{% /alert %}} 
### **Implementera ICustomValidation**
I den ovanstående kodsnutten har vi lagt till en anpassad validering i **A8**-cellen men vi har ännu inte implementerat denna anpassade validering. Som vi har förklarat i början av detta ämne att för att tillämpa anpassad validering måste vi implementera **ICustomValidation** gränssnittet. Så låt oss försöka skapa en klass för att implementera **ICustomValidation**-gränssnittet.

I kodsnutten nedan har vi implementerat en anpassad validering för att utföra följande kontroller:

- Kontrollera om cellens adress är korrekt där valideringen är tillagd
- Kontrollera om cellens datatyp är dubbel
- Kontrollera om cellens värde är större än 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Åtkomst av validering**
När en validering läggs till på en specifik arbetsbokscell kan det vara nödvändigt för utvecklare att få åtkomst till och modifiera attributen för en specifik validering vid körning. Så har Aspose.Cells.GridDesktop gjort det enkelt för utvecklare att utföra denna uppgift.

För att komma åt en specifik validering, följ stegen nedan:

- Kom åt ett önskat **Kalkylblad**
- Kom åt en specifik **Validering** i kalkylbladet genom att ange cellnamnet på vilken valideringen tillämpades
- Redigera **Validering**-attribut, om önskat



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validerings**-samlingen har två indexerare. En indexerare (som används i det följande exemplet) gör det möjligt att komma åt en **Validering**-objekt genom att ta ett cellnamn som dess index medan den andra indexeraren tar två parametrar (dvs. rad- och kolumnnummer) för att utföra samma uppgift.

{{% /alert %}} 
### **Ta bort validering**
För att ta bort en specifik validering från kalkylbladet, följ stegen nedan:

- Kom åt ett önskat **Kalkylblad**
- Ta bort en specifik **Validering** från **Kalkylbladet** genom att ange cellnamnet på vilken valideringen tillämpades



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
