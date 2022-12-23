---
title: Fonctionnalités de mise en page
type: docs
weight: 40
url: /fr/java/page-setup-features/
---
Parfois, il est nécessaire de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler l'impression. Ces paramètres de configuration de page offrent diverses options.

**Options de pages** 

![tâche : image_autre_texte](page-setup-features_1.png)

Les options de configuration de page sont entièrement prises en charge dans Aspose.Cells. Cet article explique comment définir les options de page avec Aspose.Cells.

## **Définition des options de page**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

La classe Worksheet fournit la propriété PageSetup, utilisée pour définir les options de mise en page. En fait, la propriété PageSetup est un objet de la classe PageSetup qui permet de définir les options de mise en page d'une feuille de calcul imprimée. La classe PageSetup fournit diverses propriétés utilisées pour définir les options de configuration de la page. Certaines de ces propriétés sont décrites ci-dessous.

### **Orientation des pages**

L'orientation de la page peut être réglée sur portrait ou paysage à l'aide de la[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) méthode. Le[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) méthode prend la[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) énumération comme paramètre. Les membres de la[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) énumération sont énumérés ci-dessous.

|**Types d'orientation de page**|**Description**|
|:- |:- |
|[**PAYSAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientation paysage|
|[**PORTRAIT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientation portrait|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Facteur d'échelle**

 Il est possible de réduire ou d'agrandir la taille d'une feuille de calcul en ajustant le facteur d'échelle avec la[**définirZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) méthode de la[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Options FitToPages**

 Pour adapter le contenu de la feuille de calcul à un nombre de pages spécifique, utilisez la[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) et[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) méthodes. Ces méthodes sont également utilisées pour mettre à l'échelle les feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Taille de papier**

 Définissez le format de papier sur lequel les feuilles de calcul seront imprimées à l'aide du[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**Taille de papier**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) la propriété. La propriété PaperSize accepte l'une des valeurs prédéfinies dans le[**Type de format de papier**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) énumération ci-dessous.

|**Types de format de papier**|**Description**|
|:- |:- |
|Papier10x14|10 po x 14 po|
|Papier11x17|11 po x 17 po|
|PapierA3|A3 (297 mm x 420 mm)|
|PapierA4|A4 (210 mm x 297 mm)|
|PapierA4Small|A4 Petit (210 mm x 297 mm)|
|PapierA5|A5 (148 mm x 210 mm)|
|PapierB3|B3 (13,9 x 19,7 pouces)|
|PapierB4|B4 (250 mm x 354 mm)|
|PapierB5|B5 (182 mm x 257 mm)|
|PapierCarte D'Affaires|Carte de visite (90 mm x 55 mm)|
|Feuille de papier|Feuille de format C|
|PaperDSheet|Feuille de taille D|
|PapierEnveloppe10|Enveloppe #10 (4-1/8 po x 9-1/2 po)|
|PapierEnveloppe11|Enveloppe #11 (4-1/2 po x 10-3/8 po)|
|PapierEnveloppe12|Enveloppe #12 (4-1/2 po x 11 po)|
|PapierEnveloppe14|Enveloppe #14 (5 po x 11-1/2 po)|
|PapierEnveloppe9|Enveloppe #9 (3-7/8 po x 8-7/8 po)|
|PapierEnveloppeB4|Enveloppe B4 (250 mm x 353 mm)|
|PapierEnveloppeB5|Enveloppe B5 (176 mm x 250 mm)|
|PapierEnveloppeB6|Enveloppe B6 (176 mm x 125 mm)|
|PapierEnveloppeC3|Enveloppe C3 (324 mm x 458 mm)|
|PapierEnveloppeC4|Enveloppe C4 (229 mm x 324 mm)|
|PapierEnveloppeC5|Enveloppe C5 (162 mm x 229 mm)|
|PapierEnveloppeC6|Enveloppe C6 (114 mm x 162 mm)|
|PapierEnveloppeC65|Enveloppe C65 (114 mm x 229 mm)|
|PapierEnveloppeDL|Enveloppe DL (110 mm x 220 mm)|
|PapierEnveloppeItalie|Enveloppe Italie (110 mm x 230 mm)|
|PapierEnveloppeMonarque|Enveloppe Monarch (3-7/8 po x 7-1/2 po)|
|PapierEnveloppePersonnels|Enveloppe (3-5/8 po x 6-1/2 po)|
|Feuille de papier|Feuille de taille E|
|PapierExécutif|Exécutif (7-1/2 po x 10-1/2 po)|
|PapierFanfoldLégalAllemand|Pliage accordéon légal allemand (8-1/2 po x 13 po)|
|PapierFanfoldStdAllemand|Pliage accordéon standard allemand (8-1/2 po x 12 po)|
|PapierFanfoldÉ.-U.|Pliage en accordéon standard américain (14-7/8 po x 11 po)|
|PapierFolio|Folio (8-1/2 po x 13 po)|
|Livre de papier|Registre (17 po x 11 po)|
|PapierLégal|Légal (8-1/2 po x 14 po)|
|PapierLettre|Lettre (8-1/2 po x 11 po)|
|PapierLettrePetit|Lettre petit (8-1/2 po x 11 po)|
|PapierNote|Remarque (8-1/2 po x 11 po)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Relevé (5-1/2 po x 8-1/2 po)|
|PapierTabloid|Tabloïd (11 po x 17 po)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Qualité d'impression**

 Définissez la qualité d'impression des feuilles de calcul à imprimer avec le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) méthode. L'unité de mesure de la qualité d'impression est le point par pouce (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Numéro de la première page**

 Commencez la numérotation des pages de la feuille de travail à l'aide de la[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) méthode. La méthode setFirstPageNumber définit le numéro de page de la première page de la feuille de calcul et les pages suivantes sont numérotées dans l'ordre croissant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Définition des marges**

Aspose.Cells prend entièrement en charge les options de configuration de page d'Excel Microsoft. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Cette rubrique explique comment utiliser Aspose.Cells pour configurer les marges de page.

**Marges de page dans Microsoft Excel**

![tâche : image_autre_texte](page-setup-features_2.png)

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. La classe Workbook contient la collection Worksheets qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fournit la propriété PageSetup, utilisée pour définir les options de mise en page. L'attribut PageSetup est un objet de la[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe qui permet de définir différentes options de mise en page pour une feuille de calcul imprimée. La classe PageSetup fournit diverses propriétés et méthodes utilisées pour définir les options de mise en page.

### **Marges de page**

 Définissez les marges (gauche, droite, haut, bas) d'une page avec[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) membres de la classe. Quelques-unes des méthodes utilisées pour spécifier les marges de page sont répertoriées ci-dessous :

- [**setLeftMargin(entier)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(entier)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(entier)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(entier)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrer sur la page**

 Il est possible de centrer quelque chose sur une page horizontalement et verticalement. Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe a des membres à cet effet:[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) et[**setCenterVertical**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Marges d'en-tête et de pied de page**

 Définissez les marges d'en-tête et de pied de page avec[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) membres tels que[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) et[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Définition des en-têtes et pieds de page**

Les en-têtes et les pieds de page sont les sections de texte et d'images au-dessus de la marge supérieure ou en dessous de la marge inférieure d'une page. Il est également possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul. Les en-têtes et pieds de page peuvent être utilisés pour afficher tout type d'informations utiles, par exemple le numéro de page, le nom de l'auteur, le titre du document ou la date et l'heure. Les en-têtes et pieds de page sont également gérés à l'aide de la boîte de dialogue Mise en page.

**La boîte de dialogue Mise en page** 

![tâche : image_autre_texte](page-setup-features_3.png)

Aspose.Cells permet d'ajouter des en-têtes et des pieds de page aux feuilles de calcul lors de l'exécution, mais il est recommandé que les en-têtes et les pieds de page soient définis manuellement dans un fichier préconçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme outil graphique pour définir facilement les en-têtes et les pieds de page afin de réduire le temps de développement. Aspose.Cells peut importer le fichier et réserver ces paramètres.

Pour ajouter des en-têtes et des pieds de page lors de l'exécution, Aspose.Cells fournit des classes spéciales et certaines commandes de script pour contrôler la mise en forme.

### **Commandes de script**

Les commandes de script sont des commandes spéciales fournies par Aspose.Cells qui permettent aux développeurs de formater les en-têtes et les pieds de page.

|**Commandes de script**|**Description**|
|:- |:- |
|&P|Le numéro de la page actuelle.|
|&G|Une image.|
|&N|Le nombre total de pages.|
|&RÉ|La date actuelle.|
|&T|L'heure actuelle.|
|&UNE|Nom de la feuille de calcul.|
|&F|Le nom du fichier sans le chemin.|
|&"\<FontName>"|Un nom de police. Par exemple : &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nom de police avec un style. Par exemple : &"Arial,Gras"|
|&\<FontSize>|Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre en clair à imprimer dans l'en-tête, celui-ci doit être séparé par un espace de la taille de la police. Par exemple : "&14 123".|

### **Définir les en-têtes et pieds de page**

 Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe fournit la méthode[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) pour ajouter un en-tête et[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) pour ajouter un pied de page à une feuille de calcul. Le script est utilisé comme argument pour toutes les méthodes mentionnées ci-dessus. Il représente le script à utiliser pour l'en-tête ou le pied de page. Ce script contient des commandes de script pour formater les en-têtes ou les pieds de page.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Insérer un graphique dans un en-tête ou un pied de page**

 Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe a les méthodes[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) et[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) pour ajouter des images à l'en-tête et au pied de page d'une feuille de calcul. Ces méthodes prennent deux paramètres :

- **Section**, la section de l'en-tête ou du pied de page où l'image sera placée. Il y a trois sections : gauche, centre et droite, représentées respectivement par les valeurs numériques 0, 1 et 2.
- **File InputStream**, les données graphiques. Les données binaires doivent être écrites dans le tampon d'un tableau d'octets.

Après avoir exécuté le code et ouvert le fichier, vérifiez l'en-tête de la feuille de calcul dans Microsoft Excel :

1.  Sur le**Dossier** menu, sélectionnez**Mise en page**.
1.  Dans la boîte de dialogue Mise en page, sélectionnez le**En-tête/Pied de page** languette.

**Insertion d'un graphique dans un en-tête/pied de page** 

![tâche : image_autre_texte](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Insérer un graphique dans l'en-tête de la première page uniquement**

 Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe a également d'autres méthodes utiles, par exemple[**setImage**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), pour ajouter des images dans l'en-tête/le pied de page de la première page d'une feuille de calcul. La première page est une page spéciale : il est courant de vouloir qu'elle affiche des informations particulières, par exemple un logo d'entreprise.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Définition des options d'impression**

Microsoft Les paramètres de mise en page d'Excel fournissent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler la manière dont les pages de la feuille de calcul sont imprimées. Ces options d'impression permettent aux utilisateurs de :

- Sélectionnez une zone d'impression spécifique sur une feuille de calcul.
- Titres imprimés.
- Imprimer le quadrillage.
- Imprimer les en-têtes de ligne et de colonne
- Atteindre la qualité brouillon.
- Imprimer les commentaires.
- Erreurs de cellule d'impression.
- Définissez l'ordre des pages.

Toutes ces options d'impression sont présentées ci-dessous.

**Options d'impression (feuille)** 

![tâche : image_autre_texte](page-setup-features_5.png)

### **Définition des options d'impression et de feuille**

 spose.Cells prend en charge toutes les options d'impression offertes par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)classe. La façon dont ces propriétés sont utilisées est décrite ci-dessous plus en détail.

### **Définir la zone d'impression**

Par défaut, seule la zone d'impression intègre toutes les zones de la feuille de calcul qui contiennent des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

 Pour sélectionner une zone d'impression spécifique, utilisez les[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) la propriété. Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Définir les titres d'impression**

 Aspose.Cells vous permet de désigner des en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) et[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) Propriétés.

Les lignes ou les colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Définir d'autres options d'impression**

 Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) La classe fournit également plusieurs autres propriétés pour définir les options d'impression générales comme suit :

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), une propriété booléenne qui définit s'il faut imprimer ou non le quadrillage.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), une propriété booléenne qui définit s'il faut imprimer ou non les en-têtes de ligne et de colonne.
- [**ensembleNoirEtBlanc**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), une propriété booléenne qui définit s'il faut imprimer la feuille de calcul en mode noir et blanc ou non.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), définit l'affichage des commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**setPrintBrouillon**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), une propriété booléenne qui définit s'il faut imprimer la feuille de calcul en qualité brouillon ou non.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), définit s'il faut imprimer les erreurs de cellule telles qu'affichées, vides, tirets ou N/A.

 Pour régler le[**ImprimerCommentaires**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) et[**Erreurs d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) propriétés, Aspose.Cells fournit également deux énumérations,[**ImprimerCommentairesType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) et[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) qui contiennent des valeurs prédéfinies à affecter au[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) et[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) propriétés respectivement.

 Les valeurs prédéfinies dans le[**ImprimerCommentairesType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) énumération sont décrites ci-dessous.

|**Imprimer les types de commentaires**|**Description**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Indique d'imprimer les commentaires tels qu'ils sont affichés sur la feuille de calcul.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Spécifie de ne pas imprimer les commentaires.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Indique d'imprimer les commentaires à la fin de la feuille de calcul.|

 Les valeurs prédéfinies du[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) énumération sont décrites ci-dessous.

|**Types d'erreurs d'impression**|**Description**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Spécifie de ne pas imprimer les erreurs.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Indique d'imprimer les erreurs sous la forme "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Spécifie d'imprimer les erreurs sous la forme "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Définir l'ordre des pages**

 Le[**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe fournit la[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) propriété utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit :

- **En bas puis dessus** imprime toutes les pages vers le bas avant d'imprimer les pages vers la droite.
- **Plus puis vers le bas** imprime les pages de gauche à droite avant d'imprimer les pages ci-dessous.

 Aspose.Cells fournit une énumération,[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , qui contient tous les types de commande prédéfinis à affecter à[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) méthode.

 Les valeurs prédéfinies de[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) énumération sont décrites ci-dessous.

|**Types de commande d'impression**|**Description**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Imprimez vers le bas, puis vers le haut.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Imprimez dessus, puis vers le bas.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**

Veuillez consulter cet article lié à ce sujet.

## **Sujets avancés**
- [Calculer le facteur d'échelle de mise en page](/cells/fr/java/calculate-page-setup-scaling-factor/)
- [Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination](/cells/fr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Déterminer si la taille du papier de la feuille de calcul est automatique](/cells/fr/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Obtenir la largeur et la hauteur du papier à partir de la mise en page de la feuille de calcul](/cells/fr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implémenter la taille de papier personnalisée de la feuille de calcul pour le rendu](/cells/fr/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Configuration de la page et options d'impression](/cells/fr/java/page-setup-and-printing-options/)
- [Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel](/cells/fr/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
