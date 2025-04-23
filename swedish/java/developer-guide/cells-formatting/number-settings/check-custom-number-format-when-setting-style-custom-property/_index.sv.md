---
title: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
type: docs
weight: 160
url: /sv/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ogiltigt anpassat nummerformat till [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) egenskapen kommer Aspose.Cells inte att kasta något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, vänligen ställ in [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) egenskapen till **true**.

## **Kontrollera det anpassade nummerformatet när du ställer in Style.Custom-egenskapen**

Det följande kodexemplet tilldelar ett ogiltigt anpassat nummerformat till [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) egenskapen. Eftersom vi redan har ställt in [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) egenskapen till **true**, kommer API:et att kasta CellsException t.ex. *Ogiltigt nummerformat*.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
