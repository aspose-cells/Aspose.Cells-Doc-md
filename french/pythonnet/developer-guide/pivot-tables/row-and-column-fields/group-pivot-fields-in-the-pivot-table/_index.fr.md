---
title: Regrouper les champs du tableau croisé dynamique
linktitle: Regrouper les champs du tableau croisé dynamique
description: Apprenez à regrouper les champs de ligne et de colonne d'un tableau croisé dynamique selon des périodes de dates (par exemple mois et trimestres) et selon des plages numériques à l'aide de PivotField.Group et PivotFieldGroupOptions dans Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tableau croisé dynamique, regrouper champ pivot, PivotField.Group, PivotFieldGroupOptions, regroupement par dates, regroupement par nombres, mois, trimestres, plage numérique, Python via .NET
type: docs
weight: 80
url: /fr/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Le regroupement des champs du tableau croisé dynamique est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date comportant des centaines de dates ou un champ numérique contenant de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells for Python via .NET offre cette fonctionnalité via la méthode `pivot_field.group()` (regroupement automatique selon le type de données) et `pivot_field.group(pivot_field_group_options)` (options de regroupement personnalisées).
- Le regroupement par dates agrège les dates individuelles en périodes plus larges, telles que les jours, mois, trimestres et années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances dans le temps deviennent visibles d'un coup d'œil, et chaque niveau de période devient son propre champ du tableau croisé dynamique dans la zone de ligne ou de colonne du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone de ligne ou de colonne du tableau croisé dynamique.

## **Regrouper automatiquement les champs du tableau croisé dynamique**
La surcharge sans paramètre de `pivot_field.group()` examine le type de données du champ et le regroupe automatiquement. Un champ contenant uniquement des dates (et des cellules vides) est regroupé par mois. Un champ contenant uniquement des nombres (et des cellules vides) est regroupé en plages numériques à l'aide d'un intervalle automatique.

```python
import aspose.cells as ac
# Charger le classeur d'exemple
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
pt = wb.worksheets[1].pivot_tables[0]
# Grouper automatiquement le premier champ de ligne.
# Le champ contient des dates, donc il est groupé par mois.
field = pt.row_fields[0]
field.group()
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Regrouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de type date, définissez `start_date`, `end_date` et `group_types`. Pour les champs numériques, définissez `start_number`, `end_number` et `interval`. La propriété `new_pivot_field` contrôle si le regroupement crée de nouveaux champs du tableau croisé dynamique en plus du champ d'origine (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique, puis enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est maintenant regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.group_types` est ignoré. Quel que soit l'ordre dans lequel les types de groupes sont listés, les champs regroupés sont toujours affichés de la plus grande période à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.group_types`, et pourtant les trimestres sont affichés au niveau extérieur et les mois au niveau intérieur.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Charger le classeur d'exemple
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
pt = wb.worksheets[1].pivot_tables[0]
# Grouper le premier champ de ligne (un champ de date) par mois et trimestres
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Étant donné que seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` pour déplacer `FieldTwo` dans la zone de ligne, actualise le tableau croisé dynamique, puis regroupe le champ numérique selon les plages 0-1, 2-3 et 4-5 en utilisant `start_number=0`, `end_number=5` et `interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Charger le classeur d'exemple
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et son tableau croisé dynamique
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo est un champ de données : déplacez-le d'abord dans la zone des lignes,
# car seuls les champs de ligne/colonne peuvent être groupés
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Note**

{{% alert color="primary" %}}
- Les surcharges de la méthode `pivot_field.group_by()` sont obsolètes et ont été retirées de la surface de l'API. `pivot_field.group()` et `pivot_field.group(pivot_field_group_options)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ du tableau croisé dynamique d'origine par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs du tableau croisé dynamique (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ d'origine. À partir d'Aspose.Cells 26.10, les méthodes `pivot_field.group()` suivent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.new_pivot_field` existe pour la compatibilité avec les versions antérieures : elle vaut false par défaut pour le regroupement numérique et true pour le regroupement par date et heure ; définissez-la sur false si vous souhaitez que le regroupement par date remplace le champ du tableau croisé dynamique d'origine au lieu de créer de nouveaux champs.
- La propriété `PivotFieldGroupOptions.interval` ne prend effet que pour le regroupement numérique et pour le regroupement de dates par jours (par exemple, regrouper les dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}