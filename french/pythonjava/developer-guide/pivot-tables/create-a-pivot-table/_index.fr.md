---
title: Créer un tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-java/create-a-pivot-table/
---

## **Créer un tableau croisé dynamique**
Aspose.Cells for Python via Java offre la possibilité de créer des tableaux croisés dynamiques. Pour créer un tableau croisé dynamique avec Aspose.Cells, suivez les étapes ci-dessous :

1. Ajoutez des données aux cellules de la feuille de calcul en utilisant la propriété [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) de l'objet [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell). Ces données seront utilisées comme source de données pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) de la collection [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), encapsulée dans l'objet [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet).
1. Accédez à l'objet [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) dans la [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) en utilisant l'index du [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable).
1. Utilisez l'un des objets de tableau croisé dynamique (expliqués ci-dessus) encapsulés dans la [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) pour gérer le tableau croisé dynamique.

Le code suivant montre comment créer un tableau croisé dynamique avec l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
