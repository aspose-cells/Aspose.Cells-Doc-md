---
title: Kontrollera Custom Number Format när du ställer in Style.Custom Property
type: docs
weight: 160
url: /sv/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Möjliga användningsscenarier**

 Om du tilldelar ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)egendom så kommer Aspose.Cells inte att ge något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ in[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) egendom till**Sann**.

## **Kontrollera Custom Number Format när du ställer in Style.Custom-egenskapen**

 Följande exempelkod tilldelar ett ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) fast egendom. Eftersom vi redan har satt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) egendom till**Sann** , därför kommer API:t att kasta CellsException t.ex*Ogiltigt nummerformat*.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
