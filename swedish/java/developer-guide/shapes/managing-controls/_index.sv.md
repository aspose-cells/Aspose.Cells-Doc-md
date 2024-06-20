---
title: Hantering av kontroller
type: docs
weight: 120
url: /sv/java/managing-controls/
---

## **Introduktion**

Utvecklare kan lägga till olika ritobjekt som textrutor, kryssrutor, radioknappar, kombinationsrutor, etiketter, knappar, linjer, rektanglar, bågar, ovaler, spinnare, skjutreglage, grupprutor etc. Aspose.Cells tillhandahåller Aspose.Cells.Drawing-namnrymden som innehåller alla ritobjekt. Det finns emellertid några ritobjekt eller former som ännu inte stöds. Skapa dessa ritobjekt i en designkalkylblad med hjälp av Microsoft Excel och importera sedan designkalkylbladet till Aspose.Cells. Aspose.Cells låter dig ladda dessa ritobjekt från en designkalkylblad och skriva dem till en genererad fil.

## **Lägger till TextBox-kontroll i kalkylbladet**

Ett sätt att lyfta fram viktig information i en rapport är att använda en textruta. Till exempel, lägg till text för att markera företagsnamnet eller ange den geografiska regionen med högst försäljning etc. Aspose.Cells tillhandahåller TextBoxes-klassen, som används för att lägga till en ny textruta i samlingen. Det finns en annan klass, [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), som representerar en textruta som används för att definiera alla typer av inställningar. Den har några viktiga medlemmar:

- Metoden [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) returnerar en [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame)-objekt som används för att justera innehållet i textrutan.
- Metoden [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) anger placerings typen.
- Metoden [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) anger teckensnitts attributen.
- Metoden [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) lägger till en hyperlänk för textrutan.
- Egenskapen [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) returnerar [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat)-objekt som används för att ställa in fyllningsformatet för textrutan.
- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) returnerar [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)-objekt som vanligtvis används för stil och tjocklek på textrutans linje.
- Metoden [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) anger den inmatade texten för textrutan.

I det följande exemplet skapas två textrutor i den första arbetsbladet i arbetsboken. Den första textrutan är välordnad med olika formatinställningar. Den andra är enkel.

Följande utdata genereras genom att köra koden:

**Två textrutor skapas i kalkylbladet** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulering av TextBox-kontroller i designkalkylbladen**

Aspose.Cells låter dig också komma åt textrutor i designkalkylbladen och manipulera dem. Använd egenskapen [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) för att få textrutor samlingen i arket.

I det följande exemplet används Microsoft Excel-filen – tsttextboxes.xls – som vi skapade i det ovanstående exemplet. Den hämtar textsträngarna från de två textrutorna och ändrar texten i den andra textrutan för att spara filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Lägga till kryssrutekontroll på arbetsbladet.**

Kryssrutor är användbara om du vill ge användaren ett sätt att välja mellan två alternativ, som sant eller falskt; ja eller nej. Aspose.Cells låter dig använda kryssrutor i kalkylblad. Till exempel kan du ha utvecklat ett ekonomiskt prognoskalkylblad där du antingen kan räkna med förvärvet eller inte. I detta fall vill du placera en kryssruta längst upp på kalkylbladet. Du kan sedan koppla statusen för denna kryssruta till en annan cell, så att om kryssrutan är markerad är värdet i cellen Sant; om den inte är markerad är värdet i cellen Falskt.

### **Använda Microsoft Excel**

För att placera en kryssruta i ditt kalkylblad, följ dessa steg:

1. Se till att formulär verktygsfältet visas.
1. Klicka på verktyget **Kryssruta** på formulär verktygsfältet.
1. I ditt arbetsbladsområde klickar du och drar för att definiera rektangeln som kommer att hålla kryssrutan och etiketten bredvid kryssrutan.
1. När kryssrutan är placerad, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna kryssruta ska länkas till.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Aspose.Cells tillhandahåller klassen [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection), som används för att lägga till en ny kryssruta i samlingen. Det finns en annan klass, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), som representerar en kryssruta. Den har några viktiga medlemmar:

- Metoden [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) specificerar en cell som är länkad till kryssrutan.
- Metoden [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) specificerar den textsträng som är associerad med kryssrutan. Det är etiketten för kryssrutan.
- Metoden [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) specificerar om kryssrutan är markerad eller inte.

