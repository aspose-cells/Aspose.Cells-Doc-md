---
title: Importer et placer intelligemment des données avec des marqueurs intelligents
linktitle: Marqueurs intelligents
type: docs
weight: 190
url: /fr/net/using-smart-markers/
description: Importer et placer intelligemment des données selon les modèles de fichiers Excel avec la bibliothèque Aspose.Cells.
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
- **décalage** - Maj vers le bas ou vers la droite, créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, cliquez avec le bouton droit et sélectionnez**Insérer** et précisez**décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. Bref, le**décalage** remplit la même fonction pour les marqueurs intelligents verticaux/normaux (de haut en bas) ou horizontaux (de gauche à droite).
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

Il est très facile de traiter les marqueurs intelligents. Ce qui suit sont deux extraits de code, un en C# et un en VB, qui montrent comment cela se fait.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Utilisation de tableaux variables**
L'exemple de code suivant montre comment utiliser les tableaux de variables dans les marqueurs intelligents. Nous plaçons dynamiquement un marqueur de tableau variable dans la cellule A1 de la première feuille de calcul du classeur qui contient une chaîne de valeurs que nous avons définie pour le marqueur, traitons les marqueurs pour remplir les données dans les cellules contre le marqueur. Enfin, nous enregistrons le fichier Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Regroupement de données**
Dans certains rapports Excel, vous devrez peut-être diviser les données en groupes pour en faciliter la lecture et l'analyse. L'un des principaux objectifs de la répartition des données en groupes est d'exécuter des calculs (effectuer des opérations récapitulatives) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper les données par champs et de placer des lignes récapitulatives entre les ensembles de données ou les groupes de données. Par exemple, si vous regroupez des données par Customers.CustomerID, vous pouvez ajouter un enregistrement récapitulatif chaque fois que le groupe change.
### **Paramètres**
Voici quelques-uns des paramètres de marqueur intelligent utilisés pour regrouper les données.
#### **groupe : normal/fusionner/répéter**
Nous prenons en charge trois types de groupes parmi lesquels vous pouvez choisir.

- **Ordinaire** - La valeur de regroupement par champ(s) n'est pas répétée pour les enregistrements correspondants dans la colonne ; au lieu de cela, ils sont imprimés une fois par groupe de données.
- **fusionner** - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le(s) champ(s) grouper par pour chaque ensemble de groupe.
- **répéter** - La valeur de regroupement par champ(s) est répétée pour les enregistrements correspondants.

Par exemple : &=Customers.CustomerID(group:merge)
#### **sauter**
Ignore un nombre spécifié de lignes après chaque groupe.

Par exemple, &=Employees.EmployeeID(group:normal,skip:1)
#### **sous-totalN**
Effectue une opération récapitulative pour les données d'un champ spécifié liées à un groupe par champ. Le N représente des nombres entre 1 et 11 qui spécifient la fonction utilisée lors du calcul des sous-totaux dans une liste de données. (1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SUM etc.) Reportez-vous à la référence de sous-total dans l'aide d'Excel Microsoft pour plus de détails.

Le format indique en fait que :
subtotalN:Ref où Ref fait référence à la colonne group by.

Par exemple,

-  &=Products.Units(subtotal9:Products.ProductID) spécifie la fonction récapitulative lors**Unités** domaine par rapport à la**ID produit** champ dans le**Des produits** table.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) spécifie la fonction récapitulative sur le**Col3** groupe de champs par**Col1** dans la table**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) spécifie la fonction récapitulative sur**ColonneD** groupe de champs par**ColonneA** et**ColonneB** dans la table**Tableau 1**.

Cet exemple montre certains des paramètres de regroupement en action. Il utilise la base de données Access Northwind.mdb Microsoft et extrait les données de la table nommée "Détails de la commande". Nous créons un fichier de concepteur appelé SmartMarker_Designer.xls dans Microsoft Excel et plaçons des marqueurs intelligents dans diverses cellules des feuilles de calcul. Les marqueurs sont traités pour remplir les feuilles de travail. Les données sont placées et organisées par un champ de groupe.

Le fichier de concepteur comporte deux feuilles de calcul. Dans le premier, nous mettons des marqueurs intelligents avec des paramètres de regroupement, comme indiqué dans la capture d'écran ci-dessous. Trois marqueurs intelligents (avec des paramètres de regroupement) sont placés :
&=[Détails de la commande].ID de commande(groupe : fusionner, ignorer : 1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), et
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) va respectivement dans A5, B5 et C5.

|**La première feuille de calcul du fichier SmartMarker_Designer.xls, complète avec des marqueurs intelligents**|
|:- |
|![tâche : image_autre_texte](using-smart-markers_5.png)|
Dans la deuxième feuille de calcul du fichier de concepteur, nous mettons quelques marqueurs intelligents supplémentaires, comme indiqué dans la figure ci-dessous. Nous plaçons les marqueurs intelligents suivants :
&=[Détails de la commande].ID de commande(groupe :normal),
&=[Détails de la commande].Quantité,
&=[Détails de la commande].Prix unitaire,
&=&=B(r)*C(r), et
&=sous-total9 :Détails de la commande.ID de commande dans A5, B5, C5, D5 et C6 respectivement.

