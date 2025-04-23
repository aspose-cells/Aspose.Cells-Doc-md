---
title: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 300
url: /sv/net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen**

Aspose.Cells kan användas för att lägga till anpassade egenskaper i arbetsboksobjektet som är synliga i dokumentinformationspanelen. Du kan öppna dokumentinformationspanelen i Microsoft Excel med hjälp av menyn Fil > Information > Egenskaper > Visa dokumentpanelkommandon.

Använd [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)-metoden för att lägga till en anpassad egenskap som kommer att vara synlig i dokumentinformationspanelen.

Följande exempelkod lägger till två anpassade egenskaper. Den första egenskapen är utan någon typ och den andra egenskapen har en typ som DateTime. När du öppnar den genererade Excel-filen med denna kod kommer du att se dessa två egenskaper i dokumentinformationspanelen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddingCustomPropertiesVisible-1.cs" >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

- [Använd anpassade XML-delsar i Aspose.Cells](/cells/sv/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
