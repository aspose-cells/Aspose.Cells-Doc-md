---
title: Comment ajouter une caméra pour la plage
type: docs
weight: 10
url: /fr/net/how-to-add-camera-for-range/
description: Cet article présentera comment ajouter une caméra pour le contenu de plage via l’API Aspose.Cells for .NET.
keywords: Comment utiliser la fonction Caméra, Comment ajouter une caméra pour le contenu de plage, Comment utiliser l’outil Caméra, Fonction Caméra dans Excel, Comment utiliser la fonction Caméra dans Aspose.Cells for .NET
---

## **Scénarios d'utilisation possibles**
L’outil Caméra dans Excel est une fonctionnalité cachée mais puissante qui vous permet de créer une capture instantanée en direct et liée à n’importe quelle plage de cellules. Voici pourquoi et quand l’utiliser.

Ce que fait l’outil Caméra :
1. Prend une « photo » d’une plage de cellules sélectionnée.
2. La « photo » est un lien en direct — si les cellules sources changent, l’image se met à jour automatiquement.
3. Vous pouvez déplacer ou redimensionner l’image n’importe où sur la feuille ou même vers une autre feuille.


## **Comment utiliser la fonction Caméra dans Excel**
Voici un guide étape par étape pour utiliser l’outil Caméra dans Excel — un moyen puissant de créer des images dynamiques et en direct des plages de cellules.

### Activer l’outil Caméra

L’outil Caméra est masqué par défaut. Voici comment l’ajouter :

1. Cliquez sur la flèche vers le bas dans la Barre d’outils Accès rapide (coin supérieur gauche d’Excel).
2. Sélectionnez Plus de commandes...
3. Dans la boîte de dialogue : Dans le menu déroulant « Choisir les commandes dans », sélectionnez Commandes non dans le ruban. Faites défiler vers le bas et sélectionnez Caméra. Cliquez sur Ajouter >> pour l’ajouter à la barre d’outils.
4. Cliquez sur OK. Vous verrez maintenant une petite icône de caméra dans votre barre d’outils.

### Utiliser l’outil Caméra
1. Sélectionnez la plage de cellules que vous souhaitez capturer (par exemple, A1:C5).
2. Cliquez sur l’icône de la Caméra dans la barre d’accès rapide.
3. Votre curseur changera en une croix. 
4. Cliquez n'importe où dans la feuille de calcul où vous souhaitez placer l'image. Une image en direct de la plage sélectionnée est insérée. 

### Liaison dynamique
L'image est liée aux cellules d'origine. Si les valeurs ou la mise en forme de la plage source changent, l'image se met à jour automatiquement. 


## **Comment ajouter une caméra pour une plage dans Aspose.Cells for .NET**
Aspose.Cells prend en charge l'affichage du contenu d'une cellule ou d'une plage dans une forme d'image. Vous pouvez lier l'image à la cellule ou à la plage contenant les données que vous souhaitez afficher. Étant donné que la cellule ou la plage est liée à l'objet graphique, les modifications que vous apportez aux données de cette cellule ou plage apparaissent automatiquement dans l'objet graphique.  

Voici un exemple simple de comment utiliser la fonction caméra en utilisant [fichier d'exemple](camera.xlsx) dans Aspose.Cells for .NET :

1. Chargez le fichier d'exemple en utilisant la classe [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook).
1. Ajoutez une image à la feuille de calcul en appelant la méthode [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). 
1. Spécifiez la plage de cellules en utilisant l'attribut [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) de l'objet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).
1. Mettez à jour la valeur sélectionnée des formes dans la feuille de calcul. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Résultat de sortie**
La capture d'écran suivante montre la caméra de la plage (A1:E12) créée par Aspose.Cells for .NET dans le fichier Excel de sortie. 
<br>
Avant l'ajout de données :
<br>
<img src="1.png" width=70% />
<br>
Après l'ajout de données :
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
