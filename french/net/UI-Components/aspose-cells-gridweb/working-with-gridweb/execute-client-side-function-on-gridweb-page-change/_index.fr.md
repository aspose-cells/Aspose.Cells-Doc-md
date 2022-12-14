---
title: Exécuter la fonction côté client lors du changement de page GridWeb
type: docs
weight: 140
url: /fr/net/execute-client-side-function-on-gridweb-page-change/
---
## **Scénarios d'utilisation possibles**
Parfois, vous devez exécuter votre fonction côté client lorsque la page GridWeb change. Aspose.Cells.GridWeb fournit la propriété OnPageChangeClientFunction à cet effet. Veuillez définir cette propriété avec la fonction côté client que vous souhaitez exécuter.
## **Exécuter la fonction côté client lors du changement de page GridWeb**
Le balisage aspx suivant explique comment utiliser la propriété OnPageChangeClientFunction. Il définit la propriété avec la fonction côté client nommée MyOnPageChange. Veuillez noter que cette propriété n'est valide que si vous avez activé la pagination, c'est-à-dire EnablePaging="true". Maintenant, chaque fois que vous changerez la page GridWeb, elle appellera la fonction côté client MyOnPageChange qui imprime le**index de la page courante** sur le**console** comme le montre cette capture d'écran.

![tâche : image_autre_texte](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exemple de code**
Il s'agit du code de la fonction côté client MyOnPageChange qui sera exécutée en raison de la définition de la propriété OnPageChangeClientFunction ="MyOnPageChange" dans GridWeb. Ceci est le balisage complet de la page aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
