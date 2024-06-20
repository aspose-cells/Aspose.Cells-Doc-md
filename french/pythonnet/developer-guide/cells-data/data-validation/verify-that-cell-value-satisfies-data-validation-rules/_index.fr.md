---
title: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Apprenez à vérifier si la valeur de la cellule satisfait les règles de validation des données à travers l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Obtenir la valeur de validation de cellule Python, Obtenir la valeur de validation de cellule Python, Vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule en Python.
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale spécifie que seuls les nombres entre 10 et 20 peuvent être saisis. Si un utilisateur entre un nombre différent, Microsoft Excel affiche un message d'erreur et l'invite à saisir un nombre dans la plage correcte. Si vous copiez-collez un nombre, par exemple 3, dans la cellule, Excel ne vérifie pas la validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 
## **Introduction**
Aspose.Cells for Python via .NET fournit la méthode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) pour valider les valeurs des cellules de manière programmée. Si la valeur dans une cellule ne satisfait pas la règle de validation des données appliquée à cette cellule, elle renvoie **False**, sinon **True**.

Le code d'exemple suivant illustre le fonctionnement de la méthode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#). Tout d'abord, il entre la valeur 3 dans C1. Parce que cela ne satisfait pas la règle de validation des données, la méthode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) retourne **False**. Ensuite, il entre la valeur 15 dans C1. Parce que cette valeur satisfait la règle de validation des données, la méthode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) retourne **True**. De même, elle retourne **False** pour la valeur 30.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Sortie**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
