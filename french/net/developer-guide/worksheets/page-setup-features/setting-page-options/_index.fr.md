---
title: Définition des options de page
type: docs
weight: 10
url: /fr/net/setting-page-options/
---
{{% alert color="primary" %}}

Parfois, il est nécessaire de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler l'impression. Ces paramètres de configuration de page offrent diverses options.

{{% /alert %}}

## **Définition des options de page**

Les options de configuration de page sont entièrement prises en charge dans Aspose.Cells. Cet article explique comment définir les options de page avec Aspose.Cells et montre des exemples de code pour la configuration :

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classer.

 La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) propriété utilisée pour définir les options de mise en page de la feuille de calcul. En fait, cela[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) la propriété est un objet de la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe utilisée pour définir différentes options de mise en page pour une feuille de calcul imprimée. La[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)La classe fournit diverses propriétés utilisées pour définir les options de mise en page. Certaines de ces propriétés sont décrites ci-dessous.

### **Orientation des pages**

 L'orientation de la page peut être réglée sur portrait ou paysage à l'aide de la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**Orientation**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) propriété. La[**Orientation**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) propriété accepte l'une des valeurs prédéfinies dans le[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)énumération ci-dessous.

|**Types d'orientation de page**|**La description**|
|:- |:- |
|Paysage|Orientation paysage|
|Portrait|Orientation portrait|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **Facteur d'échelle**

 Il est possible de réduire ou d'agrandir la taille d'une feuille de calcul en ajustant le facteur d'échelle avec la[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)propriété.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **Options FitToPages**

 Pour adapter le contenu de la feuille de calcul à un nombre de pages spécifique, utilisez la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) et[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)Propriétés. Ces propriétés sont également utilisées pour mettre à l'échelle les feuilles de calcul.

{{% alert color="primary" %}}

 Vous pouvez soit choisir le[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) ou la[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) propriété mais pas les deux à la fois.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **Taille de papier**

 Définissez le format de papier sur lequel les feuilles de calcul seront imprimées à l'aide du[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**Taille de papier**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) propriété. La[**Taille de papier**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) propriété accepte l'une des valeurs prédéfinies dans le[**Type de format de papier**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)énumération ci-dessous.

