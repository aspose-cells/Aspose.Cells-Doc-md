---
title: Modifications de l’API publique dans Aspose.Cells 8.2.0
type: docs
weight: 70
url: /fr/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.1.2 à la 8.2.0, qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et de méthodes publiques mises à jour, mais également une description de tout changement de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **Propriété MultiThreadReading ajoutée pour la classe Cells**
Avec Aspose.Cells for .NET 8.2.0, la propriété MultiThreadReading a été ajoutée à la classe Cells afin de fournir un mécanisme plus robuste pour lire les valeurs des cellules avec plusieurs threads simultanément. En définissant la propriété de type booléen sur true dans l'application multi-thread, chaque thread recevra la valeur correcte des cellules.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Lecture simultanée des valeurs des cellules dans un environnement multi-thread](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) pour plus d'informations.

{{% /alert %}}
## **Ajout de surcharges pour les méthodes AutoFitRows & AutoFitColumns**
De nouvelles surcharges pour les méthodes AutoFitRows & AutoFitColumns ont été ajoutées à la classe Worksheet, permettant aux développeurs d'ajuster automatiquement les lignes & colonnes en fonction de leurs plages respectives tout en passant une instance de la classe AutoFitterOptions. 

Les signatures des méthodes susmentionnées sont les suivantes :

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Ajustement automatique des lignes et colonnes](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
