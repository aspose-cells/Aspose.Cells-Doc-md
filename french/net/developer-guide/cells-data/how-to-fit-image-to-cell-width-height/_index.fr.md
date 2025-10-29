---
title: Comment ajuster une image à la largeur et à la hauteur d une cellule
type: docs
weight: 130
url: /fr/net/how-to-fit-image-to-cell-width-height/
description: Apprenez comment ajuster une image à la largeur d une cellule avec Aspose.Cells.
keywords: Comment ajuster une image à la largeur de la cellule, ajuster une image à la largeur de la cellule, comment ajuster une image à la largeur et à la hauteur de la cellule, comment ajuster une image à la hauteur de la cellule.
---


## ** Pourquoi ajuster une image à la largeur et à la hauteur de la cellule**
 Ajuster une image à la largeur et à la hauteur spécifiques d'une cellule ne concerne pas seulement l'esthétique. C'est fondamentalement une question de précision, d'automatisation et d'organisation des données.

1. Pour la Présentation Professionnelle et la Lisibilité : Lors de la création d'un tableau de bord, vous avez souvent besoin d'icônes, de drapeaux ou d'images de produits pour s'aligner parfaitement avec les points de données. Une image mal alignée donne une impression bâclée et peu professionnelle. Si vous concevez un modèle pour que d'autres l'utilisent (par exemple, un catalogue de produits, un annuaire de employés), vous souhaitez que les images s'adaptent automatiquement aux espaces désignés, garantissant une cohérence à chaque utilisation du modèle. Les images qui débordent des cellules peuvent provoquer des sauts de page inattendus et des problèmes de mise en page lors de l'impression. Une image adaptée se comporte de manière prévisible sur la page imprimée.

2. Pour l'Organisation et la Structure des Données : C'est la raison fonctionnelle la plus cruciale. Excel est une grille pour les données. Lorsqu'une image est "placée" sur la grille plutôt que "fitée" à une cellule, cela cause des problèmes. Problème avec les images flottantes : elles ne bougent pas avec les cellules : Si vous triez, filtrez ou insérez/supprimez des lignes, l'image reste à sa position absolue sur la feuille, se déconnectant complètement des données qu'elle est censée représenter. Elles ne redimensionnent pas avec les cellules : Si vous changez la hauteur de la ligne ou la largeur de la colonne, une image flottante reste de la même taille, breakant la mise en page. Avantage de faire correspondre à une cellule : La cellule devient le "conteneur" de l'image : Lorsqu'une image est ajustée à une cellule, sa position et sa taille sont définies par les coordonnées du grille de la cellule. Si vous déplacez les données (par exemple, trier un tableau), l'image se déplace avec sa ligne correspondante. Cela crée une véritable paire image-donnée : Cela vous permet de traiter l'image comme un attribut visuel des données de cette ligne, ce qui est essentiel pour l'automatisation.

3. Pour l'Automatisation et les Fonctionnalités Avancées : C'est ici que faire correspondre les images aux cellules devient une superpuissance. Lier dynamiquement les images : Vous pouvez utiliser une formule pour extraire le chemin d'une image d'une cellule, puis utiliser une macro (VBA) pour dimensionner et insérer automatiquement l'image dans une cellule adjacente. C'est ainsi que vous créez un catalogue de produits dynamique où la modification d'un ID de produit met automatiquement à jour le nom, le prix et la photo. Intégration à la base de données : Lors de l'exportation de données ou de la liaison d'Excel à une base de données, le fait d'avoir des images contenues dans des cellules spécifiques rend l'ensemble du jeu de données, y compris ses éléments visuels, plus structuré et portable.

## **Comment faire correspondre une image à la largeur et à la hauteur d'une cellule avec Excel**
Vous pouvez faire correspondre l'image à la largeur et à la hauteur de la cellule dans Excel en utilisant deux méthodes.

### **Faire correspondre l'image à la largeur et à la hauteur de la cellule en utilisant la mise en place dans la cellule**
Pour insérer une image dans une cellule d'Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer dans la cellule**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="1.png" width=60% />
3. Sélectionnez l'image et insérez-la dans une cellule.
<br>
<img src="8.png" width=60% />

### **Faire correspondre l'image à la largeur et à la hauteur de la cellule en la plaçant par-dessus les cellules**
Pour insérer une image sur des cellules dans Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer sur des cellules**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="2.png" width=60% />
3. Sélectionnez l'image et insérez-la sur des cellules.
<br>
<img src="3.png" width=60% />
4. Ajustez manuellement la largeur et la hauteur de l'image pour correspondre à celles des cellules.
<br>
<img src="6.png" width=60% />

## **Comment faire correspondre une image à la largeur et à la hauteur de la cellule en utilisant Aspose.Cells**
En raison des variations dans la largeur et la hauteur des lignes et des colonnes selon la langue et le ratio d'affichage, ajuster la largeur et la hauteur d'une image peut entraîner de légères différences, et parfois ne pas être entièrement cohérent avec la largeur et la hauteur des cellules. Vous pouvez faire correspondre l'image à la largeur et à la hauteur de la cellule dans Aspose.Cells en utilisant deux méthodes.

### **Comment faire correspondre une image à la largeur et à la hauteur de la cellule en utilisant la mise en place dans la cellule**
Insérer une image dans une cellule en utilisant Aspose.Cells. Veuillez consulter le code d'exemple suivant. Après avoir exécuté l'exemple de code, une image sera insérée dans une cellule.
1. Instancier un objet Workbook. 
2. Obtenez la cellule où vous souhaitez insérer l'image.
3. Définissez la propriété Cell.EmbeddedImage. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

### **Exemple de code pour la mise en place dans la cellule**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Comment faire correspondre une image à la largeur et à la hauteur de la cellule en la plaçant par-dessus les cellules**
Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :
Il suffit d'appeler la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) de la collection [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Ensuite, ajustez la largeur et la hauteur de l'image en fonction de celles des cellules. Enfin, enregistrez le fichier au format [output XLSX](out_net.xlsx). La méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.


### **Exemple de code pour la mise en place sur les cellules**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
