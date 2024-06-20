---
title: Écrire un script côté client pour GridWeb
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Cet article présente comment travailler avec les api js client dans GridWeb.
---

{{% alert color="primary" %}} 

Les développeurs peuvent écrire des scripts côté client pour le contrôle Aspose.Cells.GridWeb. Cela signifie qu'il est possible d'appeler une fonction JavaScript côté client pour effectuer une tâche spécifique liée au contrôle GridWeb. Par exemple, les développeurs peuvent écrire des fonctions JavaScript pour soumettre les données de GridWeb à un serveur ou afficher un message d'alerte lorsqu'une erreur de validation se produit, etc.

Ce sujet explique cette fonctionnalité à l'aide d'exemples.

{{% /alert %}} 
## **Écriture de scripts côté client pour Aspose.Cells.GridWeb**
### **Informations de base**
Aspose.Cells.GridWeb fournit deux propriétés créées spécifiquement pour prendre en charge les scripts côté client :

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Créez des fonctions JavaScript dans une page ASPX et attribuez les noms de ces fonctions aux propriétés OnSubmitClientFunction et OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La fonction JavaScript qui sera attribuée à la propriété OnSubmitClientFunction doit être définie correctement comme indiqué ci-dessous:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

où le paramètre [arg] représente la commande générée par le contrôle. La commande peut être "Enregistrer", "Soumettre", "Annuler" etc. et le paramètre [cancelEdit] est une valeur booléenne qui indique si l'entrée de l'utilisateur est annulée ou non.

Toute fonction JavaScript assignée à la propriété OnSubmitClientFunction est appelée à chaque fois par le contrôle GridWeb avant de soumettre les données de GridWeb à un serveur. De même, si une fonction est assignée à la propriété OnValidationErrorClientFunction, alors cette fonction sera invoquée chaque fois qu'une erreur de validation se produit.

{{% /alert %}} 
### **Fonctions de script côté client**
Aspose.Cells.GridWeb expose également des fonctions spécialement pour le script côté client. Ces fonctions peuvent être utilisées dans des fonctions JavaScript pour obtenir plus de contrôle sur Aspose.Cells.GridWeb. Ces fonctions côté client comprennent les suivantes:

|**Fonctions**|**Description**|
| :- | :- |
|updateData(bool cancelEdit)|Met à jour toutes les données clientes d'Aspose.Cells.GridWeb avant de les poster sur le serveur. Si le paramètre cancelEdit est vrai, alors GridWeb ignore toutes les entrées de l'utilisateur.|
|validateAll()|Utilisé pour vérifier s'il y a des erreurs de validation dans l'entrée de l'utilisateur. S'il y a une erreur, la fonction renvoie false, sinon true.|
|submit(string arg, bool cancelEdit)|Appelez cette fonction pour envoyer les données au serveur. Cette fonction effectue les deux tâches, c'est-à-dire mettre à jour les données et valider l'entrée de l'utilisateur. Cette fonction peut également déclencher un événement de commande côté serveur. Utilisez le paramètre arg pour passer votre commande. Par exemple: la commande SAVE est utilisée pour cliquer sur le bouton **Enregistrer** dans la barre de commandes du contrôle GridWeb et la commande CCMD:MYCOMMAND déclenche un événement CustomCommand.|
|setActiveCell(int row, int column)|Utilisé pour activer une cellule spécifique.|
|setCellValue(int row, int column, string value)|Utilisé pour attribuer une valeur à n'importe quelle cellule spécifiée à l'aide de ses numéros de ligne et de colonne.|
|getCellValue(int row, int column)|Renvoie la valeur de n'importe quelle cellule spécifiée.|
|getActiveRow()|Utilisé en conjonction avec la fonction getActiveColumn() pour déterminer la position d'une cellule active.|
|getActiveColumn()|Utilisé en conjonction avec la fonction getActiveRow() pour déterminer la position d'une cellule active.|
|getSelectRange()|Renvoie la dernière plage sélectionnée.|
|setSelectRange()|Sélectionne la plage donnée.|
|clearSelections()|Efface toute la sélection à l'exclusion de la cellule active actuelle.|
|getCellsArray()|Il est utilisé avec d'autres fonctions connexes telles que getCellName(), getCellValueByCell(), getCellRow() et getCellColumn(). Veuillez lire cet article pour plus d'informations sur l'utilisation de cette fonction : [Lire les valeurs des cellules GridWeb côté client](/cells/fr/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Pour créer une application de test contenant des scripts côté client qui fonctionnent avec Aspose.Cells.GridWeb, suivez les étapes ci-dessous :

1. Créez des fonctions JavaScript à invoquer par GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Attribuez les noms des fonctions aux propriétés OnSubmitClientFunction et OnValidationErrorClientFunction.

La sortie de l'exemple de code est affichée ci-dessous :

**Une validation ajoutée à la cellule C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Ajoutez une valeur invalide et cliquez sur **Enregistrer**. Une erreur de validation se produit et la fonction ValidationErrorFunction est exécutée.

**La fonction ValidationErrorFunction est invoquée en cas d'erreur de validation** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Tant que vous n'avez pas saisi une valeur valide, aucune donnée n'est soumise au serveur. Saisissez une valeur valide et cliquez sur **Enregistrer**. La fonction ConfirmFunction est exécutée.

**La fonction ConfirmFunction est invoquée avant de soumettre les données de GridWeb au serveur** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
