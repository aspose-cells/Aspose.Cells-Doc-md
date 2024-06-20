---
title: Modifications de l’API publique dans Aspose.Cells 8.1.2
type: docs
weight: 60
url: /fr/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.1.1 à la 8.1.2, qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et de méthodes publiques mises à jour, mais également une description de tout changement de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **Ajout de prise en charge pour l'avertissement si une substitution de police de caractères se produit**
Avec Aspose.Cells for .NET 8.1.2, les classes WarningInfo, WarningType, l'interface IWarningCallback et les propriétés SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback ont été ajoutées pour permettre à l'utilisateur de recevoir un avertissement en cas de substitution de police lors de la conversion des feuilles de calcul en images ou en format PDF. 

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Obtention d'avertissements pour la substitution de police lors du rendu des feuilles de calcul](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Propriété PdfSaveOptions.ChartImageType obsolète supprimée**
Aspose.Cells for .NET 8.1.2 a supprimé la propriété obsolète PdfSaveOptions.ChartImageType de l'API publique.
