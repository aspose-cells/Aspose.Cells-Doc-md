---
title: HTTP Komprimierung
type: docs
weight: 10
url: /de/net/http-compression/
---

## **Problem mit HTTP-Komprimierung**
Einige Benutzer berichten, dass sie beim Konfigurieren der HTTP-Komprimierung in IIS Fehler beim Senden von generierten Dateien an Client-Browser finden.
### **Erklärung**
Wir verwenden den **"Content-Disposition", "Inline; Filename=test.xls"**-Header, um den Browser zu zwingen, die Datei zu öffnen, und den **"Content-Disposition", "Attachment; Filename=test.xls"**-Header, um den Browser zum Öffnen des Dialogfelds **Speichern unter** zu zwingen und Microsoft Excel zum Öffnen der Datei zu verwenden. Es gibt jedoch einige Ausnahmen, die existieren.
### **Ausnahmen**
Sie können den folgenden Code verwenden, um zu überprüfen, dass es sich NICHT um einen Fehler von Aspose handelt.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Lösungen**
Sie können eine der folgenden Workarounds verwenden, um dieses Problem zu lösen:

- Verschieben Sie die angegebenen ASP.NET-Dateien (die Code enthaltende Aufrufe von Aspose.Cells enthalten) in einen anderen Ordner, der nicht komprimiert ist.
- Deaktivieren Sie die HTTP-Komprimierung für dynamische Inhalte.
- Speichern Sie die generierte Datei auf Ihrem Server und stellen Sie einen Link für Ihre Benutzer bereit.

Wenn Sie die HTTP-Komprimierung verwenden möchten, verwenden Sie bitte immer die Option *OpenInExcel* anstelle der Option *OpenInBrowser*, wenn Sie wissen, dass Sie die IIS-Komprimierung aktiviert haben.
{{< app/cells/assistant language="csharp" >}}
