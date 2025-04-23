---
title: Sicherheitsausnahmeproblem
type: docs
weight: 30
url: /de/net/security-exception-issue/
---

## **Sicherheitsausnahme Problem**
Einige Benutzer erhalten möglicherweise einen "Sicherheitsausnahmefehler", wenn sie Aspose.Cells verwenden. Dieses Problem tritt normalerweise in einer Webanwendung auf.
### **Erklärung**
Aspose.Cells muss einige **Win32 GDI-APIs** aufrufen, um einige wichtige Funktionen bereitzustellen. Wenn der Webserver ein strenges Vertrauensniveau hat, kann diese Sicherheitsausnahme ausgelöst werden.
### **Lösung**
Versuchen Sie bitte, einen neuen Berechtigungssatz zu erstellen, um Aspose.Cells.dll Sicherheitsberechtigung mit aktivierter „Aufrufe an nicht verwaltete Assemblys zulassen“ zu geben.
{{< app/cells/assistant language="csharp" >}}
