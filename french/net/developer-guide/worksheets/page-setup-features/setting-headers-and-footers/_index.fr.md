---
title: Définition des en-têtes et pieds de page
type: docs
weight: 30
url: /fr/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

Les en-têtes et les pieds de page sont les lignes de texte affichées respectivement sous la marge supérieure ou au-dessus de la marge inférieure. Il est également possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul. Les en-têtes et les pieds de page peuvent être utilisés pour afficher des informations utiles telles que le numéro de page, le nom de l'auteur, le nom du sujet ou la date et l'heure. Les en-têtes et pieds de page sont gérés à l'aide des paramètres de mise en page.

{{% /alert %}}

## **Définition des en-têtes et pieds de page**

Aspose.Cells vous permet d'ajouter des en-têtes et des pieds de page aux feuilles de calcul lors de l'exécution, mais nous vous recommandons de définir manuellement les en-têtes et les pieds de page dans un fichier préconçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme outil graphique pour définir des en-têtes et des pieds de page afin d'économiser des efforts et du temps de développement. Aspose.Cells peut importer le fichier et enregistrer les paramètres.

Pour ajouter des en-têtes et des pieds de page lors de l'exécution, Aspose.Cells fournit des appels API spéciaux et des commandes de script pour formater les en-têtes et les pieds de page.

### **Commandes de script**

Les commandes de script sont des commandes spéciales qui vous permettent de définir le formatage de l'en-tête et du pied de page.

|**Commandes de script**|**Description**|
|:- |:- |
|&P|Le numéro de la page actuelle|
|&G|Une image|
|&N|Le nombre total de pages|
|&RÉ|La date actuelle|
|&T|L'heure actuelle|
|&UNE|Le nom de la feuille de calcul|
|&F|Le nom du fichier sans son chemin|
|&"\<FontName>"|Représente un nom de police. Par exemple : &"Arial"|
|&"\<FontName>, \<FontStyle>"|Représente le nom de la police avec le style. Par exemple : &"Arial,Gras"|
|&\<FontSize>|Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre en clair à imprimer dans l'en-tête, celui-ci doit être séparé par un espace de la taille de la police. Par exemple : "&14 123".|

### **Définir les en-têtes et pieds de page**

 Le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe fournit deux méthodes,[**Définir l'en-tête**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) et[**Définir le pied de page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), utilisé pour ajouter un en-tête et un pied de page à une feuille de calcul. Ces méthodes ne prennent que deux paramètres :

- **Section** – la section où l'en-tête ou le pied de page doit être placé. Il y a trois sections : gauche, centre et droite, représentées respectivement par 0, 1 et 2.
- **Scénario** – le script à utiliser pour l'en-tête ou le pied de page. Ce script contient des commandes de script pour formater les en-têtes ou les pieds de page.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Insérer une image dans un en-tête ou un pied de page**

 Le[**Mise en page**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class a deux méthodes supplémentaires,[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) et[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), utilisé pour ajouter des images dans l'en-tête et le pied de page. Ces méthodes prennent les paramètres :

- **Section**– la section d'en-tête ou de pied de page où l'image sera placée. Il y a trois sections, gauche, centre et droite, représentées respectivement par les valeurs 0, 1 et 2.
- **Tableau d'octets** – les données graphiques (les données binaires doivent être écrites dans le tampon d'un tableau d'octets).

Après avoir exécuté le code ci-dessous et ouvert le fichier, vérifiez l'en-tête de la feuille de calcul en :

1.  Sur le**Dossier** menu, sélectionnez**Mise en page**. Une boîte de dialogue s'affiche.
1.  Sélectionnez le**En-tête/Pied de page** languette.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
