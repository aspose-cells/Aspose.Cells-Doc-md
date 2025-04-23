---
title: Importation intelligente et placement de données avec des marqueurs intelligents
linktitle: Marqueurs intelligents
type: docs
weight: 190
url: /fr/net/using-smart-markers/
description: Importation intelligente et placement de données conforme aux fichiers Excel modèle avec la bibliothèque Aspose.Cells.
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
- **décaler** - Décaler vers le bas ou vers la droite, en créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, faites un clic droit et sélectionnez **Insérer** et spécifiez **décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. En bref, le paramètre **décaler** remplit la même fonction pour les marqueurs intelligents verticaux/normaux (haut en bas) ou horizontaux (gauche à droite).
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

Il est très facile de traiter les marqueurs intelligents. L'exemple de code suivant montre comment utiliser des formules dynamiques dans les marqueurs intelligents. Nous chargeons le [fichier modèle](templateDynamicFormulas.xlsx) et créons des données de test, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Utilisation de tableaux de variables**
L'exemple de code suivant montre comment utiliser des tableaux de variables dans les marqueurs intelligents. Nous plaçons un marqueur de tableau de variables dans la cellule A1 de la première feuille de travail du classeur de manière dynamique, qui contient une chaîne de valeurs que nous définissons pour le marqueur, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. Enfin, nous enregistrons le fichier Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Regroupement de données**
Dans certains rapports Excel, vous devrez peut-être fractionner les données en groupes pour les rendre plus faciles à lire et à analyser. L'un des principaux objectifs de la division des données en groupes est d'effectuer des calculs (effectuer des opérations de synthèse) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper des données par champs et de placer des lignes de synthèse entre les ensembles de données ou les groupes de données. Par exemple, si les données sont regroupées par Clients.ClientID, vous pouvez ajouter un enregistrement de synthèse chaque fois que le groupe change.
### **Paramètres**
Voici certains des paramètres de marqueurs intelligents utilisés pour le regroupement de données.
#### **group:normal/merge/repeat**
Nous supportons trois types de regroupement entre lesquels vous pouvez choisir.

- **normal** - La valeur du champ de regroupement ne se répète pas pour les enregistrements correspondants dans la colonne; au lieu de cela, elles sont imprimées une fois par groupe de données.
- **fusion** - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le champ de regroupement pour chaque jeu de groupe.
- **répéter** - La valeur du champ de regroupement est répétée pour les enregistrements correspondants.

Par exemple: &=Clients.ClientID(group:merge)
#### **skip**
Sauter un nombre spécifié de lignes après chaque groupe.

Par exemple, &=Employés.IDEmployé(group:normal,sauter:1)
#### **subtotalN**
Effectue une opération de synthèse pour des données de champ spécifié liées à un champ de regroupement. N représente des nombres entre 1 et 11 qui spécifient la fonction utilisée lors du calcul des sous-totaux dans une liste de données. (1=MOYENNE, 2=NB, 3=NBVAL, 4=MAX, 5=MIN,...9=SUM etc.) Référez-vous à la référence des sous-totaux dans l'aide de Microsoft Excel pour plus de détails.

Le format est en fait stipulé comme suit :
subtotalN:Réf où Réf correspond au champ de regroupement.

Par exemple,

- &=Produits.Unités(subtotal9:Produits.IDProduit) spécifie la fonction de synthèse sur le champ **Unités** par rapport au champ **IDProduit** dans la table **Produits**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) spécifie la fonction de synthèse sur le champ **Col3** groupé par **Col1** dans la table **Tabx**.
- &=Table1.ColonneD(subtotal9:Table1.ColonneA&Table1.ColonneB) spécifie la fonction de synthèse sur le champ **ColonneD** groupé par **ColonneA** et **ColonneB** dans la table **Table1**.

Cet exemple illustre certains des paramètres de regroupement en action. Il utilise la base de données Microsoft Access Northwind.mdb et extrait des données de la table nommée "Détails de commande". Nous créons un fichier de conception appelé SmartMarker_Designer.xls dans Microsoft Excel et plaçons des marqueurs intelligents dans différentes cellules des feuilles de calcul. Les marqueurs sont traités pour remplir les feuilles de calcul. Les données sont placées et organisées par un champ de regroupement.

Le fichier de conception comporte deux feuilles de calcul. Dans la première, nous plaçons des marqueurs intelligents avec des paramètres de regroupement comme indiqué dans la capture d'écran ci-dessous. Trois marqueurs intelligents (avec des paramètres de regroupement) sont placés :
&=[Order Details].OrderID(group:merge,skip:1),
&=[Détails de commande].Quantité(soustotal9:Détails de commande.IDCommande), et
&=[Détails de commande].PrixUnitaire(soustotal9:Détails de commande.IDCommande) vont dans A5, B5 et C5 respectivement.

|**La première feuille de travail dans le fichier SmartMarker_Designer.xls, complète avec des marqueurs intelligents**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Dans la deuxième feuille de calcul du fichier de conception, nous plaçons quelques autres marqueurs intelligents comme indiqué dans la figure ci-dessous. Nous plaçons les marqueurs intelligents suivants :
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), et
&=subtotal9:Détails de la commande.CommandeID dans A5, B5, C5, D5 et C6 respectivement.

