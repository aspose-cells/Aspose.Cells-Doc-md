---
title: Réutilisation des objets de style
type: docs
weight: 3000
url: /fr/net/reusing-style-objects/
---
{{% alert color="primary" %}}

La réutilisation d'objets de style peut économiser de la mémoire et rendre un programme plus rapide.

{{% /alert %}}

Pour appliquer une mise en forme à une large plage de cellules dans une feuille de calcul :

1. Créez un objet de style.
1. Spécifiez les attributs.
1. Appliquez le style aux cellules de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Parce que le[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) utilise beaucoup moins de mémoire et est efficace, l'ancienne propriété Cell.Style qui consommait beaucoup de mémoire inutile a été supprimée avec la version Aspose.Cells 7.1.0.

{{% /alert %}}
