---
title: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 300
url: /sv/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen**

Aspose.Cells för Python via .NET kan användas för att lägga till anpassade egenskaper i arbetsbokens objekt som är synliga i dokumentinformationen. Du kan öppna dokumentinformationspanelen i Microsoft Excel med kommandona Arkiv > Info > Egenskaper > Visa dokumentpanel.

Använd [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add)-metoden för att lägga till en anpassad egenskap som kommer att vara synlig i dokumentinformationspanelen.

Följande exempelkod lägger till två anpassade egenskaper. Den första egenskapen är utan någon typ och den andra egenskapen har en typ som DateTime. När du öppnar den genererade Excel-filen med denna kod kommer du att se dessa två egenskaper i dokumentinformationspanelen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

- [Använd anpassade XML-delsar i Aspose.Cells](/cells/sv/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
