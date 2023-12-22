---
title: Utiliser des marqueurs intelligents
type: docs
weight: 40
url: /fr/java/using-smart-markers/
---
##  **Introduction**

{{% alert color="primary" %}}

**Marqueurs intelligents** sont utilisés pour indiquer à Aspose.Cells quelles informations placer dans un Excel Microsoft[feuille de calcul du concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/). Les marqueurs intelligents vous permettent de créer des modèles contenant uniquement les informations et le formatage pertinents.

{{% /alert %}}

##  **Feuille de calcul de conception et marqueurs intelligents**

Les feuilles de calcul Designer sont des fichiers Excel standard contenant un formatage visuel, des formules et des marqueurs intelligents. Ils peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations sur un projet et des informations sur des contacts associés. Des marqueurs intelligents sont écrits dans les cellules où vous souhaitez obtenir des informations.

Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données génère plusieurs éléments, par exemple une ligne complète, les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place aux nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez[formules dynamiques](/cells/fr/java/using-smart-markers/#dynamic-formulas).

 Les marqueurs intelligents sont constitués des**la source de données** et**nom de domaine** pièces pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule alors que les tableaux de variables peuvent en remplir plusieurs. N'utilisez qu'un seul marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Un marqueur intelligent peut également contenir des paramètres. Les paramètres vous permettent de modifier la façon dont les informations sont présentées. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme de liste séparée par des virgules.

###  **Options de marqueur intelligent**

&=DataSource.FieldName
&=[Source de données].[Nom du champ]
&=$NomVariable
&=$TableauVariable
&==Formule dynamique
&=&=RépéterFormule Dynamique

###  **Paramètres**

Les paramètres suivants sont autorisés :

- **pas d'ajout** - N'ajoutez pas de lignes supplémentaires pour ajuster les données.
- **sauter : n** - Sauter n nombre de lignes pour chaque ligne de données.
- *ascending:n ou descendant:n - Trie les données dans des marqueurs intelligents. Si n vaut 1, alors la colonne est la première clé du trieur. Les données sont triées après traitement de la source de données. Par exemple : &=Table1.Field3(ascending:1).
- **horizontal** - Écrivez les données de gauche à droite plutôt que de haut en bas.
- **numérique** - Convertissez le texte en nombre si possible.
- **changement** - Décalez vers le bas ou vers la droite, créant des lignes ou des colonnes supplémentaires pour adapter les données. Le paramètre shift fonctionne de la même manière que dans Excel Microsoft. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, cliquez avec le bouton droit et sélectionnez**Insérer** et préciser**décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. En bref, le paramètre shift remplit la même fonction pour les marqueurs intelligents verticaux/normaux (de haut en bas) ou horizontaux (de gauche à droite).
- **haricot** - Indique que la source de données est un simple POJO. Uniquement pris en charge dans le Java API.

Les paramètres noadd et skip peuvent être combinés pour insérer des données sur des lignes alternées. Étant donné que le modèle est traité de bas en haut, vous devez ajouter noadd sur la première ligne pour éviter que des lignes supplémentaires ne soient insérées avant la ligne alternative.

Si vous avez plusieurs paramètres, séparez-les par une virgule, mais pas d'espace : paramètreA,paramètreB,paramètreC

Les captures d'écran suivantes montrent comment insérer des données sur une ligne sur deux.

![tâche : image_alt_text](using-smart-markers_1.png)

**devient...**

![tâche : image_alt_text](using-smart-markers_2.png)

###  **Formules dynamiques**

Les formules dynamiques vous permettent d'insérer des formules Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Les formules dynamiques peuvent se répéter pour chaque ligne insérée ou utiliser uniquement la cellule où est placé le marqueur de données.

Les formules dynamiques autorisent les options supplémentaires suivantes :

- r - Numéro de ligne actuel.
- 2, -1 - Décalage par rapport au numéro de ligne actuel.

Ce qui suit illustre une formule dynamique répétitive et la feuille de calcul Excel résultante.

![tâche : image_alt_text](using-smart-markers_3.png)

**devient…**

![tâche : image_alt_text](using-smart-markers_4.png)

Cell C1 contient la formule =A1*B1, C2 contient = A2*B2 et C3 = A3*B3.

 Il est très simple de traiter les marqueurs intelligents. L'exemple de code suivant montre comment utiliser des formules dynamiques dans les marqueurs intelligents. Nous chargeons le[fichier modèle](templateDynamicFormulas.xlsx) et créez des données de test, traitez les marqueurs pour remplir les données dans les cellules en regard du marqueur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **Utiliser des tableaux de variables**

L'exemple de code suivant montre comment utiliser des tableaux de variables dans les marqueurs intelligents. Nous plaçons dynamiquement un marqueur de tableau variable dans la cellule A1 de la première feuille de calcul du classeur qui contient une chaîne de valeurs que nous définissons pour le marqueur, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. Enfin, nous sauvegardons le fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **Regroupement des données**

Dans certains rapports Excel, vous devrez peut-être diviser les données en groupes pour faciliter la lecture et l'analyse. L'un des principaux objectifs de la répartition des données en groupes est d'exécuter des calculs (effectuer des opérations récapitulatives) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper les données par ensemble de champs et de placer des lignes récapitulatives entre les ensembles de données ou les groupes de données. Par exemple, si vous regroupez des données par Customers.CustomerID, vous pouvez ajouter un enregistrement récapitulatif à chaque fois que le groupe change.

###  **Paramètres**

Voici quelques paramètres de marqueurs intelligents utilisés pour regrouper les données.

####  **groupe:normal/fusionner/répéter**

Nous prenons en charge trois types de groupes parmi lesquels vous pouvez choisir.

- **normale** - La valeur du regroupement par champ(s) n'est pas répétée pour les enregistrements correspondants dans la colonne ; au lieu de cela, ils sont imprimés une fois par groupe de données.
- **fusionner** - Même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules du groupe par champ(s) pour chaque ensemble de groupes.
- **répéter** - La valeur du regroupement par champ(s) est répétée pour les enregistrements correspondants.

Par exemple : &=Customers.CustomerID(group:merge)

####  **sauter**

Saute un nombre spécifique de lignes après chaque groupe.

Par exemple &=Employees.EmployeeID(group:normal,skip:1)

####  **sous-totalN**

Effectue une opération récapitulative pour les données d'un champ spécifié liées à un groupe par champ. Le N représente des nombres entre 1 et 11 qui spécifient la fonction utilisée lors du calcul des sous-totaux dans une liste de données. (1=MOYENNE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SUM etc.) Reportez-vous à la référence Sous-total dans l'aide d'Excel Microsoft pour plus de détails.

Le format indique en fait :
subtotalN:Ref où Ref fait référence au groupe par colonne.

Par exemple,

-  &=Products.Units(subtotal9:Products.ProductID) spécifie la fonction récapitulative lors**Unités** domaine par rapport à**ID produit** champ dans le**Des produits** tableau.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) spécifie la fonction de résumé lors du**Col3** groupe de champs par**Col1** dans le tableau *Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) spécifie la fonction récapitulative lors**ColonneD** groupe de champs par**ColonneA** et**ColonneB** dans le tableau *Tableau1**.

