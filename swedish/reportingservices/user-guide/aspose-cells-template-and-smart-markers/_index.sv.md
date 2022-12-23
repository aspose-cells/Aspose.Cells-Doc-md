---
title: Aspose.Cells Mall och smarta markörer
type: docs
weight: 30
url: /sv/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

 En Aspose.Cells-mall är en Microsoft Excel-arbetsbok som innehåller smarta markörer. Smarta markörer fungerar som dataplatshållare för rapportobjekt och ersätts med motsvarande data vid renderingstidpunkten. Det finns fem typer av smarta markörer, listade enligt nedan. Alla markörer kan infogas i en mall av Aspose.Cells.Report.Designer. Den kan även redigeras manuellt.

{{% /alert %}} 
### **Smarta markörer**
#### **Datamarkörer**
 Formatet på**datamarkörer**är &=DataSetName.FieldName. Till exempel: &=SalesDetail.sales där SalesDetail är namnet på en datamängd eller fråga och försäljning är namnet på ett av dess fält. Vid renderingstidpunkten ersätts datamarkörer med värdena för dataset som tillhandahålls av Reporting Services.
#### **Reporting Services Formler Markörer**
 Formatet för Reporting Services'**formlermarkörer** är &=uttryck. Till exempel: &=sum(SalesDetail.sales)/100. Uttrycket består av funktion, datasetfält, operator och så vidare. Vid renderingstid. Reporting Services formelmarkörer ersätts med beräknade värden.
#### **Reporting Services Global Variable Markers**
 Formatet för Reporting Services'**globala variabla markörer** är &=Globals! Variabelnamn. Till exempel: &=Globals!ExecutionTime där ExecutionTime är namnet på en global variabel. Globala variabelmarkörer ersätts med globala variabelvärden vid renderingstidpunkten.
#### **Reporting Services Parametrar Markörer**
En rapportparameter har två attribut: värde och etikett. Följaktligen,**parametrar markörer** har två format: &= Parametrar! ParamName.Value och &=Parametrar! ParamName.Label. De anger namnet och etiketten för parametern. Vid renderingstidpunkten ersätts parametermarkörerna med de parametervärden som angetts av användaren.
#### **Dynamiska formler**
 För att göra beräkningar på infogade rader, använd dynamiska formler.**Dynamiska formler** låter dig infoga Microsoft Excels formler i celler även när en formel refererar till rader som kommer att infogas under exportprocessen. De kan upprepas för varje infogade rad eller användas endast med celler där datamarkörer placeras för dem.

Formatet för dynamiska formler är &=&=RepeatDynamicFormula.

Dynamiska formler tillåter följande ytterligare alternativ:

- {r} – Aktuellt radnummer.
- {2}, {-1} – Offset till aktuellt radnummer.

**En återkommande dynamisk formel och det resulterande Excel-kalkylbladet** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
