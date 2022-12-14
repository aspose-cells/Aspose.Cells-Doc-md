---
title: Format Cells
type: docs
weight: 40
url: /fr/net/format-grid-cells/
---
{{% alert color="primary" %}} 

Cette rubrique fournit une discussion détaillée sur la mise en forme des cellules.

Il couvre le formatage des cellules en mode graphique à l'aide de la boîte de dialogue Style du contrôle Aspose.Cells.GridWeb. Il montre également comment formater des cellules par programmation. Différents paramètres de format comme la police, la bordure et le format numérique sont discutés, illustrés par des exemples.

{{% /alert %}} 
## **Formatage Cells à l'aide de la boîte de dialogue Style**
 Cells peut être formaté[par programmation](/cells/fr/net/format-cells/)mais le moyen le plus simple de formater des cellules dans le contrôle Aspose.Cells.GridWeb de manière WYSIWYG consiste à utiliser la boîte de dialogue Style.

Pour utiliser la boîte de dialogue Style :
 Sélectionnez une plage de cellules, puis cliquez avec le bouton droit et sélectionnez**Format Cell**. 

**Sélection du format Cell** 

![tâche : image_autre_texte](format-cells_1.png)



 La boîte de dialogue Style s'affiche.

**La boîte de dialogue Style est utilisée pour formater les cellules** 

![tâche : image_autre_texte](format-cells_2.png)

La boîte de dialogue Style permet aux utilisateurs de formater les cellules en personnalisant les paramètres de police et de bordure.
### **Personnalisation des paramètres de police**
Vous pouvez personnaliser les paramètres de police suivants à l'aide de la boîte de dialogue Style :

- Nom de la police, sélectionnez la police souhaitée dans la liste.
- Style de police, appliquez un style de police comme gras, italique, etc.
- Taille de police, sélectionnez une taille de police en points.
- Souligner, souligner le texte.
- Barré, appliquez un effet barré au texte.
- Alignement horizontal, sélectionnez l'alignement horizontal.
- Alignement vertical, sélectionnez l'alignement vertical.
- Couleur de police, sélectionnez une couleur de police.
- Arrière-plan, sélectionnez une couleur pour l'arrière-plan.

Vous pouvez vérifier les paramètres de police sélectionnés dans une petite zone d'aperçu.

**Paramètres de police personnalisés** 

![tâche : image_autre_texte](format-cells_3.png)
### **Personnalisation des paramètres de bordure**
Le contrôle permet également aux utilisateurs de dessiner une bordure autour des cellules en personnalisant les paramètres de bordure dans la boîte de dialogue Style.

Pour afficher les options liées aux bordures :
 Cliquez sur**Les frontières** dans la boîte de dialogue Style.
 Les options relatives aux bordures sont affichées.

**Options de bordure dans la boîte de dialogue de style** 

![tâche : image_autre_texte](format-cells_4.png)

Les options de bordure suivantes peuvent être sélectionnées dans la boîte de dialogue Style :

- Style de ligne de bordure, sélectionnez le style de bordure comme solide, pointillé, etc.
- Largeur de la bordure, sélectionnez la largeur de la bordure en pixels.
- Couleur de la ligne de bordure, sélectionnez la couleur de la ligne.
- Lignes de bordure, sélectionnez la numérotation et le positionnement des lignes de bordure.

**Paramètres de bordure personnalisés** 

![tâche : image_autre_texte](format-cells_5.png)
### **Application des paramètres**
 Cliquez sur**D'ACCORD** dans la boîte de dialogue Style pour appliquer les modifications.

**Paramètres de police et de bordure appliqués** 

![tâche : image_autre_texte](format-cells_6.png)


## **Formatage Cells Utilisation de API**
Cells peut également être formaté par programme avec le Aspose.Cells.GridWeb API. Chaque cellule a une propriété Style, qui représente un objet GridTableItemStyle. Utilisez la propriété Style pour personnaliser les paramètres de police et de bordure.
### **Définition de la police**
Pour personnaliser les paramètres de police par programmation :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule que vous formatez.
1. Accédez au style de la cellule.
1. Définissez la taille de la police en points.
1. Définissez le style de police.
1. Définissez les couleurs de premier plan et d'arrière-plan.
1. Définissez l'alignement horizontal et vertical.
1. Redéfinissez le style sur la cellule.

**Sortie : paramètres de police personnalisés affichés en A1** 

![tâche : image_autre_texte](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Définition des bordures**
Les bordures peuvent être appliquées à des cellules individuelles ou à une plage.
#### **Unique Cell**
Pour définir les bordures d'une seule cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule que vous êtes sur le point de formater.
1. Accédez à l'objet Style de la cellule.
1. Définissez le style de bordure.
1. Définissez la largeur de la bordure en pixels.
1. Définissez la couleur de la bordure.
1. Définissez le style de la cellule.

**Paramètres de bordure personnalisés sur une seule cellule** 

![tâche : image_autre_texte](format-cells_8.png)

{{% alert color="primary" %}} 

Il est possible de définir des styles différents pour chaque ligne de bordure avec les propriétés Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle de la cellule.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Gamme de Cells**
Pour définir des bordures sur une plage de cellules :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web
1. Accéder à une feuille de calcul souhaitée
1. Instancier un objet de la classe WebBorderStyle
1. Définissez le style de la bordure sur solide ou pointillé, etc.
1. Définir la largeur de la bordure en pixels
1. Définir la couleur de la bordure
1. Appliquer les paramètres de bordure stockés dans l'objet WebBorderStyle à une plage de cellules spécifiée

**Une plage de cellules avec des paramètres de bordure personnalisés** 

![tâche : image_autre_texte](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Définition des formats de nombre**
 Aspose.Cells.GridWeb prend en charge la configuration des formats de nombre. Il existe 59 formats numériques intégrés. Pour les voir, veuillez vous référer à ce[liste des formats numériques pris en charge](/cells/fr/net/list-of-supported-number-formats/).

Tous les formats numériques intégrés se trouvent dans l'énumération NumberType. Pour utiliser un format numérique intégré, définissez le NumberType à l'aide de la méthode SetNumberType de l'objet d'une cellule sur un format numérique de l'énumération NumberType.

Pour définir un format numérique personnalisé, utilisez la méthode SetCustom de la cellule.

**Paramètres de format de nombre appliqués sur B1 et B2** 

![tâche : image_autre_texte](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
