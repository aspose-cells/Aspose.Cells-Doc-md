---
title: Ajouter des validations de données de cellule
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,validation,validation de données,GridValidation
description: Cet article présente comment ajouter une validation de données (GridValidation) dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb vous permet d'ajouter une **Validation des données** en utilisant la méthode GridWorksheet.Validations.Add(). En utilisant cette méthode, vous devez spécifier la **Plage de cellules**. Mais si vous voulez créer une Validation de données dans une seule GridCell, vous pouvez le faire directement en utilisant la méthode GridCell.CreateValidation(). De même, vous pouvez supprimer la **Validation de données** d'une GridCell en utilisant la méthode GridCell .RemoveValidation().

{{% /alert %}} 
## **Créer une validation de données dans une cellule de GridWeb**
Le code d'exemple suivant crée une **Validation de données** dans une cellule B3. Si vous saisissez une valeur qui n'est pas comprise entre 20 et 40, la cellule B3 affichera une **Erreur de validation** sous la forme de **XXXX rouge**, comme le montre cette capture d'écran.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
