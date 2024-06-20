---
title: Travailler avec les cellules GridWeb
type: docs
weight: 50
url: /fr/java/working-with-cells-gridweb/
---

## **Accéder aux cellules dans la feuille de calcul**
Ce sujet traite des cellules, en examinant la fonctionnalité la plus élémentaire de GridWeb : l'accès aux cellules.

Chaque feuille de calcul contient un objet GridCells, une collection d'objets GridCell. Un objet GridCell représente une cellule dans Aspose.Cells.GridWeb. Il est possible d'accéder à n'importe quelle cellule en utilisant GridWeb. Il existe deux méthodes préférées :

- [Accéder à la cellule par son nom](/cells/fr/java/working-with-cells-gridweb/).
- [Accéder à la cellule par les indices de ligne et de colonne](/cells/fr/java/working-with-cells-gridweb/).

Ci-dessous, chaque approche est discutée.
### **Utilisation du nom de la cellule**
Toutes les cellules ont un nom unique. Par exemple, A1, A2, B1, B2, etc. Aspose.Cells.GridWeb permet aux développeurs d'accéder à n'importe quelle cellule désirée en utilisant le nom de la cellule. Il suffit de passer le nom de la cellule (en tant qu'indice) à la collection GridCells de la GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Utilisation des Indices de Ligne & Colonne**
Une cellule peut également être identifiée par son emplacement en termes d'indices de ligne et de colonne. Il suffit de passer les indices de ligne et de colonne d'une cellule à la collection GridCells de la GridWorksheet. Cette approche est plus rapide que la précédente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Accès et Modification de la Valeur d'une Cellule**
[Accès aux Cellules dans la Feuille de Calcul](/cells/fr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) discute de l'accès aux cellules. Ce sujet étend cette discussion pour montrer comment accéder et modifier les valeurs des cellules en utilisant l'API GridWeb.
### **Accès & Modification de la Valeur d'une Cellule**
#### **Valeurs de Chaîne**
Avant d'accéder et de modifier la valeur d'une cellule, vous devez savoir comment accéder aux cellules. Pour plus de détails sur les différentes approches pour accéder aux cellules, consultez [Accéder aux Cellules dans la Feuille de Calcul](/cells/fr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Chaque cellule a une propriété nommée getStringValue(). Une fois qu'une cellule est accédée, les développeurs peuvent utiliser la méthode getStringValue() pour accéder à la valeur de la chaîne des cellules.

{{% alert color="primary" %}} 

IMPORTANT : Cinq types de valeurs (Booléen, entier, double, DateTime et chaîne) peuvent être stockés dans les cellules mais la(es) méthode(s) getValue()/setValue() ne peuvent être utilisées que pour accéder/modifier la valeur de l'objet.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Tous Types de Valeurs**
Aspose.Cells.GridWeb fournit également une méthode spéciale, putValue, pour chaque cellule. Avec cette méthode, il est possible d'insérer ou de modifier n'importe quel type de valeur (Booléen, entier, double, DateTime et chaîne) dans une cellule.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Il existe également une version surchargée de la méthode putValue qui peut prendre n'importe quel type de valeur au format chaîne et la convertir automatiquement en un type de données approprié. Pour que cela se produise, passez la valeur Booléen true à un autre paramètre de la méthode putValue comme le montre l'exemple ci-dessous.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Ajout de Formules aux Cellules**
La fonction la plus précieuse offerte par Aspose.Cells.GridWeb est le support des formules ou fonctions. Aspose.Cells.GridWeb possède son propre Moteur de Formules qui calcule les formules dans les feuilles de calcul. Aspose.Cells.GridWeb prend en charge les fonctions ou formules intégrées et définies par l'utilisateur. Ce sujet traite de l'ajout de formules aux cellules en utilisant l'API Aspose.Cells.GridWeb en détail.
### **Comment Ajouter & Calculer une Formule ?**
Il est possible d'ajouter, d'accéder et de modifier des formules dans les cellules en utilisant la propriété Formule d'une cellule. Aspose.Cells.GridWeb prend en charge les formules définies par l'utilisateur allant du simple au complexe. Cependant, un grand nombre de fonctions ou formules intégrées (similaires à Microsoft Excel) sont également fournies avec Aspose.Cells.GridWeb. Pour voir la liste complète des fonctions intégrées, veuillez vous référer à cette [liste de fonctions prises en charge.](/cells/fr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La syntaxe des formules doit être compatible avec la syntaxe de Microsoft Excel. Par exemple, toutes les formules doivent commencer par un signe égal (=).

Pour ajouter une formule de manière programmée, Aspose.Cells.GridWeb la reconnaîtra comme une formule même si vous n'utilisez pas de signe **=**, mais si les utilisateurs finaux travaillant dans l'interface graphique doivent l'utiliser.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formule ajoutée à la cellule B3 mais non calculée par GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

Sur la capture d'écran ci-dessus, vous pouvez voir qu'une formule a été ajoutée à B3 mais n'a pas encore été calculée. Pour calculer toutes les formules, appelez la méthode calculateFormula de la collection GridWorksheet de la commande GridWeb après avoir ajouté des formules aux feuilles de calcul comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Les utilisateurs peuvent également calculer des formules en cliquant sur **Soumettre**.

**Cliquez sur le bouton Soumettre de GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**IMPORTANT** : Si un utilisateur clique sur les boutons **Enregistrer** ou **Annuler**, ou sur les onglets de feuille, toutes les formules sont calculées automatiquement par GridWeb.

**Résultat de la formule après le calcul** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Référencer des cellules à partir d'autres feuilles de calcul**
En utilisant Aspose.Cells.GridWeb, il est possible de référencer des valeurs stockées dans différentes feuilles de calcul dans leurs formules, en créant des formules complexes.

La syntaxe pour référencer une valeur de cellule à partir d'une feuille de calcul différente est NomFeuille!NomCellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Créer une validation de données dans une cellule de GridWeb**
Aspose.Cells.GridWeb vous permet d'ajouter une **Validation de données** en utilisant la méthode GridWorksheet.getValidations().add(). En utilisant cette méthode, vous devez spécifier la **Plage de cellules**. Mais si vous souhaitez créer une validation de données dans une seule GridCell, vous pouvez le faire directement en utilisant la méthode GridCell.createValidation(). De la même manière, vous pouvez supprimer **Validation de données** d'une GridCell en utilisant la méthode GridCell.removeValidation().

Le code d'exemple suivant crée une **Validation de données** dans une cellule B3. Si vous saisissez une valeur qui n'est pas comprise entre 20 et 40, la cellule B3 affichera une **Erreur de validation** sous la forme de **XXXX rouge**, comme le montre cette capture d'écran.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Création de boutons de commande personnalisés**
Aspose.Cells.GridWeb contient des boutons spéciaux tels que Soumettre, Enregistrer et Annuler. Tous ces boutons effectuent des tâches spécifiques pour Aspose.Cells.GridWeb. Il est également possible d'ajouter des boutons personnalisés qui effectuent des tâches personnalisées. Ce sujet explique comment utiliser cette fonctionnalité.

Le code d'exemple suivant explique comment créer un bouton de commande personnalisé et comment gérer son événement de clic. Vous pouvez utiliser n'importe quelle icône pour votre bouton de commande personnalisé. À des fins d'illustration, nous avons utilisé cette icône.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Comme vous pouvez le voir dans la capture d'écran suivante, lorsque l'utilisateur clique sur le bouton de commande personnalisé, il ajoute un texte dans la cellule A1 disant **"Mon bouton de commande personnalisé est cliqué."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Gestion d'événements du bouton de commande personnalisé**
Le code d'exemple suivant explique comment effectuer la gestion d'événements du bouton de commande personnalisé.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formatage des cellules pour GridWeb**
### **Scénarios d'utilisation possibles**
GridWeb prend maintenant en charge la saisie des données de cellule au format pourcentage, comme 3 % et les données dans la cellule seront automatiquement formatées en 3,00 %. Cependant, vous devrez définir le style de la cellule au format pourcentage, qui est soit GridTableItemStyle.NumberType 9 ou 10. Le nombre 9 formatera 3 % en tant que 3 %, mais le nombre 10 formatera 3 % en tant que 3,00 %.

{{% alert color="primary" %}} 

Si vous n'avez pas défini le style de la cellule au format pourcentage, alors les données d'entrée 3 % s'afficheront comme 0,03.

{{% /alert %}} 
### **Saisir les données de cellule de la feuille de calcul GridWeb en format pourcentage**
Le code d'exemple suivant définit la cellule A1 GridTableItemStyle.NumberType comme 10, donc les données d'entrée 3 % seront automatiquement formatées en 3,00 % comme indiqué dans la capture d'écran.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
