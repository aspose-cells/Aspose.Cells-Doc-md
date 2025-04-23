---
title: Lizenzdatei funktioniert nicht mehr
type: docs
weight: 60
url: /de/net/license-file-not-working-anymore/
---

## **Symptom**

Manchmal sind die Benutzer frustriert, weil ihre Lizenzdateien nicht mehr funktionieren, wenn sie ihr Webprojekt(e) auf einen neuen Server verschieben/veröffentlichen. Sie sind verärgert, da ihre Lizenzdateien auf ihrem vorherigen (alten) Server ordnungsgemäß funktionierten, sie jedoch nun in der neuen Serverumgebung ein zusätzliches **Evaluierungshinweis** Wasserzeichen-Arbeitsblatt erhalten, wenn sie Berichte mit dem Komponenten generieren.

### **Ein Szenario**

"Wir verwenden Aspose.Cells in unserem ASP.NET-Webprojekt, um Excel-Berichte zu generieren/manipulieren. Wir haben eine gültige Lizenz, die wir verwenden. Vor einigen Tagen haben wir die Website auf einen neuen Server verschoben; es gab keine Upgrades oder Änderungen, wir haben sicherzustellen versucht und einfach jede Datei auf den neuen Server verschoben, einschließlich der Aspose.Cells.dll und der zugehörigen .lic-Dateien. Jetzt, wenn wir versuchen, Excel-Berichte in der neuen Serverumgebung zu generieren, erhalten wir ein **Evaluierungshinweis** Wasserzeichen-Arbeitsblatt in unseren Berichten. Wir haben versucht, eine neue Lizenzdatei aus dem Bereich Meine Bestellungen der Website herunterzuladen und zu installieren, aber das hat das Problem überhaupt nicht behoben. Zur Info: Wir implementieren die Lizenz, indem wir die Aspose.Cells.lic-Datei im Bin-Ordner der Website zusammen mit der Aspose.Cells.dll-Komponentendatei platzieren, die, wie bereits erwähnt, auf dem alten Server problemlos funktioniert hat."

### **Lösung**

Aspose hat einen sauberen und zuverlässigen Lizenzmechanismus. Im Allgemeinen sollte das Problem mit einem Bereitstellungsproblem zusammenhängen. Wenn eine Lizenzdatei (auf einem Server) einwandfrei funktioniert, sollte sie auch auf anderen Servern/Umgebungen einwandfrei funktionieren. Normalerweise nutzen die Benutzer Application_Start oder Session_Start-Ereignisse etc. in der global.asax-Datei, um den Lizenzcode dort zu platzieren. Es ist durchaus möglich, dass das Application_Start/Session_Start-Ereignis(e) an ihren neuen Standorten nicht ausgelöst werden, um den Lizenzcode zu verarbeiten. Hier ist zu beachten, dass Aspose.Cells immer eine Ausnahme wirft, wenn die Komponente die Lizenzdatei in einem Pfad nicht finden kann. Die Benutzer sollten sicherstellen, dass der Lizenzcode (wo immer sie ihn platzieren) verarbeitet wird und die Ereignisse ausgelöst werden, in denen sie den Lizenzcode platzieren. Der Benutzer kann den zugehörigen Dienst, d.h. "World Wide Web Publishing", neu starten und herauszufinden, ob die Application_Start/Session_Start-Ereignisse ausgelöst werden, wenn sie ihre Projekte in der neuen Serverumgebung besuchen.

### **Bestätigung**

Bitte stellen Sie auch sicher, dass...

- Sie eine gültige Lizenzdatei in Ihrem Projekt verwenden.
- Sie oder jemand anders die Lizenzdatei nicht bearbeiten/ändern sollte, da andernfalls die Lizenzdatei nicht funktioniert.
- Sie über das Ablaufdatum Ihres Lizenzabonnements informiert sind (Sie können die lic-Datei einfach in Notepad öffnen und das Ablaufdatum überprüfen).
- Sie eine Version (Aspose.Cells.dll) verwenden, die nach dem Ablauf Ihres Lizenzabonnements veröffentlicht wurde. Hier ist zu beachten, dass eine Lizenzdatei nie abläuft, aber wenn Sie die Komponentenversion verwenden, die nach dem Ablauf Ihres Abonnements veröffentlicht wurde, wird bei der Erstellung einer Excel-Datei ein zusätzliches **Evaluierungshinweis** Wasserzeichen-Arbeitsblatt angezeigt.

### **Verweise**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
{{< app/cells/assistant language="csharp" >}}
