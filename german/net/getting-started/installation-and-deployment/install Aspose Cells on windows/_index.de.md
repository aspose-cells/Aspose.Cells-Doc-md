---
title: Aspose.Cells auf Windows installieren
type: docs
weight: 20
url: /de/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

Manchmal können Sie beim Installieren von **Aspose.Cells** über das Installationspaket (Aspose.Cells.msi...Windows Installer Package) auf **Windows Vista** auf Probleme stoßen. In diesem Dokument wird erläutert, wie Sie damit umgehen und die erfolgreiche Installation des Komponenten umsetzen können. Tatsächlich muss der **Aspose.Cells**-Installer einen virtuellen Ordner im IIS erstellen, um seine Web-Demos (Asp.NET Demos) auf Ihrem Rechner bereitzustellen. Daher benötigen Sie Administratorrechte, bevor Sie **Aspose.Cells** über seinen Installer installieren können. Der Installer benötigt ausdrücklich Administratorzugriff auf das System, um dies zu ermöglichen.

{{% /alert %}} 
## **Mögliche Faktoren**
Normalerweise werden in **Windows Vista** die installierten/verwendeten Produkte/Komponenten immer unter "normalen Benutzer"-Berechtigungen ausgeführt, auch wenn Sie ein **Administrator** sind. Den Programmen ist nur begrenzter Zugriff auf das Dateisystem gestattet, selbst wenn Sie als **Administrator** angemeldet sind. Dies hat einige unglückliche Nebenwirkungen, die Sie normalerweise nicht bei Windows XP erleben würden, wenn Sie als **Administrator** angemeldet sind.
## **UAC (Benutzerkontensteuerung)**
Die **UAC** ist der Teil von **Windows Vista**, der Sie um Erlaubnis bittet. Der **UAC**-Modus (auch als **Admin-Bestätigungsmodus** bekannt) ist ein Betriebsmodus, der hauptsächlich die Arbeitsweise von Administratorkonten betrifft. Wenn **UAC** eingeschaltet ist (was standardmäßig der Fall ist), müssen Sie jeder Anwendung, die "Administrator"-Rechte nutzen möchte, ausdrücklich die Erlaubnis geben. Jede Anwendung, die versucht, Admin-Rechte ohne Ihre Erlaubnis zu nutzen, wird den Zugriff verweigert. **UAC** ist auch für andere Sicherheitsfunktionen von **Windows Vista** erforderlich, einschließlich **Geschützter Modus** im Internet Explorer. Der Internet Explorer Geschützter Modus schützt Ihren Computer vor betrügerischen Webseiten und anderen webbezogenen Sicherheitslücken, einschließlich unbekannter.

Wenn der **UAC**-Modus aktiviert ist, erhält jedes von Ihnen ausgeführte Programm nur Zugriff als "normaler Benutzer" auf das System, selbst wenn Sie als Administrator angemeldet sind. **Windows Vista** hat die eingebaute Fähigkeit, das Potenzial für Sicherheitslücken im System automatisch zu verringern. Es tut dies, indem es automatisch diese Funktion namens **Benutzerkontensteuerung** (oder **UAC** kurz) aktiviert. **UAC** zwingt Benutzer, die zur lokalen Administratorengruppe gehören, so zu arbeiten, als wären sie normale Benutzer ohne Administratorenrechte. Obwohl **UAC** die Sicherheit auf **Windows Vista** klar verbessert, möchten Sie es unter bestimmten Umständen möglicherweise deaktivieren, z.B. bei Demos vor Publikum (Demos, die z.B. nicht sicherheitsrelevant sind). Einige Privatnutzer könnten versucht sein, **UAC** zu deaktivieren, aufgrund des zusätzlichen Ressourcenverbrauchs ihres Systems.
## **Schritte für die erfolgreiche Installation der Komponente**
- Stellen Sie sicher, dass IIS auf Ihrem Vista installiert ist, bevor Sie **Aspose.Cells** installieren. Dies ist unerlässlich, da der **Aspose.Cells**-Installer einen virtuellen Ordner im IIS erstellen muss, um die Web-Demos (Asp.NET Demos) bereitzustellen.
- Sie müssen die **UAC** (Benutzerkontensteuerung) deaktivieren. Stellen Sie sicher, dass Sie über Administratorrechte mit vollständiger Kontrolle des Systems verfügen, bevor Sie **Aspose.Cells** installieren. Andernfalls könnten Sie bei der Installation von **Aspose.Cells** über seinen Installer den Fehler # 2869 erhalten.

Nachfolgend einige Möglichkeiten, dies zu erreichen.
### **Verwendung der Befehlszeile**
1. Suchen Sie cmd.exe im Windows-Verzeichnis, klicken Sie dann mit der rechten Maustaste darauf und wählen Sie Ausführen als... **Administrator**
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Die Systemsteuerung verwenden**
- Klicken Sie auf Start
- Klicken Sie auf Systemsteuerung
- Klicken Sie auf Benutzerkonten und Jugendschutz
- Klicken Sie auf Benutzerkonten
- Klicken Sie auf Benutzerkontensteuerung ein- oder ausschalten
- Deaktivieren Sie das Kontrollkästchen
- Klicken Sie auf OK

{{% alert color="primary" %}} 

Sie müssen Ihren Computer neu starten, damit die Änderung wirksam wird. Diese Änderung betrifft alle Konten auf dem Computer, nicht nur Ihres.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
