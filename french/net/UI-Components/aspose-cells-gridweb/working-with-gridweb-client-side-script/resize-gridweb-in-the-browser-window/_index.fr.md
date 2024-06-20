---
title: Redimensionnez GridWeb dans la fenêtre du navigateur
type: docs
weight: 40
url: /fr/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, redimensionner
description: Cet article présente comment redimensionner dans GridWeb.
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez qu'Aspose.Cells.GridWeb se redimensionne en fonction de la fenêtre du navigateur. Vous pourriez avoir besoin que GridWeb ajuste toujours sa taille (hauteur, largeur) et qu'il soit compatible avec la taille de la fenêtre du navigateur. Aspose.Cells.GridWeb fournit la fonction *resize()* côté client à cet effet. De plus, vous pouvez même rendre le contrôle GridWeb redimensionnable dans la fenêtre du navigateur. Par exemple, vous pouvez utiliser la poignée en bas à droite (avec la souris) pour personnaliser sa largeur/hauteur dans la fenêtre. Vous devez également inclure/spécifier les fichiers Javascript de jquery pour que cela fonctionne dans la source de la page de votre projet.
## **Utilisation de la méthode de redimensionnement de GridWeb**
Le code suivant vérifiera s'il y a eu une action de redimensionnement toutes les 100 millisecondes. Lorsqu'il n'y a plus d'action de redimensionnement, il considère que l'opération de redimensionnement est maintenant terminée. Nous utilisons un fichier de modèle d'exemple qui est importé dans GridWeb. Nous utilisons du code côté client pour redimensionner le GridWeb. La capture d'écran montre que GridWeb se redimensionne en conséquence lors du redimensionnement de la fenêtre du navigateur.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Rendre GridWeb redimensionnable en utilisant la fonctionnalité resizable de jquery ui**
Le code suivant rendra le contrôle GridWeb redimensionnable dans la fenêtre du navigateur. Par exemple, vous pouvez utiliser la poignée en bas à droite pour personnaliser la taille de GridWeb dans la fenêtre. Nous utilisons le même fichier de modèle qui est importé dans GridWeb d'abord. Nous utilisons des scripts jquery pour rendre le GridWeb redimensionnable. La capture d'écran montre que GridWeb a été redimensionné en utilisant sa poignée en bas à droite dans la fenêtre du navigateur.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
