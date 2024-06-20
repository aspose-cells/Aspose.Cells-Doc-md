---
title: FAQ
type: docs
weight: 400
url: /de/net/grid-faq/
---

## **Gibt es Einschränkungen in der Evaluierungsversion der Aspose.Cells Grid Controls?**
Nein, es gibt keine Einschränkungen der Funktionen in der Evaluierungsversion dieser Controls.

Die Evaluierungsversion bietet alle Funktionen der lizenzierten Version, außer dass sie eine zusätzliche Arbeitsmappe (mit dem **Evaluierungshinweis zum Urheberrecht**) zu den Ausgabedateien hinzufügt.


## **Es gibt so viele Grid-Controls auf dem Markt. Warum sollte ich die Aspose.Cells Grid Controls kaufen?**
Nun, die Aspose.Cells Grid Controls sind sehr preisgünstig und für alle Arten von Benutzern erschwinglich. Zu einem sehr vernünftigen Preis bietet sie Ihnen einen Satz von zwei Controls, um an Windows- und Webanwendungen zu arbeiten.

Außerdem ist es nicht nur ein einfaches Grid, es ist gleichzeitig Ihr **Tabellenblatt-Anzeiger, -Editor & -Ersteller**. 

Sie können es nicht nur mit jeder Art von Datenquelle verknüpfen (wie normale Grid-Controls), sondern auch Excel-Dateien erstellen und verwalten. Zudem bietet es eine starke und umfangreiche **Formelberechnungsmaschine** zum Berechnen nicht nur der integrierten Funktionen (unterstützt von den Aspose.Cells Grid Controls), sondern auch benutzerdefinierter Formeln, die Sie definieren. Es gibt noch viele weitere Funktionen des Aspose.Cells Grid-Suites, die hier nicht abgedeckt werden können. Bitte beachten Sie die Seite mit den Editionstypen für eine ausführlichere Funktionsliste. 

Sie können es nicht nur mit jeder Art von Datenquelle verbinden (wie normale Rastersteuerelemente), sondern auch Excel-Dateien erstellen und verwalten. Es bietet außerdem einen starken und umfangreichen **Formel-Berechnungsmotor**, um nicht nur eingebaute Funktionen (unterstützt von Aspose.Cells-Rastersteuerelementen), sondern auch benutzerdefinierte Formeln, die von Ihnen definiert wurden, zu berechnen. Es gibt noch viel mehr Funktionen des Aspose.Cells Grid-Suites, die hier nicht behandelt werden können. Bitte beachten Sie die Seite Über die Editionstypen für eine detailliertere Liste der Funktionen.

## **Ich habe kürzlich meine Lizenz für Aspose.Cells Grid Controls erworben. Wie kann ich diese Lizenz in meiner Anwendung mit Aspose.Cells Grid Control verwenden?**
Bitte beachten Sie die [Lizenzierung](/cells/de/net/licensing/) Seite der Aspose.Cells Grid Controls. 

Sie enthält ausführliche Informationen dazu, wie Sie die Lizenz in Ihren Anwendungen mit den Aspose.Cells Grid Controls verwenden können.



## **Wie kann ich mein auf Aspose.Cells.GridWeb basierendes Webprojekt/-lösung auf dem Server bereitstellen?**
Wenn Sie die Webanwendung mit dem GridWeb-Control bereitstellen müssen, kopieren Sie das "acw_client"-Verzeichnis in Ihren Projektordner, da Ihre Webanwendung (die auf dem Server bereitgestellt wird) es sonst nicht finden kann.

Sie können immer den Skriptpfad angeben, indem Sie die folgenden Codezeilen in den Konfigurationsabschnitt hinzufügen (z.B. in die web.config-Datei in Ihrem VS.NET-Projekt). Das "acw_client" ist ein Ordner, der Dateien enthält, und Aspose.Cells.GridWeb verwendet diesen Ordner zur Verwaltung seiner internen Konfiguration. In ihm befinden sich Skriptdateien, Bilddateien und andere Dateien, um das Verhalten von GridWeb zu definieren und andere Operationen einzurichten. Die Konfigurationsdatei wird verwendet, um zu verhindern, dass das Control auf die eingebetteten Clientressourcen (Bilder, Skripte, etc.) zugreift, was in einigen Fällen/Szenarien nützlich ist.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Der Pfad bezieht sich immer auf das Projektverzeichnis. Sie sollten kein Verzeichnis verwenden, das außerhalb des Projektverzeichnisses liegt. Es ist also notwendig, das "acw_client"-Verzeichnis (@ Ihrem GridWeb-Installationsverzeichnis) in das Projektverzeichnis zu kopieren.

{{% /alert %}} 
## **Ausführen von Aspose.Cell.GridWeb in Internet Explorer**
Derzeit unterstützt Aspose.Cells.GridWeb Internet Explorer nicht mehr, da es ein zu veralteter Browser ist. 
Wir unterstützen Chrome, Edge, Firefox, Safari, Opera



