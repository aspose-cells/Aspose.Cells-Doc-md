---
title: Ajouter des signets PDF
type: docs
weight: 10
url: /fr/python-net/add-pdf-bookmarks/
description: Apprenez comment ajouter des signets PDF avec l API Aspose.Cells pour Python via .NET.
keywords: Ajouter des signets PDF en Python, ajouter des signets PDF en Pyton via NET, insérer des signets PDF
---

{{% alert color="primary" %}}

Cet article fournit des informations sur la façon d'insérer des signets PDF lors de la conversion d'une feuille de calcul en PDF.

Aspose.Cells pour Python via .NET vous permet d'ajouter des signets à la volée. Les signets PDF peuvent améliorer considérablement la navigabilité des documents longs. Lorsque vous ajoutez des liens de signet à un document PDF, vous pouvez avoir un contrôle précis sur la vue exacte que vous souhaitez, vous n'êtes pas limité à un simple lien vers une page. Vous pouvez définir la vue précise en positionnant la page cible, puis créer le signet.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant pour savoir comment ajouter des signets PDF. Le code génère un classeur simple, spécifie des signets PDF avec des emplacements de destination et génère le fichier PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes des formules sont actualisées et rendues correctement au format PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
