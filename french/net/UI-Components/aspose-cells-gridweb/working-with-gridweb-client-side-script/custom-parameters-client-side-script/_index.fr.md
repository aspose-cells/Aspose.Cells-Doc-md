---
title: Personnaliser les paramètres d'initialisation
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: comment personnaliser les paramètres d'initialisation dans le script côté client Aspose.Cells.GridWeb.
---
{{% alert color="primary" %}} 

 Les développeurs peuvent définir une valeur de paramètre d'initialisation différente pour effectuer un comportement différent pour le contrôle Aspose.Cells.GridWeb dans acwmain.js.

{{% /alert %}} 
 
### **Paramètres**
 
|**Paramètre**|**Description**|
|:- |:- |
|needInitAlignmentAdjust|s'il faut faire un alignement vertical pour le contenu de la cellule lors de l'initialisation, cela prendra un certain temps pour faire le travail d'alignement, si la feuille de calcul a de grandes cellules, les performances seront médiocres, si l'utilisateur ne se soucie pas de l'alignement vertical, alors il peut le régler sur être faux, la valeur par défaut est true|
|se concentrer à l'intérieur| s'il faut se concentrer à l'intérieur de la cellule, la valeur par défaut est true|
|copie_avec_style|s'il faut copier avec style, la valeur par défaut est false, ce qui signifie uniquement copier le contenu de la cellule|
|useESCAsLeave|le comportement par défaut lorsque vous appuyez sur esc fonctionne comme annuler l'opération d'édition sur la cellule, si nous définissons cette valeur sur true, nous la traiterons simplement comme une touche courte pour quitter la cellule sans revenir à la valeur précédente, et cela changera également le mode d'édition interne pour éditer rapidement, la valeur par défaut est false|
|besoinValidertout|s'il faut valider toutes les validations sur la feuille active lors de la validation, (dans la page de contrôle aspx, définissez ForceValidation="True") . la valeur par défaut est faux|
|scrollToInvalidate|s'il faut faire défiler et afficher la première cellule invalidée lorsque needValidateall est défini sur true.la valeur par défaut est true.|
 
 
 La sortie de l'exemple de code est illustrée ci-dessous, veuillez vérifier le[exemple de fichier excel](valign.xlsx):

**needInitAlignmentAdjust=true** 

![tâche : image_autre_texte](align_true.png)

**needInitAlignmentAdjust=false** 

![tâche : image_autre_texte](align_false.png)

**focusinside=vrai** 
 à l'intérieur de la manière d'éditer - lorsque vous entrez du texte, l'ancienne valeur de cellule sera toujours conservée

![tâche : image_autre_texte](focus_inside_true.png)

**focusinside=faux** 
méthode d'édition rapide - lorsque vous saisissez du texte, l'ancienne valeur de cellule sera écrasée, si vous souhaitez modifier en fonction de l'ancienne valeur de cellule, vous pouvez cliquer sur la cellule

![tâche : image_autre_texte](focus_inside_false.png)

 
 