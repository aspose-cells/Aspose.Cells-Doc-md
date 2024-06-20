---
title: Fenêtre de l Éditeur de Formules
type: docs
weight: 20
url: /fr/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

L'Éditeur de Formules vous permet de créer des formules pour un rapport.

{{% /alert %}} 

Pour modifier une formule dans une cellule de Microsoft Excel :

1. Dans Microsoft Excel, sélectionnez une cellule.
1. Ouvrez la boîte de dialogue Modifier la formule en cliquant sur **Modifier la formule** dans la barre d'outils.
   ([Ajouter des Formules de Services de Rapport](/cells/fr/reportingservices/adding-reporting-services-formulas/) guide à travers un exemple qui modifie une formule.)
   La boîte de dialogue est divisée en section : la zone d'édition en haut, et la zone de formule en bas. Utilisez la zone de formule pour remplir la zone d'édition.
1. Sélectionnez une catégorie (utilisateur, paramètres, champs, etc.) dans la liste **Champs du Rapport** (la liste à main gauche).
1. Sélectionnez le type dans la liste **Fonctions** (au milieu).
1. Sélectionnez une option dans la liste **Opérateurs** (la liste à main droite).
1. Cliquez sur **Insérer** pour ajouter l'expression à la zone **Modifier**.
1. Cliquez sur **Insérer** lorsque l'expression est complète.
   La formule est insérée dans la cellule.

**La boîte de dialogue Modifier la Formule** 

![todo:image_alt_text](formula-editor-window_1.png)

La boîte de dialogue Modifier la Formule est divisée en sections, décrites ci-dessous.
#### **Zone d'Édition**
C'est l'endroit où vous créez ou modifiez une formule. Créez une formule en double-cliquant sur l'un des composants répertoriés dans les listes **Champs du Rapport**, **Fonctions** ou **Opérateurs**. Lorsque vous choisissez un composant, la syntaxe requise est également insérée. Vous pouvez également entrer manuellement une formule. 
#### **Zone de Formule**
La zone de formule contient trois sections, chacune répertoriant les informations utilisées pour construire une formule.

- Champs de rapport - la liste de gauche répertorie tous les champs de la base de données accessibles pour le rapport. Il répertorie également toutes les formules ou groupes déjà créés.
- Fonctions - La liste du milieu contient des fonctions, des procédures prédéfinies qui retournent des valeurs. Elles effectuent des calculs tels que MOYENNE, SOMME, NB, SIN, MAJUSCULE, etc.
- Opérateurs - les “verbes d'action” utilisés dans les formules. Les opérateurs décrivent une opération ou une action à effectuer entre deux valeurs ou plus. Exemples d'opérateurs : ajouter, soustraire, inférieur à et supérieur à, etc.
#### **Contrôles**
La boîte de dialogue comporte plusieurs contrôles :

|**Nom du bouton** |**Description** |
| :- | :- |
|Undo |Annule une action. |
|Paste |Colle une chaîne de caractères constituée des composants répertoriés dans la zone de formule dans la zone d'édition. |
|Insert |Prend la valeur dans la zone d'édition et l'insère en tant que formule dans une cellule. |
|Exit |Ferme l'Éditeur de formules. |
{{% alert color="primary" %}} 

Sujets connexes :

- [Liste de formules](/cells/fr/reportingservices/formula-list/) - une liste de champs et d'opérateurs.

{{% /alert %}}
