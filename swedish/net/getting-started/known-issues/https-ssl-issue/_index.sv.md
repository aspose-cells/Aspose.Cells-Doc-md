---
title: HTTPS SSL-problem
type: docs
weight: 20
url: /sv/net/https-ssl-issue/
---
## **HTTPS/SSL-problem**
Vissa användare rapporterade att de hade problem med att ladda ner Excel-filer genererade med Aspose.Cells. När dialogrutan Spara öppnas innehåller filnamnet namnet på aspx-sidan istället för excel-filen, och filtypen är tom.
### **Förklaring**
Vi ändrade HTTP-svarsrubriker för att lösa problemet med HTTP-komprimering. Detta kan orsaka problem när du skickar filer till klientens webbläsare via HTTPS/SSL.
### **Lösning**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
