---
title: Förord
type: docs
weight: 20
url: /sv/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services innehåller främst två komponenter: Aspose.Cells.Report.Designer och Aspose.Cells.Renderer för rapporttjänster. Den förra används för att designa rapporter direkt i Microsoft Excel och den senare är ansvarig för att rendera en RDL-rapport till Microsoft Excel. 

{{% /alert %}} 
### **Designa en rapport med rapportdesignern**
De huvudsakliga stegen för att designa en rapport med Aspose.Cells.Report.Designer är:

1. **Skapa datakällor och frågor**.
   Microsoft Query integreras med Aspose.Cells.Report.Designer och används som ett grafiskt verktyg för att skapa datakällor och frågor. Användare kan också använda en befintlig RDL-fil där datakällor och frågor finns tillgängliga för operationer.
1. **Kartlägg parametrar**.
   Om SQL-uttalandena för en fråga innehåller parametrar måste användarna skapa rapportparametrar och kartlägga SQL-parametrar till rapportparametrar. Du kan ange giltiga värden för en rapportparameter i Aspose.Cells.Report.Designer.
1. **Utforma innehållet, stilar och format för Microsoft Excel-rapportmall**.
   En Aspose.Cells rapportmall kan innehålla ett valfritt antal följande typer av rapportelement: 
   1. Tabell
   1. Pivot-tabell
   1. Diagram
   1. Textbox
   1. Matris
      Vanligtvis används en fråga (det vill säga DataSet) som en datakälla för rapportobjekt. Du kan också använda rapporteringsparametrar, formler och globala variabler som en datakälla för vissa typer av rapportobjekt. Stilarna och formaten för rapportobjekten anges helt enkelt genom att ställa in stilarna och formaten för cellerna som utgör rapportobjekten.
1. **Publicera rapport**.
   Efter ovanstående steg är rapporten redo att publiceras. Användare kan ange vilken mapp rapporten publiceras till. Om det behövs kan du tilldela en delad datakälla på rapportservern som datakälla för rapporten.
1. **Förhandsgranska rapport**.
   När du väljer en rapport för förhandsgranskning på rapportservern uppmanas du att ange vilket filformat du vill exportera den till (till exempel Microsoft Excel 97-2003 binärt XLS-format, SpreadsheetML eller Microsoft Excel 2007 XLSX-format) samt eventuella inmatningsrapportparametrar som skapats under rapportdesignen. Efter detta fylls rapporten med data som tillhandahålls av rapporteringstjänsterna.
