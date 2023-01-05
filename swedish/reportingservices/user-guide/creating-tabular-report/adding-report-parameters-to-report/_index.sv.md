---
title: Lägger till rapportparametrar till rapport
type: docs
weight: 60
url: /sv/reportingservices/adding-report-parameters-to-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells' rapportmall stöder Reporting Services-rapportparametrar som en datakälla för celler som innehåller en Reporting Services-parametermarkör. Vänligen hänvisa till[Aspose.Cells Mall och smarta markörer](/cells/sv/reportingservices/aspose-cells-template-and-smart-markers/) för att lära dig om Reporting Services-parametermarkörer. Rapportparametrar placeras normalt i textområdet i tabellens sidhuvud eller sidfot.

{{% /alert %}} 
### **Lägga till en rapportparameter**
Så här lägger du till rapportparametrar till rapporter:

1.  Välj en cell.

   **Välja en cell** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Klicka på Infoga formel i verktygsfältet Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1.  Välj**Parametrar** från panelen Parametrar till vänster.
 Alla parametrar listas i den högra panelen.
1. Välj en parameter, i exemplet har vi valt EmpID.
1. Dubbelklicka på parametern för att få uttrycket att visas i editorn överst i formuläret.
 En parameter har två dataattribut: etikett och värde (standardattributet är värde).

   **Att välja en parameter** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1.  I exemplet ska parameterns etikett visas i rapporten, så ändra uttrycket till Parameters!EmpID.Label.

   **Ändring av parametern** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1.  Klick**OK**.
 Den markerade cellen innehåller en rapportparametermarkör.

   **En rapportparameter infogas i cellen** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
