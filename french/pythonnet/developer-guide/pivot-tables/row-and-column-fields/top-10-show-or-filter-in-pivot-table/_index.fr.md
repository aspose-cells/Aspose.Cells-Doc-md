---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Python via .NET. Cet article explique la méthode top_10_auto_show d’Excel 97-2003, la lecture des options avec top_10_auto_show_settings et le filtre « 10 premiers » d’Excel 2007-365 via filter_top10.
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, 10 premiers, affichage automatique, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /fr/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines de membres. Un rapport « 10 premiers » ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui correspond exactement aux besoins des rapports de classement : « 5 principaux produits par chiffre d’affaires » ou « 3 principales régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **Excel 97-2003 : affichage automatique** — la méthode `PivotField.top_10_auto_show()`. Il s’agit du paramètre classique « Afficher les N éléments supérieurs/inférieurs », directement stocké sur le champ du tableau croisé dynamique. Ce paramètre fonctionne avec toutes les versions d’Excel, anciennes et récentes, car il fait partie du format d’origine des tableaux croisés dynamiques.
- **Filtre « 10 premiers » d’Excel 2007-365** — la méthode `PivotField.filter_top10()`. Il s’agit du filtre moderne de valeurs « 10 premiers », accessible dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’un objet `PivotFilter` associé au champ et permet un classement fondé sur le nombre d’éléments ou sur un pourcentage.

## **Afficher les 10 premiers éléments dans Excel 97-2003 (top_10_auto_show)**
L’affichage automatique classique se configure par un seul appel à `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)` :
- `is_auto_show` — active ou désactive le paramètre d’affichage automatique sur le champ.
- `is_top` — `True` conserve les éléments les mieux classés (« Haut »), `False` conserve les éléments les moins bien classés (« Bas »).
- `count` — nombre d’éléments à conserver, par exemple 10 pour un rapport classique des 10 premiers éléments.
- `rank_by` — index démarrant à zéro du **champ de données** dont les valeurs servent à classer les éléments. Passez -1 pour classer les éléments selon le champ lui-même.
Le classement peut reposer sur un champ de valeurs ou sur le champ lui-même. Deux variantes possibles sont illustrées ci-dessous.

### **Classement par un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs ordinaire, tel que `Sum of Sales`. L’exemple suivant crée un tableau croisé dynamique contenant un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports dont les ventes sont les plus élevées. `rank_by` vaut 0, car `Sum of Sales` est le champ de données situé à l’index 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Afficher les 2 premiers éléments classés par « Sum of Sales » (index du champ de données 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Classement selon le champ lui-même**
Un champ peut également servir de critère de classement pour ses propres éléments — transmettez -1 comme `rank_by`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone des lignes (ou des colonnes). L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lors de l’enregistrement de ce paramètre, l’attribut `rank_by` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut du format. De plus, `top_10_auto_show_settings.rank_by` renvoie également -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Lecture des options actuelles (top_10_auto_show_settings)**
La propriété `PivotField.top_10_auto_show_settings` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options d’affichage automatique actuellement stockées sur le champ. Utilisez-la pour examiner la manière dont les éléments seront affichés dans un classeur existant ou dans un tableau croisé dynamique que vous venez de configurer. Cette lecture est également possible pour les classeurs chargés à partir d’un fichier.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Les quatre propriétés correspondent aux attributs classiques d’affichage automatique écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Par conséquent, les valeurs relues sont celles que chaque version d’Excel respectera.

## **Remarque**

{{% alert color="primary" %}}
- Les propriétés directes de `PivotField` — `is_auto_show`, `is_ascend_show`, `auto_show_count` et `auto_show_field` — sont marquées comme obsolètes. Utilisez plutôt l’objet `top_10_auto_show_settings` : `is_auto_show` devient `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` devient `top_10_auto_show_settings.is_top`, `auto_show_count` devient `top_10_auto_show_settings.auto_show_count` et `auto_show_field` devient `top_10_auto_show_settings.rank_by`. La méthode `top_10_auto_show()` est la méthode prise en charge pour modifier les paramètres.
- `top_10_auto_show` fonctionne avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre « 10 premiers » (filter_top10)**
Les versions modernes d’Excel proposent un filtre de valeurs « 10 premiers » dans le menu du champ (« Filtres de valeurs », « 10 premiers... »). Aspose.Cells gère ce filtre au moyen de la méthode `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`, qui renvoie le `PivotFilter` créé :
- `value_field_index` — index démarrant à zéro du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — indique ce que signifie `item_count`. `PivotFilterType.COUNT` conserve un nombre fixe d’éléments (l’option « Éléments » de la boîte de dialogue). `PivotFilterType.PERCENT` conserve un pourcentage d’éléments ; `item_count` correspond alors directement au pourcentage, de sorte que la valeur 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.SUM` établit le classement selon la couverture cumulée des valeurs.
- `is_top` — `True` pour « Haut », `False` pour « Bas ».
- `item_count` — le nombre N dans « N premiers » ; son unité dépend de `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Filtre Top 10 — conserver les 2 premiers éléments selon « Total des ventes » (index du champ de données 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Pour un filtre basé sur un pourcentage, conserver plutôt les 30 % premiers éléments :
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` et `filter_top10` sont deux fonctionnalités distinctes. L’affichage automatique écrit l’attribut classique `autoShow` défini sur le champ du tableau croisé dynamique et est respecté par toutes les versions d’Excel depuis Excel 97. `filter_top10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version antérieure d’Excel, un tableau croisé dynamique qui utilise le filtre moderne affiche tous les éléments. Pour les documents qui doivent faire l’objet d’aller-retours via des outils hérités, préférez `top_10_auto_show` ; pour les classeurs modernes, préférez `filter_top10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles associés**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne aux tableaux croisés dynamiques](/cells/fr/python-net/pivot-table-add-row-and-column-fields/)
- [Grouper les champs de tableau croisé dynamique dans le tableau croisé dynamique](/cells/fr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}