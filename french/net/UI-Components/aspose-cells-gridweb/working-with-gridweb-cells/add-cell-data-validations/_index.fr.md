---
title: Ajouter Cell Validations de données
type: docs
weight: 90
url: /fr/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb vous permet d'ajouter**La validation des données** en utilisant la méthode GridWorksheet.Validations.Add(). En utilisant cette méthode, vous devez spécifier le**Cell Gamme** Mais si vous souhaitez créer une validation de données dans un seul GridCell, vous pouvez le faire directement en utilisant la méthode GridCell.CreateValidation(). De même, vous pouvez supprimer**La validation des données** à partir d'un GridCell à l'aide de la méthode GridCell.RemoveValidation().

{{% /alert %}} 
## **Créer une validation de données dans une GridCell de GridWeb**
 L'exemple de code suivant crée un**La validation des données** dans une cellule B3. Si vous entrez une valeur qui n'est pas comprise entre 20 et 40, la cellule B3 affichera**erreur de validation** sous la forme de**Rouge XXXX** comme le montre cette capture d'écran.

![tâche : image_autre_texte](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
