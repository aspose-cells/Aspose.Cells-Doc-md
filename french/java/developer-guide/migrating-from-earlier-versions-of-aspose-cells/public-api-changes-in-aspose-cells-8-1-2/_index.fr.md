---
title: Public API Changements dans Aspose.Cells 8.1.2
type: docs
weight: 70
url: /fr/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.1.1 à 8.1.2, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la prise en charge de l'avertissement en cas de substitution de police**
Avec Aspose.Cells for Java 8.1.2, les classes WarningInfo et WarningType, l'interface IWarningCallback et les propriétés SaveOptions.WarningCallback et ImageOrPrintOptions.WarningCallback ont été ajoutées pour permettre aux développeurs de recevoir des avertissements en cas de substitution de polices lors de la conversion de feuilles de calcul en images, formats XPS et PDF.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Obtenir des avertissements pour la substitution de polices lors du rendu des feuilles de calcul](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) pour plus d'informations.

{{% /alert %}}
## **Suppression de la propriété obsolète PdfSaveOptions.ChartImageType**
Aspose.Cells for Java 8.1.2 a supprimé la propriété obsolète PdfSaveOptions.ChartImageType du public API.
