---
title: Rendu d’un tableau dans une cellule unique avec SmartMarker | Aspose.Cells for Python via .NET
description: Découvrez comment rendre des données de tableau dans une cellule unique à l’aide des attributs Smart Marker `arrayassingle` et `arraydelimiter` dans Aspose.Cells for Python via .NET.
linktitle: Rendu d’un tableau dans une cellule unique avec SmartMarker | Aspose.Cells
url: /fr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, bibliothèque Python via .NET, feuille de calcul, Smart Markers, arrayassingle, arraydelimiter, tableau dans une cellule unique, rendu de tableau, modèle
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells peut rendre une source de données contenant un tableau dans une cellule unique à l’aide des Smart Markers. L’attribut `arrayassingle` désactive la diffusion élément par élément par défaut, et l’attribut `arraydelimiter` choisit le séparateur inséré entre les éléments concaténés — une virgule par défaut, ou tout caractère unique ou chaîne multicaractères entre guillemets que vous spécifiez.
{{% /alert %}}

## **Introduction**

Les Smart Markers d’Aspose.Cells constituent une fonctionnalité fondée sur des modèles qui renseigne dynamiquement les données d’une feuille de calcul à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.
Par défaut, lorsqu’un Smart Marker fait référence à un champ de tableau (par exemple, `&=Product.Tags` lié à une liste de quatre valeurs), le moteur développe le tableau et place chaque élément dans une cellule distincte, en propageant les valeurs verticalement vers le bas de la colonne, sous le marqueur. Bien que ce comportement soit pratique dans de nombreux scénarios, certaines situations nécessitent de rendre l’ensemble du tableau dans une cellule unique, avec concaténation des éléments et séparation par un délimiteur de votre choix.
Les attributs `arrayassingle` et `arraydelimiter`, écrits entre les parenthèses d’un Smart Marker sous la forme `name:value`, répondent précisément à ce besoin. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en utilisant de manière native des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut de diffusion des tableaux**

Lorsqu’un Smart Marker fait référence à un champ de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags`, appliqué à une liste contenant quatre valeurs, place chaque valeur dans une cellule distincte sous le marqueur, ce qui décale les autres éléments du modèle et peut altérer des mises en page de rapport soigneusement conçues.

### **Limites des cas d’utilisation**

De nombreux scénarios pratiques rendent le comportement de diffusion par défaut inapproprié :
- **Rapports de synthèse** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** devant être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtrage ou indicateurs d’état** regroupant plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (exportation CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu’une plage étendue.
- **Compatibilité entre plateformes**, dans laquelle certains consommateurs ne peuvent pas accepter des tableaux qui se répartissent sur plusieurs cellules.

### **L’écart comblé**

En l’absence de mécanisme intégré, les développeurs seraient obligés de traiter préalablement les données en Python — en convertissant les listes en chaînes délimitées avant de les lier à `WorkbookDesigner`. Cela duplique la logique, complexifie les modèles de données et augmente les risques d’erreur. Les attributs `arrayassingle` et `arraydelimiter` suppriment ce contournement en gérant la mise en forme de manière déclarative à l’intérieur même du Smart Marker.

## **Avantages de la fonctionnalité**

L’utilisation des attributs `arrayassingle` et `arraydelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une cellule unique** : Tous les éléments du tableau sont rendus dans exactement une cellule, ce qui préserve des mises en page compactes et prévisibles.
- **Contrôle personnalisé du séparateur** : Spécifiez le séparateur de votre choix — la virgule par défaut, un point-virgule, un trait d’union, une barre verticale ou une chaîne multicaractères entre guillemets telle que `" | "`.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est requis pour traiter préalablement les données ; les règles de mise en forme résident dans la balise Smart Marker.
- **Rapports plus lisibles** : Les données de tableau ne décalent plus le contenu de modèle voisin vers d’autres lignes ou colonnes.
- **Types de données polyvalents** : Fonctionne avec des listes de chaînes et des listes numériques fournies sous forme de lignes JSON.
- **Compatibilité ascendante** : Lorsque les attributs sont omis, le comportement de diffusion d’origine est conservé, si bien que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe des Smart Markers**