|**La deuxième feuille de calcul du fichier SmartMarker_Designer.xls, montrant des marqueurs intelligents mixtes.**|
|:- |
|![tâche : image_autre_texte](using-smart-markers_6.png)|
Voici le code source utilisé dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si vous devez ajouter vos propres étiquettes personnalisées aux lignes récapitulatives ou si vous souhaitez concaténer le nom du champ avec une étiquette, par exemple "Sous-total des commandes", Aspose.Cells vous fournit les attributs Label et LabelPosition, vous pouvez donc placer vos étiquettes personnalisées dans le Smart Marqueurs lors de la concaténation avec les lignes de sous-total dans le regroupement des données. Consultez le document sur la façon d'ajouter des étiquettes personnalisées à concaténer avec les lignes de sous-total dans les marqueurs intelligents pour votre référence.

{{% /alert %}} 
## **Utilisation de types anonymes ou d'objets personnalisés**
Aspose.Cells prend également en charge les types anonymes ou les objets personnalisés dans les marqueurs intelligents. L'exemple qui suit montre comment cela fonctionne. Pour importer des données à partir d'objets dynamiques à l'aide de marqueurs intelligents, consultez l'article suivant :

[Importation à partir d'un objet dynamique en tant que source de données](/cells/fr/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Marqueurs d'images**
Les marqueurs intelligents Aspose.Cells prennent également en charge les marqueurs d'image. Cette section vous montre comment insérer des images à l'aide de marqueurs intelligents.
### **Paramètres d'images**
Paramètres de marqueurs intelligents pour la gestion des images.

- **Image : Ajuster à la cellule** - Ajustez automatiquement l'image à la hauteur de ligne et à la largeur de colonne de la cellule.
- **Image : ÉchelleN** - Mettre à l'échelle la hauteur et la largeur à N pour cent.
- **Image : largeur : Nin et hauteur : Nin** - Rendez l'image N pouces de haut et N pouces de large. Vous pouvez également spécifier les positions Gauche et Haut (en points).

Voici le code source utilisé dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Utilisation d'objets imbriqués**
Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples. Nous utilisons un simple fichier modèle. Consultez la feuille de calcul du concepteur qui contient des marqueurs intelligents imbriqués.

|**La première feuille de calcul du fichier SM_NestedObjects.xlsx montrant les marqueurs intelligents imbriqués.**|
|:- |
|![tâche : image_autre_texte](using-smart-markers_7.png)|
L'exemple qui suit montre comment cela fonctionne.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Utilisation de la liste générique comme objet imbriqué**
Aspose.Cells prend désormais également en charge l'utilisation de la liste générique en tant qu'objet imbriqué. Veuillez vérifier la capture d'écran du fichier Excel de sortie généré avec le code suivant. Comme vous pouvez le voir sur la capture d'écran, un objet Enseignant contient plusieurs objets Étudiant imbriqués.

|![tâche : image_autre_texte](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Utilisation de la propriété HTML des marqueurs intelligents**
 L'exemple de code suivant explique l'utilisation de la propriété HTML des marqueurs intelligents. Lorsqu'il sera traité, il affichera "Monde" dans "Hello World" en gras à cause du HTML<b>étiquette.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Pas ligne par ligne**
 La méthode de traitement par défaut actuelle consiste à traiter smartmaker ligne par ligne. Mais parfois, les marqueurs intelligents d'une même table de données doivent être traités ensemble, peu importe
s'ils sont dans la même ligne ou non, vous devez spécifier une plage nommée "_CellsSmartMarkers" et spécifier WorkbookDesigner.LineByLine comme false avant d'appeler le traitement.

|![tâche : image_autre_texte](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Obtenir des notifications lors de la fusion de données avec des marqueurs intelligents**
Parfois, il peut être nécessaire d'obtenir les notifications concernant la référence de cellule ou le marqueur intelligent particulier en cours de traitement avant l'achèvement. Ceci peut être réalisé en utilisant la propriété WorkbookDesigner.CallBack et ISmartMarkerCallBack

## **Sujets avancés**
- [Ajout d'un objet anonyme ou personnalisé dans les SmartMarkers](/cells/fr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Remplir automatiquement les données du marqueur intelligent dans d'autres feuilles de calcul si les données sont trop volumineuses](/cells/fr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatage des marqueurs intelligents](/cells/fr/net/formatting-smart-markers/)
- [Obtenir des notifications lors de la fusion de données avec des marqueurs intelligents](/cells/fr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Définir une source de données personnalisée pour WorkbookDesigner](/cells/fr/net/set-custom-datasource-for-workbookdesigner/)
- [Afficher l'apostrophe de tête dans les cellules](/cells/fr/net/show-leading-apostrophe-in-cells/)
- [Utilisation du paramètre Formule dans le champ Smart Marker](/cells/fr/net/using-formula-parameter-in-smart-marker-field/)
- [Utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents](/cells/fr/net/using-image-markers-while-grouping-data-in-smart-markers/)