##  **Utiliser des objets imbriqués**

Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples.

Nous utilisons un simple fichier modèle. Consultez la feuille de calcul du concepteur qui contient des marqueurs intelligents imbriqués.

**La première feuille de calcul du fichier de concepteur affichant les marqueurs intelligents imbriqués.**

![tâche : image_alt_text](using-smart-markers_5.png)

L'exemple qui suit montre comment cela fonctionne. L’exécution du code ci-dessous donne le résultat ci-dessous.

**La première feuille de calcul du fichier de sortie affichant les données résultantes.**

![tâche : image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **Utilisation d'une liste générique comme objet imbriqué**

Aspose.Cells prend désormais également en charge l'utilisation d'une liste générique comme objet imbriqué. Veuillez vérifier la capture d'écran du fichier Excel de sortie généré avec le code suivant. Comme vous pouvez le voir sur la capture d'écran, un objet Enseignant contient plusieurs objets Étudiant imbriqués.

![tâche : image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **Utilisation de la propriété HTML des marqueurs intelligents**

L'exemple de code suivant explique l'utilisation de la propriété HTML des marqueurs intelligents. Lorsqu'il sera traité, il affichera "Monde" dans "Hello World" en gras à cause de HTML \<b> étiqueter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents**

 Parfois, il peut être nécessaire de recevoir des notifications concernant la référence de cellule ou le marqueur intelligent particulier en cours de traitement avant la fin. Ceci peut être réalisé en utilisant le[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)la propriété et[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Pour un exemple de code et une explication détaillée, veuillez consulter cet article.

- [Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents](/cells/fr/java/getting-notifications-while-merging-data-with-smart-markers/)
