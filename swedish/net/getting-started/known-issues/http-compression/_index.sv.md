---
title: HTTP-komprimering
type: docs
weight: 10
url: /sv/net/http-compression/
---
## **HTTP-komprimeringsproblem**
Vissa användare rapporterar att om de konfigurerar HTTP-komprimering i IIS hittar de fel när de skickar genererade filer till klientwebbläsare.
### **Förklaring**
 Vi använder**"Content-disposition", "inline; filename=test.xls"** header för att tvinga webbläsaren att öppna filen och**"Content-disposition", "attachment; filename=test.xls"** header för att tvinga webbläsaren att öppna**Spara som** dialogrutan och använd Microsoft Excel för att öppna filen. Det finns dock några undantag som finns.
### **Undantag**
Du kan använda följande kod för att verifiera att det INTE är en bugg av Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Lösningar**
Du kan använda någon av följande lösningar för att lösa det här problemet:

- Flytta de angivna ASP.NET-filerna (som innehåller kodanrop Aspose.Cells) till en annan mapp som inte är komprimerad.
- Inaktivera HTTP-komprimering för dynamiskt innehåll.
- Spara den genererade filen på din server och ge en länk till dina användare.

 Om du vill använda HTTP-komprimering, använd alltid*Öppna i Excel* alternativ istället för*Öppna i webbläsaren* alternativet när du vet att du har aktiverat IIS-komprimering.