Les attributs `arrayassingle` et `arraydelimiter` utilisent la grammaire d’attributs `name:value` d’Aspose.Cells entre les parenthèses d’un Smart Marker standard. La syntaxe générale est la suivante :

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayField` — le Smart Marker standard qui fait référence au champ de tableau de la source de données liée.
- `arrayassingle:true` — indique au moteur de rendre l’ensemble du tableau dans une seule cellule au lieu de répartir ses éléments.
- `arraydelimiter:;` — facultatif ; définit le séparateur placé entre les éléments du tableau. En son absence, une virgule est utilisée.

{{% alert color="warning" %}}
Écrivez les attributs sous la forme `name:value` (avec deux-points, et non un signe égal) et séparez plusieurs attributs par une virgule **sans espaces**. Un espace après la virgule décale la valeur analysée d’un caractère — `(arrayassingle:true, arraydelimiter:;)` concaténerait les éléments avec le séparateur erroné `:;` au lieu de `;`.
{{% /alert %}}

### **Formes du séparateur**

- Un caractère unique est écrit directement après les deux-points : `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un séparateur multicaractères est placé entre guillemets doubles : `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Procédure pas à pas**

La procédure suivante décrit comment rendre un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparer la source de données** : Organisez chaque enregistrement comme un objet JSON dont un champ contient un tableau, par exemple `{"Tags": ["C#", "Aspose"]}`. Les instances de classes Python ordinaires, les dictionnaires et les listes transmis à `set_data_source` ne permettent pas de lier les champs de tableau sur cette plateforme — les lignes JSON constituent la forme tabulaire prise en charge.
2. **Créer un classeur de conception** : Créez un nouveau `Workbook`, ajoutez une ligne d’en-tête et placez une cellule de Smart Marker qui fait référence au champ de tableau avec l’attribut `arrayassingle` (et `arraydelimiter` lorsqu’un séparateur personnalisé est nécessaire).
3. **Instancier `WorkbookDesigner`** : Créez un `WorkbookDesigner` autour du classeur et associez vos lignes JSON à l’aide de `set_json_data_source`.
4. **Traiter les marqueurs** : Appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et renseigner le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de base d’un tableau de chaînes**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

L’exemple affiche la valeur concaténée du tableau entier. Les quatre tags sont regroupés dans une seule cellule, séparés par la virgule par défaut :

```
C#,Aspose,SmartMarker,Excel
```

### **Exemple de code 2 — Tableau numérique avec un séparateur personnalisé**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

Les nombres JSON sont concaténés exactement comme les chaînes — chaque élément conserve sa représentation numérique brute :

```
95-88-76-100-67
```

### **Exemple de code 3 — Comparaison du rendu par défaut et du rendu dans une cellule unique**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Le marqueur par défaut remplit une cellule par élément dans la colonne B, tandis que le marqueur `arrayassingle` condense le même tableau dans une seule cellule de la colonne C :

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes et bonnes pratiques**

Gardez les éléments suivants à l’esprit lorsque vous utilisez les attributs `arrayassingle` et `arraydelimiter` :
- Les valeurs d’attribut utilisent la forme `name:value`. Une forme avec un signe égal, telle que `arrayassingle=true`, n’est pas reconnue et ramène silencieusement au comportement de diffusion par défaut.
- Séparez les attributs par une virgule sans espace ; un espace après la virgule décale la valeur du séparateur d’un caractère (voir l’avertissement ci-dessus).
- La valeur de `arraydelimiter` peut être un caractère unique écrit directement après les deux-points ou une chaîne multicaractères placée entre guillemets doubles.
- Si `arraydelimiter` est omis, les éléments sont concaténés par une virgule.
- Fournissez les champs de tableau au moyen des objets de ligne de `set_json_data_source`. Les objets Python ordinaires et les dictionnaires transmis à `set_data_source` ne sont pas liés sur cette plateforme, et une instance personnalisée de `ICellsDataTable` dont une colonne renvoie une liste Python affiche le texte du conteneur de la liste au lieu de concaténer ses éléments.
- Les nombres JSON conservent leur forme d’entier simple dans la sortie concaténée.

## **Articles connexes**
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/python-net/change-page-field-layout/)
- [Convertir une sparkline en image et en HTML dans Aspose.Cells for Python via .NET](/cells/fr/python-net/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}