---
title: Ställa in delad formel
type: docs
weight: 10
url: /sv/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

Anta att du har ett kalkylblad fyllt med data i formatet som ser ut som följande exempelkalkylblad.

**Indatafil med en kolumn eller data** 

![todo:image_alt_text](setting-shared-formula_1.png)

 Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första raden med data. Skatten är**9%** Formeln som beräknar momsen är:**"=A2*0,09"**. Den här artikeln förklarar hur du använder den här formeln med Aspose.Cells.

{{% /alert %}} 

 Aspose.Cells låter dig ange en formel med hjälp av[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) egendom, närmare bestämt[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) och[Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, och så vidare) i kolumnen.

Gör antingen som du gjorde för den första cellen, ställ in formeln för varje cell och uppdatera cellreferensen därefter (A3*0,09, A4*0,09, A5*0,09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också Aspose.Cells för att analysera varje formel individuellt, vilket kan vara tidskrävande för stora kalkylblad och komplexa formler. Det lägger också till extra rader med koder även om loopar kan skära ner dem något.

 Ett annat tillvägagångssätt är att använda en**delad formel** Med en delad formel uppdateras formlerna automatiskt för cellreferenserna i varje rad så att skatten skulle beräknas korrekt. De[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) metoden är effektivare än den första metoden.

Följande exempel visar hur man använder det. Skärmdumpen nedan visar utdatafilen.

**Utdatafil: delad formel tillämpas** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
