---
title: Fonctionnalités de mise en page
type: docs
weight: 40
url: /fr/java/page-setup-features/
---

Parfois, il est nécessaire de configurer les paramètres de mise en page des feuilles de calcul pour contrôler l'impression. Ces paramètres de mise en page offrent diverses options.

**Options de Page** 

![todo:image_alt_text](page-setup-features_1.png)

Les options de configuration de page sont entièrement prises en charge dans Aspose.Cells. Cet article explique comment définir des options de page avec Aspose.Cells.

## **Définition des options de page**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une collection de feuilles de calcul qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fournit la propriété PageSetup, utilisée pour définir des options de configuration de page. En fait, la propriété PageSetup est un objet de la classe PageSetup qui permet de définir des options de mise en page pour une feuille de calcul imprimée. La classe PageSetup fournit diverses propriétés utilisées pour définir des options de configuration de page. Certaines de ces propriétés sont discutées ci-dessous.

### **Orientation de la page**

L'orientation de la page peut être définie en mode portrait ou paysage en utilisant la méthode [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La méthode [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) prend l'énumération [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) en paramètre. Les membres de l'énumération [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) sont énumérés ci-dessous.

|**Types d'orientation de page**|**Description**|
| :- | :- |
|[**PAYSAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientation paysage|
|[**PORTRAIT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientation portrait|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Facteur d'échelle**

Il est possible de réduire ou d'agrandir la taille d'une feuille de calcul en ajustant le facteur d'échelle avec la méthode [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Options FitToPages**

Pour ajuster le contenu de la feuille de calcul à un nombre spécifique de pages, utilisez les méthodes [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) et [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Ces méthodes sont également utilisées pour mettre à l'échelle les feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Taille du papier**

Définissez le format de papier sur lequel les feuilles de calcul seront imprimées en utilisant la propriété [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La propriété PaperSize accepte l'une des valeurs prédéfinies de l'énumération [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), énumérées ci-dessous.

|**Types de taille de papier**|**Description**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Qualité d'impression**

Définir la qualité d'impression des feuilles de calcul à imprimer avec la méthode [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). L'unité de mesure de la qualité d'impression est le point par pouce (PPP).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Numéro de la première page**

Commencer la numérotation des pages de la feuille de travail en utilisant la méthode [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La méthode setFirstPageNumber définit le numéro de page de la première page de la feuille de travail et les pages suivantes sont numérotées dans l'ordre croissant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Réglage des marges**

Aspose.Cells prend en charge pleinement les options de configuration de la mise en page de Microsoft Excel. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Ce sujet traite de l'utilisation d'Aspose.Cells pour configurer les marges de la page.

Marges de Page dans Microsoft Excel

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient la collection Worksheets qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fournit la propriété PageSetup, utilisée pour définir les options de mise en page. L'attribut PageSetup est un objet de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) qui permet de définir différentes options de mise en page pour une feuille de calcul imprimée. La classe PageSetup fournit diverses propriétés et méthodes utilisées pour définir les options de mise en page.

### **Marges de la page**

Définir les marges (gauche, droite, haut, bas) d'une page avec les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Quelques-unes des méthodes utilisées pour spécifier les marges de page sont répertoriées ci-dessous :

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrer sur la page**

Il est possible de centrer quelque chose sur une page horizontalement et verticalement. La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) possède des membres à cette fin : [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) et [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Marges d'en-tête et de pied de page	**

Définir les marges d'en-tête et de pied de page avec des membres de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tels que [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) et [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Définition des en-têtes et des pieds de page**

Les en-têtes et les pieds de page sont les sections de texte et d'images au-dessus de la marge supérieure ou en dessous de la marge inférieure d'une page. Il est possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul également. Les en-têtes et pieds de page peuvent être utilisés pour afficher tout type d'informations utiles, par exemple le numéro de page, le nom de l'auteur, le titre du document ou la date et l'heure. Les en-têtes et pieds de page sont également gérés à l'aide de la boîte de dialogue Mise en page.

La Boîte de Dialogue Mise en page 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells permet d'ajouter des en-têtes et des pieds de page aux feuilles de calcul à l'exécution, mais il est recommandé de définir manuellement les en-têtes et les pieds de page dans un fichier pré-conçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme outil GUI pour définir facilement les en-têtes et les pieds de page afin de réduire le temps de développement. Aspose.Cells peut importer le fichier et conserver ces paramètres.

Pour ajouter des en-têtes et des pieds de page à l'exécution, Aspose.Cells fournit des classes spéciales et des commandes de script pour contrôler le formatage.

### **Commandes de script**

Les commandes de script sont des commandes spéciales fournies par Aspose.Cells qui permettent aux développeurs de formater les en-têtes et les pieds de page.

|**Commandes de script**|**Description**|
| :- | :- |
|&P|Le numéro de page actuel.
|&G|Une image.
|&N|Le nombre total de pages.
|&D|La date actuelle.
|&T|L'heure actuelle.
|&A|Le nom de la feuille de calcul.
|&F|Le nom du fichier sans le chemin.
|&"\<FontName>"|Un nom de police. Par exemple: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nom de police avec un style. Par exemple: &"Arial,Gras"|
|&\<FontSize>| Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre ordinaire à imprimer dans l'en-tête, cela doit être séparé d'un caractère d'espace de la taille de la police. Par exemple : "&14 123".

### **Définir les en-têtes et les pieds de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fournit la méthode [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String)) pour ajouter un en-tête et [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) pour ajouter un pied de page à une feuille. Le script est utilisé comme argument pour toutes les méthodes mentionnées ci-dessus. Il représente le script à utiliser pour l'en-tête ou le pied de page. Ce script contient les commandes de script pour formater les en-têtes ou les pieds de page.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Insérer une image dans un en-tête ou un pied de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) a les méthodes [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[])) et [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) pour ajouter des images à l'en-tête et au pied de page d'une feuille. Ces méthodes prennent deux paramètres :

- **Section**, la section de l'en-tête ou du pied de page où l'image sera placée. Il existe trois sections : gauche, centre et droite, représentées par les valeurs numériques 0, 1 et 2 respectivement.
- **Flux d'entrée de fichier**, les données graphiques. Les données binaires doivent être écrites dans le tampon d'un tableau d'octets.

Après avoir exécuté le code et ouvert le fichier, vérifiez l'en-tête de la feuille de calcul dans Microsoft Excel :

1. Dans le menu **Fichier**, sélectionnez **Mise en page**.
1. Dans la boîte de dialogue Mise en page, sélectionnez l'onglet **En-tête/Pied de page**.

**Insertion d'une image dans un en-tête/pied de page** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Insérer une image dans l'en-tête de la première page uniquement**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) propose également d'autres méthodes utiles, par exemple [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), pour ajouter des images dans l'en-tête/le pied de page de la première page d'une feuille. La première page est une page spéciale : on peut souvent vouloir qu'elle affiche des informations spéciales, par exemple un logo d'entreprise.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Réglage des options d'impression**

Les paramètres de mise en page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler la façon dont les pages de feuille de calcul sont imprimées. Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes et de colonnes
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

Toutes ces options d'impression sont indiquées ci-dessous.

**Options d'impression (feuille)** 

![todo:image_alt_text](page-setup-features_5.png)

### **Paramétrage des options d'impression et de feuille**

spose.Cells prend en charge toutes les options d'impression offertes par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul à l'aide des propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Comment ces propriétés sont utilisées est discuté ci-dessous de manière plus détaillée.

### **Définir la zone d'impression**

Par défaut, seule la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent définir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Définir les titres d'impression**

Aspose.Cells vous permet de désigner les en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) et [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) de la classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fournit également plusieurs autres propriétés pour définir des options d'impression générales comme suit :

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), une propriété booléenne qui définit si les quadrillages doivent être imprimés ou non.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), une propriété booléenne qui définit si les en-têtes de lignes et de colonnes doivent être imprimés ou non.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), une propriété booléenne qui définit si la feuille de calcul doit être imprimée en mode noir et blanc ou non.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), définit si les commentaires doivent être affichés sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), une propriété booléenne qui définit si la feuille de calcul doit être imprimée en qualité brouillon ou non.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), définit si les erreurs de cellule doivent être imprimées telles qu'elles sont affichées, vides, avec un tiret ou N/A.