Följande exempel visar hur du lägger till en kryssruta i arbetsbladet. Utmatningen nedan genereras efter att koden har utförts.

** En kryssruta läggs till i arbetsbladet ** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Lägga till RadioButton-kontroll i arbetsbladet**

En radioknapp eller en alternativknapp är en kontroll gjord av en rund ruta. Användaren fattar sitt beslut genom att välja den runda rutan. En radioknapp åtföljs vanligtvis, om inte alltid, av andra. Sådana radioknappar visas och beter sig som en grupp. Användaren bestämmer vilken knapp som är giltig genom att endast välja en av dem. När användaren klickar på en knapp fylls den i. När en knapp i gruppen är vald är knapparna i samma grupp tomma.

### **Använda Microsoft Excel**

Följ dessa steg för att placera en radioknappskontroll i ditt arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget **Alternativknapp**.
1. I arbetsbladet klickar du och drar för att definiera rektangeln som kommer att hålla alternativknappen och etiketten bredvid alternativknappen.
1. När radioknappen är placerad i arbetsbladet, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna radioknapp ska länkas till.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape som kan användas för att lägga till en radioknappskontroll i ett arbetsblad. Metoden kan returnera ett RadioButton-objekt. Klassen RadioButton representerar en alternativknapp. Den har några viktiga medlemmar:

- Metoden setLinkedCell specificerar en cell som är länkad till radioknappen.
- Metoden setText specificerar den textsträng som är associerad med radioknappen. Det är etiketten för radioknappen.
- Egenskapen Checked specificerar om radioknappen är markerad eller inte.
- Metoden setFillFormat specificerar fyllningsformatet för radioknappen.
- Metoden setLineFormat specificerar linjeformatstilarna för alternativknappen.

Följande exempel visar hur du lägger till radioknappar i ett arbetsblad. Exemplet lägger till tre radioknappar som representerar åldersgrupper. Följande utmatning skulle genereras efter att koden har körts.

** Några radioknappar läggs till i arbetsbladet ** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Lägga till Combobox-kontroll i ett arbetsblad**

För att underlätta inmatning av data eller begränsa inmatningar till vissa objekt som du definierar kan du skapa en combobox eller en nedrullningslista med giltiga inmatningar som är samlade från celler någon annanstans på arbetsbladet. När du skapar en nedrullningslista för en cell visas en pil bredvid den cellen. För att ange information i den cellen klickar du på pilen och klickar sedan på den post som du vill ha.

### **Använda Microsoft Excel**

Följ dessa steg för att placera en combobox-kontroll i ditt arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget för **Kombinationsruta**.
1. I området för din arbetsblad, klicka och dra för att definiera rektangeln som kommer att hålla kombinationsrutan.
1. När kombinationsrutan är placerad i arbetsbladet, högerklicka på kontrollen för att klicka på **Formatkontroll** och ange inmatningsintervallet.
1. I fältet för **Cell Länk**, ange adressen för cellen till vilken denna kombinationsruta ska länkas.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape, som kan användas för att lägga till en kombinationsruta till arbetsbladet. Metoden kan returnera ComboBox-objekt. Klassen ComboBox representerar en kombinationsruta. Den har några viktiga medlemmar:

- Metoden setLinkedCell anger en cell som är kopplad till kombinationsrutan.
- Metoden setInputRange anger arbetsbladsintervallen av celler som används för att fylla kombinationsrutan.
- Metoden setDropDownLines anger antalet listrader som visas i nedfällningsdelen av en kombinationsruta.
 - Metoden setShadow indikerar om kombinationsrutan har 3D-skuggning.

Det följande exemplet visar hur man lägger till en kombinationsruta i arbetsbladet. Följande utdata genereras vid körning av koden.

**En kombinationsruta läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Lägga till etikettkontroll i ett arbetsblad**

Etiketter är ett sätt att ge användare information om innehållet i en kalkylblad. Aspose.Cells gör det möjligt att lägga till och hantera etiketter i ett arbetsblad. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape, använd för att lägga till en etikettkontroll till arbetsbladet. Metoden returnerar en etikettobjekt. Klassen Label representerar en etikett i arbetsbladet. Den har några viktiga medlemmar:

- Metoden setText anger en etiketts förklaringssträng.
- Metoden setPlacement specificerar PlacementType, det sätt som etiketten är kopplad till cellerna i arbetsbladet.

