---
title: Écrire le script côté client GridWeb
type: docs
weight: 10
url: /fr/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Les développeurs peuvent écrire des scripts côté client pour le contrôle Aspose.Cells.GridWeb. Cela signifie qu'il est possible d'invoquer une fonction JavaScript côté client pour effectuer une tâche spécifique liée au contrôle GridWeb. Par exemple, les développeurs peuvent écrire des fonctions JavaScript pour soumettre des données GridWeb à un serveur ou afficher un message d'alerte lorsqu'une erreur de validation se produit, etc.

Cette rubrique explique cette fonctionnalité à l'aide d'exemples.

{{% /alert %}} 
## **Écriture de scripts côté client pour Aspose.Cells.GridWeb**
### **Informations de base**
Aspose.Cells.GridWeb fournit deux propriétés créées spécifiquement pour prendre en charge les scripts côté client :

- OnSubmitClientFunctionOnSubmitClientFunction
- OnValidationErrorClientFunctionOnValidationErrorClientFunction

Créez des fonctions JavaScript dans une page ASPX et affectez les noms de ces fonctions aux propriétés OnSubmitClientFunction et OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La fonction JavaScript qui sera affectée à la propriété OnSubmitClientFunction doit être définie correctement comme indiqué ci-dessous :

**Javascript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

où le paramètre [arg] représente la commande générée par le contrôle. La commande peut être "Save", "Submit", "Undo" etc. et le paramètre [cancelEdit] est une valeur booléenne, qui indique si l'entrée utilisateur est annulée ou non.

Toute fonction JavaScript affectée à la propriété OnSubmitClientFunction est appelée à chaque fois par le contrôle GridWeb avant de soumettre des données GridWeb à un serveur. De même, si une fonction est affectée à la propriété OnValidationErrorClientFunction, cette fonction sera invoquée chaque fois qu'une erreur de validation se produit.

{{% /alert %}} 
### **Fonctions pour les scripts côté client**
Aspose.Cells.GridWeb expose également des fonctions spécialement pour les scripts côté client. Ces fonctions peuvent être utilisées dans les fonctions JavaScript pour mieux contrôler Aspose.Cells.GridWeb. Ces fonctions côté client incluent les éléments suivants :

|**Les fonctions**|**La description**|
|:- |:- |
|updateData(bool annulerModifier)|Met à jour toutes les données client de Aspose.Cells.GridWeb avant de les publier sur le serveur. Si le paramètre cancelEdit est vrai, GridWeb ignore toutes les entrées de l'utilisateur.|
|validerTout()|Utilisé pour vérifier s'il y a des erreurs de validation dans l'entrée de l'utilisateur. S'il y a une erreur, la fonction renvoie false, sinon true .|
|soumettre(chaîne arg, bool annulerModifier)|Appelez cette fonction pour publier ou soumettre des données au serveur. Cette fonction exécute à la fois les tâches de mise à jour des données et de validation des entrées utilisateur. Cette fonction peut également déclencher un événement de commande côté serveur. Utilisez le paramètre arg pour transmettre votre commande. Par exemple : la commande ENREGISTRER est utilisée pour cliquer sur le**sauvegarder** dans la barre de commandes du contrôle GridWeb et la commande CCMD:MYCOMMAND déclenche un événement CustomCommand.|
|setActiveCell(int ligne, int colonne)|Utilisé pour activer une cellule spécifique.|
|setCellValue (ligne int, colonne int, valeur de chaîne)|Utilisé pour attribuer une valeur à n'importe quelle cellule spécifiée à l'aide de ses numéros de ligne et de colonne.|
|getCellValue (int ligne, int colonne)|Renvoie la valeur de toute cellule spécifiée.|
|getActiveRow()|Utilisé conjointement avec la fonction getActiveColumn() pour déterminer la position d'une cellule active.|
|getActiveColumn()|Utilisé conjointement avec la fonction getActiveRow() pour déterminer la position d'une cellule active.|
|getSelectRange()|Renvoie la dernière plage sélectionnée.|
|setSelectRange()|Sélectionne la plage donnée.|
|clearSelections()|Efface toute la sélection à l'exception de la cellule active actuelle.|
|getCellsArray()| Il est utilisé avec d'autres fonctions connexes telles que getCellName(), getCellValueByCell(), getCellRow() et getCellColumn(). Veuillez lire cet article pour plus d'informations concernant l'utilisation de cette fonction :[Lire les valeurs des cellules GridWeb côté client](/cells/fr/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Pour créer une application de test contenant des scripts côté client qui fonctionnent avec Aspose.Cells.GridWeb, suivez les étapes ci-dessous :

1. Créez des fonctions JavaScript à invoquer par GridWeb.
 Ces fonctions seront ajoutées à la page ASP.NET<script></script>étiquette.
1. Attribuez les noms des fonctions aux propriétés OnSubmitClientFunction et OnValidationErrorClientFunction.

La sortie de l'exemple de code est illustrée ci-dessous :

**Une validation ajoutée à la cellule C1** 

![tâche : image_autre_texte](write-gridweb-client-side-script_1.png)

 Ajoutez une valeur non valide et cliquez sur**sauvegarder**. Une erreur de validation se produit et la ValidationErrorFunction est exécutée.

**ValidationErrorFunction invoquée en cas d'erreur de validation** 

![tâche : image_autre_texte](write-gridweb-client-side-script_2.png)

 Jusqu'à ce que vous saisissiez une valeur valide, aucune donnée n'est soumise au serveur. Saisissez une valeur valide et cliquez sur**sauvegarder**. La ConfirmFunction est exécutée.

**ConfirmFunction appelée avant de soumettre les données GridWeb au serveur** 

![tâche : image_autre_texte](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
