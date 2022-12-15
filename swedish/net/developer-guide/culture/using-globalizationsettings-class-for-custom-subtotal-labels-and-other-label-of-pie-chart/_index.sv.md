---
title: Använda klassen GlobalizationSettings för anpassade delsummaetiketter och andra cirkeletiketter
type: docs
weight: 70
url: /sv/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Möjliga användningsscenarier**

 Aspose.Cells API:er har avslöjat[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass för att hantera de scenarier där användaren vill använda anpassade etiketter för delsummor i ett kalkylblad. Dessutom[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass kan också användas för att ändra**Övrig** etikett för cirkeldiagrammet medan du renderar kalkylblad eller diagram.

## **Introduktion till GlobalizationSettings Class**

 De[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) class erbjuder för närvarande följande 3 metoder som kan åsidosättas i en anpassad klass för att få önskade etiketter för delsummorna eller för att återge anpassad text för**Övrig** etikett för ett cirkeldiagram.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Hämtar det totala namnet på funktionen.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Hämtar det totala namnet på funktionen.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Hämtar namnet på "Andra"-etiketter för cirkeldiagram.

### **Anpassade etiketter för delsummor**

 De[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klass kan användas för att anpassa etiketterna Delsumma genom att åsidosätta[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)metoder som visats framöver.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 För att injicera anpassade etiketter måste du tilldela[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) egendom till en instans av**Anpassade inställningar**klass definierad ovan innan delsummorna läggs till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 De[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass fungerar bara för att lägga till nya delsummor. Om ett kalkylblad redan innehåller delsummor kan deras etiketter inte ändras.

{{% /alert %}}

### **Anpassad text för annan etikett av cirkeldiagram**

 De[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klasserbjudanden[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)metod som är användbar för att ge etiketten "Övrigt" för cirkeldiagram ett anpassat värde. Följande kodavsnitt definierar en anpassad klass och åsidosätter[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)metod för att få en anpassad etikett baserad på systemets kulturidentifierare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 Följande utdrag laddar ett befintligt kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till en bild samtidigt som du använder**Anpassade inställningar**klass skapad ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
