---
title: HTTP komprimering
type: docs
weight: 10
url: /sv/net/http-compression/
---

## **Problem med HTTP-komprimering**
Vissa användare rapporterar att om de konfigurerar HTTP-komprimering i IIS hittar de fel när de skickar genererade filer till klientwebbläsare.
### **Förklaring**
Vi använder **"Content-disposition", "inline; filename=test.xls"** header för att tvinga webbläsaren att öppna filen och **"Content-disposition", "attachment; filename=test.xls"** header för att tvinga webbläsaren att öppna dialogrutan **Spara som** och använda Microsoft Excel för att öppna filen. Det finns emellertid vissa undantag.
### **Undantag**
Du kan använda följande kod för att verifiera att det INTE är en bugg i Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Lösningar**
Du kan använda en av följande arbetsmetoder för att lösa detta problem:

- Flytta de angivna ASP.NET-filerna (som innehåller kodanrop till Aspose.Cells) till en annan mapp som inte är komprimerad.
- Inaktivera HTTP-komprimering för dynamiskt innehåll.
- Spara den genererade filen på din server och tillhandahåll en länk till dina användare.

Om du vill använda HTTP-komprimering, använd alltid alternativet *OpenInExcel* i stället för alternativet *OpenInBrowser* när du vet att du har aktiverat IIS-komprimering.
{{< app/cells/assistant language="csharp" >}}
