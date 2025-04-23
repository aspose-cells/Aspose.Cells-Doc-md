---
title: HTTPS SSL problem
type: docs
weight: 20
url: /sv/net/https-ssl-issue/
---

## **HTTPS/SSL-problem**
Vissa användare rapporterade att de hade problem med att hämta Excel-filer som genererats med Aspose.Cells. När dialogrutan Spara öppnas innehåller filnamnet namnet på aspx-sidan i stället för excelfilen, och filtypen är tom.
### **Förklaring**
Vi ändrade HTTP-svarsheaders för att lösa problemet med HTTP-komprimering. Detta kan orsaka problem när filer skickas till klientens webbläsare via HTTPS/SSL.
### **Lösning**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
