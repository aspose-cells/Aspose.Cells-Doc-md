---
title: FAQ
type: docs
weight: 400
url: /de/net/grid-faq/
---
## **Gibt es Einschränkungen in der Evaluierungsversion von Aspose.Cells Grid Controls?**
 Nein, es gibt keine Funktionseinschränkung in der Evaluierungsversion von Aspose.Cells Grid Controls. Die Evaluierungsversion bietet alle Funktionen der lizenzierten Version, außer dass sie ein zusätzliches Arbeitsblatt (mit**Bewertungs-Copyright-Warnung** ) zu den Ausgabedateien.
## **Es gibt so viele Grid-Steuerelemente auf dem Markt. Warum sollte ich Aspose.Cells Grid Controls kaufen?**
 Nun, Aspose.Cells Grid Controls sind sehr preisgünstig, um für alle Arten von Benutzern erschwinglich zu sein. Zu einem sehr günstigen Preis bietet es Ihnen eine Suite von zwei Steuerelementen, um an Windows und Webanwendungen zu arbeiten. Darüber hinaus ist es nicht nur ein einfaches Raster, es gehört Ihnen**Tabellenkalkulationsbetrachter, -editor und -ersteller** zur selben Zeit. Sie können es nicht nur an jede Art von Datenquelle binden (wie normale Grid-Steuerelemente), sondern auch Excel-Dateien erstellen und verwalten. Es bietet auch eine starke und reichhaltige**Formel-Berechnungs-Engine** um nicht nur eingebaute Funktionen (unterstützt durch Aspose.Cells Grid Controls) zu berechnen, sondern auch von Ihnen definierte benutzerdefinierte Formeln. Es gibt noch viel mehr Funktionen der Aspose.Cells Grid Suite, die hier nicht behandelt werden können. Eine detailliertere Funktionsliste finden Sie auf der Seite Editionstypen.
## **Ich habe kürzlich meine Lizenz für Aspose.Cells Grid Controls erworben. Wie kann ich diese Lizenz in meiner Anwendung mit Aspose.Cells Grid Control verwenden?**
Bitte wende dich an die[Lizenzierung](/cells/de/net/licensing/) Seite von Aspose.Cells Grid Controls. Es enthält vollständige Details zur Verwendung der Lizenz mit Aspose.Cells Grid Controls in Ihren Anwendungen.
## **Werden Aspose.Cells Grid Controls von Visual Studio.NET 2005 unterstützt?**
Ja, Aspose.Cells-Rastersteuerelemente werden von Visual Studio.NET 2005 und höheren Versionen vollständig unterstützt.
## **Ich verwende das Aspose.Cells.GridWeb-Steuerelement in meiner Website mit Visual Studio.NET 2005. Aber es funktioniert überhaupt nicht. Was ist das Problem?**
 Aspose.Cells. GridWeb unterstützt beides**Dateisystem** und**HTTP** Modi von Visual Studio.NET 2005. Wenn Sie immer noch verwirrt sind, werfen Sie bitte einen Blick auf eine Schritt-für-Schritt-Anleitung zum Arbeiten mit Aspose.Cells.GridWeb unter Verwendung von Visual Studio.NET 2005.
## **Wie kann ich mein Aspose.Cells.GridWeb-basiertes Webprojekt/ meine Lösung auf dem Server bereitstellen?**
Wenn Sie die Webanwendung mit GridWeb-Steuerung bereitstellen müssen, kopieren Sie die Datei „acw_client"-Verzeichnis in Ihren Projektordner, zumindest konnte Ihre Webanwendung (die über den Server bereitgestellt wird) es nicht finden. Sie können den Skriptpfad jederzeit angeben, indem Sie die folgenden Codezeilen in den Konfigurationsabschnitt einfügen (z. B. in die Datei web.config in Ihrer .config-Datei). VS.NET Projekt) Das „acw_client" ist ein Ordner, der Dateien enthält, und Aspose.Cells. GridWeb verwendet diesen Ordner, um seine interne Konfiguration zu verwalten, er enthält Skriptdateien, Bilddateien und andere Dateien, um das Verhalten von GridWeb festzulegen und andere Vorgänge festzulegen. Die Konfigurationsdatei wird verwendet, um die Steuerung zu verhindern Verwenden der eingebetteten Client-Ressourcen (Bilder, Skripte usw.), was in einigen Fällen / Szenarien nützlich ist.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Der Pfad bezieht sich immer auf das Projektverzeichnis. Sie sollten kein Verzeichnis außerhalb des Projektverzeichnisses verwenden. Daher ist es notwendig, das Verzeichnis "acw_client" (@ Ihren GridWeb-Installationsordner) in das Verzeichnis des Projekts zu kopieren.

{{% /alert %}} 
## **Ausführen von Aspose.Cell.GridWeb in Internet Explorer 10 oder 11**
 Derzeit funktioniert Aspose.Cells.GridWeb nicht sehr gut mit Internet Explorer 10 oder 11, daher müssen Sie den Kompatibilitätsmodus von IE8/9 verwenden, um damit mit dem Browsertyp IE10/11 zu arbeiten. Sie sollten die folgende Zeile hinzufügen**<Meta>** -Tag im Header-Bereich in**.aspx** Seite:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

