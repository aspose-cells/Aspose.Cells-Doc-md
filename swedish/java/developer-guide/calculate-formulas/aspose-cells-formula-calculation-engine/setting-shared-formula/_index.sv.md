---
title: Ange Delad Formel
type: docs
weight: 10
url: /sv/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

**Ingångsfil med en kolumn eller data** 

![todo:image_alt_text](setting-shared-formula_1.png)

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

{{% /alert %}} 

Aspose.Cells låter dig ange en formel med hjälp av egenskapen [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), specifikt [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) och [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Det finns två alternativ för att lägga till formler i de andra cellerna (B3, B4, B5, och så vidare) i kolumnen.

Gör antingen det du gjorde för den första cellen, effektivt sätta formeln för varje cell och uppdatera cellreferensen, (`A3*0.09`, `A4*0.09`, `A5*0.09` och så vidare). Detta kräver uppdatering av cellreferenserna för varje rad. Det kräver också att Aspose.Cells tolkar varje formel individuellt, vilket kan vara tidskrävande för stora kalkylblad och komplexa formler. Det lägger också till extra rader med kod även om loopar kan minska dem något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenserna i varje rad så att momsen beräknas korrekt. Metoden [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) är effektivare än den första metoden.

Följande exempel visar hur du använder det. Skärmbilden nedan visar utdatafilen.

**Utdatafil: delad formel tillämpad** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
