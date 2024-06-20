---
title: Lägg till cellvalidering
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb, GridValidation, listvalidering, anpassad uttrycksvalidering
description: Den här artikeln introducerar hur man lägger till listvalidering, rullgardinsmenyvalidering och anpassad uttrycksvalidering i GridWeb.
---

{{% alert color="primary" %}} 

En av Aspose.Cells.GridWeb's avancerade funktioner är att lägga till regler för inmatningsvalidering för celler. Utvecklare kan skapa olika typer av valideringsregler för celler för att kontrollera och validera inmatningsvärden. Det här avsnittet diskuterar de stödda valideringstyperna och hur man skapar dem.

{{% /alert %}} 
## **Typer av Valideringar**
Tre typer av valideringar kan användas med Aspose.Cells.GridWeb:

- Listvalidering.
- Rullgardinsmenyvalidering.
- Anpassad uttrycksvalidering.

Var och en diskuteras i detalj nedan.
### **Listvalidering**
Listvalidering gör det möjligt för användare att ange cellinmatning antingen genom att skriva eller välja ett värde från en meny. För att skapa en listvalidering för en cell:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
1. Öppna cellen för att lägga till validering.
2. Skapa valideringen för cellen och ange valideringstypen som List.
3. Lägg till värden för listvalideringen.

Exemplet lägger till en listvalidering för C1. När en användare klickar på cellen visas en lista.

**Utmatning: välja ett värde från listan** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Rullgardinsmenyvalidering**
Rullgardinsmenyvalidering gör det möjligt för användare att ange inmatning för celler genom att välja ett värde från en fördefinierad lista. För att skapa en rullgardinsmenyvalidering:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
1. Öppna cellen för att skapa valideringen för.
2. Skapa en validering för cellen och ange typen som DropDownList.
3. Lägg till värden för valideringen.

Exemplet lägger till en rullgardinsmenyvalidering för C1. När en användare klickar på cellen visas en rullgardinsmeny och användare kan välja ett värde från den.

**Välja ett värde från en rullgardinsmeny** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Anpassad Uttrycksvalidering**
Anpassad uttrycksvalidering tillåter utvecklare att skriva sina egna anpassade reguljära uttryck för att validera inmatningsvärden. För att skapa en anpassad uttrycksvalidering:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
1. Öppna cellen för att skapa valideringen för.
2. Skapa en validering för cellen och ange typen som CustomExpression.
3. Ange valideringens reguljära uttryck.

Exemplet lägger till en anpassad uttrycksvalidering för C1. Användare kan endast lägga till ett datum i cellen enligt det format som anges av det reguljära uttrycket.

**Lägger till ett datumvärde i C1 enligt ett reguljärt uttryck** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Tvinga Validering**
Med Aspose.Cells.GridWeb kan användare skicka indata till en server. Även om det finns valideringsregler för olika celler men egenskapen ForceValidation för GridWeb-kontrollen inte är inställd på true, kommer felaktig indata ändå att skickas till servern och ingen validering tvingas. Egenskapen ForceValidation för GridWeb är alltid inställd på true som standard.

När egenskapen ForceValidation är sann skickar kontrollen inte data till webbservern förrän indata-värdena för alla celler är giltiga. Till exempel, om någon anger ett ogiltigt indata-värde i en cell eller inte anger ett värde aktiveras klientvalideringen och användarna kan inte skicka data även om de klickar på **Skicka**.

**Felaktigt indata-värde markerat av GridWeb** 

![todo:image_alt_text](add-cell-validations_4.png)
