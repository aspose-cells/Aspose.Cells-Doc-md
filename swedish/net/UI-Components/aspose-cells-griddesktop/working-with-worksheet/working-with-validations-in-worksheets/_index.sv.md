---
title: Arbeta med valideringar i arbetsblad
type: docs
weight: 70
url: /sv/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop stöder också att lägga till valideringar (eller valideringsregler) till cellerna i ett kalkylblad. Genom att tillämpa valideringsregler på celler kan utvecklare begränsa användare att ange data i Grid i ett specifikt format. Olika valideringslägen stöds av Aspose.Cells.GridDesktop. I det här ämnet kommer vi inte bara att diskutera dessa valideringslägen utan också förklara manipuleringen av dessa valideringar.

{{% /alert %}} 
## **Valideringslägen**
Det finns tre valideringslägen som stöds av Aspose.Cells.GridDesktop enligt följande:

- Krävs valideringsläge
- Valideringsläge för reguljära uttryck
- Anpassat valideringsläge
### **Krävs valideringsläge**
 I detta valideringsläge är användarna begränsade till att ange värden i specificerade celler. En gång**Krävs validering** tillämpas på en kalkylbladscell, blir det ett måste för en användare att ange värde i den cellen.
### **Valideringsläge för reguljära uttryck**
 I det här läget tillämpas begränsningar på kalkylbladsceller för användarna att skicka in data till celler i ett specifikt format. Mönstret för dataformat tillhandahålls i form av en**Vanligt uttryck**.
### **Anpassat valideringsläge**
 Att använda**Anpassad validering** , Det är ett måste för utvecklare att implementera gränssnittet Aspose.Cells.GridDesktop.ICustomValidation. Gränssnittet ger en**Bekräfta** metod. Denna metod returnerar true om data är giltig annars returnerar false.
## **Arbeta med valideringar i Aspose.Cells.GridDesktop**
### **Lägger till validering**
För att lägga till någon form av validering till en kalkylbladscell, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till en önskad validering till**Valideringar** samling av**Arbetsblad** för att ange vilken validering som skulle tillämpas på vilken cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 I figuren ovan har vi också nämnt valideringsreglerna framför celler där dessa valideringsregler tillämpas. Om något ogiltigt värde (som inte är giltigt enligt valideringsregeln definierad för den cellen) anges,**Meddelandebox** verkar meddela användaren om den ogiltiga posten.

{{% /alert %}} 
### **Implementering av ICustomValidation**
 I kodavsnittet ovan har vi lagt till en anpassad validering i**A8**cell men vi har inte implementerat den anpassade valideringen ännu. Som vi har förklarat i början av det här ämnet att för att tillämpa anpassad validering måste vi implementera**ICustomValidation** gränssnitt. Så låt oss försöka skapa en klass att implementera**ICustomValidation** gränssnitt.

I kodavsnittet nedan har vi implementerat en anpassad validering för att utföra följande kontroller:

- Kontrollera om cellens adress är korrekt där valideringen läggs till
- Kontrollera om datatypen för cellens värde är dubbelt
- Kontrollera om cellens värde är större än 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Åtkomst till validering**
När en validering har lagts till i en specifik kalkylbladscell kan det krävas av utvecklare att få tillgång till och ändra attributen för en specifik validering under körning. Så, Aspose.Cells.GridDesktop har gjort det enkelt för utvecklare att utföra denna uppgift.

För att komma åt en specifik validering, följ stegen nedan:

-  Få tillgång till en önskad**Arbetsblad**
-  Få tillgång till en specifik**Godkännande** kalkylbladet genom att ange cellnamnet som valideringen tillämpades på
-  Redigera**Godkännande** attribut, om så önskas



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Valideringar** samlingen har två indexerare. En indexerare (som används i exemplet nedan) tillåter åtkomst till en**Godkännande** objekt genom att ta ett cellnamn som dess index medan den andra indexeraren tar två parametrar (det vill säga rad- och kolumnnummer) för att utföra samma uppgift.

{{% /alert %}} 
### **Ta bort validering**
För att ta bort en specifik validering från kalkylbladet, följ stegen nedan:

-  Få tillgång till en önskad**Arbetsblad**
-  Ta bort en specifik**Godkännande** från**Arbetsblad** genom att ange cellnamnet som valideringen tillämpades på



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
