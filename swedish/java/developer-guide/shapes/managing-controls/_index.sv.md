---
title: Hantera kontroller
type: docs
weight: 120
url: /sv/java/managing-controls/
---
## **Introduktion**

Utvecklare kan lägga till olika ritobjekt såsom textrutor, kryssrutor, radioknappar, kombinationsrutor, etiketter, knappar, linjer, rektanglar, bågar, ovaler, spinnare, rullningslister, grupprutor etc. Aspose.Cells tillhandahåller namnutrymmet Aspose.Cells.Drawing som innehåller alla ritobjekt. Det finns dock några ritobjekt eller former som inte stöds ännu. Skapa dessa ritobjekt i ett designerkalkylblad med Microsoft Excel och importera sedan designerkalkylarket till Aspose.Cells. Med Aspose.Cells kan du ladda dessa ritobjekt från ett designerkalkylblad och skriva dem till en genererad fil.

## **Lägga till TextBox Control till arbetsbladet**

 Ett sätt att betona viktig information i en rapport är att använda en textruta. Till exempel, lägg till text för att markera företagsnamnet eller för att ange den geografiska region med högst försäljning etc. Aspose.Cells tillhandahåller klassen TextBoxes, som används för att lägga till en ny textruta i samlingen. Det finns en annan klass,[**Textruta**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox)som representerar en textruta som används för att definiera alla typer av inställningar. Den har några viktiga medlemmar:

-  De[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) metod returnerar en[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) objekt som används för att justera innehållet i textrutan.
-  De[**setPlacering**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) metod anger placeringstypen.
-  De[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) metod anger teckensnittsattributen.
-  De[**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String))-metoden lägger till en hyperlänk för textrutan.
-  De[**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) egendom returnerar[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) objekt som används för att ställa in fyllningsformatet för textrutan.
-  De[**Linjeformat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) egendom returnerar[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) objekt som vanligtvis används för stil och vikt på textrutans rad.
-  De[**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) metod anger inmatningstexten för textrutan.

Följande exempel skapar två textrutor i det första kalkylbladet i arbetsboken. Den första textrutan är välutrustad med olika formatinställningar. Den andra är enkel.

Följande utdata genereras genom att exekvera koden:

**Två textrutor skapas i kalkylbladet** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulera textrutekontroller i Designer-kalkylbladen**

 Aspose.Cells låter dig också komma åt textrutor i designerkalkylbladen och manipulera dem. Använd[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) egenskap för att få textboxsamlingen i arket.

Följande exempel använder Excel-filen Microsoft – tsttextboxes.xls – som vi skapade i exemplet ovan. Den hämtar textsträngarna för de två textrutorna och ändrar texten i den andra textrutan för att spara filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Lägger till CheckBox Control till arbetsbladet**

Kryssrutor är praktiska om du vill tillhandahålla ett sätt för en användare att välja mellan två alternativ, till exempel sant eller falskt; Ja eller nej. Aspose.Cells låter dig använda kryssrutor i kalkylblad. Du kan till exempel ha utvecklat ett kalkylblad för ekonomisk projektion där du antingen kan redogöra för ett visst förvärv eller inte. I det här fallet kanske du vill placera en kryssruta överst på kalkylbladet. Du kan sedan länka statusen för den här kryssrutan till en annan cell, så att om kryssrutan är markerad är cellens värde True; om den inte är markerad är cellens värde False.

### **Använder Microsoft Excel**

För att placera en kryssrutakontroll i ditt kalkylblad, följ dessa steg:

1. Se till att verktygsfältet Formulär visas.
1.  Klicka på**Kryssruta** verktyget i verktygsfältet Formulär.
1. Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla kryssrutan och etiketten bredvid kryssrutan.
1. När kryssrutan är placerad flyttar du muspekaren till etikettområdet och ändrar etiketten.
1.  I den**Cell Länk**fältet, ange adressen till cellen som den här kryssrutan ska länkas till.
1.  Klicka på**OK**.

### **Använder Aspose.Cells**

 Aspose.Cells tillhandahåller[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) klass, som används för att lägga till en ny kryssruta i samlingen. Det finns en annan klass,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), som representerar en kryssruta. Den har några viktiga medlemmar:

-  De[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) metod anger en cell som är länkad till kryssrutan.
-  De[**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) metod anger textsträngen som är associerad med kryssrutan. Det är etiketten för kryssrutan.
-  De[**satt värde**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) metod anger om kryssrutan är markerad eller inte.

