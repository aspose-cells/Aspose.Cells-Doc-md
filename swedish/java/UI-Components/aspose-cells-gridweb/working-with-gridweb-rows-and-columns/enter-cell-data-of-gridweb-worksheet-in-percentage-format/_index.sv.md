---
title: Ange celldata i GridWeb arbetsblad i procentformat
type: docs
weight: 1010
url: /sv/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **Möjliga användningsscenario**
GridWeb stöder nu att användare anger celldata i procentformat som 3% och data i cellen formateras automatiskt som 3,00%. Du måste dock ställa in cellformatet. till procentformat vilket antingen är GridTableItemStyle.NumberType a 9 eller 10. Numret 9 kommer formatera 3% som 3% men numret 10 kommer formatera 3% som 3,00%.

{{% alert color="primary" %}} 

Om du inte har ställt in cellformatet till procentformat, kommer inmatningsdata 3% visas som 0,03.

{{% /alert %}} 
## **Ange celldata i GridWeb-arbetsblad i procentformat**
Följande exempelkod ställer in cell A1 GridTableItemStyle.NumberType som 10, därmed kommer inmatningsdata 3% automatiskt formateras som 3,00% som visas på skärmdumpen.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Exempelkod**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






