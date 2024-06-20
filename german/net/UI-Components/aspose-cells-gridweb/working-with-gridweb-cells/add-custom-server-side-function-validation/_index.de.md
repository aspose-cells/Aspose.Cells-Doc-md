---
title: Benutzerdefinierte serverseitige Funktionsvalidierung hinzufügen
type: docs
weight: 110
url: /de/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, serverseitige Validierung
description: Dieser Artikel zeigt, wie man mit der serverseitigen Validierung in GridWeb arbeitet.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie möglicherweise eine Datenvalidierung serverseitig implementieren. Aspose.Cells.GridWeb ermöglicht es Ihnen, benutzerdefinierte serverseitige Datenvalidierungen hinzuzufügen. Sie müssen den Zellenbereich oder Bereich angeben. Sie können auch clientseitige Validierungsfunktionen für Rückrufe mit benutzerdefinierter serverseitiger Validierung festlegen.
## **Benutzerdefinierte serverseitige Funktionsvalidierung hinzufügen**
Sie müssen die Servervalidierungsklasse festlegen, die das **GridCustomServerValidation**-Interface über das Attribut **GridValidation.ServerValidation** implementiert. Sie müssen auch die clientseitige Validierungsfunktion festlegen (sie sollte auf der Clientseite in JavaScript geschrieben sein), diese Funktion ist obligatorisch, um die Daten clientseitig bei einem Rückruf zu validieren. Sie können die Fehlermeldung als Zeichenfolge über die Eigenschaft **GridValidation.ErrorMessage** und den Titel über die Eigenschaft **GridValidation.ErrorTitle** für Ihre Bedürfnisse festlegen. Bitte sehen Sie sich eine Reihe von Screenshots an, die zeigen, wie es in einem bestimmten Szenario funktioniert (Schritt für Schritt) nach Ausführung des unten stehenden Beispielcodes. Im Beispiel können Sie keine Daten in den Zellen B2:C3 aktualisieren. Wenn Sie versuchen, diese Zellen im Blatt zu bearbeiten, erhalten Sie Fehlermeldungen und der vorherige Wert wird wiederhergestellt. Sie können das Konsolenfenster (in Ihrem Browser) öffnen, um Zellinformationen/Details für bestimmte Ereignisse anzuzeigen. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
