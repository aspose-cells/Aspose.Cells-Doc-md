---
title: Hantera kontroller
type: docs
weight: 150
url: /sv/net/managing-controls/
---
## **Introduktion**

Utvecklare kan lägga till olika ritobjekt såsom textrutor, kryssrutor, radioknappar, kombinationsrutor, etiketter, knappar, linjer, rektanglar, bågar, ovaler, spinnare, rullningslister, grupprutor etc. Aspose.Cells tillhandahåller namnutrymmet Aspose.Cells.Drawing som innehåller alla ritobjekt. Det finns dock några ritobjekt eller former som inte stöds ännu. Skapa dessa ritobjekt i ett designerkalkylblad med Microsoft Excel och importera sedan designerkalkylarket till Aspose.Cells. Med Aspose.Cells kan du ladda dessa ritobjekt från ett designerkalkylblad och skriva dem till en genererad fil.

## **Lägga till textrutekontroll till ett kalkylblad**

 Ett sätt att betona viktig information i en rapport är att använda en textruta. Till exempel, lägg till text för att markera företagsnamnet eller för att ange den geografiska region med högst försäljning etc. Aspose.Cells ger[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) klass, används för att lägga till en ny textruta i samlingen. Det finns en annan klass,[**Textruta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), som representerar en textruta som används för att definiera alla typer av inställningar. Den har några viktiga medlemmar:

-  De[**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) egendom returnerar a[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) objekt som används för att justera innehållet i textrutan.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) egenskapen anger placeringstypen.
-  De[**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) egenskapen anger teckensnittsattributen.
-  De[**Lägg till hyperlänk**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) metod lägger till en hyperlänk för textrutan.
-  De[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) egendom returnerar en[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) objekt som används för att ställa in fyllningsformatet för textrutan.
-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) egendom returnerar[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) objekt som vanligtvis används för stil och vikt på textrutans rad.
-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) egenskapen anger inmatningstexten för textrutan.

Följande exempel skapar två textrutor i det första kalkylbladet i arbetsboken. Den första textrutan är välutrustad med olika formatinställningar. Den andra är enkel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipulera textrutekontroller i Designer-kalkylblad**

 Aspose.Cells låter dig också komma åt textrutor i designerkalkylbladen och manipulera dem. Använd[**Arbetsblad. Textrutor**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) egenskap för att få textboxsamlingen i arket.

Följande exempel använder Excel-filen Microsoft som vi skapade i exemplet ovan. Den hämtar textsträngarna för de två textrutorna och ändrar texten i den andra textrutan för att spara filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Lägga till kryssrutakontroll till ett kalkylblad**

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

 Aspose.Cells tillhandahåller[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) klass, som används för att lägga till en ny kryssruta i samlingen. Det finns en annan klass,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), som representerar en kryssruta. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) egenskapen anger en cell som är länkad till kryssrutan.
-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) egenskapen anger textsträngen som är kopplad till kryssrutan. Det är etiketten för kryssrutan.
-  De[**Värde**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) egenskapen anger om kryssrutan är markerad eller inte.

Följande exempel visar hur du lägger till en kryssruta i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Lägger till radioknappskontroll till arbetsbladet**

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

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , som används för att lägga till en alternativknappskontroll till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) objekt. Klassen[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) representerar en alternativknapp. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) egenskapen anger en cell som är länkad till alternativknappen.
-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)egenskapen anger textsträngen som är kopplad till alternativknappen. Det är radioknappens etikett.
-  De[**Är kontrollerad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) egenskapen anger om alternativknappen är markerad eller inte.
-  De[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) egenskapen anger fyllningsformatet för alternativknappen.
-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) egenskapen anger linjeformatstilarna för alternativknappen.

Följande exempel visar hur du lägger till alternativknappar i ett kalkylblad. Exemplet lägger till tre alternativknappar som representerar åldersgrupper.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

 De[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , som används för att lägga till en kombinationsrutakontroll till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) objekt. Klassen[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) representerar en kombinationsruta. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) egenskapen anger en cell som är länkad till kombinationsrutan.
-  De[**Input Range**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) egenskapen anger kalkylbladsintervallet av celler som används för att fylla kombinationsrutan.
-  De[**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) egenskapen anger antalet listrader som visas i rullgardinsmenyn i en kombinationsruta.
-  De[**Skugga**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) egenskap anger om kombinationsrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en kombinationsruta i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Lägga till etikettkontroll till ett kalkylblad**

 Etiketter är ett sätt att ge användarna information om innehållet i ett kalkylblad. Aspose.Cells gör det möjligt att lägga till och manipulera etiketter i ett kalkylblad. De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , används för att lägga till en etikettkontroll till kalkylbladet. Metoden returnerar en[**Märka**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) objekt. Klassen[**Märka**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) representerar en etikett i kalkylbladet. Den har några viktiga medlemmar:

