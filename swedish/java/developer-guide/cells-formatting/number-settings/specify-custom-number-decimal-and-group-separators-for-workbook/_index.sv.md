---
title: Ange anpassade nummerdecimaler och gruppavgränsare för arbetsbok
type: docs
weight: 100
url: /sv/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Den här artikeln visar hur du ändrar nummerdecimal och gruppavgränsare i MS Excel och med Java-koden genom att använda Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 I Microsoft Excel kan du ange anpassade decimaler och tusentals avgränsare istället för att använda systemavgränsare från**Avancerade Excel-alternativ** som visas i skärmdumpen nedan.

 Aspose.Cells tillhandahåller[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) och[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) egenskaper för att ställa in anpassade avgränsare för formatering/analys av tal.

{{% /alert %}}

## **Ange anpassade avgränsare med Microsoft Excel**

1.  Öppen**alternativ** i**Fil** flik.
1. Öppna**Avancerad** flik.
1.  Ändra inställningarna i**Redigeringsalternativ** sektion.

Följande skärmdump visar**Avancerade Excel-alternativ** och markerar avsnittet för att ange**Anpassade separatorer**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Ange anpassade avskiljare med Aspose.Cells**

 Följande exempelkod illustrerar hur man anger anpassade avgränsare med Aspose.Cells API. Den anger anpassade nummerdecimaler och gruppseparatorer som punkt respektive mellanslag. Alltså numret**123,456.789** kommer att visas som**123 456.789** som visas i skärmdumpen som visar utdata PDF som genereras av koden.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
