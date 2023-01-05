---
title: Arbeta med rader och kolumner GridWeb
type: docs
weight: 20
url: /sv/java/working-with-rows-and-columns-gridweb/
---
## **Infoga rader och kolumner**
Det här avsnittet förklarar hur man infogar nya rader och kolumner i ett kalkylblad med hjälp av Aspose.Cells.GridWeb API. Rader eller kolumner kan infogas var som helst i kalkylbladet.
### **Infoga rader**
Så här infogar du en rad var som helst i ett kalkylblad:

1. Lägg till kontrollen Aspose.Cells.GridWeb till webbformuläret eller sidan.
1. Öppna kalkylbladet du lägger till rader i.
1. Infoga en rad genom att ange ett radindex där raden ska infogas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Infoga kolumner**
Så här infogar du en kolumn på valfri plats i ett kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär eller en sida.
1. Öppna kalkylbladet du lägger till kolumner i.
1. Infoga en kolumn genom att ange kolumnindex där kolumnen ska infogas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Du kan också använda insertRows()/insertColumns() metoder för att infoga flera rader/kolumner i kalkylbladen i enlighet med detta.

{{% /alert %}} 
## **Ta bort rader och kolumner**
Det här avsnittet visar hur man tar bort rader och kolumner från ett kalkylblad med hjälp av Aspose.Cells.GridWeb API. Med hjälp av den här funktionen kan utvecklare ta bort rader eller kolumner under körning.
### **Ta bort rader**
Så här tar du bort en rad från ditt kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär eller en sida.
1. Öppna kalkylbladet du vill ta bort rader från.
1. Ta bort en rad från kalkylbladet genom att ange dess radindex.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Ta bort kolumner**
Så här tar du bort en kolumn från ditt kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär eller en sida.
1. Öppna kalkylbladet du vill ta bort kolumner från.
1. Ta bort en kolumn från kalkylbladet genom att ange dess kolumnindex.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Ställa in radhöjd och kolumnbredd**
Ibland är cellvärden bredare än cellen de är i eller finns på flera rader. Sådana värden är inte helt synliga för användare om de inte ändrar höjden och bredden på rader och kolumner. Aspose.Cells.GridWeb stöder fullt ut inställning av radhöjder och kolumnbredd. Det här ämnet diskuterar dessa funktioner i detalj med hjälp av exempel.
### **Arbeta med radhöjder och kolumnbredd**
#### **Ställa in radhöjd**
Så här ställer du in höjden på en rad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till din webbformulär/sida.
1. Få tillgång till kalkylbladets GridCells-samling.
1. Ställ in höjden på alla celler i en angiven rad.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accepterar radhöjd och kolumnbreddsmått i punkter, tum, pixlar, etc.

{{% /alert %}} 

**Utgång: höjden på den första raden har ställts in på 50 punkter** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Ställa in kolumnbredd**
Så här ställer du in bredden på en kolumn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till din webbformulär/sida.
1. Få tillgång till kalkylbladets GridCells-samling.
1. Ställ in bredden på alla celler i en viss kolumn.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Anpassa rad- och kolumnrubriker**
Som Microsoft Excel, Aspose.Cells.GridWeb använder också standardrubriker eller bildtexter för rader (siffror som 1, 2, 3 och så vidare) och kolumner (alfabetiska som A, B, C och så vidare). Aspose.Cells.GridWeb gör det också möjligt att anpassa bildtexter. Det här ämnet diskuterar anpassning av rad- och kolumnrubriker vid körning med Aspose.Cells.GridWeb API.
### **Anpassa radhuvud**
Så här anpassar du rubriken eller bildtexten för en rad:

1. Lägg till kontrollen Aspose.Cells.GridWeb till ett webbformulär/-sida.
1. Öppna kalkylbladet i GridWorksheetCollection.
1. Ställ in bildtexten för valfri angiven rad.

**Rubrikerna på rad 1 och 2 har anpassats** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Anpassa kolumnrubrik**
Så här anpassar du rubriken eller bildtexten för en kolumn:

1. Lägg till kontrollen Aspose.Cells.GridWeb till ett webbformulär/-sida.
1. Öppna kalkylbladet i GridWorksheetCollection.
1. Ställ in bildtexten för en viss kolumn.

**Rubrikerna i kolumn 1 och 2 har anpassats** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Frys och lås upp rader och kolumner**
Det här avsnittet förklarar hur man fryser och släpper rader och kolumner. Frysning av kolumner eller rader tillåter användare att hålla kolumnrubrikerna eller radrubrikerna synliga medan de rullar till andra delar av kalkylbladet. Den här funktionen är mycket användbar när du arbetar med kalkylblad som innehåller stora mängder data. När användare rullar rullas endast data nedåt och rubrikerna stannar på plats, vilket gör datumet lättare att läsa. Funktionen för frysning av rutor stöds endast i Internet Explorer 6.0 eller senare.
### **Fryser rader och kolumner**
Så här fryser du ett visst antal rader och kolumner:

1. Lägg till kontrollen Aspose.Cells.GridWeb till ett webbformulär/-sida.
1. Få tillgång till ett arbetsblad.
1. Frys ett antal rader och kolumner.

{{% alert color="primary" %}} 

 Det är också möjligt att frysa ett specifikt antal rader och kolumner med hjälp av gränssnittet. Högerklicka på en cell där du vill frysa rader och kolumner och välj**Frysa** från listan.

{{% /alert %}} 

**Rader och kolumner i fryst tillstånd** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Frigör rader och kolumner**
Så här låser du upp rader och kolumner:

1. Lägg till kontrollen Aspose.Cells.GridWeb till ett webbformulär/-sida.
1. Få tillgång till ett arbetsblad.
1. Frigör rader och kolumner.

**Arbetsblad efter att ha frysts upp** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Skydda rader och kolumner**
Det här ämnet diskuterar några tekniker för att skydda celler i rader och kolumner från alla typer av åtgärder som utförs av slutanvändare. Utvecklare kan implementera detta skydd med två tekniker: genom att göra celler i rader och kolumner skrivskyddade eller genom att begränsa GridWebs snabbmenyalternativ.
### **Begränsa kontextmenyalternativ**
GridWeb tillhandahåller en snabbmeny som slutanvändare kan använda för att utföra operationer på kontrollen. Menyn innehåller många alternativ för att manipulera celler, rader och kolumner.

**Komplettera kontextuella alternativ** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Det är möjligt att begränsa alla typer av operationer på klientsidan på rader och kolumner genom att begränsa de tillgängliga alternativen i snabbmenyn. Det kan göras genom att ställa in attributen EnableClientColumnOperations och EnableClientRowOperations för GridWeb-kontrollen till false. Det är också möjligt att begränsa användare från att frysa rader och kolumner genom att ställa in GridWeb-kontrollens EnableClientFreeze-attribut till false.

**Snabbmeny efter begränsning av rad- och kolumnalternativ** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