|**Types de format de papier**|**La description**|
|:- |:- |
|PapierLettre|Lettre (8-1/2 po x 11 po)|
|PapierLettrePetit|Lettre petit (8-1/2 po x 11 po)|
|PapierTabloid|Tabloïd (11 po x 17 po)|
|Livre de papier|Registre (17 po x 11 po)|
|PapierLégal|Légal (8-1/2 po x 14 po)|
|PaperStatement|Relevé (5-1/2 po x 8-1/2 po)|
|PapierExécutif|Exécutif (7-1/4 po x 10-1/2 po)|
|PapierA3|A3 (297 mm x 420 mm)|
|PapierA4|A4 (210 mm x 297 mm)|
|PapierA4Small|A4 Petit (210 mm x 297 mm)|
|PapierA5|A5 (148 mm x 210 mm)|
|PapierB4|JIS B4 (257 mm x 364 mm)|
|PapierB5|JIS B5 (182 mm x 257 mm)|
|PapierFolio|Folio (8-1/2 po x 13 po)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Papier10x14|10 po x 14 po|
|Papier11x17|11 po x 17 po|
|PapierNote|Remarque (8-1/2 po x 11 po)|
|PapierEnveloppe9|Enveloppe #9 (3-7/8 po x 8-7/8 po)|
|PapierEnveloppe10|Enveloppe #10 (4-1/8 po x 9-1/2 po)|
|PapierEnveloppe11|Enveloppe #11 (4-1/2 po x 10-3/8 po)|
|PapierEnveloppe12|Enveloppe #12 (4-1/2 po x 11 po)|
|PapierEnveloppe14|Enveloppe #14 (5 po x 11-1/2 po)|
|Feuille de papier|Feuille de taille C|
|PaperDSheet|Feuille de taille D|
|Feuille de papier|Feuille de taille E|
|PapierEnveloppeDL|Enveloppe DL (110 mm x 220 mm)|
|PapierEnveloppeC5|Enveloppe C5 (162 mm x 229 mm)|
|PapierEnveloppeC3|Enveloppe C3 (324 mm x 458 mm)|
|PapierEnveloppeC4|Enveloppe C4 (229 mm x 324 mm)|
|PapierEnveloppeC6|Enveloppe C6 (114 mm x 162 mm)|
|PapierEnveloppeC65|Enveloppe C65 (114 mm x 229 mm)|
|PapierEnveloppeB4|Enveloppe B4 (250 mm x 353 mm|
|PapierEnveloppeB5|Enveloppe B5 (176 mm x 250 mm)|
|PapierEnveloppeB6|Enveloppe B6 (176 mm x 125 mm)|
|PapierEnveloppeItalie|Enveloppe Italie (110 mm x 230 mm)|
|PapierEnveloppeMonarque|Enveloppe Monarch (3-7/8 po x 7-1/2 po)|
|PapierEnveloppePersonnels|Enveloppe (3-5/8 po x 6-1/2 po)|
|PapierFanfoldÉ.-U.|Pliage en accordéon standard américain (14-7/8 po x 11 po)|
|PapierFanfoldStdAllemand|Pliage accordéon standard allemand (8-1/2 po x 12 po)|
|PapierFanfoldLégalAllemand|Pliage accordéon légal allemand (8-1/2 po x 13 po)|
|PapierISOB4|B4 (ISO) 250 × 353 mm|
|PapierJaponaisCarte Postale|Carte postale japonaise (100 mm x 148 mm)|
|Papier9x11|9 po x 11 po|
|Papier10x11|10 po x 11 po|
|Papier15x11|15 po x 11 po|
|PapierEnveloppeInviter|Invitation d'enveloppe (220 mm x 220 mm)|
|PapierLettreExtra|US Letter Extra 9 \ 275 x 12 po|
|PaperLegalExtra|US Legal Extra 9 \ 275 x 15 po|
|PapierTabloidExtra|Tabloïd américain Extra 11,69 x 18 po|
|PapierA4Extra|A4 supplémentaire 9,27 x 12,69 pouces|
|PapierLettreTransverse|Lettre transversale 8 \ 275 x 11 po|
|PapierA4Transverse|A4 Transversal 210 x 297 mm|
|PapierLettreExtraTransverse|Lettre Extra Transverse 9\275 x 12 po|
|PapierSuperA|SuperA/SuperA/A4 227 × 356 mm|
|PapierSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PapierLettrePlus|Lettre US Plus 8,5 x 12,69 pouces|
|PapierA4Plus|A4 Plus 210 x 330 mm|
|PapierA5Transverse|A5 Transversal 148 x 210 mm|
|PapierJISB5Transverse|B5 (JIS) Transversal 182 x 257 mm|
|PapierA3Extra|A3 Extra 322 x 445 mm|
|PapierA5Extra|A5 Supplémentaire 174 x 235 mm|
|PapierISOB5Extra|B5 (ISO) Supplémentaire 201 x 276 mm|
|PapierA2|A2 420 × 594 mm|
|PapierA3Transverse|A3 Transversal 297 x 420 mm|
|PapierA3ExtraTransverse|A3 Extra Transversal 322 x 445 mm|
|PapierJaponaisDoubleCarte Postale|Carte postale double japonaise 200 x 148 mm|
|PapierA6|A6 105 × 148 mm|
|papierjaponaisenveloppeKaku2|Enveloppe Japonaise Kaku #2|
|PapierJaponaisEnveloppeKaku3|Enveloppe Japonaise Kaku #3|
|PapierJaponaisEnveloppeChou3|Enveloppe japonaise Chou #3|
|PapierJaponaisEnveloppeChou4|Enveloppe japonaise Chou #4|
|PapierLettreTourné|11 pouces x 8,5 pouces|
|PapierA3Rotated|420 mm x 297 mm|
|PapierA4Tourné|297 mm x 210 mm|
|PapierA5Rotated|210 mm x 148 mm|
|PapierJISB4Rotated|B4 (JIS) Rotation 364 x 257 mm|
|PapierJISB5Rotated|B5 (JIS) Rotation 257 x 182 mm|
|PapierJaponaisCarte PostaleTourné|Carte postale japonaise tournée 148 x 100 mm|
|PapierJaponaisDoubleCarte PostaleTourné|Double Carte Postale Japonaise Tournée 148 x 200 mm|
|PapierA6Rotated|A6 Rotation 148 x 105 mm|
|papierjaponaisenveloppeKaku2tourné|Enveloppe japonaise Kaku #2 tournée|
|PapierJaponaisEnveloppeKaku3Rotated|Enveloppe japonaise Kaku #3 tournée|
|PapierJaponaisEnveloppeChou3Tourné|Enveloppe japonaise Chou #3 tournée|
|PapierJaponaisEnveloppeChou4Tourné|Enveloppe japonaise Chou #4 tournée|
|PapierJISB6|B6 (JIS) 128 × 182 mm|
|PapierJISB6Rotated|B6 (JIS) Rotation 182 x 128 mm|
|Papier12x11|12 x 11 pouces|
|papierjaponaisenveloppevous4|Enveloppe japonaise You #4|
|PapierJaponaisEnveloppeYou4Rotated|Enveloppe japonaise vous # 4 pivotée|
|PapierPRC16K|RPC 16K 146 x 215 mm|
|PapierPRC32K|RPC 32K 97 x 151 mm|
|PapierPRCBig32K|PRC 32K(Grand) 97 x 151 mm|
|PapierPRCEnveloppe1|Enveloppe PRC #1 102 x 165 mm|
|PapierPRCEnvelope2|Enveloppe PRC #2 102 x 176 mm|
|PapierPRCEnveloppe3|Enveloppe PRC #3 125 x 176 mm|
|PapierPRCEnveloppe4|Enveloppe PRC #4 110 x 208 mm|
|PapierPRCEnveloppe5|Enveloppe PRC #5 110 x 220 mm|
|PapierPRCEnveloppe6|Enveloppe PRC #6 120 x 230 mm|
|PapierPRCEnveloppe7|Enveloppe PRC #7 160 x 230 mm|
|PapierPRCEnveloppe8|Enveloppe PRC #8 120 x 309 mm|
|PapierPRCEnveloppe9|Enveloppe PRC #9 229 x 324 mm|
|PapierPRCEnveloppe10|Enveloppe PRC #10 324 x 458 mm|
|PapierPRC16KRotation|RPC 16K pivoté|
|PapierPRC32KRotation|RPC 32K pivoté|
|PapierPRCBig32KRotated|PRC 32K (gros) tourné|
|PapierPRCEnvelope1Rotated|Enveloppe PRC #1 Rotation 165 x 102 mm|
|PapierPRCEnvelope2Rotated|Enveloppe PRC #2 Rotation 176 x 102 mm|
|PapierPRCEnvelope3Rotated|Enveloppe PRC #3 Rotation 176 x 125 mm|
|PapierPRCEnvelope4Rotated|Enveloppe PRC #4 Rotation 208 x 110 mm|
|PapierPRCEnvelope5Rotated|Enveloppe PRC #5 Rotation 220 x 110 mm|
|PapierPRCEnvelope6Rotated|Enveloppe PRC #6 Rotation 230 x 120 mm|
|PapierPRCEnvelope7Rotated|Enveloppe PRC #7 Rotation 230 x 160 mm|
|PapierPRCEnveloppe8Rotated|Enveloppe PRC #8 Rotation 309 x 120 mm|
|PapierPRCEnveloppe9Rotated|Enveloppe PRC #9 avec rotation 324 x 229 mm|
|PapierPRCEnvelope10Rotated|Enveloppe PRC #10 avec rotation 458 x 324 mm|
|PapierB3|B3 habituel (13,9 x 19,7 pouces)|
|PapierCarte D'Affaires|Carte de visite (90 mm x 55 mm)|
|PapierThermique|Thermique (3 x 11 po)|
|Personnalisé|Représente le format de papier personnalisé.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **Qualité d'impression**

 Définissez la qualité d'impression des feuilles de calcul à imprimer avec le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**Qualité d'impression**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)propriété. L'unité de mesure de la qualité d'impression est le point par pouce (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **Numéro de la première page**

 Commencez la numérotation des pages de la feuille de travail à l'aide de la[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classer'[**NuméroPremierPage**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) propriété. La[**NuméroPremierPage**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)La propriété définit le numéro de page de la première page de la feuille de calcul et les pages suivantes sont numérotées dans l'ordre croissant.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
