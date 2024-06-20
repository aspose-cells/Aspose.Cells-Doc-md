---
title: Mise en forme des Smart Markers
type: docs
weight: 20
url: /fr/java/formatting-smart-markers/
---

## **Copier l'attribut de style**
Parfois, lors de l'utilisation de smart markers, vous souhaitez copier le style de la cellule contenant les balises de smart marker. Vous pouvez utiliser l'attribut CopyStyle des balises de Smart Marker à cette fin.
### **Copier les styles des cellules avec les marqueurs intelligents**
Cet exemple utilise un fichier Microsoft Excel modèle simple avec deux marqueurs dans les cellules A2 et B2. Le marqueur collé dans la cellule B2 utilise l'attribut CopyStyle, tandis que le marqueur dans la cellule A2 ne le fait pas. Appliquez une mise en forme simple (par exemple, définissez la couleur de police en **rouge** et définissez la couleur de fond de la cellule en **jaune**).

Cet exemple utilise un [fichier modèle](template1.xlsx) avec quelques marqueurs dans les cellules. Lors de l'exécution du code, Aspose.Cells copie la mise en forme à tous les enregistrements de la colonne B mais ne conserve pas la mise en forme dans la colonne A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Ajout de Libellés Personnalisés**
### **Introduction**
Lorsque vous travaillez avec la fonction de regroupement des données des marqueurs intelligents, parfois vous avez besoin d'ajouter vos propres libellés personnalisés à la ligne de récapitulatif. Vous souhaitez également concaténer le nom de la colonne avec ce libellé, par exemple "Sous-total des commandes". Aspose.Cells vous fournit les attributs Label et LabelPosition, afin que vous puissiez placer vos libellés personnalisés dans les marqueurs intelligents tout en les concaténant avec les lignes de sous-total dans les données de regroupement.
### **Ajout de libellés personnalisés pour concaténer les lignes de sous-total dans les marqueurs intelligents**
Cet exemple utilise un [fichier modèle](template.xlsx) avec quelques marqueurs dans les cellules. Lors de l'exécution du code, Aspose.Cells ajoute quelques libellés personnalisés aux lignes de résumé pour les données groupées.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
