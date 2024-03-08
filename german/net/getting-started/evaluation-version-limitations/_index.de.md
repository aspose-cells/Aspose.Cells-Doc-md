---
title: Einschränkungen der Evaluierungsversion
type: docs
weight: 110
url: /de/net/evaluation-version-limitations/
description: Aspose.Cells for .NET bietet verschiedene Kaufpläne oder eine kostenlose Testversion und eine 30-tägige temporäre Lizenz zur Evaluierung unter Verwendung der Lizenz- und Abonnementrichtlinien in C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **So erhalten Sie die Testversion von Aspose.Cells**

 Sie können eine Testversion von herunterladen**Aspose.Cells** für NET ab[seine Download-Seite](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven Repos. Die Evaluierungsversion bietet absolut die gleichen Funktionen wie die lizenzierte Version des Produkts. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Codezeilen hinzufügen, um die Lizenz anzuwenden.

 Sobald Sie mit Ihrer Bewertung von *Aspose.Cells** zufrieden sind, können Sie dies tun[eine Lizenz erwerben](https://purchase.aspose.com)auf der Website Aspose. Machen Sie sich mit den verschiedenen angebotenen Abonnementarten vertraut. Bei Fragen steht Ihnen das Vertriebsteam unter Aspose jederzeit gerne zur Verfügung.

Zu jeder Aspose-Lizenz gehört ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die in diesem Zeitraum herauskommen. Der technische Support ist kostenlos und unbegrenzt und wird sowohl für lizenzierte als auch für Testbenutzer bereitgestellt.

##  **So testen Sie Aspose.Cells ohne Einschränkungen der Evaluierungsversion**

 Wenn Sie testen möchten**Aspose.Cells** Ohne Einschränkungen der Evaluierungsversion fordern Sie eine 30-tägige temporäre Lizenz an. Bitte beziehen Sie sich auf[Wie bekomme ich eine temporäre Lizenz?](https://purchase.aspose.com/temporary-license) für mehr Informationen.


##  **Einschränkungen der Evaluierungsversion**

 Evaluierungsversion von**Aspose.Cells** Das Produkt (ohne Angabe einer Lizenz) bietet die volle Produktfunktionalität, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und ein zusätzliches Arbeitsblatt mit Bewertungswasserzeichen beschränkt.

Die Einschränkungen sind unten aufgeführt:

###  **1. Einschränkung: Anzahl der geöffneten Dateien**

Beim Ausführen Ihres Programms können Sie nur 100 Excel-Dateien öffnen. Wenn Ihre Bewerbung diese Zahl überschreitet, wird eine Ausnahme ausgelöst.

###  **2. Einschränkung: Arbeitsblatt mit Bewertungswasserzeichen**
Dieses Arbeitsblatt wird immer als aktives Arbeitsblatt angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter festlegen.
<br>
<image src="1.png" width="70%" />
<br>

###  **3. Einschränkung: Nur-Text mit Bewertungsinformationen**
In der ausgegebenen Nur-Text-Datei von Aspose.Cells würden am Ende des Dokuments Bewertungsinformationen hinzugefügt.
<br>
<image src="2.png" width="70%" />
<br>

###  **4. Einschränkung: PDF und Bild mit Bewertungswasserzeichen**
In der Ausgabe PDF oder der Bilddatei von Aspose.Cells würde ein Bewertungswasserzeichen oben in das Dokument/Bild eingefügt. Sie können die Bewertungs-Copyright-Warnung (das zusätzliche Arbeitsblatt) auch im GridWeb-Steuerelement nicht ausblenden, sie wird immer hinzugefügt (am Ende in den Arbeitsblattregisterkarten) im Steuerelement.
<br>
<image src="3.png" width="70%" />
<br>

###  **5. Einschränkung: Einstellungen der Konfigurationsdatei (Aspose.Cells.GridWeb)**
Sie können den Skriptpfad nicht neu angeben, indem Sie die folgenden Codezeilen zum Konfigurationsabschnitt hinzufügen (z. B. in der Datei web.config). Der acw_client ist ein Ordner, der Dateien und Aspose.Cells enthält. GridWeb verwendet diesen Ordner zur Verwaltung seiner internen Konfiguration. Er verfügt über Skriptdateien, Bilddateien und andere Dateien, um das Verhalten von GridWeb festzulegen und andere Vorgänge festzulegen. Die Konfigurationsdatei wird verwendet, um zu verhindern, dass die Steuerung die eingebetteten Client-Ressourcen (Bilder, Skripte usw.) verwendet, was in manchen Fällen/Szenarien nützlich ist. Darüber hinaus werden diese Konfigurationseinstellungen in der Datei web.config nur mit der LIZENZIERTEN Version des Steuerelements wirksam.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Diese Einstellungen können in einigen Fällen/Szenarien obligatorisch sein, wenn Sie das Aspose.Cells.GridWeb-Steuerelement in Dateisystem-Websites oder MS Ajax-Erweiterungen usw. verwenden.

{{% /alert %}}