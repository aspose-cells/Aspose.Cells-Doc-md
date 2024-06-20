---
title: Arbeta med Cells GridWeb
type: docs
weight: 50
url: /sv/java/working-with-cells-gridweb/
---

## **Tillgång till celler i arbetsbladet**
Det här avsnittet diskuterar celler och tittar på GridWebs mest grundläggande funktion: tillgång till celler.

Varje arbetsblad innehåller ett GridCells-objekt, en samling GridCell-objekt. Ett GridCell-objekt representerar en cell i Aspose.Cells.GridWeb. Det är möjligt att komma åt vilken cell som helst med GridWeb. Det finns två föredragna metoder:

- [Åtkomst till cellen efter namn](/cells/sv/java/working-with-cells-gridweb/).
- [Åtkomst till cellen efter rad- och kolumnindex](/cells/sv/java/working-with-cells-gridweb/).

Nedan diskuteras varje tillvägagångssätt.
### **Användning av cellnamn**
Alla celler har ett unikt namn. Till exempel A1, A2, B1, B2, etc. Aspose.Cells.GridWeb gör det möjligt för utvecklare att komma åt en önskad cell genom att använda cellnamnet. Skicka helt enkelt cellnamnet (som en index) till GridCells-samlingen i GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Använda rad- och kolumnindex**
En cell kan också känns igen genom dess plats i termer av rad- och kolumnindex. Skicka helt enkelt en cells rad- och kolumnindex till GridCells-samlingen i GridWorksheet. Detta tillvägagångssätt är snabbare än det föregående.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Komma åt och modifiera värdet av en cell**
[Tillgång till celler i arbetsbladet](/cells/sv/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) diskuterade åtkomst av celler. Detta ämne utökar den diskussionen för att visa hur man kommer åt och ändrar cellvärden med hjälp av GridWeb API.
### **Komma åt och ändra ett cells värde**
#### **Strängvärden**
Innan du kommer åt och modifierar värdet av en cell måste du veta hur man kommer åt celler. För detaljer om de olika tillvägagångssätten för att komma åt celler, se [Tillgång till celler i arbetsbladet](/cells/sv/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Varje cell har en egenskap som heter getStringValue(). När en cell har kommit åt kan utvecklare komma åt getStringValue()-metoden för att komma åt cellers strängvärde.

{{% alert color="primary" %}} 

VIKTIGT: Fem typer av värden (Boolean, int, double, DateTime och sträng) kan lagras i celler, men getValue()/setValue()-metoderna kan endast användas för att komma åt/modifiera objektvärde.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Alla typer av värden**
Aspose.Cells.GridWeb tillhandahåller också en speciell metod, putValue, för varje cell. Med denna metod är det möjligt att infoga eller ändra vilken typ av värde som helst (Boolean, int, double, DateTime och sträng) i en cell.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Det finns också en överbelastad version av putValue-metoden som kan ta vilken typ av värde som helst i strängformat och konvertera det till en lämplig datatyp automatiskt. För att göra det, skicka det Booleska värdet true till en annan parameter i putValue-metoden enligt exemplet nedan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Lägga till formler i cellerna**
Den mest värdefulla funktionen som erbjuds av Aspose.Cells.GridWeb är stöd för formler eller funktioner. Aspose.Cells.GridWeb har sin egen Formula Engine som beräknar formlerna i arbetsblad. Aspose.Cells.GridWeb stöder både inbyggda och användardefinierade funktioner eller formler. Detta ämne diskuterar lägg till formler i celler med hjälp av Aspose.Cells.GridWeb API i detalj.
### **Hur man lägger till och beräknar en formel?**
Det är möjligt att lägga till, komma åt och modifiera formler i celler genom att använda cellens Formula-egenskap. Aspose.Cells.GridWeb stöder användardefinierade formler som sträcker sig från enkla till komplexa. Dock medföljer även ett stort antal inbyggda funktioner eller formler (liknande Microsoft Excel) med Aspose.Cells.GridWeb. För att se den fullständiga listan över inbyggda funktioner, vänligen hänvisa till denna [lista över stödda funktioner.](/cells/sv/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formelsyntaxen ska vara kompatibel med Microsoft Excel syntax. Till exempel måste alla formler börja med ett lika med-tecken (=).

För att lägga till en formel programmatiskt kommer Aspose.Cells.GridWeb att känna igen den som en formel även om du inte använder ett **=**-tecken, men om slutanvändare som arbetar i GUI måste använda det.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formel tillagd till cell B3 men inte beräknad av GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

På skärmbilden ovan kan du se att en formel har lagts till B3 men har ännu inte beräknats. För att beräkna alla formler, anropa GridWeb kontrollens GridWorksheetCollections calculateFormula-metod efter att ha lagt till formler i arbetsbladen enligt nedan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Användare kan också beräkna formler genom att klicka på **Skicka**.

**Klicka på Submit-knappen i GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**VIKTIGT**: Om en användare klickar på **Spara** eller **Ångra**-knapparna, eller arbetsbladets flikar, beräknas alla formler automatiskt av GridWeb.

**Formelresultat efter beräkning** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Referera till celler från andra arbetsblad**
Med Aspose.Cells.GridWeb är det möjligt att referera till värden som lagras i olika arbetsblad i deras formler och skapa komplexa formler.

Syntaxen för att referera till en cells värde från ett annat arbetsblad är ArkNamn!CellNamn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Skapa datavalidering i en GridCell av GridWeb**
Aspose.Cells.GridWeb gör det möjligt att lägga till **Data Validering** med hjälp av metoden GridWorksheet.getValidations().add(). Med denna metod måste du ange **Cell Range**. Men om du vill skapa en Data Validering i en enda GridCell kan du göra det direkt med metoden GridCell.createValidation(). På liknande sätt kan du ta bort **Data Validering** från en GridCell med hjälp av metoden GridCell.removeValidation().

Följande exempelkod skapar en **Data Validering** i en cell B3. Om du anger något värde som inte ligger mellan 20 och 40, kommer cellen B3 att visa en **Valideringsfel** i form av **Rött XXXX** som visas på skärmdumpen.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Skapande av Anpassade Kommandoknappar**
Aspose.Cells.GridWeb innehåller specialknappar som Submit, Save och Undo. Alla dessa knappar utför specifika uppgifter för Aspose.Cells.GridWeb. Det är också möjligt att lägga till anpassade knappar som utför anpassade uppgifter. Detta ämne förklarar hur du använder den här funktionen.

Följande exempelkod förklarar hur man skapar en anpassad kommandoknapp och hur man hanterar dess klickevenemang. Du kan använda vilken ikon som helst för din anpassade kommandoknapp. Som illustrering använde vi den här bild-ikonen.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Som du kan se på följande skärmdump, när användaren klickar på den anpassade kommandoknappen, läggs en text till i cell A1 som säger **"Min anpassade kommandoknapp har klickats"**.

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Hantering av Anpassad Kommandoknappshändelse**
Följande exempelkod förklarar hur man utför händelshantering av anpassad kommandoknapp.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formatering av celler för GridWeb**
### **Möjliga användningsscenario**
GridWeb stöder nu att användare anger celldata i procentformat som 3% och data i cellen formateras automatiskt som 3,00%. Du måste dock ställa in cellformatet. till procentformat vilket antingen är GridTableItemStyle.NumberType a 9 eller 10. Numret 9 kommer formatera 3% som 3% men numret 10 kommer formatera 3% som 3,00%.

{{% alert color="primary" %}} 

Om du inte har ställt in cellformatet till procentformat, kommer inmatningsdata 3% visas som 0,03.

{{% /alert %}} 
### **Ange celldata i GridWeb-arbetsblad i procentformat**
Följande exempelkod ställer in cell A1 GridTableItemStyle.NumberType som 10, därmed kommer inmatningsdata 3% automatiskt formateras som 3,00% som visas på skärmdumpen.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
