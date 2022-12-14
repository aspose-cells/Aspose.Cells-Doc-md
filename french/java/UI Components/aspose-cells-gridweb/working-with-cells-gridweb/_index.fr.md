---
title: Travailler avec Cells GridWeb
type: docs
weight: 50
url: /fr/java/working-with-cells-gridweb/
---
## **Accéder à Cells dans la feuille de calcul**
Cette rubrique traite des cellules, en examinant la fonctionnalité la plus élémentaire de GridWeb : l'accès aux cellules.

Chaque feuille de calcul contient un objet GridCells, une collection d'objets GridCell. Un objet GridCell représente une cellule dans Aspose.Cells.GridWeb. Il est possible d'accéder à n'importe quelle cellule en utilisant GridWeb. Il existe deux méthodes préférées :

- [Accéder à la cellule par son nom](/cells/fr/java/working-with-cells-gridweb/).
- [Accéder aux indices de cellule par ligne et colonne](/cells/fr/java/working-with-cells-gridweb/).

Ci-dessous, chaque approche est discutée.
### **Utilisation du nom Cell**
Toutes les cellules ont un nom unique. Par exemple, A1, A2, B1, B2, etc. Aspose.Cells.GridWeb permet aux développeurs d'accéder à n'importe quelle cellule souhaitée en utilisant le nom de la cellule. Transmettez simplement le nom de la cellule (en tant qu'index) à la collection GridCells de GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Utilisation des indices de ligne et de colonne**
Une cellule peut également être reconnue par son emplacement en termes d'indices de ligne et de colonne. Passez simplement les indices de ligne et de colonne d'une cellule à la collection GridCells de GridWorksheet. Cette approche est plus rapide que la précédente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Accéder et modifier la valeur d'un Cell**
[Accéder à Cells dans la feuille de calcul](/cells/fr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) discuté de l'accès aux cellules. Cette rubrique étend cette discussion pour montrer comment accéder aux valeurs de cellule et les modifier à l'aide de GridWeb API.
### **Accéder et modifier la valeur d'un Cell**
#### **Valeurs de chaîne**
 Avant d'accéder et de modifier la valeur d'une cellule, vous devez savoir comment accéder aux cellules. Pour plus de détails sur les différentes approches d'accès aux cellules, reportez-vous à[Accéder à Cells dans la feuille de calcul](/cells/fr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Chaque cellule a une propriété nommée getStringValue(). Une fois qu'une cellule est accédée, les développeurs peuvent accéder à la méthode getStringValue() pour accéder à la valeur de chaîne des cellules.

{{% alert color="primary" %}} 

IMPORTANT : Cinq types de valeurs (Boolean, int, double, DateTime et string) peuvent être stockés dans des cellules, mais la ou les méthodes getValue()/setValue() ne peuvent être utilisées que pour accéder/modifier la valeur de l'objet.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Tous les types de valeurs**
Aspose.Cells.GridWeb fournit également une méthode spéciale, putValue, pour chaque cellule. Avec cette méthode, il est possible d'insérer ou de modifier tout type de valeur (booléen, entier, double, DateHeure et chaîne) dans une cellule.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Il existe également une version surchargée de la méthode putValue qui peut prendre n'importe quel type de valeur au format chaîne et la convertir automatiquement en un type de données approprié. Pour ce faire, passez la valeur booléenne true à un autre paramètre de la méthode putValue comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Ajout de formules au Cells**
La fonctionnalité la plus précieuse offerte par Aspose.Cells.GridWeb est la prise en charge des formules ou des fonctions. Aspose.Cells.GridWeb possède son propre moteur de formule qui calcule les formules dans les feuilles de calcul. Aspose.Cells.GridWeb prend en charge les fonctions ou formules intégrées et définies par l'utilisateur. Cette rubrique décrit en détail l'ajout de formules aux cellules à l'aide de Aspose.Cells.GridWeb API.
### **Comment ajouter et calculer une formule ?**
 Il est possible d'ajouter, d'accéder et de modifier des formules dans les cellules en utilisant la propriété Formule d'une cellule. Aspose.Cells.GridWeb prend en charge les formules définies par l'utilisateur allant du simple au complexe. Cependant, un grand nombre de fonctions ou de formules intégrées (similaires à Microsoft Excel) sont également fournies avec Aspose.Cells.GridWeb. Pour voir la liste complète des fonctions intégrées, veuillez vous référer à ce[liste des fonctions prises en charge.](/cells/fr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La syntaxe de la formule doit être compatible avec la syntaxe Excel Microsoft. Par exemple, toutes les formules doivent commencer par un signe égal (=).

Pour ajouter une formule par programme, Aspose.Cells.GridWeb la reconnaîtra comme une formule même si vous n'utilisez pas de signe **=**, mais si les utilisateurs finaux travaillant dans l'interface graphique doivent l'utiliser.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formule ajoutée à la cellule B3 mais non calculée par GridWeb** 

![tâche : image_autre_texte](working-with-cells-gridweb_1.png)

Dans la capture d'écran ci-dessus, vous pouvez voir qu'une formule a été ajoutée à B3 mais n'a pas encore été calculée. Pour calculer toutes les formules, appelez la méthode calculateFormula du contrôle GridWorksheetCollection après avoir ajouté des formules aux feuilles de calcul, comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Les utilisateurs peuvent également calculer des formules en cliquant sur**Soumettre**.

**En cliquant sur le bouton Soumettre de GridWeb** 

![tâche : image_autre_texte](working-with-cells-gridweb_2.png)

**IMPORTANT** : Si un utilisateur clique sur le**sauvegarder** ou**annuler** ou les onglets de la feuille, toutes les formules sont calculées automatiquement par GridWeb.

**Résultat de la formule après calcul** 

![tâche : image_autre_texte](working-with-cells-gridweb_3.png)
### **Référence Cells à partir d'autres feuilles de travail**
En utilisant Aspose.Cells.GridWeb, il est possible de référencer des valeurs stockées dans différentes feuilles de calcul dans leurs formules, créant ainsi des formules complexes.

La syntaxe pour référencer une valeur de cellule à partir d'une autre feuille de calcul est SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Créer une validation de données dans une GridCell de GridWeb**
 Aspose.Cells.GridWeb vous permet d'ajouter**La validation des données** en utilisant la méthode GridWorksheet.getValidations().add(). En utilisant cette méthode, vous devez spécifier le**Cell Gamme** . Mais si vous souhaitez créer une validation de données dans un seul GridCell, vous pouvez le faire directement en utilisant la méthode GridCell.createValidation(). De même, vous pouvez supprimer**La validation des données** à partir d'un GridCell à l'aide de la méthode GridCell.removeValidation().

 L'exemple de code suivant crée un**La validation des données** dans une cellule B3. Si vous entrez une valeur qui n'est pas comprise entre 20 et 40, la cellule B3 affichera**erreur de validation** sous la forme de**Rouge XXXX** comme le montre cette capture d'écran.

![tâche : image_autre_texte](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Création de boutons de commande personnalisés**
Aspose.Cells.GridWeb contient des boutons spéciaux tels que Soumettre, Enregistrer et Annuler. Tous ces boutons effectuent des tâches spécifiques pour Aspose.Cells.GridWeb. Il est également possible d'ajouter des boutons personnalisés qui effectuent des tâches personnalisées. Cette rubrique explique comment utiliser cette fonction.

L'exemple de code suivant explique comment créer un bouton de commande personnalisé et comment gérer son événement de clic. Vous pouvez utiliser n'importe quelle icône pour votre bouton de commande personnalisé. À des fins d'illustration, nous avons utilisé cette icône d'image.

![tâche : image_autre_texte](working-with-cells-gridweb_5.png)

 Comme vous pouvez le voir dans la capture d'écran suivante, lorsque l'utilisateur clique sur le bouton de commande personnalisé, il ajoute un texte dans la cellule A1 disant**"Mon bouton de commande personnalisé est cliqué."**

![tâche : image_autre_texte](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Gestion des événements du bouton de commande personnalisé**
L'exemple de code suivant explique comment effectuer la gestion des événements du bouton de commande personnalisé.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Mise en forme des cellules pour GridWeb**
### **Scénarios d'utilisation possibles**
GridWeb permet désormais aux utilisateurs de saisir des données de cellule au format de pourcentage comme 3 % et les données de la cellule seront automatiquement formatées en 3,00 %. Cependant, vous devrez définir le style de cellule sur Format de pourcentage qui est soit GridTableItemStyle.NumberType a 9 ou 10. Le nombre 9 formatera 3 % en 3 % mais le nombre 10 formatera 3 % en 3,00 %.

{{% alert color="primary" %}} 

Si vous n'avez pas défini le style de cellule sur Format de pourcentage, les données d'entrée 3 % s'afficheront sous la forme 0,03.

{{% /alert %}} 
### **Entrez les données Cell de la feuille de calcul GridWeb au format pourcentage**
L'exemple de code suivant définit la cellule A1 GridTableItemStyle.NumberType sur 10. Par conséquent, les données d'entrée 3 % sont automatiquement formatées en 3,00 %, comme indiqué dans la capture d'écran.

![tâche : image_autre_texte](working-with-cells-gridweb_7.png)
### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
