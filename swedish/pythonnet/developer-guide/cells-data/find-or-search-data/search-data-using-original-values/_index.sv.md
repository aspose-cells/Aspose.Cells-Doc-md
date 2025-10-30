---
title: Sök data med hjälp av ursprungliga värden
type: docs
weight: 380
url: /sv/python-net/search-data-using-original-values/
description: Lär dig hur du söker data med hjälp av ursprungliga värden genom Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Sök Data med ursprungliga värden, Hitta Data med ursprungliga värden, Sök Data efter ursprungliga värden i Python, Hitta Data med ursprungliga värden i Python
---

{{% alert color="primary" %}}

Ibland är värdet på datan dold eftersom den är formaterad på något sätt. Till exempel, anta att cell D4 har formeln =Sum(A1:A2) och dess värde är 20 men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells for Python via .NET genom att använda [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype).

{{% /alert %}}

Följande exempelkod illustrerar ovanstående. Den hittar cell D4 som inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med hjälp av [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype). Läs kommentarerna i koden för mer information.

## Python-kod för att söka data med ursprungliga värden

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Konsolutdata som genereras av exempelkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
