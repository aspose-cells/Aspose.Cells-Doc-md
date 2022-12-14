---
title: Sicherheitsausnahmeproblem
type: docs
weight: 30
url: /de/net/security-exception-issue/
---
## **Sicherheitsausnahmeproblem**
Einige Benutzer erhalten möglicherweise den Fehler „Sicherheitsausnahme“, wenn sie versuchen, Aspose.Cells zu verwenden. Dieses Problem tritt im Allgemeinen in einer Webanwendung auf.
### **Erläuterung**
 Aspose.Cells muss einige anrufen**Win32-GDI-APIs** um einige wichtige Funktionen bereitzustellen. Wenn der Webserver eine strikte Vertrauensebene hat, kann diese Sicherheitsausnahme ausgelöst werden.
### **Lösung**
Versuchen Sie, einen neuen Berechtigungssatz zu erstellen, um Aspose.Cells.dll die Sicherheitsberechtigung zu erteilen, wobei „Aufrufe an nicht verwaltete Assemblys zulassen“ aktiviert ist.
