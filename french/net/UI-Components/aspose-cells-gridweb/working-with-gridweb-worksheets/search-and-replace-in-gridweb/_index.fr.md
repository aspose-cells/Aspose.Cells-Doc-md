---
title: Recherche et Remplacement dans GridWeb
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/search-and-replace-in-gridweb/
keywords: GridWeb,recherche,remplacer
description: Cet article présente comment rechercher et remplacer dans GridWeb.
---

{{% alert color="primary" %}} 

Un des moyens les plus rapides pour apporter des modifications répétitives dans une grande feuille de calcul est d'utiliser la fonction de recherche et de remplacement. La fonction de recherche vous aide à localiser une chaîne de texte ou des données et le remplacement la substitue par une nouvelle valeur. Aspose.Cells.GridWeb fournit cette fonctionnalité. Elle vous permet de rechercher et de remplacer une chaîne de texte spécifique ou une valeur dans le client de feuille de calcul via une boîte de dialogue simple. Elle vous permet même de rechercher une donnée partielle.

{{% /alert %}} 
## **Travailler avec Rechercher/Remplacer**
### **La boîte de dialogue Rechercher/Remplacer**
Il y a deux façons d'ouvrir la boîte de dialogue Rechercher/Remplacer :

1. Lorsque le contrôle est actif, appuyez sur **CTRL+F** pour ouvrir la boîte de dialogue, ou appuyez sur la touche **CTRL+R** pour ouvrir la boîte de dialogue avec le bouton **Remplacer** activé.
1. Déplacez le curseur vers la zone de cellule dans la feuille de calcul, puis faites un clic droit. Sélectionnez **Rechercher** ou **Remplacer** dans le menu. 

   **Sélection de Rechercher** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




Une boîte de dialogue de style est affichée. 

**La boîte de dialogue Rechercher/Remplacer** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Utilisation de la recherche**
Pour rechercher:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer.
1. Tapez la chaîne que vous souhaitez rechercher dans le champ **Rechercher**.
1. Cliquez sur **Suivant** pour rechercher.

La prochaine cellule correspondant à votre critère de recherche est mise en surbrillance.

{{% alert color="primary" %}} 

Si votre critère de recherche n'est pas trouvé, une boîte de dialogue s'affiche pour vous informer.

{{% /alert %}} 
### **Options de Recherche**
Il existe des options de recherche que vous pouvez personnaliser dans la boîte de dialogue. Le tableau ci-dessous les répertorie.

|**N°** |**Nom de l'option** |**Description** |
| :- | :- | :- |
|1 |Respecter la casse |Indique si oui ou non respecter la casse lors de la recherche. |
|2 |Mot entier |Indique si l'option de correspondance doit être un mot entier lors de la recherche. |
|3 |Recherche ascendante |Indique si la recherche se fera du bas vers le haut. |
|4 |Expression régulière |Lorsqu'elle est cochée, le contrôle traitera la chaîne dans la zone de texte Rechercher comme une expression régulière dans le processus de recherche. |
|5 |Rechercher dans Formules/Valeurs |Si les Formules sont sélectionnées, le contrôle recherchera la formule ou la valeur non formatée des cellules si la formule ou la valeur non formatée est présente. Si les Valeurs sont sélectionnées, le contrôle ne recherchera que la valeur affichée des cellules. |
### **Utilisation de Remplacer**
Pour remplacer du texte ou des valeurs:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer en appuyant sur **CTRL+F**, ou sélectionnez un clic droit sur une cellule et sélectionnez **Rechercher** avant de cliquer sur **Remplacer**.
1. Tapez la chaîne de remplacement dans le champ **Remplacer par**.
1. Cliquez sur **Remplacer**.

Pour remplacer le texte :

1. Ouvrez la boîte de dialogue.
1. Entrez le texte que vous souhaitez trouver dans le champ **Rechercher** et le texte que vous souhaitez remplacer dans le champ **Remplacer par**.
1. Remplacez une occurrence à la fois en cliquant sur **Suivant** suivi de **Remplacer**.
1. Si vous êtes très sûr de ce que contient la feuille de calcul, cliquez sur **Remplacer tout**.

{{% alert color="primary" %}} 

Si la feuille de calcul n'est pas en mode édition, le bouton **Remplacer** n'est pas affiché.

{{% /alert %}}
