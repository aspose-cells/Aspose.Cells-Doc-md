---
title: Ajouter PDF Favoris
type: docs
weight: 10
url: /fr/python-net/add-pdf-bookmarks/
description: Apprenez à ajouter des signets PDF avec Aspose.Cells for Python via .NET API.
keywords: Python add pdf bookmarks, add pdf book marks Pyton via NET, insert pdf bookmarks
---
{{% alert color="primary" %}}

Cet article fournit des informations sur la façon d'insérer des signets PDF lors de la conversion d'une feuille de calcul en PDF.

Aspose.Cells for Python via .NET vous permet d'ajouter des favoris à la volée. Les signets PDF peuvent améliorer considérablement la navigabilité des documents longs. Lorsque vous ajoutez des liens de signets au document PDF, vous pouvez avoir un contrôle précis sur la vue exacte que vous souhaitez, vous n'êtes pas limité à créer un lien vers une page. Vous pouvez configurer la vue précise en positionnant la page cible, puis créer le signet.

{{% /alert %}}

Veuillez consulter l'exemple de code suivant pour savoir comment ajouter les signets PDF. Le code génère un classeur simple, spécifie les signets PDF avec les emplacements de destination et génère le fichier PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont actualisées et rendues correctement dans PDF.

{{% /alert %}}
