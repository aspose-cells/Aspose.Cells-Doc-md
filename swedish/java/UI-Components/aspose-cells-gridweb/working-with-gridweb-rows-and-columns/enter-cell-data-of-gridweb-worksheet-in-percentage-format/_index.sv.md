---
title: Ange Cell Data för GridWeb-arbetsbladet i procentformat
type: docs
weight: 1010
url: /sv/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **Möjliga användningsscenarier**
GridWeb stöder nu användare att ange celldata i procentformat som 3% och data i cellen kommer automatiskt att formateras som 3,00%. Du måste dock ställa in cellformatet till procentformat som antingen är GridTableItemStyle.NumberType en 9 eller 10. Siffran 9 kommer att formatera 3 % som 3 % men siffran 10 kommer att formatera 3 % som 3,00 %.

{{% alert color="primary" %}} 

Om du inte har ställt in cellformatet till Procentformat, kommer indata 3% att visas som 0,03.

{{% /alert %}} 
##  **Ange Cell Data för GridWeb-arbetsbladet i procentformat**
Följande exempelkod ställer in cellen A1 GridTableItemStyle.NumberType som 10, därför formateras indata 3 % automatiskt till 3,00 % som visas på skärmdumpen.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **Exempelkod**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






