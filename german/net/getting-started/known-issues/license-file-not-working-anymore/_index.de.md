---
title: Lizenzdatei funktioniert nicht mehr
type: docs
weight: 60
url: /de/net/license-file-not-working-anymore/
---
## **Symptom**

 Manchmal sind die Benutzer frustriert, weil ihre Lizenzdateien nicht mehr funktionieren, wenn sie ihre Webprojekte auf einen neuen Server verschieben / veröffentlichen. Sie sind verärgert, weil ihre Lizenzdateien auf ihrem vorherigen (alten) Server ordnungsgemäß funktionierten, aber jetzt bekommen sie eine zusätzliche**Bewertungs-Copyright-Warnung** Wasserzeichen-Arbeitsblatt (immer wenn sie Berichte mit der Komponente generieren) in der neuen Serverumgebung.

### **Ein Szenario**

"Wir haben Aspose.Cells in unserem ASP.NET-Webprojekt verwendet, um Excel-Berichte zu erstellen/zu manipulieren, wir haben eine gültige Lizenz, die wir verwenden. Vor einigen Tagen haben wir die Website auf einen neuen Server umgezogen; es gab keinerlei Upgrades oder Änderungen, wir haben sichergestellt und einfach jede einzelne Datei auf den neuen Server verschoben, einschließlich der Aspose.Cells.dll und der zugehörigen .lic-Datei(en).Wenn wir nun versuchen, Excel-Berichte in der neuen Serverumgebung zu generieren, erhalten wir eine**Bewertungs-Copyright-Warnung** Wasserzeichenblatt auf unseren Berichten. Wir haben versucht, eine neue Lizenzdatei aus dem Abschnitt „Meine Bestellungen“ der Website herunterzuladen und zu installieren, aber das Problem wurde dadurch überhaupt nicht behoben. Zu Ihrer Information, wir implementieren die Lizenz, indem wir die Datei Aspose.Cells.lic zusammen mit der Komponentendatei Aspose.Cells.dll in den bin-Ordner der Site legen, was, wie ich bereits erwähnt habe, auf dem alten Server problemlos funktioniert hat."

### **Lösung**

Aspose hat einen sauberen und zuverlässigen Lizenzierungsmechanismus. Im Allgemeinen sollte das Problem mit dem Bereitstellungsproblem zusammenhängen. Wenn eine Lizenzdatei gut funktioniert (auf einem Server), sollte sie auch auf anderen Servern / Umgebungen genauso gut funktionieren. Normalerweise verwenden die Benutzer Application_Start oder Sitzung_Starten Sie Ereignisse usw. in der Datei global.asax, um dort den Lizenzcode zu platzieren. Es ist also durchaus möglich, dass die Anwendung_Start / Sitzung_Startereignisse werden nicht ausgelöst, um den Lizenzcode an ihrem/ihren neuen Standort(en) zu verarbeiten. Hier ist zu beachten, dass Aspose.Cells immer eine Ausnahme auslöst, wenn die Komponente die Lizenzdatei nicht in einem Pfad finden kann. Die Benutzer sollten sicherstellen, dass der Lizenzcode (wo immer sie ihn platzieren) verarbeitet und Ereignisse ausgelöst werden sollten, in die sie den Lizenzcode einfügen. Der Benutzer kann den zugehörigen Dienst, dh "World Wide Web Publishing" neu starten und versuchen, nachzuverfolgen, ob Application_Start / Sitzung_Startereignisse werden ausgelöst, wenn sie ihre Projekte in der neuen Serverumgebung besuchen.

### **Bestätigung**

Bitte achten Sie auch darauf, dass …

- Sie verwenden in Ihrem Projekt eine gültige Lizenzdatei.
- Sie oder jemand anderes sollten die Lizenzdatei nicht bearbeiten / modifizieren, da die Lizenzdatei sonst nicht funktioniert.
- Sie sollten sich des Ablaufs Ihres Lizenzabonnements bewusst sein (Sie können einfach die lic-Datei in Notepad öffnen und das Ablaufdatum überprüfen).
-  Sie verwenden keine Version (Aspose.Cells.dll), die nach Ablauf Ihres Lizenzabonnements freigegeben wird. Hier ist zu beachten, dass eine Lizenzdatei nie abläuft, aber wenn Sie die Komponentenversion verwenden, die nach Ablauf Ihres Abonnements veröffentlicht wird, erhalten Sie eine zusätzliche**Bewertungs-Copyright-Warnung** Wasserzeichenblatt, wenn Sie eine Excel-Datei erstellen.

### **Verweise**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
