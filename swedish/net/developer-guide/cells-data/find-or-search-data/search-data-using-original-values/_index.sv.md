---
title: Sök efter data med originalvärden
type: docs
weight: 380
url: /sv/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 Ibland döljs värdet av datan eftersom det är formaterat på något sätt. Anta till exempel att cell D4 har formeln =Sum(A1:A2) och dess värde är 20 men den är formaterad som ---, då är värdet 20 dolt och kan inte hittas med Microsoft Excel-sökalternativ. Du kan dock hitta den med Aspose.Cells med[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Följande exempelkod illustrerar punkten ovan. Den hittar cell D4 som inte kan hittas med Microsoft Excel-sökalternativ men Aspose.Cells kan hitta den med[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Läs kommentarerna i koden för mer information.

## C# kod för att söka data med hjälp av originalvärden

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Konsolutdata genererad av exempelkoden

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