-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) metod anger en etiketts bildtextsträng.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) metoden specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), hur etiketten är fäst vid cellerna i kalkylbladet.

Följande exempel visar hur du lägger till en etikett i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , som används för att lägga till en listboxkontroll till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) objekt. Klassen[**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) representerar en listruta. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) metod anger en cell som är länkad till listrutan.
-  De[**Input Range**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) metod anger kalkylbladsintervallet av celler som används för att fylla listrutan.
-  De[**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)metod anger valläget för listrutan.
-  De[**Skugga**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) metod anger om listrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en listruta i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Lägga till knappkontroll till ett kalkylblad**

Knappar är användbara för att utföra vissa åtgärder. Ibland är det användbart att tilldela ett VBA-makro till knappen eller tilldela en hyperlänk för att öppna en webbsida.

### **Använder Microsoft Excel**

Så här placerar du en knappkontroll i ditt kalkylblad:

1.  Se till att**Blanketter** verktygsfältet visas.
1.  Klicka på**Knapp** verktyg.
1. Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla knappen.
1.  När listrutan är placerad i kalkylbladet högerklickar du på kontrollen och väljer**Formatkontroll**, ange sedan ett VBA-makro och attribut relaterat typsnitt, justering, storlek, marginal etc.
1.  Klicka på**OK**.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , används för att lägga till en knappkontroll till kalkylbladet. Metoden returnerar en[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) objekt. Klassen[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) representerar en knapp. Den har några viktiga medlemmar:

-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) egenskapen anger rubriken för knappen.
-  De[**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) egenskapen anger teckensnittsattributen för knappkontrollens etikett.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) egenskapen specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), hur knappen är fäst vid cellerna i kalkylbladet.
-  De[**Lägg till hyperlänk**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) egenskapen lägger till en hyperlänk för knappkontrollen. Genom att klicka på knappen navigeras till relaterad URL.

Följande exempel visar hur man lägger till en knapp i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Lägga till linjekontroll i arbetsbladet**

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**AutoShapes** , peka mot**Rader**och välj den linjestil du vill ha.
1. Dra för att rita linjen.
1. Gör ett eller båda av följande:
 1. För att begränsa linjen att rita i 15 graders vinkel från dess startpunkt, håll ned SKIFT medan du drar.
 1. För att förlänga linjen i motsatta riktningar från den första slutpunkten, håll ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , som används för att lägga till en linjeform till kalkylbladet. Metoden returnerar en[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objekt. Klassen[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) representerar en linje. Den har några viktiga medlemmar:

-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) metod anger formatet för en rad.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) metoden specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)hur linjen är fäst vid cellerna i kalkylbladet.

Följande exempel visar hur man lägger till rader i kalkylbladet. Det skapar tre linjer med olika stilar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Lägga till ett pilhuvud till en linje**

Aspose.Cells låter dig också rita pillinjer. Det är möjligt att lägga till en pilspets på en linje och att formatera linjen. Du kan till exempel ändra färgen på linjen eller ange linjens vikt och stil.

Följande exempel visar hur man lägger till en pilspets på en linje.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Lägga till rektangelkontroll till ett kalkylblad**

Aspose.Cells låter dig rita rektangelformer i dina kalkylblad. Du kan skapa en rektangel, fyrkant etc. Du får även formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Du kan till exempel ändra färgen på rektangeln, ställa in skuggfärgen, ange vikten och stilen på rektangeln för ditt behov.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**Rektangel**.
1. Dra för att rita rektangeln.
1. Gör ett eller båda av följande:
 1. För att begränsa rektangeln att rita en kvadrat från dess startpunkt, håll ned SKIFT medan du drar.
 1. För att rita en rektangel från en mittpunkt, håll ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**Lägg till rektangel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , som används för att lägga till en rektangelform till ett kalkylblad. Metoden återkommer[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objekt. Klassen[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) representerar en rektangel. Den har några viktiga medlemmar:

-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) egenskapen anger linjeformatattributen för en rektangel.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) egenskapen specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), hur rektangeln är fäst vid cellerna i kalkylbladet.
-  De[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) egenskapen anger fyllningsformatsstilarna för en rektangel.

Följande exempel visar hur du lägger till en rektangel i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Lägger till bågkontroll i arbetsbladet**

Aspose.Cells låter dig rita bågformer i dina kalkylblad. Du kan skapa enkla och fyllda bågar. Det är tillåtet att formatera kontrollens fyllningsfärg och kantlinjefärg. Du kan till exempel ange / ändra färgen på bågen, ställa in skuggningsfärgen, ange vikten och stilen på formen för ditt behov.

### **Använder Microsoft Excel**

