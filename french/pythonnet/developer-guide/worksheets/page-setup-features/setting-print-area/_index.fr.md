---
title: Comment définir la zone d impression avec Python.NET
linktitle: Comment définir une zone d impression
type: docs
weight: 200
url: /fr/python-net/how-to-set-print-area/
description: Apprenez comment définir et effacer les zones d impression dans les fichiers Excel en utilisant Aspose.Cells pour Python via .NET.
keywords: python définir zone d impression, effacer la plage d impression, paramètres d impression excel en python, aspose.cells python zone d impression, python limiter la gamme d impression
---

## **Scénarios d'utilisation possibles**

La définition d'une zone d'impression dans un document aide à contrôler le contenu imprimé. Les raisons clés incluent :

1. Concentration sur des données spécifiques : imprimer uniquement les sections pertinentes
1. Amélioration de la mise en page : organiser le contenu proprement sur plusieurs pages
1. Économiser des ressources : réduire la consommation de papier/encres
1. Présentation professionnelle : garantir un rendu impeccable
1. Cohérence : maintenir des impressions uniformes

## **Comment définir une zone d'impression dans Excel**

Pour définir une zone d'impression de manière programmatique :

1. Accéder aux propriétés de mise en page de la feuille
1. Définir la zone d'impression en utilisant la notation de plage de cellules
1. Enregistrer le classeur modifié

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **Comment effacer la zone d'impression dans Excel**

Pour supprimer les contraintes de la zone d'impression :

1. Accéder aux propriétés de mise en page
1. Réinitialiser la zone d'impression à une chaîne vide
1. Enregistrer les modifications

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **Que se passe-t-il après avoir effacé la zone d'impression**

La suppression de la zone d'impression aboutit à :

1. Impression par défaut de toute la feuille
1. Suppression des contraintes de plages précédentes
1. Inclusion de toutes les cellules formatées

## **Comment définir la zone d'impression avec Aspose.Cells**

Définir la zone d'impression via la mise en page de la feuille :

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **Comment effacer la zone d'impression avec Aspose.Cells**

Supprimer la définition existante de la zone d'impression :

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
{{< app/cells/assistant language="python-net" >}}
