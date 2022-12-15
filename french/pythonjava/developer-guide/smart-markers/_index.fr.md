---
title: Importer et placer intelligemment des données avec des marqueurs intelligents dans Python via java
linktitle: Marqueurs intelligents
type: docs
weight: 190
url: /fr/python-java/using-smart-markers/
description: Importer et placer intelligemment des données selon les modèles de fichiers Excel avec Aspose.Cells for Python via la bibliothèque Java.
---
## **Introduction**
**Marqueurs intelligents**sont utilisés pour indiquer au Aspose.Cells quelles informations placer dans une feuille de calcul de concepteur Excel Microsoft. Les marqueurs intelligents vous permettent de créer des modèles contenant uniquement des informations et une mise en forme spécifiques.
## **Tableur Designer et marqueurs intelligents**
Les feuilles de calcul Designer sont des fichiers Excel standard qui contiennent une mise en forme visuelle, des formules et des marqueurs intelligents. Ils peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations d'un projet et des informations sur des contacts associés. Des marqueurs intelligents sont écrits dans les cellules où vous voulez les informations.

 Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données génère plusieurs éléments, par exemple une ligne complète, les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place aux nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez**formules dynamiques**.

 Les marqueurs intelligents consistent en**la source de données** et**nom de domaine**pièces pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule alors que les tableaux de variables peuvent en remplir plusieurs. N'utilisez qu'un marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Le marqueur intelligent peut également contenir des paramètres. Les paramètres permettent de modifier la présentation des informations. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme de liste séparée par des virgules.
### **Options de marqueur intelligent**
 &=DataSource.FieldName
 &=[Source de données].[Nom du champ]&=$NomVariable
 &=$VariableArray
 &==Formule Dynamique
&=&=RépéterDynamicFormula
### **Paramètres**
Les paramètres suivants sont autorisés :

- **pas d'ajout** - N'ajoutez pas de lignes supplémentaires pour ajuster les données.
- **sauter :n** - Sauter n nombre de lignes pour chaque ligne de données.
- **ascendant : n** ou**descendant:n** - Trier les données dans des marqueurs intelligents. Si n vaut 1, alors la colonne est la première clé du trieur. Les données sont triées après le traitement de la source de données. Par exemple : &=Table1.Field3(croissant : 1).
- **horizontal** - Écrivez les données de gauche à droite, au lieu de haut en bas.
- **numérique** - Convertissez le texte en nombre si possible.
- **décalage** - Maj vers le bas ou vers la droite, créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, cliquez avec le bouton droit et sélectionnez**Insérer** et précisez ?**décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. Bref, le**décalage** remplit la même fonction pour les marqueurs intelligents verticaux/normaux (de haut en bas) ou horizontaux (de gauche à droite).
- **style de copie** - Copiez le style de la cellule de base dans toutes les cellules de cette colonne.

Les paramètres noadd et skip peuvent être combinés pour insérer des données sur des lignes alternées. Étant donné que le modèle est traité de bas en haut, vous devez ajouter noadd sur la première ligne pour éviter que des lignes supplémentaires ne soient insérées avant l'autre ligne.

Si vous avez plusieurs paramètres, séparez-les par des virgules, mais sans espace : paramètreA, paramètreB, paramètreC

Les captures d'écran suivantes montrent comment insérer des données sur une ligne sur deux.

|**Fichier de modèle**|**Fichier de sortie**|
|:- |:- |
|![tâche : image_autre_texte](using-smart-markers_1.jpg)|![tâche : image_autre_texte](using-smart-markers_2.jpg)|
### **Formules dynamiques**
Les formules dynamiques vous permettent d'insérer des formules Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Les formules dynamiques peuvent se répéter pour chaque ligne insérée ou utiliser uniquement la cellule dans laquelle le marqueur de données est placé.

Les formules dynamiques permettent les options supplémentaires suivantes :

- r - Numéro de ligne actuel.
- 2, -1 - Décalage par rapport au numéro de ligne actuel.

Par exemple:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dans le marqueur de formule dynamique, "-1" indique le décalage par rapport à la ligne actuelle dans les colonnes B et C respectivement qui sera défini pour l'opération de division, le paramètre de saut est d'une ligne. De plus, nous devons spécifier le caractère suivant :

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

comme caractère de séparation pour appliquer d'autres paramètres dans les formules dynamiques.

Les captures d'écran suivantes illustrent une formule dynamique répétitive et la feuille de calcul Excel qui en résulte.

|**Fichier de modèle**|**Fichier de sortie**|
|:- |:- |
|![tâche : image_autre_texte](using-smart-markers_3.jpg)|![tâche : image_autre_texte](using-smart-markers_4.jpg)|
 Cell "C1" contient la formule**= A1*B1** , la cellule "C2" contient**= A2*B2** et la cellule "C3" contient**= A3*B3**.

Il est très facile de traiter les marqueurs intelligents. Ce qui suit est un extrait de code dans Python via Java, qui montre comment cela se fait.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "SmartMarker-SimpleProcess.py" >}}


