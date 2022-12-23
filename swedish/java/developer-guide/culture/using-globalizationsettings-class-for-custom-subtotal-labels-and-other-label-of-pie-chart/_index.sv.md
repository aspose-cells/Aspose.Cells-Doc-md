---
title: Använda klassen GlobalizationSettings för anpassade delsummaetiketter och andra cirkeletiketter
type: docs
weight: 50
url: /sv/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Möjliga användningsscenarier**
 Aspose.Cells API:er har avslöjat[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) klass för att hantera de scenarier där användaren vill använda anpassade etiketter för delsummor i ett kalkylblad. Dessutom[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) klass kan också användas för att ändra**Övrig** etikett för cirkeldiagrammet medan du renderar kalkylblad eller diagram.
## **Introduktion till GlobalizationSettings Class**
 De[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class erbjuder för närvarande följande 3 metoder som kan åsidosättas i en anpassad klass för att få önskade etiketter för delsummorna eller för att återge anpassad text för**Övrig** etikett för ett cirkeldiagram.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Får det totala namnet på funktionen.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Får det totala namnet på funktionen.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Hämtar namnet på "Andra"-etiketter för cirkeldiagram.
### **Anpassade etiketter för delsummor**
 De[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)klass kan användas för att anpassa etiketterna Delsumma genom att åsidosätta[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) metoder som visats framöver.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 För att injicera anpassade etiketter måste du tilldela[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) egendom till en instans av*Anpassade inställningar*klass definierad ovan innan delsummorna läggs till i kalkylbladet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 De[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)klass fungerar bara för att lägga till nya delsummor. Om ett kalkylblad redan innehåller delsummor kan deras etiketter inte ändras.

{{% /alert %}} 
### **Anpassad text för annan etikett av cirkeldiagram**
 De[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) klass erbjuder[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) metod som är användbar för att ge etiketten "Övrigt" för cirkeldiagram ett anpassat värde. Följande kodavsnitt definierar en anpassad klass och åsidosätter[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) metod för att få en anpassad etikett baserad på standardspråk som är inställt för JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Följande utdrag laddar ett befintligt kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till en bild samtidigt som du använder*Anpassade inställningar*klass skapad ovan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Följande är den resulterande bilden när maskinens språk är inställt på Frankrike. Som du kan se att etiketten "Övrigt" har översatts till "Autre" enligt definitionen i*Anpassade inställningar*klass.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
