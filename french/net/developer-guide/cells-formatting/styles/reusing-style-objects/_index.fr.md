---
title: Réutilisation d'objets de style
description: Dans Aspose.Cells for .NET, en créant et en utilisant des objets de style réutilisables, vous pouvez simplifier la gestion des styles et améliorer l'efficacité du code. Notre guide vous aidera à tirer parti des avantages des objets de style réutilisables et à les implémenter dans votre application.
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
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

 Parce que le[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Cette approche utilise beaucoup moins de mémoire et est efficace. L'ancienne propriété Cell.Style, qui consommait beaucoup de mémoire inutile, a été supprimée avec la sortie de Aspose.Cells 7.1.0.

{{% /alert %}}