Följande exempel visar hur du lägger till en kryssruta i kalkylbladet. Utdata nedan genereras efter exekvering av koden.

**En kryssruta läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Lägger till RadioButton Control till arbetsbladet**

En alternativknapp, eller en alternativknapp, är en kontroll gjord av en rund låda. Användaren fattar sitt beslut genom att markera den runda rutan. En alternativknapp är vanligtvis, om inte alltid, åtföljd av andra. Sådana alternativknappar visas och fungerar som en grupp. Användaren bestämmer vilken knapp som är giltig genom att endast välja en av dem. När användaren klickar på en knapp fylls den. När en knapp i gruppen är vald är knapparna i samma grupp tomma.

### **Använder Microsoft Excel**

För att placera en radioknappkontroll i ditt kalkylblad, följ dessa steg:

1.  Se till att**Blanketter** verktygsfältet visas.
1.  Klicka på**Alternativknapp** verktyg.
1. I kalkylbladet klickar och drar du för att definiera rektangeln som håller alternativknappen och etiketten bredvid alternativknappen.
1. När alternativknappen är placerad i kalkylbladet flyttar du muspekaren till etikettområdet och ändrar etiketten.
1.  I den**Cell Länk** fältet, ange adressen till cellen som denna alternativknapp ska länkas till.
1.  Klick**OK**.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)klass tillhandahåller en metod som heter addShape som kan användas för att lägga till en alternativknappskontroll till ett kalkylblad. Metoden kan returnera ett RadioButton-objekt. Klassen RadioButton representerar en alternativknapp. Den har några viktiga medlemmar:

- Metoden setLinkedCell specificerar en cell som är länkad till alternativknappen.
- Metoden setText anger textsträngen som är kopplad till alternativknappen. Det är radioknappens etikett.
- Egenskapen Markerad anger om alternativknappen är markerad eller inte.
- Metoden setFillFormat anger fyllningsformatet för alternativknappen.
- Metoden setLineFormat anger linjeformatsstilarna för alternativknappen.

Följande exempel visar hur du lägger till alternativknappar i ett kalkylblad. Exemplet lägger till tre alternativknappar som representerar åldersgrupper. Följande utdata skulle genereras efter exekvering av koden.

**Vissa RadioButtons läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Lägga till Combo Box Control till ett kalkylblad**

För att göra datainmatning enklare, eller för att begränsa poster till vissa objekt som du definierar, kan du skapa en kombinationsruta eller en rullgardinslista med giltiga poster som kompileras från celler någon annanstans i kalkylbladet. När du skapar en rullgardinslista för en cell visas en pil bredvid den cellen. För att ange information i den cellen, klicka på pilen och klicka sedan på posten du vill ha.

### **Använder Microsoft Excel**

För att placera en kombinationsrutakontroll i ditt kalkylblad, följ dessa steg:

1.  Se till att**Blanketter** verktygsfältet visas.
1.  Klicka på**Kombinationsrutan** verktyg.
1. Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla kombinationsrutan.
1.  När kombinationsrutan är placerad i kalkylbladet högerklickar du på kontrollen för att klicka**Formatkontroll** och ange ingångsintervallet.
1.  I den**Cell Länk** fältet, ange adressen till cellen som denna kombinationsruta ska länkas till.
1.  Klicka på**OK**.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)klass tillhandahåller en metod som heter addShape, som kan användas för att lägga till en kombinationsrutakontroll till kalkylbladet. Metoden kan returnera ComboBox-objekt. Klassen ComboBox representerar en kombinationsruta. Den har några viktiga medlemmar:

- Metoden setLinkedCell specificerar en cell som är länkad till kombinationsrutan.
- Metoden setInputRange anger kalkylbladsintervallet för celler som används för att fylla kombinationsrutan.
- Metoden setDropDownLines anger antalet listrader som visas i den nedrullningsbara delen av en kombinationsruta.
- Metoden setShadow anger om kombinationsrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en kombinationsruta i kalkylbladet. Följande utdata genereras när koden exekveras.

**En kombinationsruta läggs till i kalkylbladet** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Lägga till etikettkontroll till ett kalkylblad**

 Etiketter är ett sätt att ge användarna information om innehållet i ett kalkylblad. Aspose.Cells gör det möjligt att lägga till och manipulera etiketter i ett kalkylblad. De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)klass tillhandahåller en metod som heter addShape, som används för att lägga till en etikettkontroll till kalkylbladet. Metoden returnerar ett Label-objekt. Klassen Label representerar en etikett i kalkylbladet. Den har några viktiga medlemmar:

