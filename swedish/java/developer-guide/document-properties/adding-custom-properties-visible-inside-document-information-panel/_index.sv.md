---
title: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 500
url: /sv/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells kan användas för att lägga till anpassade egenskaper i arbetsboksobjektet som är synliga i dokumentinformationspanelen. Du kan öppna dokumentinformationspanelen i Microsoft Excel med hjälp av menyn Fil > Information > Egenskaper > Visa dokumentpanelkommandon.

Använd [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) metoden för att lägga till en anpassad egenskap som kommer att vara synlig i dokumentinformationspanelen

{{% /alert %}}

## **Exempel**

Följande exempelkod lägger till två anpassade egenskaper. Den första egenskapen är utan någon typ och den andra egenskapen har en typ som DateTime. När du öppnar den genererade Excel-filen med denna kod kommer du att se dessa två egenskaper i dokumentinformationspanelen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Relaterad artikel**

{{% alert color="primary" %}}

- [Användning av anpassade XML-dels i Aspose.Cells](/cells/sv/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
