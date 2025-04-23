---
title: Changements de l API publique dans Aspose.Cells 8.2.1
type: docs
weight: 90
url: /fr/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.2.0 à la version 8.2.1, qui peuvent être d'intérêt pour les développeurs de modules/applications. Il inclut non seulement de nouvelles méthodes publiques et mises à jour, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **Méthode getValidation() ajoutée pour la classe Cell**
La validation des données est l'une des fonctionnalités que les concepteurs de feuilles de calcul utilisent pour empêcher les utilisateurs d'insérer des valeurs non valides dans une cellule particulière. Avec Aspose.Cells for Java 8.2.1, l'API a exposé un mécanisme simple qui identifie si une validation des données a été appliquée sur une cellule. Utilisez la méthode getValidation de la classe Cell pour acquérir toute validation appliquée. S'il n'y a pas de validation, la méthode retourne null. De même, vous pouvez utiliser la méthode getValidationInCell de la classe ValidationCollection pour acquérir la validation appliquée sur une cellule en fournissant ses indices de ligne et de colonne.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Obtenir la validation appliquée sur une cellule](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) pour plus d'informations.

{{% /alert %}}
## **Méthode getValidationValue() ajoutée pour la classe Cell**
En plus de déterminer si une validation a été appliquée, vous pouvez également vérifier si une valeur donnée satisfait les règles de validation des données pour une cellule particulière. Cette fonctionnalité est utile dans les scénarios où vous souhaitez vérifier si la valeur saisie dans la cellule satisfait les règles de validation des données en direct. L'API Aspose.Cells a exposé la méthode getValidationValue pour la classe Cell. Si la valeur saisie dans une cellule ne satisfait pas les règles de validation des données, la méthode getValidationValue pour la classe Cell retourne false.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Vérifier si la valeur de la cellule satisfait les règles de validation des données](/cells/fr/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Méthode de surcharge toPrinter(PrinterSettings printerSettings) ajoutée pour la classe WorkbookRender**
Vous pouvez utiliser la méthode surchargée pour rendre le classeur sur l'imprimante via PrinterSettings.
{{< app/cells/assistant language="java" >}}
