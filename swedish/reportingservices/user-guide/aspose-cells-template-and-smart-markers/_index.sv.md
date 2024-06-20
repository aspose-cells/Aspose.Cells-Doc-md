---
title: Aspose.Cells Mall och Smarta Markörer
type: docs
weight: 30
url: /sv/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

En Aspose.Cells-mall är en Microsoft Excel-arbetsbok som innehåller Smarta Markörer. Smarta markörer fungerar som dataplatshållare för rapportobjekt och ersätts med motsvarande data vid renderingtiden. Det finns fem typer av smarta markörer, listade nedan. Alla markörer kan infogas i en mall med Aspose.Cells.Report.Designer. De kan också redigeras manuellt. 

{{% /alert %}} 
### **Smart Markers**
#### **Datamarkörer**
Formatet för **datamarkörer** är &=DataSetName.FieldName. Till exempel: &=SalesDetail.sales där SalesDetail är namnet på en datamängd eller fråga och sales är namnet på en av dess fält. Vid renderingtiden ersätts datamarkörer med värdena i datamängden som tillhandahålls av rapporteringstjänster.
#### **Rapporteringstjänsters Formelmarkörer**
Formatet för Rapporteringstjänsters **formelmarkörer** är &=expression. Till exempel: &=sum(SalesDetail.sales)/100. Uttrycket består av funktion, datamängdsfält, operator och så vidare. Vid renderingtiden ersätts rapporteringstjänsters formlermarkörer med beräknade värden.
#### **Rapporteringstjänsters Globala Variabelmarkörer**
Formatet för Rapporteringstjänsters **globala variabelmarkörer** är &=Globals! Variable Name. Till exempel: &=Globals!ExecutionTime där ExecutionTime är namnet på en global variabel. Globala variabelmarkörer ersätts med globala variabelvärden vid renderingtiden.
#### **Rapporteringstjänsters Parametrarmarkörer**
En rapportparameter har två atribut: värde och etikett. Följaktligen har **parametrarmarkörer** två format: &= Parameters! ParamName.Value och &=Parameters! ParamName.Label. De anger namnet och etikett för parametern respektive. Vid renderingtiden ersätts parametrarmarkörer med de av användaren angivna parameter-värdena.
#### **Dynamiska formler**
För att göra beräkningar på infogade rader, använd dynamiska formler. **Dynamiska formler** gör det möjligt för dig att infoga Microsoft Excels formler i celler även när en formel hänvisar till rader som kommer att infogas under exportprocessen. De kan upprepas för varje infogad rad eller användas endast med celler där datamarkörer placeras för dem.

Formatet för dynamiska formler är &=&=UpprepaDynamiskFormel.

Dynamiska formler tillåter följande ytterligare alternativ:

- {r} – Aktuellt radnummer.
- {2}, {-1} – Offset till aktuellt radnummer.

**En dynamisk upprepning av en formel och den resulterande Excel-kalkylbladet** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