- Metoden setText anger en etiketts textsträng.
- Metoden setPlacement anger PlacementType, hur etiketten är fäst vid cellerna i kalkylbladet.

Följande exempel visar hur du lägger till en etikett i kalkylbladet. Följande utdata genereras när koden exekveras.

**En etikett läggs till i arbetsbladet**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Lägger till listboxkontroll till ett kalkylblad**

En listboxkontroll skapar en listkontroll som tillåter val av ett eller flera objekt.

### **Använder Microsoft Excel**

Så här placerar du en listboxkontroll i ett kalkylblad:

1.  Se till att**Blanketter** verktygsfältet visas.
1.  Klicka på**Listbox** verktyg.
1. Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla listrutan.
1.  När listrutan är placerad i kalkylbladet högerklickar du på kontrollen för att klicka**Formatkontroll** och ange ingångsintervallet.
1.  I den**Cell Länk**fältet, ange adressen till cellen som denna listbox ska länkas till och ange attributet urvalstyp (Single, Multi, Extend)
1.  Klick**OK**.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klass tillhandahåller en metod som heter addShape, som används för att lägga till en listboxkontroll till ett kalkylblad. Metoden returnerar ett ListBox-objekt. Klassen ListBox representerar en listbox. Den har några viktiga medlemmar:

- Metoden setLinkedCell specificerar en cell som är länkad till listrutan.
- Metoden setInputRange anger kalkylbladsintervallet för celler som används för att fylla listrutan.
- Metoden setSelectionType anger valläget för listrutan.
- Metoden setShadow anger om listrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en listruta i kalkylbladet. Följande utdata genereras när koden exekveras.

**En listruta läggs till i kalkylbladet** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Lägga till knappkontroll till ett arbetsblad**

Knappar är användbara för att utföra vissa åtgärder. Ibland är det användbart att tilldela ett VBA-makro till knappen eller tilldela en hyperlänk för att öppna en webbsida.

### **Använder Microsoft Excel**

Så här placerar du en knappkontroll i ditt kalkylblad:

1.  Se till att**Blanketter** verktygsfältet visas.
1.  Klicka på**Knapp** verktyg.
1. Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla knappen.
1.  När listrutan är placerad i kalkylbladet högerklickar du på kontrollen och väljer**Formatkontroll**, ange sedan ett VBA-makro och attribut relaterat typsnitt, justering, storlek, marginal etc.
1.  Klicka på**OK**.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klass tillhandahåller en metod som heter addShape, som används för att lägga till en knappkontroll till kalkylbladet. Metoden kan returnera ett Button-objekt. Klassknappen representerar en knapp. Den har några viktiga medlemmar:

- Metoden setText anger rubriken för knappen.
- Metoden setPlacement anger PlacementType, hur knappen är fäst vid cellerna i kalkylbladet.
- Metoden addHyperlink lägger till en hyperlänk för knappkontrollen. Genom att klicka på knappen navigeras till relaterad URL.

Följande exempel visar hur man lägger till en knapp i kalkylbladet. Följande utdata genereras när koden exekveras

**En knapp läggs till i arbetsbladet**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Lägga till linjekontroll till ett kalkylblad**

Aspose.Cells låter dig rita autoformer i dina kalkylblad. Du kan enkelt skapa en linje. Du får också formatera raden. Du kan till exempel ändra färgen på linjen, ange linjens vikt och stil för ditt behov.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**AutoShapes** , peka mot**Rader**, och välj den linjestil du vill ha.
1. Dra för att rita linjen.
1. Gör ett eller båda av följande:
 1. För att begränsa linjen att rita i 15 graders vinkel från dess startpunkt, håll ned SKIFT medan du drar.
 1. För att förlänga linjen i motsatta riktningar från den första slutpunkten, håll ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)klass tillhandahåller en metod som heter addShape, som används för att lägga till en linjeform till kalkylbladet. Metoden kan returnera ett LineShape-objekt. Klassen LineShape representerar en linje. Den har några viktiga medlemmar:

- Metoden setDashStyle anger formatet för en rad.
- Metoden setPlacement anger PlacementType, hur linjen är fäst vid cellerna i kalkylbladet.

Följande exempel visar hur man lägger till rader i kalkylbladet. Det skapar tre linjer med olika stilar. Följande utdata genereras efter exekvering av koden

**Några rader läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Lägga till en pilspets till en linje**

