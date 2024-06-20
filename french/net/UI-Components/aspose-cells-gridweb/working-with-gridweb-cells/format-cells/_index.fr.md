---
title: Formater la cellule
type: docs
weight: 40
url: /fr/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb,formatage,style
description: Cet article présente comment définir ou appliquer un format de style pour une cellule (GridCell) dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet offre une discussion détaillée sur la façon de formater les cellules.

Il couvre le formatage des cellules en mode GUI en utilisant la boîte de dialogue Style du contrôle Aspose.Cells.GridWeb. Il montre également comment formater les cellules de manière programmée. Différents paramètres de format comme la police, les bordures et le format numérique sont discutés, illustrés par des exemples.

{{% /alert %}} 
## **Formatage des cellules à l'aide de la boîte de dialogue Style**
Les cellules peuvent être formatées de manière [programmatique](/cells/fr/net/aspose-cells-gridweb/format-cells/), mais le moyen le plus simple de formater les cellules dans le contrôle Aspose.Cells.GridWeb de manière WYSIWYG est d'utiliser la boîte de dialogue Style.

Pour utiliser la boîte de dialogue Style :
Sélectionnez une plage de cellules, puis cliquez avec le bouton droit et sélectionnez **Formater la cellule**. 

**Sélectionner le format de cellule** 

![todo:image_alt_text](format-cells_1.png)



La boîte de dialogue Style est affichée. 

**La boîte de dialogue Style est utilisée pour formater les cellules** 

![todo:image_alt_text](format-cells_2.png)

La boîte de dialogue Style permet aux utilisateurs de formater les cellules en personnalisant les paramètres de police et de bordure.
### **Personnalisation des paramètres de police**
Vous pouvez personnaliser les paramètres de police suivants en utilisant la boîte de dialogue Style:

- Nom de la police, sélectionner une police désirée dans la liste.
- Style de la police, appliquer un style de police comme gras, italique, etc.
- Taille de la police, sélectionner une taille de police en points.
- Souligné, souligner le texte.
- Barré, appliquer un effet de barré au texte.
- Alignement horizontal, sélectionner l'alignement horizontal.
- Alignement vertical, sélectionner l'alignement vertical.
- Couleur de police, sélectionner une couleur de police.
- Arrière-plan, sélectionner une couleur pour l'arrière-plan.

Vous pouvez vérifier les paramètres de police sélectionnés dans une petite zone de prévisualisation.

**Paramètres de police personnalisés** 

![todo:image_alt_text](format-cells_3.png)
### **Personnalisation des paramètres de bordure**
Le contrôle permet également aux utilisateurs de dessiner une bordure autour des cellules en personnalisant les paramètres de bordure dans la boîte de dialogue Style.

Pour afficher les options liées aux bordures:
Cliquez sur **Bordures** dans la boîte de dialogue Style.
Les options liées aux bordures s'affichent. 

**Options de bordures dans la boîte de dialogue Style** 

![todo:image_alt_text](format-cells_4.png)

Les options de bordure suivantes peuvent être sélectionnées dans la boîte de dialogue Style :

- Style de ligne de bordure, sélectionnez le style de bordure comme solide, en pointillé, etc.
- Largeur de ligne de bordure, sélectionnez la largeur de la bordure en pixels.
- Couleur de la ligne de bordure, sélectionnez la couleur de la ligne.
- Lignes de bordure, sélectionnez la numérotation et le positionnement des lignes de bordure.

**Paramètres de bordure personnalisés** 

![todo:image_alt_text](format-cells_5.png)
### **Application des paramètres**
Cliquez sur **OK** dans la boîte de dialogue Style pour appliquer les changements.

**Paramètres de police et de bordure appliqués** 

![todo:image_alt_text](format-cells_6.png)


## **Mise en forme des cellules à l'aide de l'API**
Les cellules peuvent également être mises en forme de manière programmée avec l'API Aspose.Cells.GridWeb. Chaque cellule a une propriété Style, qui représente un objet GridTableItemStyle. Utilisez la propriété Style pour personnaliser les paramètres de police et de bordure.
### **Réglage de la police**
Pour personnaliser les paramètres de police de manière programmée :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule que vous formatez.
1. Accédez au style de la cellule.
1. Définissez la taille de la police en points.
1. Définir le style de police.
1. Définir les couleurs avant-plan et arrière-plan.
1. Définir l'alignement horizontal et vertical.
1. Rétablir le style par défaut de la cellule.

**Sortie : paramètres de police personnalisée affichés en A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Paramétrage des bordures**
Les bordures peuvent être appliquées à des cellules individuelles ou à une plage.
#### **Cellule unique**
Pour définir les bordures d'une seule cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule que vous souhaitez formater.
1. Accédez à l'objet Style de la cellule.
1. Définir le style de bordure.
1. Définir la largeur de la bordure en pixels.
1. Définir la couleur de la bordure.
1. Définir le style pour la cellule.

**Paramètres de bordure personnalisée sur une cellule unique** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Il est possible de définir des styles différents pour chaque ligne de bordure avec les propriétés Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle de la cellule.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Plage de cellules**
Pour définir des bordures sur une plage de cellules :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web
1. Accédez à une feuille de calcul souhaitée
1. Instanciez un objet de la classe WebBorderStyle
1. Définissez le style de la bordure sur Solide ou Pointillé, etc.
1. Définissez la largeur de la bordure en pixels
1. Définissez la couleur de la bordure
1. Appliquez les paramètres de bordure stockés dans l'objet WebBorderStyle à une plage spécifiée de cellules

**Une plage de cellules avec des paramètres de bordure personnalisés** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Réglage des formats de nombre**
Aspose.Cells.GridWeb prend en charge le réglage des formats de nombre. Il existe 59 formats de nombre intégrés. Pour les voir, veuillez consulter cette [liste des formats de nombre pris en charge](/cells/fr/net/aspose-cells-gridweb/list-of-supported-number-formats/).

Tous les formats de nombre intégrés se trouvent dans l'énumération NumberType. Pour utiliser un format de nombre intégré, définissez le NumberType à l'aide de la méthode SetNumberType d'un objet de cellule sur un format de nombre de l'énumération NumberType.

Pour définir un format de nombre personnalisé, utilisez la méthode SetCustom de la cellule.

**Paramètres de format de nombre appliqués sur B1 et B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
