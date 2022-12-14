---
title: Public API Changements dans Aspose.Cells 8.2.0
type: docs
weight: 80
url: /fr/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.1.2 à 8.2.0, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la propriété MultiThreadReading pour la classe Cells**
Avec Aspose.Cells for Java 8.2.0, la propriété MultiThreadReading a été ajoutée à la classe Cells afin de fournir un mécanisme plus robuste pour lire les valeurs des cellules avec plusieurs threads simultanément. La définition de la propriété Boolean type sur true dans l'application multithread garantit que chaque thread recevra la valeur de cellule correcte.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Lire simultanément les valeurs Cells dans un environnement multithread](/cells/fr/java/reading-cell-values-in-multiple-threads-simultaneously/) pour plus d'informations.

{{% /alert %}}
## **Ajout de surcharges pour les méthodes autoFitRows et autoFitColumns**
 De nouvelles surcharges pour autoFitRows et autoFitColumns ont été ajoutées à la classe Worksheet, permettant aux développeurs d'adapter automatiquement les lignes et les colonnes en fonction de leurs plages respectives tout en transmettant une instance de la classe AutoFitterOptions.

Les signatures des procédés précités sont les suivantes :

1. autoFitRows(int startRow, int endRow, options AutoFitterOptions)
1. autoFitColumns(int firstColumn, int lastColumn, options AutoFitterOptions)

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Ajustement automatique des lignes et des colonnes](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
