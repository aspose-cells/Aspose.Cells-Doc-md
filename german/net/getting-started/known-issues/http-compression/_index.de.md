---
title: HTTP-Komprimierung
type: docs
weight: 10
url: /de/net/http-compression/
---
## **HTTP-Komprimierungsproblem**
Einige Benutzer berichten, dass sie beim Konfigurieren der HTTP-Komprimierung in IIS Fehler finden, während sie generierte Dateien an Clientbrowser senden.
### **Erläuterung**
 Wir gebrauchen**"Inhaltsdisposition", "inline; Dateiname=test.xls"** Header, um den Browser zu zwingen, die Datei zu öffnen und**"Inhaltsdisposition", "Anhang; Dateiname=test.xls"** Kopfzeile, um den Browser zu zwingen, die zu öffnen**Speichern als** Dialog und verwenden Sie Microsoft Excel, um die Datei zu öffnen. Es gibt jedoch einige Ausnahmen, die existieren.
### **Ausnahmen**
Sie können den folgenden Code verwenden, um zu überprüfen, ob es sich NICHT um einen Fehler von Aspose handelt.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Lösungen**
Sie können eine der folgenden Problemumgehungen verwenden, um dieses Problem zu lösen:

- Verschieben Sie die angegebenen ASP.NET-Dateien (die Code enthalten, der Aspose.Cells aufruft) in einen anderen Ordner, der nicht komprimiert ist.
- Deaktivieren Sie die HTTP-Komprimierung für dynamische Inhalte.
- Speichern Sie die generierte Datei auf Ihrem Server und stellen Sie Ihren Benutzern einen Link zur Verfügung.

 Wenn Sie die HTTP-Komprimierung verwenden möchten, verwenden Sie bitte immer*OpenInExcel* Option statt*OpenInBrowser* Option, wenn Sie wissen, dass Sie die IIS-Komprimierung aktiviert haben.
