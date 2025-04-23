---
title: Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram
type: docs
weight: 50
url: /sv/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Möjliga användningsscenario**
Aspose.Cells API:er har exponerat klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) för att hantera scenarier där användaren vill använda anpassade etiketter för subtotaler i ett kalkylblad. Dessutom kan klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) också användas för att modifiera **Other**-etiketten för cirkeldiagrammet vid rendering av kalkylbladet eller diagrammet.
## **Introduktion till klassen GlobalizationSettings**
Klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) erbjuder för närvarande följande 3 metoder som kan åsidosättas i en anpassad klass för att få önskade etiketter för subtotaler eller för att rendera anpassad text för **Other**-etiketten för ett cirkeldiagram.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Hämtar det totala namnet för funktionen.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Hämtar det sammanlagda namnet för funktionen.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Hämtar namnet på "Other"-etiketter för tårtdiagram.
### **Anpassade etiketter för subtotaler**
Klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) kan användas för att anpassa delbelappen genom att åsidosätta metoderna [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) och [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) som demonstreras nedan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


För att injicera anpassade etiketter är det nödvändigt att tilldela egenskapen [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) till en instans av klassen för *Anpassade inställningar* som definieras ovan innan du lägger till subtotaler i kalkylarket.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

Klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) fungerar endast för att lägga till nya subtotaler. Om ett kalkylblad redan innehåller subtotaler kan deras etiketter inte ändras.

{{% /alert %}} 
### **Anpassad text för annan etikett för cirkeldiagram**
Klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) erbjuder metoden [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) vilket är användbart för att ge "Other"-etiketten för tårtdiagram ett anpassat värde. Följande kod definierar en anpassad klass och åsidosätter metoden [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) för att få en anpassad etikett baserad på det standard språk som är inställt för JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Följande kodstycke laddar ett befintligt kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till en bild med hjälp av klassen *Anpassade inställningar* som skapats ovan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Följande är den resulterande bilden när landets lokalisering är inställd på Frankrike. Som du kan se har etiketten "Other" översatts till "Autre" enligt definitionen i *Anpassade inställningar* klassen.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
