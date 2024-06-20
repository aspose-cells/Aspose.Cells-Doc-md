---
title: Convertir un tableau Excel en une plage de données
type: docs
weight: 10
url: /fr/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Convertir un tableau Excel en une plage de données**
Aspose.Cells pour Python via Java offre la possibilité de convertir un tableau Excel en une plage de données. Pour cela, l'API fournit la méthode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). Le code suivant illustre l'utilisation de la méthode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) pour convertir un tableau Excel en une plage de données.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convertir un tableau Excel en plage avec des options**
Vous pouvez fournir des options supplémentaires lors de la conversion d'un tableau en plage avec la classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). Vous pouvez passer une instance de la classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) à la méthode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) pour spécifier des options supplémentaires. Le code suivant montre l'utilisation de la classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) pour définir l'index de la dernière ligne du tableau. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