Pour définir les propriétés [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) et [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), Aspose.Cells fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) et [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), qui contiennent des valeurs prédéfinies à attribuer aux propriétés [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) et [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) respectivement.

Les valeurs prédéfinies de l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) sont décrites ci-dessous.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Indique d'imprimer les commentaires tels qu'ils apparaissent sur la feuille de calcul.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Indique de ne pas imprimer les commentaires.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Indique d'imprimer les commentaires à la fin de la feuille de calcul.|

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) sont décrites ci-dessous.

|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Spécifie de ne pas imprimer les erreurs.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Spécifie d'imprimer les erreurs comme "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Spécifie d'imprimer les erreurs telles qu'elles sont affichées.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Spécifie d'imprimer les erreurs comme "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fournit la propriété [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit :

- **Bas puis à droite** imprime toutes les pages vers le bas avant d'imprimer les pages vers la droite.
- **À droite puis en bas** imprime les pages de gauche à droite avant d'imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), qui contient tous les types d'ordre prédéfinis à attribuer à la méthode [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order).

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) sont décrites ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Imprimer vers le bas, puis vers la droite.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Imprimer vers la droite, puis vers le bas.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**

Veuillez consulter cet article lié à ce sujet.

## **Sujets avancés**
- [Calculer le facteur d'échelle de la mise en page](/cells/fr/java/calculate-page-setup-scaling-factor/)
- [Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination](/cells/fr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Déterminer si la taille du papier de la feuille de calcul est automatique](/cells/fr/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Obtenir la largeur et la hauteur du papier à partir de la mise en page de la feuille de calcul](/cells/fr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu](/cells/fr/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Configuration de la page et options d'impression](/cells/fr/java/page-setup-and-printing-options/)
- [Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel](/cells/fr/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
