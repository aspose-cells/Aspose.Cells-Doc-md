---
title: Installieren Sie Aspose.Cells auf Windows
type: docs
weight: 20
url: /de/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 Manchmal kann es bei der Installation zu Problemen kommen**Aspose.Cells** mit seinem Installationspaket (Aspose.Cells.msi...Windows Installationspaket) an**Windows Vista** . Dieses Dokument erklärt, wie wir damit umgehen und die erfolgreiche Installation der Komponente umsetzen können. Eigentlich**Aspose.Cells**Das Installationsprogramm muss einen virtuellen Ordner auf IIS für die Bereitstellung seiner Webdemos (Asp.NET Demos) auf Ihrem Computer erstellen, daher müssen Sie vor der Installation über Administratorrechte verfügen**Aspose.Cells** mit seinem Installer. Der Installer fordert den Zugriff auf Administratorebene auf das System an und muss dies explizit erlauben.

{{% /alert %}} 
## **Mögliche Faktoren**
 Normalerweise drin**Windows Vista** , werden die Produkte/Komponenten, die Sie installieren/verwenden, immer unter "normalen Benutzer"-Berechtigungen implementiert, auch wenn Sie ein**Administrator** . Die Programme haben nur eingeschränkten Zugriff auf das Dateisystem, auch wenn Sie als angemeldet sind**Administrator** . Dies hat einige unglückliche Nebeneffekte, auf die Sie normalerweise in Windows XP nicht stoßen würden, wenn Sie als angemeldet sind**Administrator**.
## **UAC (Benutzerkontensteuerung)**
**Benutzerkontensteuerung** ist der Teil von**Windows Vista** die um Erlaubnis bittet. Das**Benutzerkontensteuerung** Modus (auch bekannt als**Admin-Genehmigungsmodus** ) ist ein Betriebsmodus, der sich (hauptsächlich) auf die Funktionsweise von Administratorkonten auswirkt. Wann**Benutzerkontensteuerung**aktiviert ist (was standardmäßig der Fall ist), müssen Sie jedem Programm, das "Administrator"-Befugnisse verwenden möchte, ausdrücklich die Erlaubnis erteilen. Jedem Programm, das versucht, ohne Ihre Erlaubnis Administratorrechte zu nutzen, wird der Zugriff verweigert.**Benutzerkontensteuerung** wird auch für andere Sicherheitsfunktionen von benötigt**Windows Vista** , einschließlich**Sicherheitsmodus** im Internet-Explorer. Der geschützte Modus von Internet Explorer schützt Ihren Computer vor betrügerischen Webseiten und anderen webbezogenen Sicherheitslücken, einschließlich unbekannter.

 Wann**Benutzerkontensteuerung** Modus aktiviert ist, erhält jedes Programm, das Sie ausführen, nur "Standardbenutzer"-Zugriff auf das System, selbst wenn Sie als Administrator angemeldet sind.**Windows Vista** hat die eingebaute Fähigkeit, das Potenzial von Sicherheitslücken im System automatisch zu reduzieren. Dies geschieht durch automatisches Aktivieren dieser aufgerufenen Funktion**Benutzerkontensteuerung** (oder**Benutzerkontensteuerung** kurz). Das**Benutzerkontensteuerung**zwingt Benutzer, die Teil der lokalen Administratorgruppe sind, so zu arbeiten, als wären sie normale Benutzer ohne Administratorrechte. Obwohl**Benutzerkontensteuerung** hebt die Sicherheit deutlich auf**Windows Vista** , in einigen Szenarien möchten Sie es möglicherweise deaktivieren, z. B. wenn Sie Demos vor einem Publikum geben (z. B. Demos, die nicht sicherheitsrelevant sind). Einige Heimanwender könnten versucht sein, sie zu deaktivieren**Benutzerkontensteuerung** aufgrund der Nutzung zusätzlicher Ressourcen ihres Systems.
## **Schritte für eine erfolgreiche Installation der Komponente**
-  Bitte stellen Sie vor der Installation sicher, dass IIS auf Ihrem Vista installiert ist**Aspose.Cells** . Es ist obligatorisch, weil**Aspose.Cells** Installer muss einen virtuellen Ordner auf IIS für die Bereitstellung der Webdemos (Asp.NET Demos) erstellen.
-  Sie müssen deaktivieren**Benutzerkontensteuerung** (Benutzerkontensteuerung). Sie müssen sicherstellen, dass Sie eine haben**Administratorrechte** mit voller Kontrolle über das System vor der Installation**Aspose.Cells** . Andernfalls erhalten Sie während der Installation möglicherweise einen Fehler # 2869**Aspose.Cells**mit seinem Installer.

Im Folgenden finden Sie einige Möglichkeiten, dies zu erreichen.
### **Verwenden der Befehlszeile**
1.  Suchen Sie in Ihrem Windows-Verzeichnis nach cmd.exe, klicken Sie dann mit der rechten Maustaste darauf und wählen Sie Ausführen als ...**Administrator**
 2. Führen Sie nun den folgenden Befehl an der Eingabeaufforderung aus: msiexec /i<your path>/Aspose.Cells.msi und Enter.
### **Verwenden der Systemsteuerung**
- Klicken Sie auf Starten
- Klicken Sie auf Systemsteuerung
- Klicken Sie auf Benutzerkonten und Jugendschutz
- Klicken Sie auf Benutzerkonten
- Klicken Sie auf Benutzerkontensteuerung ein- oder ausschalten
- Deaktivieren Sie das Kontrollkästchen
- OK klicken

{{% alert color="primary" %}} 

Sie müssen Ihren Computer neu starten, damit die Änderung wirksam wird. Diese Änderung wirkt sich auf alle Konten auf dem Computer aus, nicht nur auf Ihre.

{{% /alert %}}
