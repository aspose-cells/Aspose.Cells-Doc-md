---
title: Convertir un tableau Excel en une plage de données
type: docs
weight: 10
url: /fr/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Convertir un tableau Excel en une plage de données**
Aspose.Cells for Python via Java offre la possibilité de convertir le tableau Excel en une plage de données. Pour cela, le API fournit le[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) méthode. L'extrait de code suivant illustre l'utilisation de[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) pour convertir un tableau Excel en une plage de données.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convertir un tableau Excel en une plage avec des options**
Vous pouvez fournir des options supplémentaires lors de la conversion d'un tableau en une plage avec le[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) classe. Vous pouvez passer une instance de[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)classe à la[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) pour spécifier des options supplémentaires. L'extrait de code suivant illustre l'utilisation de[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)class pour définir le dernier index de ligne de la table. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
