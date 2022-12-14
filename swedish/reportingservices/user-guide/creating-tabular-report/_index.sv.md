---
title: Skapa tabellrapport
type: docs
weight: 70
url: /sv/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

En tabell i en Aspose.Cells rapportmall består av en sidhuvud, tabelldatarader, radgrupper och sidfötter. En exempeltabell visas nedan.

**En exempeltabell** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Tabellhuvud**
Tabellrubrik innehåller normalt rubriken för varje tabellkolumn och andra textobjekt som statisk text, rapportparametrar, globala rapportvariabler och så vidare. Tabellhuvudet är valfritt. Om du använder en rubrik ska rubriktaggen placeras till vänster om den första kolumnen med tabelldata för att indikera att raden är en rubrik.
#### **Tabelldatarad**
En tabelldatarad är en rad med celler som innehåller smarta markörer. En tabell kan bara innehålla en enda datarad.
#### **Radgrupp**
Radgruppen följer tätt efter tabelldataraden och består av två delar: grupptagg och gruppdatarad.

Grupptaggen ska placeras till vänster om den första tabelldatakolumnen för att indikera att raden är radgruppens datarad. Formatet för grupptaggen är ##group{GroupColumn}, till exempel ##group{SalesOrderNumber} där SalesOrderNumber är ett av datamängden kolumnnamn. En tabell kan bara innehålla en radgrupp, men en radgrupp kan innehålla mer än en gruppdatarad. Grupptaggen får endast placeras i den första dataraden, som visas i exemplet ovan.

Grupptaggen tas bort från Microsoft Excel-filen vid rendering. Radgrupper är valfria.
#### **Sidfötter**
 Sidfötter kommer efter radgruppen och innehåller tre delar: sidfotstagg, sidfotsdatarad och sidfotstextområde.

Footer-taggen ska placeras till vänster om den första kolumnen i tabelldatakolumnen som anger att raden är tabellsidfoten. En tabell kan innehålla mer än en sidfotsdatarad och varje sidfotsrad måste markeras med en sidfotstagg.

Sidfotstextområdet kan innehålla statisk text, rapportparametrar och globala rapportvariabler, som visas i exemplet ovan.

Footer-taggen tas bort från Microsoft Excel-filen vid rendering. Sidfötter är valfria.

Utdata från exempelmallen visas nedan.

**Exempel mall** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Det här avsnittet innehåller följande ämnen:**
- [Förbereder för att skapa tabellrapport](/cells/sv/reportingservices/preparing-for-creating-table-report/)
- [Lägger till basinformation för tabell](/cells/sv/reportingservices/adding-base-information-for-table/)
- [Lägga till formler för Reporting Services](/cells/sv/reportingservices/adding-reporting-services-formulas/)
- [Lägger till tabellgrupp](/cells/sv/reportingservices/adding-table-group/)
- [Lägga till tabellsidfot](/cells/sv/reportingservices/adding-table-footers/)
- [Lägger till rapportparametrar till rapport](/cells/sv/reportingservices/adding-report-parameters-to-report/)
- [Lägga till rapporteringstjänster globala variabler till rapport](/cells/sv/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Ställa in rapportattribut](/cells/sv/reportingservices/setting-report-attributes/)
- [Ändra rapportattribut](/cells/sv/reportingservices/modifying-report-attributes/)
