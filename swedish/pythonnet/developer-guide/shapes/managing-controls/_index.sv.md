---
title: Hantering av kontroller
type: docs
weight: 150
url: /sv/python-net/managing-controls/
---

## **Introduktion**

Utvecklare kan lägga till olika ritobjekt som textrutor, kryssrutor, radioknappar, listrutor, etiketter, knappar, linjer, rektanglar, bågar, ovaler, spinners, scrollbarer, grupprutor etc. Aspose.Cells för Python via .NET tillhandahåller namnutrymmet Aspose.Cells.Drawing som innehåller alla ritobjekt. Dock stöds några ritobjekt eller former ännu inte. Skapa dessa ritobjekt i ett designer-kalkblad med Microsoft Excel och importera sedan till Aspose.Cells. Aspose.Cells för Python via .NET låter dig ladda dessa ritobjekt från ett designer-kalkblad och skriva dem till en genererad fil.

## **Lägga till textruta-kontroll till ett arbetsblad**

Ett sätt att betona viktig information i en rapport är att använda en textruta. Till exempel, lägg till text för att framhäva företagsnamnet eller för att indikera den geografiska regionen med högst försäljning. Aspose.Cells för Python via .NET tillhandahåller klassen [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection), som används för att lägga till en ny textruta till samlingen. Det finns en annan klass, [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox), som representerar en textruta som används för att definiera alla typer av inställningar. Den har några viktiga medlemmar:

- [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) -egenskapen returnerar ett [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe)-objekt som används för att justera innehållet i textrutan.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) -egenskapen specificerar placeringstypen.
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) -egenskapen specificerar teckensnittattributen.
- Metoden [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) lägger till en hyperlänk för textrutan.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) -egenskapen returnerar ett [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat)-objekt som används för att ställa in fyllningsformatet för textrutan.
- Egenskapen [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) returnerar [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat)-objekt som vanligtvis används för stil och tjocklek på textrutans linje.
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) -egenskapen specificerar den inmatade texten för textrutan.

I det följande exemplet skapas två textrutor i den första arbetsbladet i arbetsboken. Den första textrutan är välordnad med olika formatinställningar. Den andra är enkel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Manipulera textrute-kontroller i designer- kalkylblad**

Aspose.Cells för Python via .NET låter dig även komma åt textrutor i designerarbetsblad och manipulera dem. Använd egenskapen [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) för att få textlorsamlingen i bladet.

Följande exempel använder Microsoft Excel-filen som vi skapade i det ovanstående exemplet. Det hämtar textsträngarna för de två textrutorna och ändrar texten i den andra textrutan för att spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Lägger till kontrollrutan för kryssruta i en arbetsbok**

Kryssrutor är praktiska om du vill ge användaren en möjlighet att välja mellan två alternativ, till exempel sant eller falskt; ja eller nej. Aspose.Cells för Python via .NET låter dig använda kryssrutor i arbetsblad. Till exempel kan du ha utvecklat ett kalkylblad för finansiella prognoser där du antingen kan ta hänsyn till ett specifikt förvärv eller inte. I detta fall kanske du vill placera en kryssruta högst upp i kalkbladet. Sedan kan du länka statusen för denna kryssruta till en annan cell, så att om kryssrutan är vald är cellens värde Sant; om den inte är vald är cellens värde Falskt.

### **Använda Microsoft Excel**

För att placera en kryssruta i ditt kalkylblad, följ dessa steg:

1. Se till att formulär verktygsfältet visas.
1. Klicka på verktyget **Kryssruta** på formulär verktygsfältet.
1. I ditt arbetsbladsområde klickar du och drar för att definiera rektangeln som kommer att hålla kryssrutan och etiketten bredvid kryssrutan.
1. När kryssrutan är placerad, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna kryssruta ska länkas till.
1. Klicka på **OK**.

### **Användning av Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET tillhandahåller klassen [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection), som används för att lägga till en ny kryssruta till samlingen. Det finns en annan klass, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), som representerar en kryssruta. Den har några viktiga medlemmar:

