---
title: Comment formater un nombre en pourcentage
type: docs
weight: 10
url: /fr/nodejs-cpp/how-to-format-number-to-percentage/
description: Cet article expliquera comment formater un nombre en pourcentage en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Convertir un nombre en format pourcentage, transformer des valeurs numériques en pourcentages, changer l affichage des nombres en pourcentages, formater les nombres en pourcentages, ajuster les chiffres numériques pour la représentation en pourcentage, formater un nombre en pourcentage
---

## **Scénarios d'utilisation possibles**
Le formatage des nombres en pourcentages dans Excel est une pratique courante pour plusieurs raisons, chacune améliorant la clarté, la précision et l'interprétation des données. Voici quelques-unes des principales raisons pour lesquelles vous pourriez formater des nombres en pourcentages dans Excel :

1. **Clarté et lisibilité** : Les pourcentages sont un format universellement compris qui peut rendre les données plus faciles à lire et à interpréter. En convertissant un décimal ou une fraction en pourcentage, vous indiquez immédiatement qu'il s'agit d'une partie d'un tout, ce qui peut être plus intuitif pour de nombreux utilisateurs.

2. **Cohérence** : Dans les rapports ou analyses de données impliquant des comparaisons, le formatage des nombres en pourcentage assure la cohérence. Cela est particulièrement important lorsque vous comparez des ratios ou des proportions entre différents ensembles de données. La cohérence dans la présentation des données aide à faire des comparaisons plus précises et des conclusions.

3. **Simplification** : Les pourcentages simplifient des informations complexes. Par exemple, dire "50 %" est plus simple et plus facile à comprendre pour la plupart des gens que "0.5" ou "1/2". Cette simplification est cruciale lorsqu'il s'agit de communiquer des données à un public qui n'a peut-être pas de formation technique.

4. **Visualisation** : Lors de la création de graphiques ou de diagrammes, les pourcentages peuvent rendre la visualisation des données plus efficace. Par exemple, les graphiques en secteurs représentent intrinsèquement des parties d'un tout et sont plus intuitifs lorsque les données sont formatées en pourcentages.

5. **Analyse et prise de décision** : Dans le monde des affaires et de la finance, les pourcentages sont souvent utilisés pour représenter la croissance, les marges bénéficiaires et d'autres indicateurs clés de performance (KPIs). Le formatage de ces nombres en pourcentages facilite l'analyse et la prise de décisions basées sur des métriques claires et compréhensibles.

6. **Gain de place** : Dans certains cas, formater les nombres en pourcentages peut économiser de l'espace dans votre document ou votre feuille de calcul, donnant un aspect plus propre et plus organisé. Cela est particulièrement utile dans les tableaux ou tableaux de bord où l'espace est limité.

7. **Usage éducatif et pédagogique** : Dans les contextes éducatifs, formater les nombres en pourcentages peut aider les étudiants à mieux comprendre les fractions, les ratios et les proportions. C'est une application pratique des concepts mathématiques.

Pour formater un nombre en pourcentage dans Excel, il suffit de sélectionner la ou les cellule(s) contenant vos données, puis de choisir l'option de format "Pourcentage", soit depuis l'onglet Accueil du ruban, soit en faisant un clic droit et en sélectionnant "Format de cellule". Excel affichera alors les nombres en pourcentages, en multipliant les valeurs décimales originales par 100 et en ajoutant un signe de pourcentage. Cette conversion automatique facilite les raisons mentionnées ci-dessus, rendant la gestion et la présentation des données plus efficaces et efficaces.

## **Comment formater un nombre en pourcentage dans Excel**
Formater des nombres en pourcentages dans Excel est une procédure simple qui peut être réalisée en quelques étapes. Voici comment faire :

### Utilisation du Ruban

1. **Sélectionner les cellules** : Tout d'abord, sélectionnez la ou les cellule(s) que vous souhaitez formater en pourcentage.
2. **Aller dans le ruban** : Regardez le ruban en haut d'Excel. Vous y trouverez un onglet intitulé "Accueil".
3. **Bouton de format pourcentage** : Dans l'onglet "Accueil", dans le groupe "Nombre", vous verrez un bouton avec un symbole "%". C'est le bouton "Format pourcentage".
4. **Appliquer le format pourcentage** : Cliquez sur le bouton "%". Excel formatera automatiquement les cellules sélectionnées en pourcentage, en multipliant la valeur de la cellule par 100 et en affichant un signe de pourcentage. Par exemple, si vous tapez "0,1" dans une cellule puis appliquez le format pourcentage, cela s'affichera sous forme de "10 %".

