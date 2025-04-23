---
title: HTTPS SSL Problem
type: docs
weight: 20
url: /de/net/https-ssl-issue/
---

## **HTTPS/SSL-Problem**
Einige Benutzer berichteten, dass sie Probleme hatten, Excel-Dateien herunterzuladen, die mit Aspose.Cells generiert wurden. Wenn der Speicherdialog geöffnet wird, enthält der Dateiname den Namen der aspx-Seite anstelle der Excel-Datei, und der Dateityp ist leer.
### **Erklärung**
Wir haben die HTTP-Antwortheader geändert, um das Problem mit der HTTP-Komprimierung zu lösen. Dies kann jedoch Probleme beim Senden von Dateien an den Client-Browser über HTTPS/SSL verursachen.
### **Lösung**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
