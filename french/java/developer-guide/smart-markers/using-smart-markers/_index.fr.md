---
title: Utilisation des Smart Markers
type: docs
weight: 40
url: /fr/java/using-smart-markers/
---

## **Introduction**

{{% alert color="primary" %}}

**Les smart markers** sont utilisés pour permettre à Aspose.Cells de savoir quelles informations placer dans une feuille de calcul [designer Excel](/cells/fr/java/what-is-a-designer-spreadsheet/). Les smart markers vous permettent de créer des modèles qui ne contiennent que des informations pertinentes et une mise en forme.

{{% /alert %}}

## **Feuille de calcul du Concepteur & Marqueurs intelligents**

Les feuilles de calcul de conception sont des fichiers Excel standards qui contiennent une mise en forme visuelle, des formules et des smart markers. Ils peuvent contenir des smart markers qui font référence à une ou plusieurs sources de données, telles que des informations provenant d'un projet et des informations pour des contacts connexes. Les smart markers sont écrits dans les cellules où vous souhaitez des informations.

Tous les smart markers commencent par &=. Un exemple d'un marqueur de données est &=Party.FullName. Si le marqueur de données donne lieu à plus d'un élément, par exemple, une ligne complète, les lignes suivantes sont déplacées vers le bas automatiquement pour faire de la place pour les nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez les [formules dynamiques](/cells/fr/java/using-smart-markers/#dynamic-formulas).

Les marqueurs intelligents se composent des parties **source de données** et **nom de champ** pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule tandis que les tableaux de variables peuvent en remplir plusieurs. Utilisez un seul marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Un smart marker peut également contenir des paramètres. Les paramètres vous permettent de modifier la façon dont les informations sont disposées. Ils sont ajoutés à la fin du marqueur de données entre parenthèses sous forme d'une liste séparée par des virgules.

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
- *ascendant:n ou descendant:n - Trier les données dans les smart markers. Si n vaut 1, la colonne est la première clé du trieur. Les données sont triées après le traitement de la source de données. Par exemple : &=Table1.Champ3(ascendant:1).
- **horizontal** - Écrire les données de gauche à droite, au lieu du haut en bas.
- **numérique** - Convertir le texte en nombre si possible.
- **décalage** - Décaler vers le bas ou vers la droite, en créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, faites un clic droit et sélectionnez **Insérer** et spécifiez **décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. En résumé, le paramètre de décalage remplit la même fonction pour les smart markers verticaux/normaux (de haut en bas) ou horizontaux (de gauche à droite).
- **bean** - Indique que la source de données est un simple POJO. Uniquement pris en charge dans l'API Java.

Les paramètres noadd et skip peuvent être combinés pour insérer des données sur des lignes alternées. Comme le modèle est traité de bas en haut, vous devez ajouter noadd sur la première ligne pour éviter l'insertion de lignes supplémentaires avant la ligne alternative.

Si vous avez plusieurs paramètres, séparez-les par une virgule, mais sans espace : paramètreA,paramètreB,paramètreC

Les captures d'écran suivantes montrent comment insérer des données sur chaque autre ligne.

![todo:image_alt_text](using-smart-markers_1.png)

**devient...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Formules dynamiques**

Les formules dynamiques vous permettent d'insérer des formules Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Les formules dynamiques peuvent se répéter pour chaque ligne insérée ou utiliser uniquement la cellule où le marqueur de données est placé.

Les formules dynamiques permettent les options supplémentaires suivantes :

- r - Numéro de ligne actuelle.
- 2, -1 - Décalage par rapport au numéro de ligne actuelle.

L'exemple suivant illustre une formule dynamique répétitive et la feuille de calcul Excel résultante.

![todo:image_alt_text](using-smart-markers_3.png)

**devient...**

![todo:image_alt_text](using-smart-markers_4.png)

La cellule C1 contient la formule =A1*B1, C2 contient = A2*B2 et C3 = A3*B3.

Il est très facile de traiter les marqueurs intelligents. L'exemple de code suivant montre comment utiliser des formules dynamiques dans les marqueurs intelligents. Nous chargeons le [fichier modèle](templateDynamicFormulas.xlsx) et créons des données de test, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Utilisation de tableaux de variables**

Le code d'exemple suivant montre comment utiliser des tableaux de variables dans les marqueurs intelligents. Nous plaçons un marqueur de tableau de variables dans la cellule A1 de la première feuille de calcul du classeur de manière dynamique, qui contient une chaîne de valeurs que nous définissons pour le marqueur, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. Enfin, nous sauvegardons le fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Regroupement de données**

Dans certains rapports Excel, vous devrez peut-être fractionner les données en groupes pour les rendre plus faciles à lire et à analyser. L'un des principaux objectifs de la division des données en groupes est d'effectuer des calculs (effectuer des opérations de synthèse) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper les données par des champs définis et de placer des lignes de synthèse entre les ensembles de données ou les groupes de données. Par exemple, si vous regroupez les données par Clients.CustomerID, vous pouvez ajouter un enregistrement de synthèse à chaque fois que le groupe change.

### **Paramètres**

Voici quelques paramètres de marqueurs intelligents utilisés pour regrouper les données.

#### **group:normal/merge/repeat**

Nous supportons trois types de regroupement entre lesquels vous pouvez choisir.

- **normal** - La valeur du champ de regroupement ne se répète pas pour les enregistrements correspondants dans la colonne; au lieu de cela, elles sont imprimées une fois par groupe de données.
- **fusion** - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le champ de regroupement pour chaque jeu de groupe.
- **répéter** - La valeur du champ de regroupement est répétée pour les enregistrements correspondants.

Par exemple: &=Clients.ClientID(group:merge)

#### **skip**

Ignore un nombre spécifique de lignes après chaque groupe.

Par exemple &=Employés.EmployeeID(groupe:normal,saute:1)

#### **subtotalN**

Effectue une opération de synthèse pour des données de champ spécifié liées à un champ de regroupement. N représente des nombres entre 1 et 11 qui spécifient la fonction utilisée lors du calcul des sous-totaux dans une liste de données. (1=MOYENNE, 2=NB, 3=NBVAL, 4=MAX, 5=MIN,...9=SUM etc.) Référez-vous à la référence des sous-totaux dans l'aide de Microsoft Excel pour plus de détails.

Le format est en fait stipulé comme suit :
subtotalN:Réf où Réf correspond au champ de regroupement.

Par exemple,

- &=Produits.Unités(subtotal9:Produits.IDProduit) spécifie la fonction de synthèse sur le champ **Unités** par rapport au champ **IDProduit** dans la table **Produits**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) spécifie la fonction de synthèse sur le champ **Col3** groupé par **Col1** dans la table **Tabx**.
- &=Table1.ColonneD(sous-total9:Table1.ColonneA&Table1.ColonneB) spécifie la fonction de synthèse sur le champ **ColonneD** regroupé par **ColonneA** et **ColonneB** dans la table **Table1**.

