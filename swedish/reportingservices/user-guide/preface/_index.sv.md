---
title: Förord
type: docs
weight: 20
url: /sv/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services innehåller huvudsakligen två komponenter : Aspose.Cells.Report.Designer och Aspose.Cells.Renderer for Reporting Services. Den förra används för att designa rapporter direkt i Microsoft Excel och den senare renderar en R613 rapport från Excel och den senare är 0713 ansvarig för att 0613 rapportera Excel.

{{% /alert %}} 
### **Utforma en rapport med rapportdesignern**
De viktigaste stegen för att utforma en rapport med Aspose.Cells.Report.Designer är:

1. **Skapa datakällor och frågor**.
 Microsoft Query är integrerad med Aspose.Cells.Report.Designer och används som ett grafiskt verktyg för att skapa datakällor och frågor. Användare kan också använda en befintlig RDL-fil där datakällor och frågor är tillgängliga för operationer.
1. **Kartparametrar**.
 Om SQL-satserna för en fråga inkluderar parametrar måste användarna skapa rapportparametrar och mappa SQL-parametrar till rapportparametrar. Du kan ange giltiga värden för en rapportparameter i Aspose.Cells.Report.Designer.
1. **Design Microsoft Excel-rapportmalls innehåll, stilar och format**.
En Aspose.Cells rapportmall kan innehålla valfritt antal av följande typer av rapportobjekt:
 1. Tabell
 1. Pivottabell
 1. Diagram
 1. Textruta
 1. Matris
 Normalt används en fråga (det vill säga DataSet) som datakälla för rapportobjekt. Du kan också använda Reporting Services-parametrar, formler och globala variabler som en datakälla för vissa typer av rapportobjekt. Formaten och formaten för rapportobjekt specificeras helt enkelt genom att ställa in stilar och format för cellerna som utgör rapportobjekten.
1. **Publicera rapport**.
 Efter stegen ovan är rapporten redo att publiceras. Användare kan ange vilken mapp rapporten publiceras till. Om det behövs kan du tilldela en delad datakälla på rapportservern som datakälla för rapporten.
1. **Förhandsgranska rapport**.
När du väljer en rapport för förhandsgranskning på rapportservern uppmanas du att ange vilket filformat den ska exporteras till (till exempel Microsoft Excel 97-2003 binärt XLS format, SpreadsheetML eller Microsoft Excel 2007 08161 inmatningsparametrar),3 och valfritt indataformat för rapport. under rapportutformningen. Efter detta fylls rapporten med data från Reporting Services.
