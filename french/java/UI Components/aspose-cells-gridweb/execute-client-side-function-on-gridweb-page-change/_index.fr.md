---
title: Exécuter la fonction côté client lors du changement de page GridWeb
type: docs
weight: 70
url: /fr/java/execute-client-side-function-on-gridweb-page-change/
---
## **Scénarios d'utilisation possibles**
Parfois, vous devez exécuter votre fonction côté client lorsque la page GridWeb change. Aspose.Cells.GridWeb fournit la propriété OnPageChangeClientFunction à cet effet. Veuillez définir cette propriété avec la fonction côté client que vous souhaitez exécuter.
## **Exécuter la fonction côté client lors du changement de page GridWeb**
Le code Java suivant explique comment utiliser la propriété GridWebBean.setOnPageChangeClientFunction(). Il définit la propriété avec la fonction côté client nommée MyOnPageChange. Veuillez noter que cette propriété n'est valide que si vous avez activé la pagination, c'est-à-dire GridWebBean.setEnablePaging(true). Maintenant, chaque fois que vous changerez la page GridWeb, elle appellera la fonction côté client MyOnPageChange qui imprime le**index de la page courante** sur le**console** comme le montre cette capture d'écran.

![tâche : image_autre_texte](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exemple de code**
Il s'agit du code de la fonction côté client MyOnPageChange qui sera exécutée à cause de cette ligne, c'est-à-dire Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Le code suivant explique comment activer la pagination et définir la propriété OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