|**La deuxième feuille de calcul du fichier SmartMarker_Designer.xls, montrant des marqueurs intelligents mixtes.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Voici le code source utilisé dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si vous avez besoin d'ajouter vos propres étiquettes personnalisées aux lignes de résumé ou si vous souhaitez concaténer le nom du champ avec une étiquette, par ex. "Sous-total des commandes", Aspose.Cells vous fournit les attributs Label et LabelPosition, vous pouvez donc placer vos étiquettes personnalisées dans les marqueurs intelligents tout en les concaténant avec les lignes de sous-total dans les données de regroupement. Consultez le document sur Comment Ajouter des Étiquettes Personnalisées à Concaténer avec les Lignes de Sous-total dans les Marqueurs Intelligents pour votre référence.

{{% /alert %}} 
## **Utilisation de types anonymes ou d'objets personnalisés**
Aspose.Cells prend également en charge les types anonymes ou les objets personnalisés dans les marqueurs intelligents. L'exemple suivant montre comment cela fonctionne. Pour importer des données à partir d'objets dynamiques à l'aide de Smart Markers, consultez l'article suivant :

[Importation à partir d'un objet dynamique en tant que source de données](/cells/fr/net/importer-des-donnees-dans-la-feuille-de-calcul/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Marqueurs d'image**
Les marqueurs intelligents d'Aspose.Cells prennent également en charge les marqueurs d'image. Cette section montre comment insérer des images à l'aide de marqueurs intelligents.
### **Paramètres de l'image**
Paramètres de marqueurs intelligents pour gérer les images.

- **Image:Ajusteràlacellule** - Ajuster automatiquement l'image à la hauteur de la ligne et à la largeur de la colonne de la cellule.
- **Image:EchelleN** - Adapter la hauteur et la largeur à N pour cent.
- **Image:Largeur:NpoetHauteur:Npoet** - Rendre l'image haute de N pouces et large de N pouces. Vous pouvez également spécifier les positions Gauche et Haut (en points).

Voici le code source utilisé dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Utilisation d'objets imbriqués**
Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples. Nous utilisons un fichier de modèle simple. Consultez la feuille de calcul de conception qui contient quelques marqueurs intelligents imbriqués.

|**La première feuille de calcul du fichier SM_NestedObjects.xlsx montrant des marqueurs intelligents imbriqués.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'exemple suivant montre comment cela fonctionne.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **Utilisation des données JSON**
Aspose.Cells supporte les données JSON dans les marqueurs intelligents, les données JSON peuvent être imbriquées hiérarchiquement. Veuillez vérifier [le fichier modèle](smartmarker.xlsx), [le fichier JSON](smartmarker.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier smartmarker.xlsx montrant les marqueurs intelligents.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Données JSON comme suit :
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}

## **Utiliser Generic List comme objet imbriqué**
Aspose.Cells prend désormais en charge l'utilisation d'une liste générique comme objet imbriqué. Veuillez vérifier la capture d'écran du fichier Excel généré avec le code suivant. Comme vous pouvez le voir dans la capture d'écran, un objet Teacher contient plusieurs objets Student imbriqués.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Utilisation de la propriété HTML des marqueurs intelligents**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Pas ligne par ligne**
La méthode de traitement par défaut actuelle consiste à traiter les marqueurs intelligents ligne par ligne. Mais parfois, les marqueurs intelligents de la même table de données doivent être traités ensemble, peu importe s'ils se trouvent dans la même ligne ou non, alors vous devez spécifier une plage nommée "_CellulesMarqueursIntelligents" et spécifier WorkbookDesigner.LineByLine comme faux avant d'appeler le traitement. 
s'ils sont dans la même ligne ou non, alors vous devez spécifier une plage nommée "_CellsSmartMarkers" et spécifier WorkbookDesigner.LineByLine comme faux avant d'appeler le traitement.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents**
Parfois, il peut être nécessaire de recevoir des notifications sur la référence de cellule ou le marqueur intelligent particulier en cours de traitement avant son achèvement. Cela peut être réalisé en utilisant la propriété WorkbookDesigner.CallBack et ISmartMarkerCallBack

## **Sujets avancés**
- [Ajouter un objet anonyme ou personnalisé dans les SmartMarkers](/cells/fr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Remplir automatiquement les données de Smart Marker dans d'autres feuilles de calcul si les données sont trop nombreuses](/cells/fr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatage des Smart Markers](/cells/fr/net/formatting-smart-markers/)
- [Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents](/cells/fr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Définir une source de données personnalisée pour WorkbookDesigner](/cells/fr/net/set-custom-datasource-for-workbookdesigner/)
- [Afficher une apostrophe de tête dans les cellules](/cells/fr/net/show-leading-apostrophe-in-cells/)
- [Utilisation du paramètre de formule dans le champ Smart Marker](/cells/fr/net/using-formula-parameter-in-smart-marker-field/)
- [Utilisation des marqueurs d'image lors du regroupement des données dans des marqueurs intelligents](/cells/fr/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
