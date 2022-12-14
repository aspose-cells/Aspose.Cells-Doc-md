---
title: Aspose.Cells for Java 18.10 Notes de mise à jour
type: docs
weight: 30
url: /fr/java/aspose-cells-for-java-18-10-release-notes/
---
{{% alert color="primary" %}} 

Cette page contient les notes de version pour Aspose.Cells for Java 18.10.

{{% /alert %}} 

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSJAVA-42634|Convertir la forme du ruban gauche droite en image|Renforcement|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - fichier de liste de packages manquant|Renforcement|
|CELLSJAVA-42528|La police n'est pas une balise HTML5 valide et à fermeture automatique et les navigateurs Web déforment son contenu|Renforcement|
|CELLSJAVA-42728|Une exception (StackOverFlow) se déclenche lors de l'enregistrement en sortie PDF|Punaise|
|CELLSJAVA-42729|Valeur erronée calculée par ROUNDUP()|Punaise|
|CELLSJAVA-42724|Copier une plage avec PasteType.ALL (options de collage) ne copie pas correctement les hauteurs de ligne|Punaise|
|CELLSJAVA-42722|La mise en forme du texte du lien hypertexte est perdue lorsqu'un nouveau texte est défini|Punaise|
|CELLSJAVA-42688|Sortie de format de date russe non valide|Punaise|
|CELLSJAVA-42721|Problème avec les polices SheetRender|Punaise|
|CELLSJAVA-42723|Exception "java.lang.OutOfMemoryError : Java heap space" lors du rendu du fichier MS Excel au format PDF|Punaise|
|CELLSJAVA-42725|Les guillemets apparaissent dans la formule lors de la récupération de la formule de cellule via Aspose.Cells|Punaise|
|CELLSJAVA-42720|Dégradation des performances lors de l'utilisation de la mise en forme conditionnelle|Punaise|
## **Public API et modifications incompatibles avec les versions antérieures**
Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for Java. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.
### **Ajoute la propriété HtmlSaveOptions.WidthScalable**
Indique si l'unité évolutive est utilisée pour décrire la largeur de la colonne lors de l'exportation du fichier au format HTML. La valeur par défaut est faux.
### **Ajoute la propriété WorkbookDesigner.UpdateEmptyStringAsNull**
Indique si la valeur de chaîne vide est traitée comme nulle.
### **Met à jour la valeur renvoyée de la méthode DocumentProperty.ToDateTime(), les propriétés BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted et BuiltInDocumentPropertyCollection.LastSavedTime.**
Renvoie l'heure dans le fuseau horaire local.
### **Nécessite une contrainte plus forte pour l'entrée de l'utilisateur pour FormatCondition.Formula1/Formula2**
La chaîne d'entrée en clair ne peut pas être déterminée si elle doit faire référence à une référence de nom ou s'il s'agit simplement d'une valeur de chaîne constante. Donc, maintenant, nous avons besoin que la formule commence par le signe '='. Pour la valeur de chaîne simple "sss", veuillez utiliser un format tel que "=\"sss\"".
