---
title: Redimensionner GridWeb dans la fenêtre du navigateur
type: docs
weight: 40
url: /fr/net/resize-gridweb-in-the-browser-window/
---
## **Scénarios d'utilisation possibles**
Parfois, vous voulez que Aspose.Cells. GridWeb se redimensionne en fonction de la fenêtre du navigateur. Vous pourriez avoir besoin que GridWeb ajuste toujours sa taille (hauteur, largeur) et soit compatible avec la taille de la fenêtre du navigateur. Aspose.Cells.GridWeb fournit côté client*redimensionner()* fonction à cet effet. De plus, vous pouvez même rendre le contrôle GridWeb redimensionnable dans la fenêtre du navigateur. Par exemple, vous pouvez utiliser la poignée en bas à droite (via la souris) pour personnaliser sa largeur/hauteur dans la fenêtre. Vous devez également inclure/spécifier les fichiers Javascript jquery pour le faire fonctionner dans la source de la page de votre projet.
## **Utilisation de la méthode de redimensionnement de GridWeb**
Le code suivant vérifiera si une action de redimensionnement a lieu toutes les 100 millisecondes. Lorsqu'il n'y a plus d'action de redimensionnement, il pense que l'opération de redimensionnement est maintenant terminée. Nous utilisons un exemple de fichier modèle qui est importé dans GridWeb. Nous utilisons du code côté client pour redimensionner le GridWeb. La capture d'écran montre que GridWeb se redimensionne en conséquence lors du redimensionnement de la fenêtre du navigateur.

![tâche : image_autre_texte](resize-gridweb-in-the-browser-window_1.png)
### **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Rendre GridWeb redimensionnable à l'aide de la fonction d'interface utilisateur jquery redimensionnable**
Le code suivant rendra le contrôle GridWeb redimensionnable dans la fenêtre du navigateur. Par exemple, vous pouvez utiliser la poignée en bas à droite pour personnaliser sa taille de GridWeb dans la fenêtre. Nous utilisons le même fichier modèle qui est d'abord importé dans GridWeb. Nous utilisons des scripts jquery pour rendre le GridWeb redimensionnable. La capture d'écran montre que GridWeb a été redimensionné à l'aide de sa poignée en bas à droite dans la fenêtre du navigateur.

![tâche : image_autre_texte](resize-gridweb-in-the-browser-window_2.png)
### **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
