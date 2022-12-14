---
title: Aspose.Cells for Java 17.6 Notes de mise à jour
type: docs
weight: 70
url: /fr/java/aspose-cells-for-java-17-6-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for Java 17.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.6/).

{{% /alert %}} 

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSJAVA-42315|Ajouter le client JS API pour l'événement AjaxCallFinished - GridWeb (JAVA)|Nouvelle fonctionnalité|
|CELLSJAVA-42194|Regrouper les lignes dans la feuille de calcul - GridWeb (JAVA)|Nouvelle fonctionnalité|
|CELLSJAVA-42308|Le tableau croisé dynamique est incorrect (lignes manquantes, en-têtes de champ croisé imprimés deux fois, date convertie en valeurs numériques, etc.) dans le rendu Excel vers HTML|Punaise|
|CELLSJAVA-42298|Caractères supplémentaires présents dans la sortie HTML du fichier Excel|Punaise|
|CELLSJAVA-42277|L'image ne s'affiche pas dans le HTML de sortie lorsque HtmlSaveOptions.setExportHiddenWorksheet est défini sur false|Punaise|
|CELLSJAVA-42259|HTML n'a pas pu être converti correctement en fichier Excel|Punaise|
|CELLSJAVA-42256|Problème avec le rendu du tableau HTML vers Excel|Punaise|
|CELLSJAVA-42319|Problème de calcul de la zone d'impression lors de la spécification de formules|Punaise|
|CELLSJAVA-42273|La fonction Définir l'en-tête de colonne ne fonctionne pas dans GridWeb (JAVA)|Punaise|
|CELLSJAVA-42269|GridWorksheet.setColumnHeaderToolTip() ne fonctionne pas dans GridWeb (JAVA)|Punaise|
|CELLSJAVA-42320|Le graphique n'est pas mis à jour s'il existe dans une feuille séparée|Punaise|
|CELLSJAVA-42295|La valeur Cell est ajoutée au début lorsque nous cliquons sur une cellule existante (ayant une certaine valeur)|Punaise|
|CELLSJAVA-42325|Lorsque XLSX est enregistré au format PDF, les mots sont mis en miroir|Punaise|
|CELLSJAVA-42299|Caractères supplémentaires présents dans la sortie PDF/image du fichier Excel|Punaise|
|CELLSJAVA-42301|Les barres sont manquantes dans la sortie PDF du graphique à barres|Punaise|
|CELLSJAVA-42293|L'image du graphique est incorrecte dans le HTML de sortie|Punaise|
|CELLSJAVA-42292|L'image du graphique est incorrecte dans le HTML de sortie|Punaise|
|CELLSJAVA-42270|Le contenu est manquant lorsque le graphique Excel est converti en PDF|Punaise|
|CELLSJAVA-42258|Le PDF du graphique a un format de date incorrect pour les étiquettes de l'axe des x|Punaise|
|CELLSJAVA-42252|Mise à l'échelle incorrecte de l'axe Y dans le PDF de sortie|Punaise|
|CELLSJAVA-42245|Le style/la mise en forme est erronée lors de l'enregistrement au format HTML|Punaise|
|CELLSJAVA-42316|L'option de compression des images n'est pas conservée lors de l'ouverture et de l'enregistrement du fichier Excel|Punaise|
|CELLSJAVA-42306|La couleur d'arrière-plan des cellules dans File2 est modifiée lors de l'ouverture et de l'enregistrement du classeur|Punaise|
|CELLSJAVA-42305|La couleur d'arrière-plan des cellules dans File1 est modifiée lors de l'ouverture et de l'enregistrement du classeur|Punaise|
|CELLSJAVA-42303|La cellule de formule Excel devient une cellule sans formule lors de la définition du texte de la forme|Punaise|
|CELLSJAVA-42284|Workbook.getFonts() affiche une police supplémentaire après le rechargement de la même feuille de calcul|Punaise|
|CELLSJAVA-42307|Exception : "L'index de ligne ne doit pas se trouver dans le rapport de tableau croisé dynamique" s'est produite lors du rendu au format de fichier HTML|Exception|
|CELLSJAVA-42285|Exception : "L'index de ligne ne peut pas être négatif" s'est produit si un tableau croisé dynamique existe dans la feuille de calcul à convertir au format de fichier HTML|Exception|
|CELLSJAVA-42318|Une exception est levée lors de la tentative d'ouverture du classeur|Exception|
|CELLSJAVA-42311|Exception : "java.lang.NullPointerException" lors de l'ouverture d'un fichier ODS via les API Aspose.Cells|Exception|
|CELLSJAVA-42302|NullPointerException lors de la création d'une instance de classeur à partir du fichier Excel source|Exception|
## **Public API et modifications incompatibles avec les versions antérieures**
Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for Java. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.
### **Ajoute la propriété Gridweb.OnAjaxCallFinishedClientFunction**
Obtient ou définit le nom de la fonction côté client à appeler lorsque ajaxcall est terminé.
### **Ajoute l'énumération StyleModifyFlag.RelativeIndent**
Représente le retrait relatif.
### **Ajoute la propriété TextureFill.IsTiling**
Indique si l'image de mosaïque est une texture.


### **Exemples d'utilisation**
Veuillez consulter la liste des rubriques d'aide ajoutées dans les documents Wiki Aspose.Cells :

- [Image en mosaïque en tant que texture à l'intérieur de la forme](/cells/fr/java/tile-picture-as-a-texture-inside-the-shape/)
- [Utilisation de la fonction OnAjaxCallFinishedClient de GridWeb](/cells/fr/java/using-onajaxcallfinishedclientfunction-of-gridweb/)
- [Utilisation du paramètre Formule dans le champ Smart Marker](/cells/fr/java/using-formula-parameter-in-smart-marker-field/)