- Egenskapen [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är länkad till kryssrutan.
- Egenskapen [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specificerar den textsträng som är associerad med kryssrutan. Det är etiketten för kryssrutan.
- Egenskapen [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) specificerar om kryssrutan är markerad eller inte.

Följande exempel visar hur man lägger till en kryssruta i arbetsboken.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

## **Lägger till alternativknappsstyrning till arbetsboken**

En radioknapp eller en alternativknapp är en kontroll gjord av en rund ruta. Användaren fattar sitt beslut genom att välja den runda rutan. En radioknapp åtföljs vanligtvis, om inte alltid, av andra. Sådana radioknappar visas och beter sig som en grupp. Användaren bestämmer vilken knapp som är giltig genom att endast välja en av dem. När användaren klickar på en knapp fylls den i. När en knapp i gruppen är vald är knapparna i samma grupp tomma.

### **Använda Microsoft Excel**

Följ dessa steg för att placera en radioknappskontroll i ditt arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget **Alternativknapp**.
1. I arbetsbladet klickar du och drar för att definiera rektangeln som kommer att hålla alternativknappen och etiketten bredvid alternativknappen.
1. När radioknappen är placerad i arbetsbladet, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna radioknapp ska länkas till.
1. Klicka på **OK**.

### **Användning av Aspose.Cells för Python via .NET**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button), som används för att lägga till en alternativknappsstyrning till en arbetsbok. Metoden returnerar ett [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton)-objekt. Klassen [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) representerar en optionsknapp. Den har några viktiga medlemmar:

- Egenskapen [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är länkad till alternativknappen.
- Egenskapen [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specificerar den textsträng som är associerad med alternativknappen. Det är etiketten för alternativknappen.
- Egenskapen [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) specificerar om alternativknappen är markerad eller inte.
- Egenskapen [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specificerar fill formatet för alternativknappen.
- Egenskapen [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specificerar linjeformatet för optionsknappen.

Följande exempel visar hur man lägger till alternativknappar i en arbetsbok. Exemplet lägger till tre alternativknappar som representerar åldersgrupper.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box), vilket används för att lägga till en combo box-kontroll till ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox)-objekt. Klassen [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) representerar en combo box. Den har några viktiga medlemmar:

- Egenskapen [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är länkad till combo boxen.
- Egenskapen [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) specificerar arbetsbokens område av celler som används för att fylla combo boxen.
- Egenskapen [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) specificerar antalet listrader som visas i nedrullningsdelen av en combo box.
- Egenskapen [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) indikerar om combo boxen har 3D-skuggning.

Följande exempel visar hur man lägger till en combo box i arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Lägga till etikettkontroll i ett arbetsblad**

Etiketter är ett sätt att ge användare information om ett kalkylblads innehåll. Aspose.Cells för Python via .NET gör det möjligt att lägga till och hantera etiketter i ett kalkylblad. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label), som används för att lägga till en etikettkontroll till kalkylbladet. Metoden returnerar ett [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label)-objekt. Klassen [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) representerar en etikett i kalkylbladet. Den har några viktiga medlemmar:

- Metoden [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specificerar en etiketts bildtext.
- Metoden [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specificerar [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), det sätt som etiketten är fäst vid cellerna i arbetsbladet.

Följande exempel visar hur man lägger till en etikett i arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box), vilket används för att lägga till en list box-kontroll i ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox)-objekt. Klassen [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) representerar en listbox. Den har några viktiga medlemmar:

- Metoden [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är länkad till listboxen.
- Metoden [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) anger kalkylbladintervall av celler som används för att fylla listrutan.
- Metoden [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) anger urvalsläge för listrutan.
- Metoden [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) indikerar om listrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en listruta i kalkylbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Lägga till knappkontroll i ett kalkylblad**

Knappar är användbara för att utföra vissa åtgärder. Ibland är det användbart att tilldela en VBA-makro till knappen eller tilldela en hyperlänk för att öppna en webbsida.

### **Använda Microsoft Excel**

För att placera en knappkontroll i ditt kalkylblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på **Knapp**-verktyget.
1. I ditt kalkylbladsområde klicka och dra för att definiera rektangeln som kommer att innehålla knappen.
1. När listrutan väl är placerad i kalkylbladet, högerklicka på kontrollen och välj **Formatera kontroll**, ange sedan en VBA-makro och attributrelaterad font, justering, storlek, marginal etc.
1. Klicka på **OK**.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button), som används för att lägga till en knappkontroll i kalkylbladet. Metoden returnerar ett [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) objekt. Klassen [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) representerar en knapp. Den har några viktiga medlemmar:

- Egenskapen [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) anger knappens text.
- Egenskapen [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) anger teckensnittsattribut för etiketten på knappkontrollen.
- Egenskapen [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) anger [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), sättet knappen är kopplad till cellerna i kalkylbladet.
- Egenskapen [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) lägger till en hyperlänk för knappkontrollen. Genom att klicka på knappen navigeras till relaterad URL.

Följande exempel visar hur man lägger till en knapp i kalkylbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Lägga Till Linjekontroll i Kalkylbladet**

### **Använda Microsoft Excel**

1. På **Ritning** verktygsfältet, klicka på **Autoshapes**, peka på **Linjer** och välj linjestilen du vill ha.
1. Dra för att rita linjen.
1. Gör en eller båda av följande:
   1. För att begränsa linjen att rita vid 15-graders vinklar från dess startpunkt, håll ner SKIFT när du drar.
   1. För att förlänga linjen i motsatta riktningar från första ändpunkten, håll ner CTRL när du drar.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line), som används för att lägga till en linjeform till kalkylbladet. Metoden returnerar ett [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) objekt. Klassen [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) representerar en linje. Den har några viktiga medlemmar:

- Metoden [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) anger formatet för en linje.
- Metoden [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) anger [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), sättet linjen är kopplad till cellerna i kalkylbladet.

Följande exempel visar hur man lägger till linjer i kalkylbladet. Det skapar tre linjer med olika stilar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Lägga Till en Pilkontroll till en Linje**

Aspose.Cells för Python via .NET tillåter dig också att rita pilrader. Det är möjligt att lägga till ett pilhuvud till en linje och formatera linjen. Till exempel kan du ändra linjens färg, eller ange vikt och stil på linjen.

Det följande exemplet visar hur du lägger till en pilspets på en linje.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Lägga till rektangelkontroll i ett arbetsblad**

Aspose.Cells för Python via .NET låter dig rita rektangulära former i dina kalkylblad. Du kan skapa en rektangel, kvadrat etc. Du får också möjlighet att formatera fyllningsfärgen och kantlinjefärgen på kontrollen. Till exempel kan du ändra färgen på rektangeln, ställa in skuggfärgen, specificera vikt och stil på rektangeln efter behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Rektangel**.
1. Dra för att rita rektangeln.
1. Gör en eller båda av följande:
   1. För att begränsa rektangeln för att rita en kvadrat från dess startpunkt, håll ned SKIFT när du drar.
   1. För att rita en rektangel från en mittpunkt, håll ned CTRL när du drar.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle), som används för att lägga till en rektangelform på ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) objekt. Klassen [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) representerar en rektangel. Den har några viktiga medlemmar:

- Egenskapen [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) anger linjeformatattribut för en rektangel.
- Egenskapen [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) anger [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), sättet rektangeln är ansluten till cellerna i arbetsbladet.
- Egenskapen [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) anger fyllningsformatstilar för en rektangel.

Det följande exemplet visar hur du lägger till en rektangel i arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Lägga till bågekontroll till arbetsbladet**

Aspose.Cells för Python via .NET låter dig rita bågformer i dina kalkylblad. Du kan skapa enkla och fyllda bågar. Du kan också formatera fyllningsfärgen och kantlinjefärgen på kontrollen. Till exempel kan du specificera / ändra färgen på bågen, ställa in skuggfärgen och ange vikt och stil på formen efter behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Båge** i **AutoShapes**.
1. Dra för att rita bågen.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc), som används för att lägga till en bågform på ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) objekt. Klassen [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) representerar en båge. Den har några viktiga medlemmar:

