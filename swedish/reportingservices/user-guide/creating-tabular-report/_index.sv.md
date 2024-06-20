---
title: Skapa tabellrapport
type: docs
weight: 70
url: /sv/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

En tabell i en Aspose.Cells Rapportmall består av en sidhuvud, tabellraddata, radgrupper och sidfötter. Ett exempel på en tabell visas nedan.

**Ett exempel på en tabell** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Tabellhuvud**
Tabellhuvudet innehåller vanligtvis titeln för varje tabellkolumn och andra textobjekt som statisk text, rapportparametrar, globala rapportvariabler och så vidare. Tabellhuvudet är valfritt. Om du använder en rubrik ska rubriktaggen placeras till vänster om första kolumnen av tabelldata för att ange att raden är en rubrik.
#### **Tabellraddata**
En tabellraddata är en rad med celler som innehåller smarta markörer. En tabell kan bara innehålla en enda rad för data.
#### **Radgrupp**
Radgruppen följer tätt efter tabellraddata och består av två delar: grupptagg och gruppdata. rad. 

Grupptaggen ska placeras till vänster om den första tabelldatakolumnen för att ange att raden är radgruppens datarad. Formatet för grupptaggen är ##group{GroupColumn}, till exempel ##group{SalesOrderNumber} där SalesOrderNumber är ett av datasetets kolumnnamn. En tabell kan bara innehålla en radgrupp, men en radgrupp kan innehålla mer än en grupprad. Grupptaggen kan endast placeras i den första data raden, som visas i exemplet ovan.

Grupptaggen tas bort från den resulterande Microsoft Excel-filen vid renderingtiden. Radgrupper är valfria.
#### **Sidfötter**
Sidfötter kommer efter radgruppen och inkluderar tre delar: fotslag, fotodata rad och fototextområde. 

Fotslaget ska placeras till vänster om den första kolumnen i tabelldatakolumnen som anger att raden är tabellfoten. En tabell kan innehålla mer än en fotodatarad och varje fotrad måste markeras med ett fotslag. 

Fototextområdet kan innehålla statisk text, rapportparametrar och globala rapportvariabler, som visas i exemplet ovan.

Fotslaget tas bort från utmatnings Microsoft Excel-filen vid renderingtiden. Sidfötter är valfria.

Utmatningen av exempelmallen visas nedan.

**Exempel på mall** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Denna avsnitt innehåller följande ämnen:** 
- [Förberedelse för att skapa tabellrapport](/cells/sv/reportingservices/preparing-for-creating-table-report/)
- [Lägga till grundinformation för tabell](/cells/sv/reportingservices/adding-base-information-for-table/)
- [Lägga till formler för rapporttjänster](/cells/sv/reportingservices/adding-reporting-services-formulas/)
- [Lägga till tabellgrupp](/cells/sv/reportingservices/adding-table-group/)
- [Lägga till tabellfötter](/cells/sv/reportingservices/adding-table-footers/)
- [Lägga till rapportparametrar till rapporten](/cells/sv/reportingservices/adding-report-parameters-to-report/)
- [Lägga till globala variabler för rapporttjänster till rapporten](/cells/sv/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Inställning av rapportattribut](/cells/sv/reportingservices/setting-report-attributes/)
- [Modifiera rapportattribut](/cells/sv/reportingservices/modifying-report-attributes/)
