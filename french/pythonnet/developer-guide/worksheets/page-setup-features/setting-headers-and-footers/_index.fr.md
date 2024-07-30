---
title: Définir des en têtes et des pieds de page
type: docs
weight: 30
url: /fr/python-net/setting-headers-and-footers/
description: Cet article explique comment insérer de manière programmatique une image dans l en tête et le pied de page des feuilles Excel en définissant l en tête et le pied de page avec des commandes de script en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, insérer une image dans l en tête et le pied de page Excel en Python, définir des commandes de script pour l en tête et le pied de page Excel en Python.
---

{{% alert color="primary" %}}

Les en-têtes et les pieds de page sont les lignes de texte affichées en dessous de la marge supérieure ou au-dessus de la marge inférieure respectivement. Il est possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul également. Les en-têtes et les pieds de page peuvent être utilisés pour afficher des informations utiles comme le numéro de page, le nom de l'auteur, le nom du sujet ou la date et l'heure. Les en-têtes et les pieds de page sont gérés à l'aide des paramètres de configuration de la page.

{{% /alert %}}

## **Définition des en-têtes et des pieds de page**

Aspose.Cells for Python via .NET vous permet d'ajouter des en-têtes et des pieds de page aux feuilles de calcul en temps d'exécution, mais nous recommandons de définir manuellement les en-têtes et les pieds de page dans un fichier pré-conçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme outil graphique pour définir les en-têtes et les pieds de page et gagner du temps de développement. Aspose.Cells for Python via .NET peut importer le fichier et enregistrer les paramètres.

Pour ajouter des en-têtes et des pieds de page en cours d'exécution, Aspose.Cells for Python via .NET fournit des appels d'API spéciaux et des commandes de script pour formater les en-têtes et les pieds de page.

### **Commandes de script**

Les commandes de script sont des commandes spéciales qui vous permettent de définir le formatage des en-têtes et des pieds de page.

|**Commandes de script**|**Description**|
| :- | :- |
|&P| Le numéro de la page actuelle
|&G| Une image
|&N| Le nombre total de pages
|&D| La date actuelle
|&T| L'heure actuelle
|&A| Le nom de la feuille de calcul
|&F| Le nom du fichier sans son chemin d'accès
|&"\<FontName>"| Représente un nom de police. Par exemple : &"Arial"
|&"\<FontName>, \<FontStyle>"| Représente un nom de police avec un style. Par exemple : &"Arial, Gras"
|&\<FontSize>| Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre ordinaire à imprimer dans l'en-tête, cela doit être séparé d'un caractère d'espace de la taille de la police. Par exemple : "&14 123".

### **Comment définir des en-têtes et des pieds de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fournit deux méthodes, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) et [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), utilisées pour ajouter un en-tête et un pied de page à une feuille de calcul. Ces méthodes ne prennent que deux paramètres :

- **Section** – la section où l'en-tête ou le pied de page doit être placé. Il existe trois sections : gauche, centre et droite, représentées respectivement par 0, 1 et 2.
- **Script** – le script à utiliser pour l'en-tête ou le pied de page. Ce script contient des commandes de script pour formater les en-têtes ou les pieds de page.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **Comment insérer une image dans un en-tête ou un pied de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) possède deux méthodes supplémentaires, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) et [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), utilisées pour ajouter des images dans l'en-tête et le pied de page. Ces méthodes prennent les paramètres :

- **Section** – la section d'en-tête ou de pied de page où l'image sera placée. Il existe trois sections, left, center et right, représentées respectivement par les valeurs 0, 1 et 2.
- **Tableau de bytes** – les données graphiques (les données binaires doivent être écrites dans le buffer d'un tableau de bytes).

Après l'exécution du code ci-dessous et l'ouverture du fichier, vérifiez l'en-tête de la feuille de calcul en :

1. Dans le menu **Fichier**, sélectionnez **Mise en page**. Une boîte de dialogue s'affichera.
1. Sélectionnez l'onglet **En-tête/Pied de page**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