1.  På**Teckning** verktygsfältet, klicka**Båge** i**AutoShapes**.
1. Dra för att rita bågen.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , som används för att lägga till en bågform till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) objekt. Klassen[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) representerar en båge. Den har några viktiga medlemmar:

-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) egenskapen anger linjeformatattributen för en bågform.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) egenskapen specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), hur bågen är fäst vid cellerna i arbetsbladet.
-  De[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)egenskapen anger formens fyllningsformatstilar.
-  De[**Nedre högerrad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) egenskapen anger radindexet i det nedre högra hörnet.
-  De[**Nedre högerkolumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) egenskapen anger kolumnindex i det nedre högra hörnet.

Följande exempel visar hur du lägger till bågformer i kalkylbladet. Exemplet skapar två bågformer: en är fylld och den andra är enkel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Lägga till Oval Control till ett arbetsblad**

Aspose.Cells låter dig rita ovala former i kalkylblad. Skapa enkla och fyllda ovala former och formatera kontrollens fyllningsfärg och kantlinjefärg. Till exempel kan du ange / ändra färgen på ovalen, ställa in skuggningsfärgen, ange vikten och stilen på formen.

### **Använder Microsoft Excel**

-  På*Teckning* verktygsfältet, klicka*Oval*.
- Dra för att rita ovalen.
- Gör ett eller båda av följande:
- Om du vill begränsa ovalen att rita en cirkel från dess startpunkt håller du ned SKIFT medan du drar.
- Om du vill rita en oval från en mittpunkt håller du ned CTRL medan du drar.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**Lägg till Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , som används för att lägga till en oval form till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) objekt. Klassen[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) representerar en oval form. Den har några viktiga medlemmar:

-  De[**Linjeformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) egenskapen anger linjeformatattributen för en oval form.
-  De[**Placering**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) egenskapen specificerar[**Placeringstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), hur ovalen är fäst vid cellerna i arbetsbladet.
-  De[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)egenskapen anger formens fyllningsformatstilar.
-  De[**Nedre högerrad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) egenskapen anger radindexet i det nedre högra hörnet.
-  De[**Nedre högerkolumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) egenskapen anger kolumnindex i det nedre högra hörnet.

Följande exempel visar hur du lägger till ovala former i kalkylbladet. Exemplet skapar två ovala former: den ena är fylld oval, den andra är en enkel cirkel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Lägga till Spinner Control till arbetsbladet**

 En snurrruta är en textruta kopplad till en knapp (kallad snurrknapp) som består av en upp- och nedpil som du klickar på för att stegvis ändra värdet i textrutan. Genom att använda snurrrutor kan du se hur indataändringar i din ekonomiska modell kommer att förändra modellens utdata. Du kan koppla en snurrknapp till en specifik inmatningscell. Medan du klickar på upp- eller nedåtpilen på snurrknappen, ökar eller minskar heltalsvärdet i den riktade inmatningscellen.*Aspose.Cells* låter dig skapa spinnare i dina kalkylblad.

### **Använder Microsoft Excel**

Så här placerar du en spin box-kontroll i ditt kalkylblad:

-  Se till att*Blanketter* verktygsfältet visas.
-  Klicka på*Spinnare* verktyg.
- Klicka och dra i ditt kalkylbladsområde för att definiera rektangeln som ska hålla spinnern.
-  När spinnern är placerad i kalkylbladet högerklickar du på kontrollen och klickar*Formatkontroll* och ange maximi-, lägsta- och inkrementella värden.
-  I den*Cell Länk* fältet, ange adressen till cellen som denna spin-box ska länkas till.
-  Klicka på*OK*.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) som används för att lägga till en spin box-kontroll till ett kalkylblad. Metoden returnerar en[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) objekt. Klassen[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) representerar en spin box. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) egenskapen anger en cell som är länkad till spin-rutan.
-  De[**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) egenskapen anger det maximala värdet för spin box-intervallet.
-  De[**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) egenskapen anger det lägsta värdet för spin box-intervallet.
-  De[**Inkrementell förändring**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) egenskapen anger värdebeloppet för vilket en spinner ökas en radrullning.
-  De[**Skugga**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) egenskapen indikerar om spin-boxen har 3D-skuggning.
-  De[**Nuvarande värde**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) egenskapen anger det aktuella värdet på spin-boxen.

Följande exempel visar hur man lägger till en snurrruta i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Lägga till rullningslistkontroll till ett kalkylblad**

En rullningslistskontroll används för att hjälpa till att välja data på ett kalkylblad på ett liknande sätt som en spin box-kontroll. Genom att lägga till kontrollen i ett kalkylblad och länka den till en cell är det möjligt att returnera ett numeriskt värde för kontrollens aktuella position.

### **Använder Microsoft Excel**

