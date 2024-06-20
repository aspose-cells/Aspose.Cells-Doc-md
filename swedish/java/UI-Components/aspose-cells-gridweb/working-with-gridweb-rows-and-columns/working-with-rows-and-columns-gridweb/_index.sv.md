---
title: Arbete med Rader och Kolumner i GridWeb
type: docs
weight: 20
url: /sv/java/working-with-rows-and-columns-gridweb/
---

## **Infoga Rader och Kolumner**
I den här artikeln förklaras hur man lägger till nya rader och kolumner i ett kalkylblad med hjälp av Aspose.Cells.GridWeb API. Rader eller kolumner kan infogas på vilken position som helst i kalkylbladet.
### **Infoga rader**
För att infoga en rad på valfri position i ett kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på webbformuläret eller sidan.
1. Hämta kalkylbladet du lägger till rader i.
1. Infoga en rad genom att ange en radindex där raden ska infogas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Infoga kolumner**
För att infoga en kolumn på valfri position i ett kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär eller en sida.
1. Hämta kalkylbladet du lägger till kolumner i.
1. Infoga en kolumn genom att ange kolumnindex där kolumnen ska infogas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Du kan också använda insertRows()/insertColumns() metoder för att infoga flera rader/kolumner i arbetsbladen enligt behov.

{{% /alert %}} 
## **Ta bort rader och kolumner**
Det här ämnet visar hur man tar bort rader och kolumner från ett arbetsblad med hjälp av Aspose.Cells.GridWeb API. Med hjälp av den här funktionen kan utvecklare ta bort rader eller kolumner vid runtime.
### **Ta bort rader**
För att ta bort en rad från ditt kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär eller en sida.
1. Kom åt det arbetsblad du vill ta bort rader från.
1. Ta bort en rad från kalkylbladet genom att specificera dess radindex.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Ta bort kolumner**
För att ta bort en kolumn från ditt kalkylblad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär eller en sida.
1. Öppna det kalkylblad där du vill ta bort kolumner.
1. Ta bort en kolumn från kalkylbladet genom att specificera dess kolumnindex.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Ställa in radhöjd och kolumnbredd**
Ibland är cellvärden bredare än cellen de är i eller är på flera rader. Sådana värden är inte helt synliga för användare om de inte ändrar höjden och bredden på rader och kolumner. Aspose.Cells.GridWeb stöder fullt ut inställning av radhöjder och kolumnbredd. Detta ämne diskuterar dessa funktioner i detalj med hjälp av exempel.
### **Arbeta med radhöjder och kolumnbredder**
#### **Ange radhöjd**
För att ställa in höjden på en rad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ditt webbformulär/sida.
1. Kom åt arbetsbladets GridCells-samling.
1. Ställ in höjden på alla celler i valfri angiven rad.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accepterar mått för radhöjd och kolumnbredd i punkter, tum, pixlar, osv.

{{% /alert %}} 

**Resultat: höjden på den första raden har ställts in till 50 punkter** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Ange kolumnbredd**
För att ställa in bredden på en kolumn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ditt webbformulär/sida.
1. Kom åt arbetsbladets GridCells-samling.
1. Ställ in bredden på alla celler i valfri angiven kolumn.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Anpassa rad- och kolumnrubriker**
Liksom Microsoft Excel använder även Aspose.Cells.GridWeb standardrubriker eller bildtext för rader (nummer som 1, 2, 3 osv.) och kolumner (alfabetiskt som A, B, C osv.). Aspose.Cells.GridWeb gör det också möjligt att anpassa rubriker. Detta ämne diskuterar anpassning av rad- och kolumnrubriker vid runtime med hjälp av Aspose.Cells.GridWeb API.
### **Anpassa radrubrik**
För att anpassa rubriken eller bildtexten för en rad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär/sida.
1. Få åtkomst till arbetsbladet i GridWorksheetCollection.
1. Ställ in bildtexten för en angiven rad.

**Rubrikerna för rad 1 och 2 har anpassats** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Anpassa kolumnrubrik**
För att anpassa rubriken eller bildtexten för en kolumn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär/sida.
1. Få åtkomst till arbetsbladet i GridWorksheetCollection.
1. Ställ in bildtexten för en angiven kolumn.

**Rubrikerna för kolumn 1 och 2 har anpassats** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Frys och Avfrys rader och kolumner**
Detta ämne förklarar hur man fryser och avfryser rader och kolumner. Att frysa kolumner eller rader gör att användarna kan behålla kolumnrubriker eller radrubriker synliga medan de bläddrar till andra delar av kalkylbladet. Den här funktionen är mycket användbar när man arbetar med kalkylblad som innehåller stora mängder data. När användarna bläddrar rullas bara data ner och rubrikerna stannar på plats, vilket gör det enklare att läsa datumen. Frysrutorna stöds endast i Internet Explorer 6.0 eller senare.
### **Frysa rader och kolumner**
För att frysa ett visst antal rader och kolumner:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär/sida.
2. Hämta ett arbetsblad.
1. Frysa ett antal rader och kolumner.

{{% alert color="primary" %}} 

Det är också möjligt att frysa ett visst antal rader och kolumner med hjälp av gränssnittet. Högerklicka på en cell där du vill frysa rader och kolumner och välj **Frys** från listan.

{{% /alert %}} 

**Rader och kolumner i ett fryst tillstånd** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Avfrysa rader och kolumner**
För att avfrysa rader och kolumner:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på ett webbformulär/sida.
2. Hämta ett arbetsblad.
1. Avfrysa rader och kolumner.

**Arbetsblad efter att ha avfrostats** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Skydda rader och kolumner**
Detta ämne diskuterar några tekniker för att skydda celler i rader och kolumner från alla typer av åtgärder som användarna utför. Utvecklare kan implementera detta skydd med hjälp av två tekniker: genom att göra celler i rader och kolumner skrivskyddade eller genom att begränsa GridWeb's kontextmenyalternativ.
### **Begränsa alternativen i kontextmenyn**
GridWeb tillhandahåller en kontextmeny som slutanvändare kan använda för att utföra operationer på kontrollen. Menyn ger många alternativ för att manipulera celler, rader och kolumner.

**Fullständiga kontextuella alternativ** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Det är möjligt att begränsa alla typer av klientåtgärder på rader och kolumner genom att begränsa de tillgängliga alternativen i kontextmenyn. Det kan göras genom att ställa in attributen EnableClientColumnOperations och EnableClientRowOperations i GridWeb-kontrollen till false. Det är också möjligt att förhindra användare från att frysa rader och kolumner genom att ställa in attributet EnableClientFreeze i GridWeb-kontrollen till false.

**Kontextmeny efter begränsning av alternativ för rad och kolumn** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
