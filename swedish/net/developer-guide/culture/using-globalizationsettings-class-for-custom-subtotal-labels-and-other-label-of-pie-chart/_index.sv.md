---
title: Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram
type: docs
weight: 70
url: /sv/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Möjliga användningsscenario**

Aspose.Cells API:er har exponerat [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klassen för att hantera scenarier där användaren vill använda anpassade etiketter för subtotals i en kalkylblad. Dessutom kan [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klassen också användas för att modifiera **Oavslutad**-etiketten för Pie-diagrammet medan kalkylbladet eller diagrammet renderas.

## **Introduktion till klassen GlobalizationSettings**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klassen erbjuder för närvarande följande 3 metoder som kan åsidosättas i en anpassad klass för att få önskade etiketter för subtotaler eller för att rendera anpassad text för **Oavslutad**-etiketten på ett Pie-diagram.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Hämtar det totala namnet på funktionen.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Hämtar det totala namnet på den totala funktionen.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Hämtar namnet på "Övrigt"-etiketter för Pie-diagram.

### **Anpassade etiketter för subtotaler**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klassen kan användas för att anpassa subtotal-etiketterna genom att åsidosätta [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) metoderna som visas framåt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

För att infogna anpassade etiketter krävs det att [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) egenskapen tilldelas en instans av **CustomSettings** klassen som definieras ovan innan subtotalerna läggs till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

Klassen [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) fungerar endast för att lägga till nya delsummeringar. Om ett kalkylblad redan innehåller delsummeringar kan deras etiketter inte ändras.

{{% /alert %}}

### **Anpassad text för annan etikett för cirkeldiagram**

Klassen [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) erbjuder [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) metod som är användbar för att ge Pie-diagram en anpassad värde för etiketten "Övrigt". Följande avsnitt definierar en anpassad klass och åsidosätter metoden [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) för att få en anpassad etikett baserad på systemets kulturtillhörighet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

Följande avsnutt laddar ett befintligt kalkylblad som innehåller ett Pie-diagram och renderar diagrammet till en bild med hjälp av **CustomSettings**-klassen skapad ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
