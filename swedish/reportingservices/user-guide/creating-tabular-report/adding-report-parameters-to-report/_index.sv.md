---
title: Lägg till rapportparametrar till rapport
type: docs
weight: 60
url: /sv/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Aspose.Cells rapportmall stödjer rapporteringsresursers rapportparametrar som en datakälla för celler som innehåller en rapporteringsresursparametermarkör. Se [Aspose.Cells Mall och Smarta Markörer](/cells/sv/reportingservices/aspose-cells-template-and-smart-markers/) för att lära dig om rapporteringsresursens parametermarkörer. Rapportparametrar placeras normalt i textområdet för tabellhuvudet eller sidfoten.

{{% /alert %}} 
### **Lägga till en rapportparameter**
För att lägga till rapportparametrar till rapporter:

1. Välj en cell. 

   **Välja en cell** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Klicka på Infoga formel på verktygsfältet Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Välj **Parametrar** från panelen Parametrar till vänster.
   Alla parametrar listas i höger panel. 
1. Välj en parameter, i exemplet har vi valt EmpID.
1. Dubbelklicka på parametern för att få uttrycket att visas i redigeraren högst upp på formuläret.
   En parameter har två dataattribut: etikett och värde (standardattributet är värde). 

   **Val av parameter** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. I exemplet ska parameterns etikett visas i rapporten, så ändra uttrycket till Parameters!EmpID.Label. 

   **Ändra parametern** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Klicka på **OK**.
   Den valda cellen innehåller en rapportparametrarmarkör. 

   **En rapportparameter infogad i cellen** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
