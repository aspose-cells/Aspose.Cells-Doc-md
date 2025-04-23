---
title: Définir des en têtes et des pieds de page différents pour différentes pages
type: docs
weight: 35
url: /fr/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Cet article fournit un code d exemple qui montre comment définir de manière programmatique divers en têtes et pieds de page des paramètres de configuration de la page de la feuille de calcul Excel en utilisant la bibliothèque C# et l API .NET. Vous pouvez définir les en têtes et les pieds de page pour la première page, les pages impaires et les pages paires.
keywords: définir l en tête Excel pieds de page première page c#, définir l en tête Excel pieds de page pages impaires c#, définir l en tête Excel pieds de page pages paires c#
---

{{% alert color="primary" %}}

MS Excel prend en charge le paramétrage de différents en-têtes et pieds de page pour la première page, les pages impaires et les pages paires depuis Excel 2007.
Aspose.Cells prend en charge la même fonctionnalité.

{{% /alert %}}

## **Définir des en-têtes et des pieds de page différents dans MS Excel**

**![Définir des en-têtes et des pieds de page différents](difpage.png)**

1. Cliquez sur **Mise en page > Titres et en-têtes > En-tête/pied de page**.
1. Cochez **Pages impaires et paires différentes** ou **Différent sur la première page**.
1. Entrez des en-têtes et pieds de page différents.

## **Définir des en-têtes et pieds de page différents avec Aspose.Cells**

Aspose.Cells se comporte de la même manière qu'Excel.
1. Définit les indicateurs [PageSetup.IsHFDiffOddEven]( https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) et [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Entrez des en-têtes et pieds de page différents.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
