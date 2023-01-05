---
title: Fügen Sie eine benutzerdefinierte serverseitige Funktionsvalidierung hinzu
type: docs
weight: 110
url: /de/net/add-custom-server-side-function-validation/
---
## **Mögliche Nutzungsszenarien**
Manchmal müssen Sie möglicherweise eine Datenvalidierung serverseitig implementieren. Aspose.Cells.GridWeb ermöglicht es Ihnen, eine benutzerdefinierte serverseitige Datenvalidierung hinzuzufügen. Sie müssen den Zellbereich oder Bereich angeben. Sie können auch clientseitige Validierungsfunktionen für Rückrufe mit benutzerdefinierter serverseitiger Validierung festlegen.
## **Fügen Sie eine benutzerdefinierte serverseitige Funktionsvalidierung hinzu**
 Sie müssen die Servervalidierungsklasse festlegen, die die implementiert**GridCustomServerValidation** Schnittstelle über**GridValidation.ServerValidation** Attribut. Sie müssen auch die clientseitige Validierungsfunktion festlegen (sie sollte auf der Clientseite in JavaScript geschrieben sein), diese Funktion ist obligatorisch, um die Daten auf der Clientseite beim Rückruf zu validieren. Sie können die Zeichenfolge der Fehlermeldung über festlegen**GridValidation.ErrorMessage** und Titel über**GridValidation.ErrorTitle**Eigenschaften für Ihre Bedürfnisse. Bitte sehen Sie sich eine Reihe von Screenshots an, die zeigen, wie es (Schritt für Schritt) in einem bestimmten Szenario funktioniert, nachdem Sie den Beispielcode unten ausgeführt haben. Im Beispiel können Sie Daten in B2:C3-Zellen nicht aktualisieren. Wenn Sie versuchen, diese Zellen im Blatt zu bearbeiten, erhalten Sie einige Fehlermeldungen und der vorherige Wert wird wiederhergestellt. Sie können das Konsolenfenster (in Ihrem Browser) öffnen, um die Informationen/Details der Zelle für bestimmte Ereignisse auszudrucken.

![todo: Bild_alt_Text](add-custom-server-side-function-validation_1.png)

![todo: Bild_alt_Text](add-custom-server-side-function-validation_2.png)

![todo: Bild_alt_Text](add-custom-server-side-function-validation_3.png)

![todo: Bild_alt_Text](add-custom-server-side-function-validation_4.png)

![todo: Bild_alt_Text](add-custom-server-side-function-validation_5.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
