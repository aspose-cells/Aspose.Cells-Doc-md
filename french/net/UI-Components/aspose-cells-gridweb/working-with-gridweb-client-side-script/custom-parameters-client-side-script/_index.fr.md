---
title: Personnaliser les paramètres d initialisation
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb, personnaliser, personnaliser les paramètres
description: comment personnaliser les paramètres d initialisation dans le script côté client Aspose.Cells.GridWeb.
---

{{% alert color="primary" %}} 

Les développeurs peuvent définir une valeur de paramètre d'initialisation différente pour effectuer un comportement différent pour le contrôle Aspose.Cells.GridWeb dans acwmain.js.  

{{% /alert %}} 

### **Paramètres**

|**Paramètre**|**Description**|
| :- | :- |
|needInitAlignmentAdjust| indique si l'alignement vertical du contenu de la cellule doit être effectué à l'initialisation, cela prendra du temps pour effectuer le travail d'alignement, si la feuille de calcul comporte de grandes cellules, les performances seront mauvaises, si l'utilisateur ne prête pas attention à l'alignement vertical, il peut le définir sur false, la valeur par défaut est true |
|focusinside| indique s'il faut se concentrer à l'intérieur de la plage de cellules, la valeur par défaut est true |
|copy_with_style| indique s'il faut copier avec style, la valeur par défaut est false, ce qui signifie qu'il ne copie que le contenu de la cellule|
|useESCAsLeave| le comportement par défaut lors de l'appui sur Echap fonctionne comme une opération d'annulation de modification sur la cellule, si nous définissons cette valeur sur true, nous le traiterons simplement comme un raccourci pour quitter la cellule sans revenir à la valeur précédente, et cela changera également le mode d'édition interne en mode d'édition rapide, la valeur par défaut est false|
|needValidateall| indique s'il faut valider toutes les validations sur la feuille active lors de la validation, (dans la page de contrôle aspx, définissez ForceValidation="True"). la valeur par défaut est false|
|scrollToInvalidate| indique s'il faut faire défiler et ramener la première cellule non valide dans la vue lorsque needValidateall est défini sur true. la valeur par défaut est true.|


Le résultat de l'exemple de code est montré ci-dessous.Veuillez consulter le [fichier Excel d'exemple](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
dans la façon d'édition interne - lorsque vous saisissez du texte, l'ancienne valeur de la cellule sera conservée   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
façon d'édition rapide - lorsque vous saisissez du texte, l'ancienne valeur de la cellule sera écrasée, si vous souhaitez éditer en fonction de l'ancienne valeur de la cellule, vous pouvez cliquer sur la cellule

![todo:image_alt_text](focus_inside_false.png)



