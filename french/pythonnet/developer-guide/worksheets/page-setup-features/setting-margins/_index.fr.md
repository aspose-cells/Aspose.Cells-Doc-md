---
title: Réglage des marges
type: docs
weight: 20
url: /fr/python-net/setting-margins/
description: Dans cet article, vous apprendrez à définir les marges d une feuille de calcul Excel en utilisant un code d exemple. Vous apprendrez également à définir de manière programmatique les marges pour le centre de la page, l en tête et le pied de page de la configuration de page en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Python définir la marge de la feuille de calcul Excel au centre, définir la marge d en tête et de pied de page de la feuille de calcul en utilisant Python.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET prend en charge entièrement les options de configuration de la mise en page de Microsoft Excel. Les développeurs peuvent avoir besoin de configurer les paramètres de la mise en page pour contrôler le processus d'impression. Ce sujet explique comment utiliser Aspose.Cells pour Python via .NET pour configurer les marges de la page.

{{% /alert %}}

## **Comment définir les marges**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient la collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit la propriété [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) utilisée pour définir les options de mise en page pour une feuille de calcul. L'attribut [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) est un objet de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) qui permet aux développeurs de définir différentes options de mise en page pour une feuille de calcul imprimée. La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fournit différentes propriétés et méthodes utilisées pour définir les options de mise en page.

## **Comment définir les marges de la page**

Définir les marges de la page (gauche, droite, haut, bas) en utilisant les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Quelques-unes des méthodes sont répertoriées ci-dessous et sont utilisées pour spécifier les marges de la page :

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Comment centrer sur la page**

Il est possible de centrer quelque chose sur une page horizontalement et verticalement. Pour cela, il existe quelques membres utiles de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) et [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Comment définir les marges de l'en-tête et du pied de page**

Définir les marges d'en-tête et de pied de page avec les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) tels que [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) et [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
