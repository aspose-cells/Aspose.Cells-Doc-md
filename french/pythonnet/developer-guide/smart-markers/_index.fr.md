---
title: Importation intelligente et placement de données avec des marqueurs intelligents en Python via .Net
linktitle: Marqueurs intelligents
type: docs
weight: 190
url: /fr/python-net/using-smart-markers/
description: Importation et placement intelligents des données selon les fichiers Excel modèle avec Aspose.Cells pour Python via la bibliothèque .Net.
---

## **Introduction**
Les **marqueurs intelligents** sont utilisés pour informer Aspose.Cells des informations à placer dans une feuille de calcul Microsoft Excel. Les marqueurs intelligents vous permettent de créer des modèles contenant des informations spécifiques et un formatage uniquement.
## **Feuille de calcul du Concepteur & Marqueurs intelligents**
Les feuilles de calcul du concepteur sont des fichiers Excel standard contenant un formatage visuel, des formules et des marqueurs intelligents. Elles peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations d'un projet et des informations pour des contacts associés. Les marqueurs intelligents sont écrits dans les cellules où vous souhaitez afficher les informations.

Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données donne lieu à plusieurs éléments, par exemple une ligne complète, alors les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place pour les nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez des **formules dynamiques**.

Les marqueurs intelligents se composent des parties **source de données** et **nom de champ** pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule tandis que les tableaux de variables peuvent en remplir plusieurs. Utilisez un seul marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Le marqueur intelligent peut également contenir des paramètres. Les paramètres vous permettent de modifier comment les informations sont disposées. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme d'une liste séparée par des virgules.
### **Options de marqueur intelligent**
&=DataSource.FieldName 
&=[Source de donnée].[Nom du champ] 
&=$NomVariable 
&=$TableauVariable 
&==DynamicFormula 
&=&=RepeatDynamicFormula
### **Paramètres**
Les paramètres suivants sont autorisés :

- **noadd** - Ne pas ajouter de lignes supplémentaires pour s'adapter aux données.
- **skip:n** - Ignorer n lignes pour chaque ligne de données.
- **ascending:n** ou **descending:n** - Trier les données dans les marqueurs intelligents. Si n est 1, alors la colonne est la première clé du trieur. Les données sont triées après le traitement de la source de données. Par exemple : &=Table1.Field3(ascending:1).
- **horizontal** - Écrire les données de gauche à droite, au lieu du haut en bas.
- **numérique** - Convertir le texte en nombre si possible.
- **décalage** - Décaler vers le bas ou vers la droite, créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, faites un clic droit et sélectionnez **Insérer** et spécifiez? **décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. En bref, le paramètre **décalage** remplit la même fonction pour les marqueurs intelligents verticaux/normaux (du haut vers le bas) ou horizontaux (de gauche à droite).
- **copierstyle** - Copier le style de la cellule de base dans toutes les cellules de cette colonne.

Les paramètres noadd et skip peuvent être combinés pour insérer des données sur des lignes alternées. Étant donné que le modèle est traité de bas en haut, vous devriez ajouter noadd sur la première ligne pour éviter que des lignes supplémentaires ne soient insérées avant la ligne alternative.

Si vous avez plusieurs paramètres, séparez-les par des virgules, mais sans espace : paramètreA, paramètreB, paramètreC

Les captures d'écran suivantes montrent comment insérer des données sur chaque autre ligne.

|**Fichier modèle**|**Fichier de sortie**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Formules dynamiques**
Les formules dynamiques vous permettent d'insérer des formules Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Les formules dynamiques peuvent se répéter pour chaque ligne insérée ou utiliser uniquement la cellule où le marqueur de données est placé.

Les formules dynamiques permettent les options supplémentaires suivantes :

- r - Numéro de ligne actuelle.
- 2, -1 - Décalage par rapport au numéro de ligne actuelle.

Par exemple:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dans le marqueur de formule dynamique, "-1" désigne le décalage par rapport à la ligne actuelle dans les colonnes B et C respectivement, qui sera défini pour l'opération de division, le paramètre de saut est d'une ligne. De plus, nous devons spécifier le caractère suivant:

{{< highlight java >}}

 "~"

{{< /highlight >}}

comme caractère de séparateur pour appliquer d'autres paramètres dans les formules dynamiques.

Les captures d'écran suivantes illustrent une formule dynamique répétitive et la feuille de calcul Excel résultante.

|**Fichier Modèle**|**Fichier de Sortie**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
La cellule "C1" contient la formule **= A1*B1**, la cellule "C2" contient **= A2*B2** et la cellule "C3" contient **= A3*B3**.

Il est très facile de traiter les marqueurs intelligents. Voici un extrait de code en Python via .Net, montrant comment cela est fait.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


