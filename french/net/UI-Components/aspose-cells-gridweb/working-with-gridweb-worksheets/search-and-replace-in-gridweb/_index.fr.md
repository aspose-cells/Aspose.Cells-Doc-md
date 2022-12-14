---
title: Rechercher et remplacer dans GridWeb
type: docs
weight: 90
url: /fr/net/search-and-replace-in-gridweb/
---
{{% alert color="primary" %}} 

L'un des moyens les plus rapides d'apporter des modifications répétitives dans une grande feuille de calcul consiste à utiliser la fonction Rechercher et remplacer. Find vous aide à localiser une chaîne de texte ou des données et replace les remplace par une nouvelle valeur. Aspose.Cells.GridWeb fournit cette fonctionnalité. Il vous permet de rechercher et de remplacer par une chaîne de texte ou une valeur spécifique dans la feuille de calcul côté client via une simple boîte de dialogue. Il vous permet même de rechercher des données partielles.

{{% /alert %}} 
## **Travailler avec Rechercher/Remplacer**
### **La boîte de dialogue Rechercher/Remplacer**
Il existe deux manières d'ouvrir la boîte de dialogue Rechercher/Remplacer :

1.  Lorsque la commande est active, appuyez sur**CTRL+F** pour ouvrir la boîte de dialogue, ou appuyez sur**CTRL+R** touche pour ouvrir la boîte de dialogue avec la**Remplacer** bouton activé.
1.  Déplacez le curseur vers la zone de cellule dans la feuille de calcul, puis cliquez avec le bouton droit. Sélectionner**Trouver** ou**Remplacer** du menu.

   **Sélection de Rechercher** 

![tâche : image_autre_texte](search-and-replace-in-gridweb_1.png)




 Une boîte de dialogue de style s'affiche.

**La boîte de dialogue Rechercher/Remplacer** 

![tâche : image_autre_texte](search-and-replace-in-gridweb_2.png)
### **Utilisation de la recherche**
Chercher:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer.
1.  Tapez la chaîne que vous souhaitez rechercher dans le champ**Trouver quoi** champ.
1.  Cliquez sur**Rechercher suivant** chercher.

La cellule suivante qui correspond à votre condition de recherche est mise en surbrillance.

{{% alert color="primary" %}} 

Si votre critère de recherche n'est pas trouvé, une boîte de dialogue s'affiche pour vous le signaler.

{{% /alert %}} 
### **Options de recherche**
Vous pouvez personnaliser certaines options de recherche dans la boîte de dialogue. Le tableau ci-dessous les répertorie.

|**Non.** |**Nom de l'option** |**La description** |
|:- |:- |:- |
|1 | Cas de correspondance| Indique s'il faut utiliser la sensibilité à la casse dans la recherche.|
|2 | Correspond à un mot entier| Indique si le mot entier doit correspondre à la recherche.|
|3 | Rechercher|Indique si la recherche se fera de bas en haut.|
|4 | Expression régulière| Lorsque cette case est cochée, le contrôle traitera la chaîne dans la zone de texte Rechercher comme une expression régulière dans le processus de recherche.|
|5 | Rechercher dans les formules/valeurs| Lorsque les formules sont sélectionnées, le contrôle correspondra à la formule ou à la valeur non formatée des cellules si la formule ou la valeur non formatée est présente. Lorsque les valeurs sont sélectionnées, le contrôle ne correspondra qu'à la valeur affichée des cellules.|
### **Utiliser Remplacer**
Pour remplacer du texte ou des valeurs :

1.  Ouvrez la boîte de dialogue Rechercher/Remplacer en appuyant sur**CTRL+F** , ou cliquez avec le bouton droit sur une cellule et sélectionnez**Trouver** avant de cliquer**Remplacer**.
1.  Tapez la chaîne de remplacement dans le champ**Remplacer par** champ.
1.  Cliquez sur**Remplacer**.

Pour remplacer du texte :

1. Ouvrez la boîte de dialogue.
1.  Entrez le texte que vous souhaitez rechercher dans le**Trouver quoi** champ, et le texte par lequel vous voulez le remplacer dans le**Remplacer par** champ.
1.  Remplacez une occurrence à la fois en cliquant sur**Rechercher suivant** suivie par**Remplacer**.
1.  Si vous êtes sûr du contenu de la feuille de calcul, cliquez sur**Remplace tout**.

{{% alert color="primary" %}} 

 Si la feuille de calcul n'est pas en mode édition, le**Remplacer** le bouton ne s'affiche pas.

{{% /alert %}}
