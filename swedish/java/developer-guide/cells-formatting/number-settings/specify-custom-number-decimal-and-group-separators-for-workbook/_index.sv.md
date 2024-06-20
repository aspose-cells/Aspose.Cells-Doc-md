---
title: Ange anpassade decimal och grupptalsavskiljare för arbetsboken
type: docs
weight: 100
url: /sv/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Denna artikel visar hur du ändrar decimal och gruppavskiljare i MS Excel och med Java kod med användning av Aspose.Cells for Java API.
keywords: ange anpassade decimalavskiljare excel, ange anpassade decimalavskiljare excel java, ange anpassad gruppavskiljare excel, ange anpassad gruppavskiljare excel java, ange anpassade decimal och gruppavskiljare excel, ange anpassade decimal och gruppavskiljare excel java, ändra decimal och gruppavskiljare excel java, ändra decimal och gruppavskiljare excel, ändra decimalavskiljare excel, ändra decimalavskiljare excel java, ändra gruppavskiljare excel, ändra gruppavskiljare excel java
---

{{% alert color="primary" %}}

I Microsoft Excel kan du ange anpassade decimal- och tusentalsavskiljare istället för att använda systemavskiljare från **Avancerade Excel-alternativ** enligt skärmbilden nedan.

Aspose.Cells tillhandahåller egenskaperna [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) och [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) för att ange anpassade avskiljare för formatering/parsning av nummer.

{{% /alert %}}

## **Ange anpassade avskiljare i Microsoft Excel**

1. Öppna **Alternativ** i fliken **Arkiv**.
1. Öppna fliken **Avancerat**.
1. Ändra inställningarna i avsnittet **Redigering**.

Följande skärmbild visar **Avancerade Excel-alternativ** och markerar avsnittet för att ange **Anpassade avskiljare**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Ange anpassade avskiljare med Aspose.Cells**

Följande kodexempel illustrerar hur man anger anpassade avgränsare med Aspose.Cells API. Det anger egna decimal- och gruppavgränsare som punkt och mellanslag. Så kommer numret **123,456.789** att visas som **123 456.789** som visas i skärmbilden som visar den genererade PDF av koden.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
