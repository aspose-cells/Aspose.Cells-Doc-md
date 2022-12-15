---
title: Fenêtre de l'éditeur de formules
type: docs
weight: 20
url: /fr/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

L'Editeur de formule vous permet de créer des formules pour un rapport.

{{% /alert %}} 

Pour modifier une formule dans une cellule Excel Microsoft :

1. Dans Microsoft Excel, sélectionnez une cellule.
1.  Ouvrez la boîte de dialogue Modifier la formule en cliquant sur**Modifier la formule** sur la barre d'outils.
   ([Ajout de formules Reporting Services](/cells/fr/reportingservices/adding-reporting-services-formulas/) passe en revue un exemple qui modifie une formule.)
 La boîte de dialogue est divisée en sections : la zone d'édition en haut et la zone de formule en bas. Utilisez la zone de formule pour remplir la zone d'édition.
1.  Sélectionnez une catégorie (utilisateur, paramètres, champs, etc.) dans la**Champs de rapport** liste (la liste de gauche).
1.  Sélectionnez le type dans le**Les fonctions** liste (au milieu).
1.  Sélectionnez une option dans la**Les opérateurs** liste (la liste de droite).
1.  Cliquez sur**Insérer**pour ajouter l'expression au**Éditer** Région.
1.  Cliquez sur**Insérer** lorsque l'expression est complète.
 La formule est insérée dans la cellule.

**La boîte de dialogue Modifier la formule** 

![tâche : image_autre_texte](formula-editor-window_1.png)

La boîte de dialogue Modifier la formule est divisée en sections, décrites ci-dessous.
#### **Modifier la zone**
 Il s'agit de la zone dans laquelle vous créez ou modifiez une formule. Créez une formule en double-cliquant sur l'un des composants répertoriés dans la**Champs de rapport**, **Les fonctions** ou**Les opérateurs** listes. Lorsque vous choisissez un composant, la syntaxe requise est également insérée. Vous pouvez également saisir manuellement une formule.
#### **Zone de formule**
La zone de formule contient trois sections, chacune répertoriant les informations utilisées pour créer une formule.

- Champs de rapport - la liste de gauche répertorie tous les champs de base de données accessibles pour le rapport. Il répertorie également toutes les formules ou tous les groupes déjà créés.
- Fonctions - la liste du milieu contient des fonctions, des procédures prédéfinies qui renvoient des valeurs. Ils effectuent des calculs tels que AVERAGE, SUM, COUNT, SIN, UPPERCASE, etc.
- Opérateurs - les "verbes d'action" utilisés dans les formules. Les opérateurs décrivent une opération ou une action devant avoir lieu entre deux ou plusieurs valeurs. Exemples d'opérateurs : ajouter, soustraire, inférieur à et supérieur à, etc.
#### **Les contrôles**
La boîte de dialogue comporte plusieurs contrôles :

|**Nom du bouton** |**La description** |
|:- |:- |
| annuler| Annule une action.|
| Pâte| Colle une chaîne de caractères composée des composants répertoriés dans la zone de formule dans la zone d'édition.|
| Insérer| Prend la valeur dans la zone d'édition et l'insère sous forme de formule dans une cellule.|
| Sortir| Ferme l'Editeur de formule.|
{{% alert color="primary" %}} 

Rubriques connexes:

- [Liste de formules](/cells/fr/reportingservices/formula-list/) - une liste de champs et d'opérateurs.

{{% /alert %}}
