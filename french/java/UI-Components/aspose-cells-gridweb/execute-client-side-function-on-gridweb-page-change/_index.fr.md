---
title: Exécuter une fonction côté client lors du changement de page de GridWeb
type: docs
weight: 70
url: /fr/java/execute-client-side-function-on-gridweb-page-change/
---

## **Scénarios d'utilisation possibles**
Parfois, vous avez besoin d'exécuter votre fonction côté client lorsque la page de GridWeb change. Aspose.Cells.GridWeb fournit la propriété OnPageChangeClientFunction à cette fin. Veuillez définir cette propriété avec la fonction côté client que vous souhaitez exécuter.
## **Exécuter une fonction côté client lors du changement de page de GridWeb**
Le code java suivant explique comment utiliser la propriété GridWebBean.setOnPageChangeClientFunction(). Il définit la propriété avec la fonction côté client nommée MyOnPageChange. Veuillez noter que cette propriété est valide uniquement si vous avez activé la pagination, c'est-à-dire GridWebBean.setEnablePaging(true). Désormais, à chaque changement de page de GridWeb, il appellera la fonction côté client MyOnPageChange qui affiche l'**index de page actuel** sur la **console** comme le montre cette capture d'écran.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Code d'exemple**
Ceci est le code de la fonction côté client MyOnPageChange qui sera exécutée à cause de cette ligne, c'est-à-dire Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Le code suivant explique comment activer la pagination et définir la propriété OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