- Egenskapen [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) anger linjeformatattribut för en bågform.
- Egenskapen [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) anger [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), sättet bågen är ansluten till cellerna i arbetsbladet.
- Egenskapen [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specificerar fyllnadformatstilar för formen.
- Egenskapen [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) specificerar den nedre högra hörnradsindex.
- Egenskapen [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) specificerar den nedre högra hörnkolumnindex.

Det följande exemplet visar hur du lägger till bågformer i arbetsbladet. Exemplet skapar två bågformer: en är fylld och den andra är enkel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Lägga till ovalkontroll i ett arbetsblad**

Aspose.Cells för Python via .NET låter dig rita ovalformer i kalkylblad. Skapa enkla och fyllda ovalformer och formatera fyllningsfärgen samt kantlinjefärgen på kontrollen. Till exempel kan du specificera / ändra färgen på ovalen, ställa in skuggfärgen och ange vikt och stil på formen.

### **Använda Microsoft Excel**

- På *Rita*-verktygsfältet klickar du på *Oval*.
- Dra för att rita ovalen.
- Gör en eller båda följande:
- För att begränsa ovalen och rita en cirkel från dess startpunkt, håll ned SKIFT när du drar.
- För att rita en oval från en mittpunkt, håll ner CTRL när du drar.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval), som används för att lägga till en oval form i en arbetsbok. Metoden returnerar ett [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) objekt. Klassen [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) representerar en oval form. Det har några viktiga medlemmar:

