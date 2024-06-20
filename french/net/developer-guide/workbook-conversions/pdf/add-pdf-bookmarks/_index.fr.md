---
title: Ajouter des signets PDF
type: docs
weight: 10
url: /fr/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

Cet article fournit des informations sur la façon d'insérer des signets PDF lors de la conversion d'une feuille de calcul en PDF.

Aspose.Cells vous permet d'ajouter des signets à la volée. Les signets PDF peuvent améliorer considérablement la navigabilité des documents longs. Lors de l'ajout de liens de signet au document PDF, vous pouvez avoir un contrôle précis sur la vue exacte que vous souhaitez, vous n'êtes pas limité à un lien vers une page. Vous pouvez configurer la vue précise en positionnant la page cible, puis créer le signet.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant pour savoir comment ajouter des signets PDF. Le code génère un classeur simple, spécifie des signets PDF avec des emplacements de destination et génère le fichier PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes des formules sont actualisées et rendues correctement au format PDF.

{{% /alert %}}
