---
title: Définir des en têtes et des pieds de page différents pour différentes pages
type: docs
weight: 35
url: /fr/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Cet article fournit un code d exemple montrant comment définir de manière programmatique divers en têtes et pieds de page de la configuration de la page d Excel en utilisant l API Aspose.Cells pour Python. Vous pouvez définir les en têtes et pieds de page pour la première page, les pages impaires et les pages paires.
keywords: Bibliothèque Excel en Python, définir l en tête et le pied de page de l Excel pour la première page, définir l en tête et le pied de page pour les pages impaires en Python, définir l en tête et le pied de page pour les pages paires en Python.
---

{{% alert color="primary" %}}

MS Excel prend en charge le paramétrage de différents en-têtes et pieds de page pour la première page, les pages impaires et les pages paires depuis Excel 2007.
Aspose.Cells pour Python via .NET prend en charge cette même fonctionnalité.

{{% /alert %}}

## **Comment définir différents en-têtes et pieds de page dans MS Excel**

**![Définir des en-têtes et des pieds de page différents](difpage.png)**

1. Cliquez sur **Mise en page > Titres et en-têtes > En-tête/pied de page**.
1. Cochez **Pages impaires et paires différentes** ou **Différent sur la première page**.
1. Entrez des en-têtes et pieds de page différents.

## **Comment définir différents en-têtes et pieds de page avec la bibliothèque Excel Aspose.Cells pour Python**

Aspose.Cells pour Python via .NET fonctionne de la même manière qu'Excel.
1. Définir les indicateurs [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) et [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Entrez des en-têtes et pieds de page différents.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}
