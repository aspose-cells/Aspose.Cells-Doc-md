---
title: Arbetar med Cells GridWeb
type: docs
weight: 50
url: /sv/java/working-with-cells-gridweb/
---
## **Åtkomst till Cells i arbetsbladet**
Det här ämnet diskuterar celler och tittar på GridWebs mest grundläggande funktion: åtkomst till celler.

Varje kalkylblad innehåller ett GridCells-objekt, en samling GridCell-objekt. Ett GridCell-objekt representerar en cell i Aspose.Cells.GridWeb. Det är möjligt att komma åt vilken cell som helst med hjälp av GridWeb. Det finns två föredragna metoder:

- [Åtkomst till cellen med namn](/cells/sv/java/working-with-cells-gridweb/).
- [Åtkomst till cellen efter rad- och kolumnindex](/cells/sv/java/working-with-cells-gridweb/).

Nedan diskuteras varje tillvägagångssätt.
### **Använder Cell Namn**
Alla celler har ett unikt namn. Till exempel A1, A2, B1, B2, etc. Aspose.Cells.GridWeb tillåter utvecklare att komma åt vilken cell som helst genom att använda cellnamnet. Skicka helt enkelt cellnamnet (som ett index) till GridCells-samlingen i GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Använda rad- och kolumnindex**
En cell kan också kännas igen på sin plats i termer av rad- och kolumnindex. Skicka bara en cells rad- och kolumnindex till GridCells-samlingen i GridWorksheet. Detta tillvägagångssätt är snabbare än ovanstående.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Få åtkomst till och ändra värdet på en Cell**
[Åtkomst till Cells i arbetsbladet](/cells/sv/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) diskuterade tillgång till celler. Det här ämnet utökar den diskussionen för att visa hur man kommer åt och ändrar cellvärden med GridWeb API.
### **Få åtkomst till och ändra en Cells värde**
#### **Strängvärden**
 Innan du kommer åt och ändrar värdet på en cell måste du veta hur du kommer åt celler. För detaljer om de olika metoderna för att komma åt celler, se[Åtkomst till Cells i arbetsbladet](/cells/sv/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Varje cell har en egenskap som heter getStringValue(). När en cell väl har nåtts kan utvecklare komma åt metoden getStringValue() för att komma åt cellsträngsvärdet.

{{% alert color="primary" %}} 

VIKTIGT: Fem typer av värden (Boolean, int, double, DateTime och string) kan lagras i celler men metoden getValue()/setValue() kan endast användas för att komma åt/ändra objektvärde.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Alla typer av värden**
Aspose.Cells.GridWeb tillhandahåller också en speciell metod, putValue, för varje cell. Med den här metoden är det möjligt att infoga eller ändra vilken typ av värde som helst (Boolean, int, double, DateTime och string) i en cell.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Det finns också en överbelastad version av putValue-metoden som kan ta vilken typ av värde som helst i strängformat och konvertera det till en korrekt datatyp automatiskt. För att få det att hända, skicka det booleska värdet true till en annan parameter i putValue-metoden som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Lägger till formler till Cells**
Den mest värdefulla funktionen som erbjuds av Aspose.Cells.GridWeb är stöd för formler eller funktioner. Aspose.Cells.GridWeb har sin egen Formula Engine som beräknar formlerna i kalkylblad. Aspose.Cells.GridWeb stöder både inbyggda och användardefinierade funktioner eller formler. Det här ämnet diskuterar hur man lägger till formler i celler med Aspose.Cells.GridWeb API i detalj.
### **Hur lägger man till och beräknar en formel?**
 Det är möjligt att lägga till, komma åt och ändra formler i celler genom att använda en cells formelegenskap. Aspose.Cells.GridWeb stöder användardefinierade formler som sträcker sig från enkla till komplexa. Men ett stort antal inbyggda funktioner eller formler (liknande Microsoft Excel) levereras också med Aspose.Cells.GridWeb. För att se hela listan över inbyggda funktioner, se denna[lista över funktioner som stöds.](/cells/sv/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formelsyntaxen bör vara kompatibel med Microsoft Excel-syntaxen. Till exempel måste alla formler börja med ett likhetstecken (=).

För att lägga till en formel programmatiskt kommer Aspose.Cells.GridWeb att känna igen den som en formel även om du inte använder ett **=**-tecken, men om slutanvändare som arbetar i GUI måste använda den.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formel har lagts till i B3-cellen men inte beräknats av GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

I ovanstående skärmdump kan du se att en formel har lagts till i B3 men inte har beräknats ännu. För att beräkna alla formler, anrop GridWeb-kontrollens GridWorksheetCollections calculateFormula-metod efter att ha lagt till formler till kalkylblad som visas nedan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Användare kan också beräkna formler genom att klicka**Skicka in**.

**Klicka på knappen Skicka på GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**VIKTIG** : Om en användare klickar på**Spara** eller**Ångra** knappar, eller arkflikarna, beräknas alla formler automatiskt av GridWeb.

**Formelresultat efter beräkning** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Refererar till Cells från andra arbetsblad**
Med hjälp av Aspose.Cells.GridWeb är det möjligt att referera värden lagrade i olika kalkylblad i deras formler, vilket skapar komplexa formler.

Syntaxen för att referera till ett cellvärde från ett annat kalkylblad är SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Skapa datavalidering i en GridCell av GridWeb**
 Aspose.Cells.GridWeb låter dig lägga till**Datavalidering** med metoden GridWorksheet.getValidations().add(). Med den här metoden måste du ange**Cell Räckvidd** . Men om du vill skapa en datavalidering i en enda GridCell kan du göra det direkt med metoden GridCell.createValidation(). På samma sätt kan du ta bort**Datavalidering** från en GridCell med metoden GridCell.removeValidation().

 Följande exempelkod skapar en**Datavalidering** i en cell B3. Om du anger något värde som inte är mellan 20 och 40, visas cellen B3**Valideringsfel** i formen av**Röd XXXX** som visas i denna skärmdump.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Skapa anpassade kommandoknappar**
Aspose.Cells.GridWeb innehåller specialknappar som Skicka, Spara och Ångra. Alla dessa knappar utför specifika uppgifter för Aspose.Cells.GridWeb. Det är också möjligt att lägga till anpassade knappar som utför anpassade uppgifter. Det här avsnittet förklarar hur du använder den här funktionen.

Följande exempelkod förklarar hur man skapar en anpassad kommandoknapp och hur man hanterar dess klickhändelse. Du kan använda vilken ikon som helst för din anpassade kommandoknapp. Som illustration använde vi denna bildikon.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

 Som du kan se i följande skärmdump, när användaren klickar på den anpassade kommandoknappen, lägger den till en text i cell A1 som säger**"Min anpassade kommandoknapp klickas."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Händelsehantering av anpassad kommandoknapp**
Följande exempelkod förklarar hur man utför händelsehantering av anpassad kommandoknapp.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formatera celler för GridWeb**
### **Möjliga användningsscenarier**
GridWeb stöder nu användare att ange celldata i procentformat som 3% och data i cellen kommer automatiskt att formateras som 3,00%. Du måste dock ställa in cellformatet till procentformat som antingen är GridTableItemStyle.NumberType en 9 eller 10. Siffran 9 kommer att formatera 3 % som 3 % men siffran 10 kommer att formatera 3 % som 3,00 %.

{{% alert color="primary" %}} 

Om du inte har ställt in cellformatet till Procentformat, kommer indata 3% att visas som 0,03.

{{% /alert %}} 
### **Ange Cell Data för GridWeb-arbetsbladet i procentformat**
Följande exempelkod ställer in cellen A1 GridTableItemStyle.NumberType som 10, därför formateras indata 3 % automatiskt till 3,00 % som visas på skärmdumpen.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