Det följande exemplet visar hur man lägger till en etikett i arbetsbladet. Följande utdata genereras vid körning av koden.

**En etikett läggs till i arbetsbladet**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Lägga till en listrutekontroll i ett arbetsblad**

En listrutekontroll skapar en listkontroll som tillåter enkel eller flervals. artikelval.

### **Använda Microsoft Excel**

För att placera en listrutekontroll i ett arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget för **Listrute**.
1. I ditt arbetsbladsområde, klicka och dra för att definiera rektangeln som kommer att hålla listrutan.
1. När listrutan är placerad i arbetsbladet, högerklicka på kontrollen för att klicka på **Formatkontroll** och ange inmatningsintervallet.
1. I fältet för **Cell Länk**, ange adressen för cellen till vilken denna listruta ska länkas och ange attributet för valtyp (Enkel, Multi, Utöka).
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape, som används för att lägga till en listrutekontroll till ett arbetsblad. Metoden returnerar ett ListBox-objekt. Klassen ListBox representerar en listruta. Den har några viktiga medlemmar:

- Metoden setLinkedCell anger en cell som är kopplad till listrutan.
- Metoden setInputRange anger arbetsbladsintervallen av celler som används för att fylla listrutan.
- Metoden setSelectionType specifierar urvalsmoden för listrutan.
- Metoden setShadow indikerar om listrutan har 3D-skuggning.

Exemplet nedan visar hur man lägger till en listruta i arket. Följande utdata genereras vid körning av koden.

**En listruta läggs till i arket** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Lägga till knappkontroll i ett kalkylblad**

Knappar är användbara för att utföra vissa åtgärder. Ibland är det användbart att tilldela en VBA-makro till knappen eller tilldela en hyperlänk för att öppna en webbsida.

### **Använda Microsoft Excel**

För att placera en knappkontroll i ditt kalkylblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på **Knapp**-verktyget.
1. I ditt kalkylbladsområde klicka och dra för att definiera rektangeln som kommer att innehålla knappen.
1. När listrutan väl är placerad i kalkylbladet, högerklicka på kontrollen och välj **Formatera kontroll**, ange sedan en VBA-makro och attributrelaterad font, justering, storlek, marginal etc.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape, används för att lägga till en knappkontroll i arket. Metoden kan returnera ett Button-objekt. Klassen Button representerar en knapp. Den har några viktiga medlemmar:

- Metoden setText specificerar knappens undertext.
- Metoden setPlacement specificerar PlacementType, sättet som knappen är bifogad till cellerna i arket.
- Metoden addHyperlink lägger till en hyperlänk för knappkontrollen. Genom att klicka på knappen navigerar man till relaterad URL.

Exemplet nedan visar hur man lägger till en knapp i arket. Följande utdata genereras vid körning av koden.

**En knapp läggs till i arket**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Lägga till linjekontroll i ett kalkylblad**

Aspose.Cells tillåter dig att rita autoshapes i dina kalkylblad. Du kan skapa en linje med lätthet. Du får även formatera linjen. Till exempel kan du ändra färgen på linjen, specificera vikten och stilen för linjen enligt ditt behov.

### **Använda Microsoft Excel**

1. På **Ritning** verktygsfältet, klicka på **Autoshapes**, peka på **Linjer** och välj linjestilen du vill ha.
1. Dra för att rita linjen.
1. Gör en eller båda av följande:
   1. För att begränsa linjen att rita vid 15-graders vinklar från dess startpunkt, håll ner SKIFT när du drar.
   1. För att förlänga linjen i motsatta riktningar från första ändpunkten, håll ner CTRL när du drar.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) tillhandahåller en metod som heter addShape, vilket används för att lägga till en linjeform i arket. Metoden kan returnera ett LineShape-objekt. Klassen LineShape representerar en linje. Den har några viktiga medlemmar:

- Metoden setDashStyle specificerar formatet på en linje.
- Metoden setPlacement specificerar PlacementType, sättet som linjen är bifogad till cellerna i arket.

Exemplet nedan visar hur man lägger till linjer i arket. Det skapar tre linjer med olika stilar. Följande utdata genereras efter att koden har körts.

**Några linjer läggs till i arket** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Lägga till en pilspets i en linje**

Aspose.Cells låter dig också rita pilrakningar. Det är möjligt att lägga till en pilspets på en linje och formatera linjen. Till exempel kan du ändra färgen på linjen eller ange linjens vikt och stil.

