---
title: Sök data med hjälp av ursprungliga värden
type: docs
weight: 380
url: /sv/net/search-data-using-original-values/
description: Lär dig hur man söker data med ursprungliga värden genom API Aspose.Cells for .NET.
keywords: Sök data med ursprungliga värden, Hitta data med ursprungliga värden, Sök data efter ursprungliga värden, Hitta data enligt ursprungliga värden
---

{{% alert color="primary" %}}

Ibland är värdet på datan dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln = Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells genom att använda [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

Följande exempelkod illustrerar ovanstående. Den hittar cell D4 som inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med hjälp av [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Läs kommentarerna i koden för mer information.

## C# kod för att söka data med ursprungliga värden

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Konsolutdata som genereras av exempelkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
