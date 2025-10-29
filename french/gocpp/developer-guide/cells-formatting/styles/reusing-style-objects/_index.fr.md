---
title: Réutilisation des objets Style avec Golang via C++
linktitle: Réutilisation d objets de style
description: Dans Aspose.Cells for C++, en créant et en utilisant des objets de style réutilisables, vous pouvez simplifier la gestion des styles et améliorer l efficacité du code. Notre guide vous aidera à exploiter les avantages des objets de style réutilisables et à les implémenter dans votre application.
keywords: Aspose.Cells for C++, Réutilisation des objets de style, Gestion des styles, Efficacité du code, Styles réutilisables, Développement d’applications, Référence API, Exemple de code, Téléchargement, Support.
type: docs
weight: 3000
url: /fr/go-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

La réutilisation d'objets de style peut économiser de la mémoire et rendre un programme plus rapide.

{{% /alert %}}

Pour appliquer une mise en forme à une grande plage de cellules dans une feuille de calcul :

1. Créer un objet de style.
1. Spécifier les attributs.
1. Appliquer le style aux cellules dans la plage.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReusingStyleObjects.go" >}}
{{% alert color="primary" %}}

Parce que l'approche [**Cell.GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) utilise beaucoup moins de mémoire et est efficace, l'ancienne propriété Cell.Style, qui consommait beaucoup de mémoire inutile, a été supprimée avec la version Aspose.Cells 7.1.0.

{{% /alert %}}
