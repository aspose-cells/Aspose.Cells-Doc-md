---
title: Modifications de l’API publique dans Aspose.Cells 8.1.2
type: docs
weight: 70
url: /fr/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.1.1 à la 8.1.2, qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et de méthodes publiques mises à jour, mais également une description de tout changement de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **Ajout de prise en charge pour l'avertissement si une substitution de police de caractères se produit**
Avec Aspose.Cells for Java 8.1.2, les classes WarningInfo et WarningType, l'interface IWarningCallback, et les propriétés SaveOptions.WarningCallback et ImageOrPrintOptions.WarningCallback ont été ajoutées pour permettre aux développeurs de recevoir des avertissements lorsque des substitutions de polices de caractères se produisent lors de la conversion des feuilles de calcul en images, XPS et PDF. 

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Obtention d'avertissements pour la substitution de police de caractères lors du rendu de feuilles de calcul](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) pour plus d'informations.

{{% /alert %}}
## **Propriété PdfSaveOptions.ChartImageType obsolète supprimée**
Aspose.Cells for Java 8.1.2 a supprimé la propriété obsolète PdfSaveOptions.ChartImageType de l'API publique.
{{< app/cells/assistant language="java" >}}
