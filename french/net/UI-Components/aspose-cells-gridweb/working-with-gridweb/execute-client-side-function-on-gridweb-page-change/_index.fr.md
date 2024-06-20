---
title: Exécuter une fonction côté client lors du changement de page de GridWeb
type: docs
weight: 140
url: /fr/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Cet article présente comment travailler avec la fonction js client dans GridWeb.
---

## **Scénarios d'utilisation possibles**
Parfois, vous avez besoin d'exécuter votre fonction côté client lorsque la page de GridWeb change. Aspose.Cells.GridWeb fournit la propriété OnPageChangeClientFunction à cette fin. Veuillez définir cette propriété avec la fonction côté client que vous souhaitez exécuter.
## **Exécuter une fonction côté client lors du changement de page de GridWeb**
Le balisage aspx suivant explique comment utiliser la propriété OnPageChangeClientFunction. Il définit la propriété avec la fonction côté client nommée MyOnPageChange. Veuillez noter que cette propriété est valide uniquement si vous avez activé la pagination, c'est-à-dire EnablePaging="true". Désormais, chaque fois que vous changerez la page GridWeb, il appellera la fonction côté client MyOnPageChange qui imprime l'**indice de page actuel** sur la **console** comme le montre cette capture d'écran.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Code d'exemple**
Voici le code de la fonction côté client MyOnPageChange qui sera exécutée en raison du paramètre OnPageChangeClientFunction ="MyOnPageChange" dans GridWeb. Il s'agit du balisage complet de la page aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