- För att lägga till en rullningslist i Excel 2003 och i tidigare versioner, klicka på*Rullningslist* knappen på*Blanketter* verktygsfältet och skapa sedan en rullningslist som täcker cellerna B2:B6 på höjden och är ungefär en fjärdedel av spaltens bredd.
-  För att lägga till en rullningslist i Excel 2007, klicka på*Utvecklaren* fliken, klicka*Föra in* , och klicka sedan*Rullningslist* i avsnittet Formulärkontroller.
-  Högerklicka på rullningslisten och klicka sedan*Formatkontroll*.
-  Skriv in följande information och klicka*OK*:
 - I*Nuvarande värde* box, typ 1.
 - I*Minsta värde* rutan, skriv 1. Detta värde begränsar toppen av rullningslisten till det första objektet i listan.
 - I*Maximalt värde* rutan, skriv 20. Detta nummer anger det maximala antalet poster i listan.
 - I*Inkrementell förändring* ruta, skriv 1. Detta värde styr hur många siffror rullningslistens kontroll ökar det aktuella värdet.
 - I*Sidbyte* rutan, skriv 5. Den här posten styr hur mycket det aktuella värdet kommer att ökas om du klickar inuti rullningslisten på vardera sidan av rullningsrutan.
 För att sätta ett talvärde i cell G1 (beroende på vilket objekt som är markerat i listan), skriv G1 i*Cell länk* låda.
- Klicka på valfri cell så att rullningslisten inte är markerad.

När du klickar på upp- eller nedkontrollen på rullningslisten uppdateras cell G1 till ett nummer som anger det aktuella värdet på rullningslisten plus eller minus den inkrementella förändringen av rullningslisten.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , som används för att lägga till en rullningslist i kalkylbladet. Metoden returnerar en[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) objekt. Klassen[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) representerar en rullningslist. Den har några viktiga medlemmar:

-  De[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) egenskapen anger en cell som är länkad till rullningslisten.
-  De[**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) egenskapen anger det maximala värdet för rullningslistens intervall.
-  De[**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) egenskapen anger det lägsta värdet för rullningslistens intervall.
-  De[**Inkrementell förändring**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) egenskapen anger värdebeloppet för vilket en rullningslist inkrementeras en radrullning.
-  De[**Skugga**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) egenskapen indikerar om rullningslisten har 3D-skuggning.
-  De[**Nuvarande värde**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) egenskapen anger det aktuella värdet på rullningslisten.
-  De[**Page Change**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)egenskapen anger hur mycket det aktuella värdet kommer att ökas om du klickar inuti rullningslisten på vardera sidan av rullningsrutan.

Följande exempel visar hur man lägger till en rullningslist i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Lägga till GroupBox Control till Group Controls i ett kalkylblad**

Ibland behöver du implementera radioknappar eller andra kontroller som tillhör en viss grupp, du kan implementera genom att inkludera antingen en gruppruta eller rektangelkontroll. Vilket som helst av dessa två objekt skulle fungera som avgränsare för gruppen. Efter att ha lagt till en av dessa former kan du sedan lägga till två eller flera alternativknappar eller andra gruppobjekt.

### **Använder Microsoft Excel**

Så här placerar du en grupprutakontroll i ditt kalkylblad och placerar kontroller i den:

-  För att starta ett formulär, klicka på huvudmenyn*Se* , följd av*Verktygsfält* och*Blanketter*.
-  På*Blanketter* verktygsfältet, klicka på*Grupplåda* och rita en rektangel på arbetsbladet.
- Skriv en bildtextsträng för rutan.
-  På*Blanketter* verktygsfältet, klicka*Alternativknapp* och klicka inuti*Grupplåda* precis under bildtextsträngen.
-  Från*Blanketter* verktygsfältet igen, klicka*Alternativknapp* och klicka inuti*Grupplåda*under den första alternativknappen.
-  Än en gång på*Blanketter* verktygsfältet, klicka*Alternativknapp* och klicka inuti*Grupplåda* under föregående alternativknapp.

### **Använder Aspose.Cells**

 De[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , som används för att lägga till en grupprutakontroll till kalkylbladet. Metoden returnerar en[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) objekt. Dessutom[**Grupp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) metod för[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass grupperar formerna, det tar en[**Form**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) array som parameter och returnerar en[**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) objekt. Klassen[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) representerar en gruppruta. Den har några viktiga medlemmar:

-  De[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) egenskapen anger grupprutans bildtextsträng.
-  De[**Skugga**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) egenskap anger om grupprutan har 3D-skuggning.

Följande exempel visar hur man lägger till en gruppruta och grupperar kontrollerna i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Förhandsämnen**
- [Lägg till ActiveX-kontroller med Aspose.Cells](/cells/sv/net/add-activex-controls-using-aspose-cells/)
- [Ta bort ActiveX-kontrollen](/cells/sv/net/remove-activex-control/)
- [Uppdatera ActiveX ComboBox Control](/cells/sv/net/update-activex-combobox-control/)
