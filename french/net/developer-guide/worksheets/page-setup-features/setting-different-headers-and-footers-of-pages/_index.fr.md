---
title: Définir différents en-têtes et pieds de page pour différentes pages
type: docs
weight: 35
url: /fr/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel prend en charge la définition de différents en-têtes et pieds de page pour la première page, les pages impaires et les pages paires depuis Excel 2007.
Aspose.Cells prend en charge la même fonctionnalité.

{{% /alert %}}

## **Définition de différents en-têtes et pieds de page dans MS Excel**

**![Définir différents en-têtes et pieds de page](difpage.png)**

1.  Cliquez sur**Mise en page > Imprimer les titres > En-tête/Pied de page**.
1.  Vérifier**Différentes pages paires et impaires** ou**Page de sapin différente**.
1. Entrez différents en-têtes et pieds de page.

## **Définition de différents en-têtes et pieds de page avec Aspose.Cells**

Aspose.Cells se comporte comme Excel.
1.  Définit les drapeaux[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) et[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Entrez différents en-têtes et pieds de page.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
