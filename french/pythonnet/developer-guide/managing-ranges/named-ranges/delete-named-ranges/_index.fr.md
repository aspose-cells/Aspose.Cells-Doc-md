---
title: Supprimer les plages nommées
type: docs
weight: 90
url: /fr/python-net/delete-named-ranges/
description: Vous pouvez apprendre comment supprimer les noms définis ou les plages nommées des fichiers Excel ou OpenOffice avec Aspose.Cells pour Python via .Net.
keywords: Bibliothèque Excel Python, Supprimer les noms définis en double Python, Supprimer les noms définis en double Python, Supprimer les noms définis en double Python.
---

## **Introduction**
S'il y a trop de noms définis ou de plages nommées dans les fichiers Excel, nous devons en effacer certains car ils ne sont plus référencés.

## **Supprimer une plage nommée dans MS Excel**

Pour supprimer une plage nommée dans Excel, suivez les étapes suivantes :
1. Ouvrez Microsoft Excel et ouvrez le classeur contenant la plage nommée.
2. Allez à l'onglet "Formules" dans le ruban Excel.
3. Cliquez sur le bouton "Gestionnaire de noms" dans le groupe "Noms définis". Cela ouvrira la boîte de dialogue Gestionnaire de noms.
4. Dans la boîte de dialogue Gestionnaire de noms, sélectionnez la plage nommée que vous souhaitez supprimer.
5. Cliquez sur le bouton "Supprimer". Confirmez la suppression lorsqu'on vous le demande.
6. Cliquez sur le bouton "Fermer" pour fermer la boîte de dialogue Gestionnaire de noms.
7. Enregistrez le classeur pour conserver les modifications.

## **Supprimer la plage nommée en utilisant Aspose.Cells for Python via .NET**
Avec Aspose.Cells for Python via .NET, vous pouvez supprimer des plages nommées ou des noms définis par [texte](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) dans la liste.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

Remarque : si le nom défini est référencé par des formules, il ne peut pas être supprimé. Nous ne pouvons supprimer que la formule du nom défini.

## **Supprime certaines plages nommées**
Lorsque nous supprimons un nom défini, nous devons vérifier s'il est référencé par toutes les formules du fichier.
Afin d'améliorer les performances de suppression des plages nommées, nous pouvons en supprimer certaines ensemble.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **Supprimer les noms définis en double**
Certains fichiers Excel sont corrompus car certains noms définis sont en double. Nous pouvons donc supprimer ces noms en double pour réparer le fichier.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
{{< app/cells/assistant language="python-net" >}}
