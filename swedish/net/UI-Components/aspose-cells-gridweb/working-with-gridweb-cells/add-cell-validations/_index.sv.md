---
title: Lägg till Cell Valideringar
type: docs
weight: 70
url: /sv/net/add-cell-validations/
---
{{% alert color="primary" %}} 

En av Aspose.Cells.GridWebs avancerade funktioner är att lägga till regler för indatavalidering för celler. Utvecklare kan skapa olika typer av valideringsregler för celler för att kontrollera och validera indatavärden. Det här ämnet diskuterar de valideringstyper som stöds och hur man skapar dem.

{{% /alert %}} 
## **Typer av valideringar**
Tre typer av valideringar kan tillämpas med Aspose.Cells.GridWeb:

- Listvalidering.
- Validering av rullgardinsmenyn.
- Validering av anpassat uttryck.

Var och en diskuteras i detalj nedan.
### **Listvalidering**
Listvalidering tillåter användare att tillhandahålla cellinmatning antingen genom att skriva eller välja ett värde från en meny. Så här skapar du en listvalidering för en cell:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Gå till cellen för att lägga till validering.
1. Skapa valideringen för cellen och ange valideringstypen som Lista.
1. Lägg till värden för listvalideringen.

Exempelkoden lägger till en listvalidering till C1. När en användare klickar på cellen visas en lista.

**Utdata: välj ett värde från listan** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Validering av rullgardinsmenyn**
Validering av rullgardinslistor tillåter användare att ge indata för celler genom att välja ett värde från en fördefinierad lista. Så här skapar du en validering av rullgardinsmenyn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Gå till cellen för att skapa valideringen för.
1. Skapa en validering för cellen och ange typen som DropDownList.
1. Lägg till värden för valideringen.

Exempelkoden lägger till en listvalidering till C1. När en användare klickar på cellen visas en rullgardinsmeny och användare kan välja ett värde från den.

**Välja ett värde från en rullgardinsmeny** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Validering av anpassat uttryck**
Validering av anpassade uttryck låter utvecklare skriva sina egna anpassade reguljära uttryck för att validera indatavärden. Så här skapar du en anpassad uttrycksvalidering:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Gå till cellen för att skapa en validering för.
1. Skapa en validering för cellen och ange typen som CustomExpression.
1. Ställ in valideringens reguljära uttryck.

Exempelkoden lägger till en anpassad uttrycksvalidering till C1. Användare kan bara lägga till ett datum i cellen enligt formatet som anges av det reguljära uttrycket.

**Lägga till ett datumvärde till C1 enligt ett reguljärt uttryck** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Framtvinga validering**
Med hjälp av Aspose.Cells.GridWeb kan användare skicka indata till en server. Även om det finns valideringsregler för olika celler men GridWeb-kontrollens ForceValidation-egenskap inte är satt till true, kommer indata som är felaktiga också att skickas till servern och ingen validering tvingas fram. GridWebs ForceValidation-egenskap är alltid satt till true som standard.

 När egenskapen ForceValidation är sant skickar kontrollen inte data till webbservern förrän indatavärdena för alla celler är giltiga. Till exempel, om någon anger ett ogiltigt inmatningsvärde i en cell, eller inte anger ett värde, aktiveras valideringen på klientsidan och användarna kan inte lägga upp data även om de klickar**Skicka in**.

**Fel inmatningsvärde markerat av GridWeb** 

![todo:image_alt_text](add-cell-validations_4.png)
