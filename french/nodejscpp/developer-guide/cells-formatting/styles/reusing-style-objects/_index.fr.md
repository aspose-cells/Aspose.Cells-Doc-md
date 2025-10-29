---  
title: Réutilisation d objets de style
linktitle: Réutilisation d objets de style  
description: Dans Aspose.Cells for Node.js via C++, en créant et en utilisant des objets de style réutilisables, vous pouvez simplifier la gestion des styles et améliorer l efficacité du code. Notre guide vous aidera à exploiter les avantages des objets de style réutilisables et à les mettre en œuvre dans votre application.  
keywords: Aspose.Cells for Node.js via C++, Réutilisation d Objets de Style, Gestion des Styles, Efficacité du Code, Styles Réutilisables, Développement d Applications, Référence API, Exemple de Code, Télécharger, Support.  
type: docs  
weight: 3000  
url: /fr/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
La réutilisation d'objets de style peut économiser de la mémoire et rendre un programme plus rapide.  
{{% /alert %}}  

Pour appliquer une mise en forme à une grande plage de cellules dans une feuille de calcul :

1. Créer un objet de style.
1. Spécifier les attributs.
1. Appliquer le style aux cellules dans la plage.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
Parce que l'approche [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) utilise beaucoup moins de mémoire, et est efficace, l'ancienne propriété Cell.style qui consommait beaucoup de mémoire inutile a été supprimée avec la sortie de Aspose.Cells 7.1.0.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
