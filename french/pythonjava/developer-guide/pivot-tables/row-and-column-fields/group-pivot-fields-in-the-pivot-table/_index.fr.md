---
title: Regrouper les champs du tableau croisé dynamique dans le tableau croisé dynamique
linktitle: Regrouper les champs du tableau croisé dynamique dans le tableau croisé dynamique
description: Apprenez à regrouper les champs de ligne et de colonne d'un tableau croisé dynamique en périodes de dates (mois, trimestres) et en plages numériques à l'aide de PivotField.group et PivotFieldGroupOptions dans Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tableau croisé dynamique, regrouper champ tableau croisé dynamique, PivotField.group, PivotFieldGroupOptions, regroupement par dates, regroupement par nombres, mois, trimestres, plage numérique, Python
type: docs
weight: 80
url: /fr/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Cas d'utilisation possibles**
- Le regroupement des champs du tableau croisé dynamique est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreuses valeurs distinctes, par exemple un champ de date avec des centaines de dates ou un champ numérique avec de nombreuses valeurs dispersées. Le regroupement condense ces valeurs en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells offre cette fonctionnalité via la méthode `PivotField.group()` (regroupement automatique selon le type de données) et `PivotField.group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par dates agrège les dates individuelles en périodes plus larges, telles que les jours, mois, trimestres et années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances dans le temps deviennent visibles d'un seul coup d'œil, et chaque niveau de période devient son propre champ du tableau croisé dynamique dans la zone de ligne ou de colonne du tableau croisé dynamique.
- Le regroupement est disponible uniquement pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone de ligne ou de colonne du tableau croisé dynamique.

## **Regrouper automatiquement les champs du tableau croisé dynamique**
La surcharge sans paramètres `PivotField.group()` inspecte le type de données du champ et le regroupe automatiquement. Un champ contenant uniquement des dates (et des cellules vides) est regroupé par mois. Un champ contenant uniquement des nombres (et des cellules vides) est regroupé en plages numériques selon un intervalle automatique.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Charger le classeur d'exemple
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Grouper automatiquement le premier champ de ligne.
# Le champ contient des dates, il est donc groupé par mois.
field = pt.getRowFields().get(0)
field.group()
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Regrouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `StartDate`, `EndDate` et `GroupTypes`. Pour les champs numériques, définissez `StartNumber`, `EndNumber` et `Interval`. La propriété `NewPivotField` contrôle si le regroupement crée de nouveaux champs du tableau croisé dynamique à côté du champ d'origine (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est désormais regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.GroupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de regroupement sont listés, les champs regroupés sont toujours affichés de la période la plus grande à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.GroupTypes`, et pourtant les trimestres sont affichés comme niveau externe et les mois comme niveau interne.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Charger le classeur d'exemple
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Grouper le premier champ de ligne (un champ de date) par mois et trimestres
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Étant donné que seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` pour déplacer `FieldTwo` vers la zone de ligne, actualise le tableau croisé dynamique, puis regroupe le champ numérique dans les plages 0-1, 2-3 et 4-5 en utilisant `StartNumber = 0`, `EndNumber = 5` et `Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Charger le classeur d'exemple
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo est un champ de données : déplacez-le d'abord dans la zone des lignes,
# car seuls les champs de ligne/colonne peuvent être groupés
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Note**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.groupBy()` sont obsolètes et ont été supprimées de la surface de l'API. `PivotField.group()` et `PivotField.group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ du tableau croisé dynamique d'origine par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs du tableau croisé dynamique (un par niveau de regroupement, par exemple Trimestres et Mois) à côté du champ d'origine. À partir de Aspose.Cells 26.10, les méthodes `PivotField.group()` adoptent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.NewPivotField` existe pour la compatibilité avec les versions antérieures : elle vaut par défaut false pour le regroupement numérique et true pour le regroupement date-heure ; définissez-la sur false si vous souhaitez que le regroupement par dates remplace le champ du tableau croisé dynamique d'origine au lieu de créer de nouveaux champs du tableau croisé dynamique.
- La propriété `PivotFieldGroupOptions.Interval` ne prend effet que pour le regroupement numérique et pour le regroupement par dates par jours (par exemple, regrouper des dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}