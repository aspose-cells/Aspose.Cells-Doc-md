---
title: Définition des marges
type: docs
weight: 20
url: /fr/net/setting-margins/
description: Dans cet article, vous apprendrez à définir les marges d'une feuille de calcul Excel à l'aide d'un exemple de code. Vous apprendrez également à définir par programme les marges du centre de la page, les marges d'en-tête et de pied de page de la mise en page à l'aide de la bibliothèque C# API ou .NET.
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---
{{% alert color="primary" %}}

Aspose.Cells prend entièrement en charge les options de configuration de page d'Excel Microsoft. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Cette rubrique explique comment utiliser Aspose.Cells pour configurer les marges de page.

{{% /alert %}}

##  **Définition des marges**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient le[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

 Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) propriété utilisée pour définir les options de mise en page d'une feuille de calcul. Le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) l'attribut est un objet de la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) classe qui permet aux développeurs de définir différentes options de mise en page pour une feuille de calcul imprimée. Le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)La classe fournit diverses propriétés et méthodes utilisées pour définir les options de configuration de la page.

###  **Marges de page**

 Définissez les marges de la page (gauche, droite, haut, bas) à l'aide de[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)membres de la classe. Quelques-unes des méthodes sont répertoriées ci-dessous qui sont utilisées pour spécifier les marges de page :

- [**Marge de gauche**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Marge droite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Marge supérieure**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Marge inférieure**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

###  **Centrer sur la page**

 Il est possible de centrer quelque chose sur une page horizontalement et verticalement. Pour cela, il y a quelques membres utiles du[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) classe,[**Centrer horizontalement**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) et[**CentreVerticalement**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

###  **Marges d'en-tête et de pied de page**

 Définissez les marges d'en-tête et de pied de page avec[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) membres de la classe tels que[**Marge d'en-tête**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) et[**Marge de pied de page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
