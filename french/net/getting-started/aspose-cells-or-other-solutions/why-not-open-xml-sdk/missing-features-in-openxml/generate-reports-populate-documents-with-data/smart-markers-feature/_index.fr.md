---
title: Fonction marqueurs intelligents dans Aspose.Cells
type: docs
weight: 30
url: /fr/net/smart-markers-feature-in-aspose-cells/
---
**Marqueurs intelligents** sont utilisés pour indiquer au Aspose.Cells quelles informations placer dans une feuille de calcul de concepteur Excel Microsoft. Les marqueurs intelligents vous permettent de créer des modèles contenant uniquement des informations et une mise en forme spécifiques.
## **Tableur Designer et marqueurs intelligents**
Les feuilles de calcul Designer sont des fichiers Excel standard qui contiennent une mise en forme visuelle, des formules et des marqueurs intelligents. Ils peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations d'un projet et des informations sur des contacts associés. Des marqueurs intelligents sont écrits dans les cellules où vous voulez les informations.

Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données génère plusieurs éléments, par exemple une ligne complète, les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place à toutes les nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez des formules dynamiques.

 Les marqueurs intelligents consistent en**la source de données** et**nom de domaine**pièces pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule alors que les tableaux de variables peuvent en remplir plusieurs. N'utilisez qu'un marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Le marqueur intelligent peut également contenir des paramètres. Les paramètres permettent de modifier la disposition des informations. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme de liste séparée par des virgules.
### **Options de marqueur intelligent**
- &=DataSource.FieldName
- &=Source de données.Nom du champ
- &=$NomVariable
- &=$VariableArray
- &==Formule Dynamique
- &=&=RépéterDynamicFormula
### **Paramètres**
Les paramètres suivants sont autorisés :

- noadd - N'ajoute pas de lignes supplémentaires pour ajuster les données.
- skip:n - Ignore n nombre de lignes pour chaque ligne de données.
- croissant:n ou décroissant:n - Trie les données dans des marqueurs intelligents. Si n vaut 1, alors la colonne est la première clé du trieur. Les données sont triées après le traitement de la source de données. Par exemple &=Table1.Field3(croissant : 1).
- horizontal - Ecrit les données de gauche à droite, au lieu de haut en bas.
- numérique - Convertit le texte en nombre si possible. Uniquement pris en charge dans la version .NET.
- shift - Maj vers le bas ou vers la droite, créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans MS Excel, lorsque vous sélectionnez une plage de cellules, cliquez avec le bouton droit de la souris et sélectionnez Insérer et spécifiez le décalage des cellules vers le bas, le décalage des cellules vers la droite et d'autres options. En bref, le paramètre de décalage remplit la même fonction pour les marqueurs intelligents verticaux/normaux (de haut en bas) ou horizontaux (de gauche à droite).
- copystyle - Copie le style de la cellule de base dans toutes les cellules de cette colonne.

 Les paramètres**pas d'ajout** et skip peuvent être combinés pour insérer des données sur des lignes alternées. Étant donné que le modèle est traité de bas en haut, vous devez ajouter noadd sur la première ligne pour éviter que des lignes supplémentaires ne soient insérées avant l'autre ligne.

Cette section comprend les rubriques suivantes

- [Regroupement des données en Aspose.Cells](/cells/fr/net/grouping-data-in-aspose-cells/)
- [Marqueurs d'image dans Aspose.Cells](/cells/fr/net/image-markers-in-aspose-cells/)
- [Utilisation de types anonymes ou d'objets personnalisés dans Aspose.Cells](/cells/fr/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Utilisation d'objets imbriqués dans Aspose.Cells](/cells/fr/net/using-nested-objects-in-aspose-cells/)
