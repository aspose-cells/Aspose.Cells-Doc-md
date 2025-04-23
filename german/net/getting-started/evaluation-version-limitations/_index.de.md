---
title: Grenzen der Testversion
type: docs
weight: 110
url: /de/net/evaluation-version-limitations/
description: Aspose.Cells for .NET bietet verschiedene Pläne zum Kauf oder bietet eine kostenlose Testversion und eine 30 tägige temporäre Lizenz zur Evaluierung mithilfe von Lizenzierungs und Abonnementrichtlinien in C#.
keywords: Evaluierungsversionseinschränkungen, Anzahl der geöffneten Dateien in Evaluierungsversion, Evaluierungswasserzeichen bei Verwendung der Evaluierungsversion.
---

## **So erhalten Sie die Evaluierungsversion von Aspose.Cells**

Sie können eine Evaluierungsversion von **Aspose.Cells** für .NET von [ihrer Downloadseite](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) bei Maven repos herunterladen. Die Evaluierungsversion bietet genau die gleichen Funktionen wie die lizenzierte Version des Produkts. Außerdem wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Zeilen Code hinzufügen, um die Lizenz anzuwenden.

Wenn Sie mit Ihrer Evaluierung von **Aspose.Cells** zufrieden sind, können Sie [eine Lizenz erwerben](https://purchase.aspose.com) auf der Aspose-Website. Machen Sie sich mit den verschiedenen angebotenen Abonnementtypen vertraut. Bei Fragen zögern Sie nicht, das Aspose-Verkaufsteam zu kontaktieren.

Jede Aspose-Lizenz beinhaltet ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die während dieser Zeit veröffentlicht werden. Der technische Support ist kostenlos und unbegrenzt und wird sowohl für lizenzierte als auch für Evaluierungsnutzer bereitgestellt.

## **Wie man Aspose.Cells ohne Evaluierungsversionseinschränkungen testet**

Wenn Sie **Aspose.Cells** ohne Einschränkungen der Evaluierungsversion testen möchten, fordern Sie eine 30-tägige temporäre Lizenz an. Bitte beachten Sie [Wie man eine temporäre Lizenz erhält](https://purchase.aspose.com/temporary-license) für weitere Informationen.


## **Evaluierungsversion-Beschränkungen**

Die Evaluierungsversion des **Aspose.Cells**-Produkts (ohne spezifizierte Lizenz) bietet die volle Funktionalität des Produkts, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und ein zusätzliches Arbeitsblatt mit Evaluierungswasserzeichen beschränkt.

Die Beschränkungen werden unten angezeigt:

### **1. Beschränkung: Anzahl der geöffneten Dateien**

Beim Ausführen Ihres Programms können Sie nur 100 Excel-Dateien öffnen. Wenn Ihre Anwendung diese Anzahl überschreitet, wird eine Ausnahme ausgelöst.

### **2. Beschränkung: Arbeitsblatt mit Evaluierungswasserzeichen**
Dieses Arbeitsblatt wird immer als aktives Arbeitsblatt angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter festlegen.
<br>
<image src="1.png" width="70%" />
<br>

### **3. Einschränkung: Klartext mit Evaluierungsinformationen**
In der Ausgabe der Klartextdatei von Aspose.Cells wird am Ende des Dokuments eine Evaluierungsinformation hinzugefügt.
<br>
<image src="2.png" width="70%" />
<br>

### **4. Einschränkung: PDF und Bild mit Evaluierungswasserzeichen**
In der Ausgabe der PDF- oder Bilddatei von Aspose.Cells wird ein Evaluierungswasserzeichen oben im Dokument/Bild eingefügt. Sie können den Evaluierungshinweis für das Urheberrecht (das zusätzliche Arbeitsblatt) im GridWeb-Steuerelement auch nicht ausblenden. Es wird immer hinzugefügt (am Ende in den Arbeitsblattregisterkarten) im Steuerelement.
<br>
<image src="3.png" width="70%" />
<br>

### **5. Einschränkung: Konfigurationsdateieinstellungen (Aspose.Cells.GridWeb)**
Sie können den Skriptpfad nicht neu festlegen, indem Sie die folgenden Codezeilen in den Konfigurationsabschnitt hinzufügen (z.B. in die web.config-Datei). Der acw_client ist ein Ordner, der Dateien enthält, und Aspose.Cells.GridWeb verwendet diesen Ordner, um seine interne Konfiguration zu verwalten. Er enthält Skriptdateien, Bilddateien und andere Dateien zur Festlegung des Verhaltens von GridWeb und zur Ausführung anderer Operationen. Die Konfigurationsdateieinstellungen in der web.config-Datei wirken sich nur auf die LIZENZIERTE Version des Steuerelements aus.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Diese Einstellungen können in einigen Fällen / Szenarien obligatorisch sein, wenn Sie die Aspose.Cells.GridWeb-Steuerung in Dateisystem-Websites oder MS Ajax-Erweiterungen verwenden.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
