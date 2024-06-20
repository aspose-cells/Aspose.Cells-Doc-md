---
title: Réglage des marges
type: docs
weight: 20
url: /fr/net/setting-margins/
description: Dans cet article, vous apprendrez comment définir les marges d une feuille de calcul Excel à l aide d un code d exemple. Vous apprendrez également comment définir de manière programmatique les marges pour le centre de la page, les marges d en tête et de pied de page de la Mise en page en utilisant l API C# ou la bibliothèque .NET.
keywords: définir la marge de la feuille de calcul Excel au centre c#, définir la marge de l en tête et du pied de page de la feuille de calcul en c#
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge pleinement les options de configuration de la mise en page de Microsoft Excel. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Ce sujet traite de l'utilisation d'Aspose.Cells pour configurer les marges de la page.

{{% /alert %}}

## **Réglage des marges**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient la collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit la propriété [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) utilisée pour définir les options de mise en page pour une feuille de calcul. L'attribut [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) est un objet de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) qui permet aux développeurs de définir différentes options de mise en page pour une feuille de calcul imprimée. La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) fournit différentes propriétés et méthodes utilisées pour définir les options de mise en page.

### **Marges de la page**

Définir les marges de la page (gauche, droite, haut, bas) en utilisant les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). Quelques-unes des méthodes sont répertoriées ci-dessous et sont utilisées pour spécifier les marges de la page :

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centrer sur la page**

Il est possible de centrer quelque chose sur une page horizontalement et verticalement. Pour cela, il existe quelques membres utiles de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) et [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Marges d'en-tête et de pied de page	**

Définir les marges d'en-tête et de pied de page avec les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) tels que [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) et [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
