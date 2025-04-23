---
title: Verwendung der GlobalizationSettings Klasse für benutzerdefinierte Teilergebnisbezeichnungen und andere Beschriftungen des Kuchendiagramms
type: docs
weight: 70
url: /de/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**

Die Aspose.Cells-APIs haben die [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)-Klasse freigegeben, um mit Szenarien umzugehen, in denen der Benutzer benutzerdefinierte Bezeichnungen für Teilergebnisse in einer Tabellenkalkulation verwenden möchte. Außerdem kann die [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)-Klasse auch verwendet werden, um die **Andere**-Bezeichnung für das Kuchendiagramm beim Rendern des Arbeitsblatts oder Diagramms zu ändern.

## **Einführung in die GlobalizationSettings-Klasse**

Die [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)-Klasse bietet derzeit die folgenden 3 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um gewünschte Bezeichnungen für die Teilergebnisse zu erhalten oder benutzerdefinierten Text für die **Andere**-Bezeichnung eines Kuchendiagramms zu rendern.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Gibt den Gesamtwertnamen der Funktion zurück.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Gibt den Gesamtergebnisnamen der Funktion zurück.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Ruft den Namen der "Andere"-Beschriftungen für Kreisdiagramme ab.

### **Benutzerdefinierte Beschriftungen für Zwischensummen**

Die Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) kann verwendet werden, um die Zwischensummenbeschriftungen anzupassen, indem die Methoden [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) wie weiter unten dargestellt überschrieben werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Um benutzerdefinierte Beschriftungen einzufügen, muss die Eigenschaft [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) einer Instanz der oben definierten **CustomSettings**-Klasse zugewiesen werden, bevor die Zwischensummen zum Arbeitsblatt hinzugefügt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

Die Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) funktioniert nur für das Hinzufügen neuer Zwischensummen. Wenn ein Tabellenblatt bereits Zwischensummen enthält, können ihre Beschriftungen nicht geändert werden.

{{% /alert %}}

### **Benutzerdefinierter Text für Andere Beschriftung im Kreisdiagramm**

Die Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) bietet eine Methode [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername), die nützlich ist, um der "Andere"-Beschriftung von Kreisdiagrammen einen benutzerdefinierten Wert zu geben. Der folgende Code definiert eine benutzerdefinierte Klasse und überschreibt die Methode [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername), um eine benutzerdefinierte Beschriftung basierend auf dem Kulturkennzeichen des Systems zu erhalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

Der folgende Code lädt ein vorhandenes Tabellenblatt, das ein Kreisdiagramm enthält, und rendert das Diagramm zu einem Bild unter Verwendung der zuvor erstellten **CustomSettings**-Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
