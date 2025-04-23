---
title: Changements de l API publique dans Aspose.Cells 8.2.1
type: docs
weight: 80
url: /fr/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.2.0 à la version 8.2.1, qui peuvent être d'intérêt pour les développeurs de modules/applications. Il inclut non seulement de nouvelles méthodes publiques et mises à jour, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **Méthode GetValidation() ajoutée pour la classe Cell**
La validation des données est l'une des fonctionnalités que les concepteurs de feuilles de calcul utilisent pour empêcher les utilisateurs d'insérer des valeurs invalides dans une cellule particulière. Avec Aspose.Cells for .NET 8.2.1, l'API a exposé un mécanisme simple qui identifie si une validation des données a été appliquée sur une cellule. Utilisez la méthode GetValidation de la classe Cell pour récupérer toute validation appliquée. S'il n'y a pas de validation, la méthode renvoie null. De même, vous pouvez utiliser la méthode GetValidationInCell de la classe ValidationCollection pour récupérer la validation appliquée sur une cellule en fournissant ses indices de ligne et de colonne.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Obtenir la validation appliquée sur une cellule](/cells/fr/net/get-validation-applied-on-a-cell/) pour plus d'informations.

{{% /alert %}}
## **Ajout de la méthode GetValidationValue() pour la classe Cell**
En plus de déterminer si une validation a été appliquée, vous pouvez également vérifier si une valeur donnée satisfait les règles de validation des données pour une cellule particulière. Cette fonctionnalité est utile dans les scénarios où vous souhaitez vérifier si la valeur entrée dans la cellule satisfait les règles de validation des données sur le vol. L'API Aspose.Cells a exposé la méthode GetValidationValue pour la classe Cell. Si la valeur entrée dans une cellule ne satisfait pas les règles de validation des données, la méthode GetValidationValue pour la classe Cell renvoie false.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Vérifiez si la valeur de la cellule satisfait les règles de validation des données](/cells/fr/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Ajout de la méthode de surcharge ToPrinter(PrinterSettings) pour la classe WorkbookRender**
Vous pouvez utiliser la méthode surchargée pour rendre le classeur sur l'imprimante via PrinterSettings.
{{< app/cells/assistant language="csharp" >}}
