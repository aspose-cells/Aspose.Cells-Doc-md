---
title: Ange celldata i GridWeb arbetsblad i procentformat
type: docs
weight: 80
url: /sv/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: Den här artikeln introducerar att ange celldata med procentformat i GridWeb.
---


## **Möjliga användningsscenario**
GridWeb stöder nu att användare anger celldata i procentformat som 3% och data i cellen formateras automatiskt som 3,00%. Du måste dock ställa in cellformatet. till procentformat vilket antingen är GridTableItemStyle.NumberType a 9 eller 10. Numret 9 kommer formatera 3% som 3% men numret 10 kommer formatera 3% som 3,00%.

{{% alert color="primary" %}} 

Om du inte har ställt in cellformatet till procentformat, kommer inmatningsdata 3% visas som 0,03.

{{% /alert %}} 
## **Ange celldata i GridWeb-arbetsblad i procentformat**
Följande exempelkod ställer in cell A1 GridTableItemStyle.NumberType som 10, därmed kommer inmatningsdata 3% automatiskt formateras som 3,00% som visas på skärmdumpen.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Exempelkod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