Aspose.Cells låter dig också rita pillinjer. Det är möjligt att lägga till en pilspets på en linje och att formatera linjen. Du kan till exempel ändra färgen på linjen eller ange linjens vikt och stil.

Följande exempel visar hur man lägger till en pilspets på en linje. Följande utdata genereras när koden exekveras.

**En rad med pilspets läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Lägga till rektangelkontroll till ett kalkylblad**

Aspose.Cells låter dig rita rektangelformer i dina kalkylblad. Du kan skapa en rektangel, fyrkant etc. Du får även formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Du kan till exempel ändra färgen på rektangeln, ställa in skuggfärgen, ange vikten och stilen på rektangeln för ditt behov.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**Rektangel**.
1. Dra för att rita rektangeln.
1. Gör ett eller båda av följande:
 1. För att begränsa rektangeln att rita en kvadrat från dess startpunkt, håll ned SKIFT medan du drar.
 1. För att rita en rektangel från en mittpunkt, håll ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klass tillhandahåller en metod som heter addShape, som används för att lägga till en rektangelform till ett kalkylblad. Metoden kan returnera ett RectangleShape-objekt. Klassen RectangleShape representerar en rektangel. Den har några viktiga medlemmar:

- Metoden setLineFormat anger linjeformatattributen för en rektangel.
- Metoden setPlacement anger PlacementType, hur rektangeln är fäst vid cellerna i kalkylbladet.
- Egenskapen FillFormat anger fyllningsformatstilar för en rektangel.

Följande exempel visar hur du lägger till en rektangel i kalkylbladet. Följande utdata genereras när koden exekveras.

**En rektangel läggs till i kalkylbladet** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Lägger till bågkontroll i arbetsbladet**

Aspose.Cells låter dig rita bågformer i dina kalkylblad. Du kan skapa enkla och fyllda bågar. Det är tillåtet att formatera kontrollens fyllningsfärg och kantlinjefärg. Du kan till exempel ange / ändra färgen på bågen, ställa in skuggningsfärgen, ange vikten och stilen på formen för ditt behov.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**Båge** i**AutoShapes**.
1. Dra för att rita bågen.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klass tillhandahåller en metod som heter addShape, som används för att lägga till en bågform till kalkylbladet. Metoden kan returnera ett ArcShape-objekt. Klassen ArcShape representerar en båge. Den har några viktiga medlemmar:

- Metoden setLineFormat anger linjeformatattributen för en bågform.
- Metoden setPlacement specificerar PlacementType, hur bågen är fäst vid cellerna i kalkylbladet.
- Egenskapen FillFormat anger formens fyllningsformatstilar.

Följande exempel visar hur du lägger till bågformer i kalkylbladet. Exemplet skapar två bågformer: en är fylld och den andra är enkel. Följande utdata genereras när koden exekveras

**Två bågformer läggs till i kalkylbladet** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Lägga till Oval Control till ett arbetsblad**

Aspose.Cells låter dig rita ovala former i kalkylblad. Skapa enkla och fyllda ovala former och formatera kontrollens fyllningsfärg och kantlinjefärg. Till exempel kan du ange / ändra färgen på ovalen, ställa in skuggningsfärgen, ange vikten och stilen på formen.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**Oval** .
1. Dra för att rita ovalen.
1. Gör ett eller båda av följande:
 1. För att begränsa ovalen att rita en cirkel från dess startpunkt, håll ner SKIFT medan du drar.
1. För att rita en oval från en mittpunkt, håll ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klass tillhandahåller en metod som heter addShape, som används för att lägga till en oval form till ett kalkylblad. Metoden kan returnera ett ovalt objekt. Klassen Oval representerar en oval form. Den har några viktiga medlemmar:

- Metoden setLineFormat anger linjeformatattributen för en oval form.
-  Metoden setPlacement specificerar**Placeringstyp** , hur ovalen är fäst vid cellerna i arbetsbladet.
- Egenskapen FillFormat anger formens fyllningsformatstilar.

Följande exempel visar hur du lägger till ovala former i kalkylbladet. Exemplet skapar två ovala former: den ena är fylld oval, den andra är en enkel cirkel. Följande utdata genereras när koden exekveras.

**Två ovala former läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Förhandsämnen**
- [Lägg till ActiveX-kontroller med Aspose.Cells](/cells/sv/java/add-activex-controls-using-aspose-cells/)
- [Ta bort ActiveX-kontrollen](/cells/sv/java/remove-activex-control/)
