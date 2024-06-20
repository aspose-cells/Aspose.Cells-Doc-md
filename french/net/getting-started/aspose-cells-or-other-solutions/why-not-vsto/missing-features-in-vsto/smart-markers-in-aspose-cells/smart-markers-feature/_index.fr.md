---
title: Fonctionnalité des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/smart-markers-feature/
---

**Les marqueurs intelligents** sont utilisés pour informer Aspose.Cells des informations à placer dans une feuille de calcul Excel. Les marqueurs intelligents vous permettent de créer des modèles contenant uniquement des informations spécifiques et des mises en forme.
## **Feuille de calcul du Concepteur & Marqueurs intelligents**
Les feuilles de calcul du concepteur sont des fichiers Excel standard contenant un formatage visuel, des formules et des marqueurs intelligents. Elles peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations d'un projet et des informations pour des contacts associés. Les marqueurs intelligents sont écrits dans les cellules où vous souhaitez afficher les informations.

Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données donne lieu à plus d'un élément, par exemple, une ligne complète, alors les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place à toutes les nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez des formules dynamiques.

Les marqueurs intelligents se composent des parties **source de données** et **nom de champ** pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule tandis que les tableaux de variables peuvent en remplir plusieurs. Utilisez un seul marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Le marqueur intelligent peut également contenir des paramètres. Les paramètres permettent de modifier la manière dont les informations seront disposées. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme de liste séparée par des virgules.
### **Options de marqueur intelligent**
- &=NomSource.DeNomChamp
- &=Source de données.Nom de champ
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Paramètres**
Les paramètres suivants sont autorisés :

- noadd - Ne pas ajouter de rangées supplémentaires pour adapter les données.
- skip:n - Ignorer n rangées pour chaque rangée de données.
- ascending:n or descending:n - Trier les données dans les marqueurs intelligents. Si n vaut 1, alors la colonne est la première clé du trie. Les données sont triées après le traitement de la source de données. Par exemple, &=Table1.Field3(ascending:1).
- horizontal - Écrire les données de gauche à droite, au lieu de haut en bas.
- numeric - Convertir le texte en nombre si possible. Pris en charge uniquement dans la version .NET.
- shift - Décaler vers le bas ou la droite, en créant des rangées ou des colonnes supplémentaires pour adapter les données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans MS Excel, lorsque vous sélectionnez une plage de cellules, cliquez avec le bouton droit et sélectionnez Insérer, spécifiez le décalage vers le bas des cellules, décalage vers la droite et autres options. En résumé, le paramètre de décalage remplit la même fonction pour les marqueurs intelligents verticaux/normaux (haut vers le bas) ou horizontaux (gauche à droite).
- copystyle - Copier le style de la cellule de base dans toutes les cellules de cette colonne.

Les paramètres **noadd** et skip peuvent être combinés pour insérer des données sur des rangées alternées. Comme le modèle est traité de bas en haut, vous devez ajouter noadd sur la première rangée pour éviter que des rangées supplémentaires ne soient insérées avant la rangée alternative.