## **Utilisation d'objets imbriqués**

Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples.

Nous utilisons un fichier de modèle simple. Consultez la feuille de calcul du concepteur qui contient certains marqueurs intelligents imbriqués.

**La première feuille de calcul du fichier modèle montrant des marqueurs intelligents imbriqués.**

![todo:image_alt_text](using-smart-markers_5.png)

L'exemple qui suit montre comment cela fonctionne. L'exécution du code ci-dessous donne le résultat ci-dessous.

**La première feuille de calcul du fichier de sortie montrant les données résultantes.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Utiliser Generic List comme objet imbriqué**

Aspose.Cells prend désormais également en charge l'utilisation d'une liste générique en tant qu'objet imbriqué. Veuillez vérifier la capture d'écran du fichier Excel de sortie généré avec le code suivant. Comme vous pouvez le voir dans la capture d'écran, un objet Enseignant contient plusieurs objets étudiants imbriqués.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Utilisation de la propriété HTML des marqueurs intelligents**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents**

Parfois, il peut être nécessaire de recevoir des notifications sur la référence de cellule ou le marqueur intelligent particulier en cours de traitement avant la fin. Cela peut être réalisé en utilisant la [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) propriété et [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack).

Pour un exemple de code et une explication détaillée, veuillez consulter cet article.

- [Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents](/cells/fr/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
