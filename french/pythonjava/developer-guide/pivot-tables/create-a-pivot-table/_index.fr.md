---
title: Créer un tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-java/create-a-pivot-table/
---
## **Créer un tableau croisé dynamique**
Aspose.Cells for Python via Java fournit la fonctionnalité pour créer des tableaux croisés dynamiques. Pour créer un tableau croisé dynamique à l'aide du Aspose.Cells, veuillez suivre les étapes ci-dessous :

1. Ajoutez des données aux cellules de la feuille de calcul à l'aide de la[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)objets[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)propriété. Ces données seront utilisées comme source de données pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant le[Collection de tableaux croisés dynamiques](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[ajouter](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)), encapsulée dans la méthode[Feuille de travail](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)objet.
1. Accéder au[Tableau croisé dynamique](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)objet de la[Collection de tableaux croisés dynamiques](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)en passant le[Tableau croisé dynamique](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)indice.
1. Utilisez n'importe lequel des objets de tableau croisé dynamique (expliqués ci-dessus) encapsulés dans le[Collection de tableaux croisés dynamiques](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)objet pour gérer le tableau croisé dynamique.

L'extrait de code suivant illustre la création d'un tableau croisé dynamique avec le Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