- Egenskapen [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specificerar linjeformatattributen för en oval form.
- Egenskapen [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specificerar [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), sättet som ovalen är kopplad till cellerna i arbetsboken.
- Egenskapen [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specificerar fyllnadformatstilar för formen.
- Egenskapen [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) specificerar den nedre högra hörnradsindex.
- Egenskapen [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) specificerar den nedre högra hörnkolumnindex.

Följande exempel visar hur man lägger till ovala former i arbetsboken. Exemplet skapar två ovala former: en är fylld oval, den andra är en enkel cirkel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Lägger till spinnerkontroll på arbetsboken**

En snurrbox är en textruta kopplad till en knapp (kallad snurrknapp) som består av en uppåtpil och en nedåtpil som du klickar på för att gradvis ändra värdet i textrutan. Genom att använda snurrboxar kan du se hur insignaländringar i din finansiella modell kommer att påverka modellens utdata. Du kan koppla en snurrknapp till en specifik inmatningscell. När du klickar på upp- eller nedpilen på snurrknappen ökar eller minskar det heltalsvärde som finns i den riktade inmatningscellen. *Aspose.Cells för Python via .NET* tillåter dig att skapa snurrare i dina kalkylblad.

### **Använda Microsoft Excel**

För att placera en snurrkontroll i ditt arbetsblad:

- Se till att *Formulär * verktygsfält visas.
- Klicka på *Snurr* verktyget.
- I ditt arbetsbladsområde klicka och dra för att definiera rektangeln som kommer att hålla snurraren.
- När snurraren är placerad i arbetsbladet, högerklicka på kontrollen och klicka på *Formatkontroll* och ange maximala, minimala och inkrementella värden.
- I fältet *Cellänk* ange adressen för cellen till vilken denna snurrfunktion ska länkas.
- Klicka på *OK*.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner), som används för att lägga till en snurrknapp till ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) objekt. Klassen [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) representerar en snurrknapp. Det har några viktiga medlemmar:

- Egenskapen [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är kopplad till snurrknappen.
- Egenskapen [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) specificerar det maximala värdet för snurrknappsområdet.
- Egenskapen [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) specificerar det minimala värdet för snurrknappsområdet.
- Egenskapen [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) specificerar värdet för vilket en snurrare ökar med en linjebläddring.
- Egenskapen [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) indikerar om snurrknappen har 3D-skuggning.
- Egenskapen [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) specificerar det aktuella värdet för snurrknappen.

Följande exempel visar hur man lägger till en snurrknapp till arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

## **Lägger till rullningsfältkontroll till ett arbetsblad**

En rullningsfältkontroll används för att hjälpa till att välja data på ett arbetsblad på ett liknande sätt som en snurrknappkontroll. Genom att lägga till kontrollen till ett arbetsblad och koppla den till en cell är det möjligt att returnera ett numeriskt värde för den aktuella positionen för kontrollen.

### **Använda Microsoft Excel**

- För att lägga till ett rullningsfält i Excel 2003 och i tidigare versioner, klicka på *Rullningsfält* knappen på *Formulär* verktygsfältet, och skapa sedan ett rullningsfält som täcker cellerna B2:B6 i höjd och är ungefär en fjärdedel av bredden av kolumnen.
- För att lägga till ett rullningsfält i Excel 2007, klicka på *Utvecklar* fliken, klicka på *Infoga*, och klicka sedan på *Rullningsfält* i avsnittet Formulärkontroller.
- Högerklicka på rullningsfältet och klicka sedan på *Formatkontroll*.
- Skriv följande information och klicka på *OK*:
  - I rutan för *Aktuellt värde*, skriv 1.
  - I rutan för *Minsta värde*, skriv 1. Detta värde begränsar överkanten av rullningslisten till det första objektet i listan.
  - I rutan för *Högsta värde*, skriv 20. Detta nummer anger det maximala antalet poster i listan.
  - I rutan för *Inkrementellt värde*, skriv 1. Detta värde styr hur många nummer rullningslisten ökar det aktuella värdet med.
  - I rutan för *Sidändring*, skriv 5. Detta styrs hur mycket det aktuella värdet kommer att öka om du klickar inne i rullningslisten på någon av sidorna av skrollådan.
  - För att placera ett nummervärde i cell G1 (beroende på vilket objekt som är valt i listan), skriv G1 i rutan för *Cellkoppling*.
- Klicka på vilken cell som helst så att rullningslisten inte är vald.

När du klickar på upp- eller nedkontrollen på rullningslisten, uppdateras cellen G1 till ett nummer som indikerar det aktuella värdet för rullningslisten plus eller minus det inkrementella värdet för rullningslisten.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar), som används för att lägga till en rullningslistkontroll i kalkylarket. Metoden returnerar en [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) objekt. Klassen [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) representerar en rullningslist. Den har några viktiga medlemmar:

- Egenskapen [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specificerar en cell som är kopplad till rullningslisten.
- Egenskapen [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) specificerar det maximala värdet för rullningslistintervallet.
- Egenskapen [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) specificerar det minsta värdet för rullningslistintervallet.
- Egenskapen [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) specificerar beloppet med vilket en rullningslist ökas en linjerullning.
- Egenskapen [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) indikerar om rullningslisten har 3D-skuggning.
- Egenskapen [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) specificerar det aktuella värdet för rullningslisten.
- Egenskapen [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) specificerar hur mycket det aktuella värdet kommer att öka om du klickar inne i rullningslisten på någon av sidorna av skrollådan.

Följande exempel visar hur du lägger till en rullningslist i kalkylarket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

## **Lägga till GroupBox-kontroll till gruppkontroller i ett kalkylblad**

Ibland måste du implementera alternativknappar eller andra kontroller som tillhör en viss grupp, du kan implementera genom att inkludera antingen en groupbox-kontroll eller en rektangelkontroll. Någon av dessa två objekt skulle fungera som avgränsare för gruppen. Efter att ha lagt till en av dessa former kan du sedan lägga till två eller fler alternativknappar eller andra gruppkontroller.

### **Använda Microsoft Excel**

För att placera en groupbox-kontroll i ditt kalkylblad och placera kontroller i den:

- För att starta en formulär, på huvudmenyn, klicka på *Visa*, följt av *Verktygsfält* och *Formulär*.
- På *Formulär* verktygsfält, klicka på *Group Box* och rita en rektangel på kalkylarket.
- Skriv en bildtext för rutan.
- På *Formulär* verktygsfält, klicka på *Alternativknapp* och klicka inne i *Group Box* strax under bildtexten.
- Från *Formulär* verktygsfältet igen, klicka på *Alternativknapp* och klicka inne i *Group Box* under den första alternativknappen.
- Ännu en gång på *Formulär* verktygsfält, klicka på *Alternativknapp* och klicka inne i *Group Box* under den föregående alternativknappen.

### **Användning av Aspose.Cells för Python via .NET**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box), som används för att lägga till en group box-kontroll i kalkylarket. Metoden returnerar en [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) objekt. Dessutom grupperar [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) metoden av klassen [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) formerna, den tar en [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) array som parameter och returnerar en [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape) objekt. Klassen [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) representerar en group box. Den har några viktiga medlemmar:

- Egenskapen [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specificerar en sträng för group box.
- Egenskapen [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) indikerar om group box har 3D-skuggning.

Följande exempel visar hur du ska lägga till en gruppbox och gruppera kontrollerna på arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Fortsatta ämnen**
- [Lägg till ActiveX-kontroller](/cells/sv/python-net/add-activex-controls-using-aspose-cells/)
- [Ta bort ActiveX-kontroll](/cells/sv/python-net/remove-activex-control/)
- [Uppdatera ActiveX ComboBox Control](/cells/sv/python-net/update-activex-combobox-control/)
{{< app/cells/assistant language="python-net" >}}
