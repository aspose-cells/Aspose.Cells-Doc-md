---
title: Définition des options d'impression
type: docs
weight: 40
url: /fr/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Les paramètres de mise en page d'Excel fournissent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler la manière dont les pages de la feuille de calcul sont imprimées.

{{% /alert %}}

## **Définition des options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionnez une zone d'impression spécifique sur une feuille de calcul.
- Titres imprimés.
- Imprimer le quadrillage.
- Imprimer les en-têtes de lignes/colonnes.
- Atteindre la qualité brouillon.
- Imprimer les commentaires.
- Erreurs de cellule d'impression.
- Définissez l'ordre des pages.

 Aspose.Cells prend en charge toutes les options d'impression offertes par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)classer. La façon dont ces propriétés sont utilisées est décrite ci-dessous plus en détail.

### **Définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul qui contiennent des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

 Pour sélectionner une zone d'impression spécifique, utilisez les[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**Zone d'impression**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)propriété. Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Définir les titres d'impression**

 Aspose.Cells vous permet de désigner des en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) et[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)Propriétés.

Les lignes ou les colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Définir d'autres options d'impression**

 La[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)La classe fournit également plusieurs autres propriétés pour définir les options d'impression générales comme suit :

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)une propriété booléenne qui définit s'il faut imprimer ou non le quadrillage.
- [**Imprimer les en-têtes**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): une propriété booléenne qui définit s'il faut imprimer ou non les en-têtes de ligne et de colonne.
- [**Noir et blanc**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): une propriété booléenne qui définit s'il faut imprimer la feuille de calcul en mode noir et blanc ou non.
- [**ImprimerCommentaires**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): définit s'il faut afficher les commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**ImprimerBrouillon**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): une propriété booléenne qui définit s'il faut imprimer la feuille sans graphiques..
- [**Erreurs d'impression**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): définit s'il faut imprimer les erreurs de cellule telles qu'affichées, vides, tirets ou N/A.

 Pour régler le[**ImprimerCommentaires**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) et[**Erreurs d'impression**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) propriétés, Aspose.Cells fournit également deux énumérations,[**ImprimerCommentairesType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , et[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) qui contiennent des valeurs prédéfinies à affecter au[**ImprimerCommentaires**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) et[**Erreurs d'impression**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)propriétés respectivement.

 Les valeurs prédéfinies dans le[**ImprimerCommentairesType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)énumération sont énumérés ci-dessous avec leurs descriptions.

|**Imprimer les types de commentaires**|**La description**|
|:- |:- |
|Impression sur place|Indique d'imprimer les commentaires tels qu'ils sont affichés sur la feuille de calcul.|
|ImprimerPas de commentaire|Spécifie de ne pas imprimer les commentaires.|
|ImprimerFeuilleFeuille|Indique d'imprimer les commentaires à la fin de la feuille de calcul.|

 Les valeurs prédéfinies de[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)énumération sont énumérés ci-dessous avec leurs descriptions.



|**Types d'erreurs d'impression**|**La description**|
|:- |:- |
|ImprimerErreursVide|Spécifie de ne pas imprimer les erreurs.|
|PrintErrorsDash|Indique d'imprimer les erreurs sous la forme "--".|
|Erreurs d'impression affichées|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|Erreurs d'impressionNA|Spécifie d'imprimer les erreurs sous la forme "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Définir l'ordre des pages**

 La[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)la classe fournit la[**Ordre**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)propriété utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit.

- **En bas puis dessus :** imprime toutes les pages vers le bas avant d'imprimer les pages vers la droite.
- **Dessus puis vers le bas :** imprime les pages de gauche à droite avant d'imprimer les pages ci-dessous.

 Aspose.Cells fournit une énumération,[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)qui contient tous les types de commande prédéfinis.

 Les valeurs prédéfinies du[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)énumération sont énumérés ci-dessous.

|**Types de commande d'impression**|**La description**|
|:- |:- |
|DownPuisPlus|Représente l'ordre d'impression en bas puis en haut.|
|OverThenDown|Représente l'ordre d'impression comme dessus puis vers le bas.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
