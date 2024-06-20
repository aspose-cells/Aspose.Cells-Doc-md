---
title: Modifications de l’API publique dans Aspose.Cells 8.2.0
type: docs
weight: 80
url: /fr/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.1.2 à la 8.2.0, qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et de méthodes publiques mises à jour, mais également une description de tout changement de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **Propriété MultiThreadReading ajoutée pour la classe Cells**
Avec Aspose.Cells for Java 8.2.0, la propriété MultiThreadReading a été ajoutée à la classe Cells afin de fournir un mécanisme plus robuste pour lire simultanément les valeurs des cellules avec plusieurs threads. En définissant la propriété de type Boolean sur true dans l'application multi-threadée, chaque thread s'assurera de recevoir la valeur correcte des cellules.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Lecture simultanée des valeurs des cellules dans un environnement multi-threadé](/cells/fr/java/reading-cell-values-in-multiple-threads-simultaneously/) pour plus d'informations.

{{% /alert %}}
## **Ajout de surcharges pour les méthodes autoFitRows et autoFitColumns**
De nouvelles surcharges pour les méthodes autoFitRows et autoFitColumns ont été ajoutées à la classe Worksheet, permettant aux développeurs d'ajuster automatiquement les lignes et les colonnes en fonction de leurs plages respectives tout en passant une instance de la classe AutoFitterOptions. 

Les signatures des méthodes susmentionnées sont les suivantes :

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Ajuster automatiquement les lignes et les colonnes](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
