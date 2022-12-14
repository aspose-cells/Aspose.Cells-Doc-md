---
title: Verwenden der GlobalizationSettings-Klasse für benutzerdefinierte Zwischensummenbeschriftungen und andere Beschriftungen von Kreisdiagrammen
type: docs
weight: 70
url: /de/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells APIs haben die ausgesetzt[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse, um mit den Szenarien fertig zu werden, in denen der Benutzer benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle verwenden möchte. Außerdem die[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse kann auch verwendet werden, um die zu ändern**Sonstiges** Bezeichnung für das Kreisdiagramm beim Rendern des Arbeitsblatts oder Diagramms.

## **Einführung in die GlobalizationSettings-Klasse**

 Das[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) Die Klasse bietet derzeit die folgenden 3 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um gewünschte Beschriftungen für die Zwischensummen zu erhalten oder benutzerdefinierten Text für die zu rendern**Sonstiges** Beschriftung eines Tortendiagramms.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Ruft den Gesamtnamen der Funktion ab.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Ruft den Gesamtsummennamen der Funktion ab.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Ruft den Namen von „Anderen“ Beschriftungen für Kreisdiagramme ab.

### **Benutzerdefinierte Beschriftungen für Zwischensummen**

 Das[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) -Klasse kann zum Anpassen der Zwischensummenbeschriftungen verwendet werden, indem die Klasse überschrieben wird[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)Methoden wie oben gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Um benutzerdefinierte Labels einzufügen, ist es erforderlich, die zuzuweisen[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) Eigenschaft zu einer Instanz der**Benutzerdefinierte Einstellungen**oben definierte Klasse, bevor Sie die Zwischensummen zum Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 Das[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse funktioniert nur zum Hinzufügen neuer Zwischensummen. Wenn eine Tabelle bereits Zwischensummen enthält, können ihre Bezeichnungen nicht geändert werden.

{{% /alert %}}

### **Benutzerdefinierter Text für andere Beschriftungen des Kreisdiagramms**

 Das[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) Klasse Angebote[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)Methode, die nützlich ist, um der Bezeichnung "Andere" von Kreisdiagrammen einen benutzerdefinierten Wert zuzuweisen. Der folgende Codeausschnitt definiert eine benutzerdefinierte Klasse und überschreibt die[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)-Methode, um eine benutzerdefinierte Bezeichnung basierend auf dem Kulturbezeichner des Systems abzurufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 Das folgende Snippet lädt eine vorhandene Tabelle, die ein Kreisdiagramm enthält, und rendert das Diagramm in ein Bild, während es verwendet wird**Benutzerdefinierte Einstellungen**oben erstellte Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