Följande exempel visar hur du lägger till en pilspets på en linje. Följande utdata genereras vid utförande av koden.

**En linje med pilspets läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Lägga till rektangelkontroll i ett arbetsblad**

Aspose.Cells låter dig rita rektangelformar i dina arbetsblad. Du kan skapa en rektangel, kvadrat etc. Du har också möjlighet att formatera fyllningsfärgen och kantlinjens färg för kontrollen. Till exempel kan du ändra färgen på rektangeln, ange skuggningsfärg, specificera vikten och stilen på rektangeln enligt ditt behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Rektangel**.
1. Dra för att rita rektangeln.
1. Gör en eller båda av följande:
   1. För att begränsa rektangeln för att rita en kvadrat från dess startpunkt, håll ned SKIFT när du drar.
   1. För att rita en rektangel från en mittpunkt, håll ned CTRL när du drar.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) har en metod som heter addShape, som används för att lägga till en rektangelform till ett arbetsblad. Metoden kan returnera ett RectangleShape-objekt. Klassen RectangleShape representerar en rektangel. Den har några viktiga medlemmar:

- Metoden setLineFormat specificerar linjeformatattributen för en rektangel.
- Metoden setPlacement specificerar PlacementType, sättet rektangeln är kopplad till cellerna i arbetsbladet.
- Egenskapen FillFormat specificerar fyllningsformatstilarna för en rektangel.

Följande exempel visar hur du lägger till en rektangel på arbetsbladet. Följande utdata genereras vid utförande av koden.

**En rektangel läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Lägga till bågekontroll till arbetsbladet**

Aspose.Cells låter dig rita bågformer i dina arbetsblad. Du kan skapa enkla och fyllda bågar. Du har möjlighet att formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Till exempel kan du specificera/ändra färgen på bågen, ange skuggningsfärg, specificera vikten och stilen på formen enligt ditt behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Båge** i **AutoShapes**.
1. Dra för att rita bågen.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) innehåller en metod som heter addShape, som används för att lägga till en bågform till arbetsbladet. Metoden kan returnera ett ArcShape-objekt. Klassen ArcShape representerar en båge. Den har några viktiga medlemmar:

- Metoden setLineFormat specificerar linjeformatattributen för en bågform.
- Metoden setPlacement specificerar PlacementType, sättet bågen är kopplad till cellerna i arbetsbladet.
- FillFormat egenskapen anger fyllningsformatstilarna för formen.

Följande exempel visar hur du lägger till bågformer på arbetsbladet. Exemplet skapar två bågformer: en är fylld och den andra är enkel. Följande utdata genereras vid utförande av koden.

**Två bågformer läggs till i arbetsbladet** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Lägga till ovalkontroll i ett arbetsblad**

Aspose.Cells låter dig rita ovala former i arbetsblad. Skapa enkla och fyllda ovala former och formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Till exempel kan du specificera/ändra färgen på ovalen, ange skuggningsfärg, specificera vikten och stilen på formen enligt ditt behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Oval**.
1. Dra för att rita ovalen.
1. Gör en eller båda av följande:
   1. För att begränsa ovalen och rita en cirkel från dess startpunkt, håll ner SKIFT när du drar.
   1. För att rita en oval från en mitt punkt, håll ner CTRL när du drar.

### **Använda Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) klassen tillhandahåller en metod som heter addShape, som används för att lägga till en oval form till en arbetsbok. Metoden kan returnera ett Oval objekt. Klassen Oval representerar en oval form. Den har några viktiga medlemmar:

- setLineFormat metoden anger linjeformatattribut för en oval form.
- setPlacement metoden anger Placeringstyp, på vilket sätt ovalen är fäst vid cellerna i arbetsboken.
- FillFormat egenskapen anger fyllningsformatstilarna för formen.

Följande exempel visar hur man lägger till ovala former i arbetsboken. Exemplet skapar två ovala former: en är fylld oval och den andra är en enkel cirkel. Följande utdata genereras vid utförande av koden.

**Två ovala former läggs till i arbetsboken** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Fortsatta ämnen**
- [Lägg till ActiveX-kontroller med hjälp av Aspose.Cells](/cells/sv/java/add-activex-controls-using-aspose-cells/)
- [Ta bort ActiveX-kontroll](/cells/sv/java/remove-activex-control/)