### Utilisation de la boîte de dialogue Format de cellules

1. **Sélectionner les cellules** : Mettez en surbrillance les cellules que vous souhaitez formater.
2. **Ouvrir la boîte de dialogue Format de cellules** : Faites un clic droit sur une des cellules sélectionnées et choisissez "Format de cellule" dans le menu contextuel. Alternativement, vous pouvez appuyer sur `Ctrl + 1` sur votre clavier pour ouvrir la boîte de dialogue Format de cellule.
3. **Sélectionner Pourcentage** : Dans la boîte de dialogue Format de cellules, cliquez sur l'onglet "Nombre" si ce n'est pas déjà sélectionné. Ensuite, dans la liste à gauche, cliquez sur "Pourcentage".
4. **Ajuster le nombre de décimales** : Vous pouvez ajuster le nombre de décimales que vous souhaitez afficher. Par exemple, si vous souhaitez afficher deux décimales, entrez "2" dans la case "Décimales".
5. **Appliquer** : Cliquez sur "OK" pour appliquer le format pourcentage. Vos cellules sélectionnées afficheront alors les valeurs en pourcentage.

### Utilisation d'une formule

Si vous entrez une formule ou souhaitez convertir un nombre existant en pourcentage dans une formule, vous pouvez simplement multiplier le nombre par 100 et ajouter le signe de pourcentage au format.

Par exemple, si vous avez une valeur dans la cellule A1 et que vous souhaitez l'afficher en pourcentage dans la cellule B1, vous pouvez utiliser la formule suivante dans B1 :

```excel
=A1*100 & "%"
```

Cependant, notez que cette méthode considère le résultat comme du texte plutôt que comme une valeur numérique formatée en pourcentage, ce qui pourrait affecter les calculs ultérieurs.

### Raccourci clavier

Pour un changement de format rapide sans utiliser la souris :
- Sélectionnez les cellules que vous souhaitez formater.
- Appuyez sur `Ctrl + Shift + %`. Cela appliquera le format pourcentage aux cellules sélectionnées.

N'oubliez pas que lorsque vous formatez un nombre en pourcentage, Excel multiplie essentiellement la valeur de la cellule par 100. Donc, si vous entrez des données que vous souhaitez afficher en pourcentage, vous devez l'entrer sous forme décimale (par exemple, entrez "0,1" pour 10%).

## **Comment formater un nombre en pourcentage dans Aspose.Cells for Node.js via C++**
Formatage des nombres en pourcentages dans Aspose.Cells for Node.js via C++, un processus simple. Aspose.Cells est une bibliothèque puissante qui vous permet de créer, manipuler et convertir des fichiers Excel dans des applications Node.js sans nécessiter l'installation de Microsoft Excel. Voici comment formater des nombres en pourcentages avec Aspose.Cells for Node.js via C++ :

### Étape 1 : Installer Aspose.Cells for Node.js via C++

Tout d'abord, assurez-vous que vous avez référencé Aspose.Cells for Node.js via C++ dans votre projet. Vous pouvez l'obtenir depuis le site Aspose.

### Étape 2 : Créer un nouveau classeur ou ouvrir un classeur existant

Vous pouvez soit créer un nouveau classeur, soit ouvrir un classeur existant. 


### Étape 3 : Accéder à la feuille de calcul

Vous devez accéder à la feuille de calcul où vous souhaitez formater les nombres en pourcentages. Si vous travaillez avec un nouveau classeur, vous utiliserez probablement la première feuille.

### Étape 4 : Appliquer le format de pourcentage

Pour formater une cellule ou une plage de cellules pour afficher les nombres en pourcentages, vous devrez définir le format de nombre du style de la cellule ou de la plage sur un format de pourcentage. Pour une plage de cellules, vous parcourez la plage et appliquez le style à chaque cellule individuellement.

### Étape 5 : Enregistrer le classeur

Enfin, enregistrez le classeur dans un fichier ou une stream.

### Code d'exemple

Voici un extrait de code illustrant ces étapes :
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToPercentage.js" >}}

### Conclusion

En suivant ces étapes, vous pouvez facilement formater des nombres en pourcentage dans Aspose.Cells for Node.js via C++. Aspose.Cells offre une large gamme de fonctionnalités pour manipuler les fichiers Excel, y compris le formatage des cellules, le travail avec des formules, et bien plus encore, en faisant un outil puissant pour les développeurs Node.js manipulant des données Excel.

{{< app/cells/assistant language="nodejs-cpp" >}}
