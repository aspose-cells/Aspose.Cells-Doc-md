---
title: Renommer les feuilles de calcul
type: docs
weight: 40
url: /fr/net/rename-worksheets/
---
{{% alert color="primary" %}} 

Renommer une feuille de calcul peut être très utile lorsque vous travaillez avec de nombreuses feuilles de calcul dans Aspose.Cells.GridWeb et décidez de changer leurs noms pour les rendre plus significatifs. Par exemple, une feuille de calcul contenant une facture peut être renommée Facture au lieu de Feuille1. Cette rubrique décrit cette fonctionnalité simple mais utile.

{{% /alert %}} 
## **Renommer une feuille de calcul**
Toutes les feuilles de calcul contiennent une propriété Name qui permet aux développeurs d'accéder ou de modifier les noms des feuilles de calcul. Pour renommer une feuille de calcul :

1. Accédez à une feuille de calcul à partir de GridWorksheetCollection.
1. Renommer la feuille de calcul sélectionnée.



{{% alert color="primary" %}} 

 Pour plus de détails sur la façon d'accéder aux feuilles de calcul dans Aspose.Cells.GridWeb, veuillez vous référer à[Accéder aux feuilles de travail](/cells/fr/net/access-worksheets/).

{{% /alert %}} 

Avant d'exécuter le code, la feuille de calcul a un nom par défaut, tel que Sheet1.

**Fichier d'entrée : une feuille de calcul avec un nom par défaut Sheet1** 

![tâche : image_autre_texte](rename-worksheets_1.png)

Après avoir exécuté le code, la feuille de calcul est renommée Étudiants.

**Sortie : la feuille de calcul est renommée Étudiants** 

![tâche : image_autre_texte](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
