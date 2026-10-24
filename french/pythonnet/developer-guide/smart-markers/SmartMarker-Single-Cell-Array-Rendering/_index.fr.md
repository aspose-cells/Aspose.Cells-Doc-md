---
title: Rendu de tableau SmartMarker dans une seule cellule | Aspose.Cells for Python via .NET
linktitle: Rendu de tableau SmartMarker dans une seule cellule | Aspose.Cells for Python via .NET
description: Découvrez comment rendre des données de tableau dans une seule cellule à l’aide des attributs `ArrayAsSingle` et `ExtraDelimiter` dans les Smart Markers avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, bibliothèque Python via .NET, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau dans une seule cellule, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet de rendre les données d’un tableau dans une seule cellule à l’aide des Smart Markers. En utilisant l’attribut `ArrayAsSingle` conjointement avec l’attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans une seule cellule, ce qui offre une mise en forme souple pour les rapports et les modèles.
{{% /alert %}}

## **Introduction**
Les Smart Markers d’Aspose.Cells constituent une fonctionnalité puissante basée sur des modèles, qui permet de renseigner dynamiquement des données de feuille de calcul à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un Smart Marker référence une propriété de tableau, par exemple `&=DataSource.Numbers`, le moteur étend le tableau et place chaque élément dans une cellule adjacente distincte — horizontalement le long d’une ligne ou verticalement le long d’une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préféreriez rendre l’ensemble du tableau dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble au sein d’une balise Smart Marker, répondent précisément à ce besoin. Ils permettent de conserver des mises en page de rapport compactes et prévisibles tout en utilisant nativement des sources de données contenant des tableaux.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Lorsqu’un Smart Marker référence une propriété de tableau, Aspose.Cells répartit par défaut le tableau sur plusieurs cellules. Par exemple, un marqueur tel que `&=Product.Tags`, associé à un `string[]` contenant quatre valeurs, place chaque valeur dans une cellule distincte. Cela repousse les autres éléments du modèle et peut compromettre des mises en page de rapport soigneusement conçues.

### **Use Case Limitations**
De nombreux scénarios pratiques nécessitent un comportement différent du comportement de répartition par défaut :
- **Rapports de synthèse** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** devant être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d’état** regroupant plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée par cellule plutôt qu’une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas tolérer des tableaux qui s’étendent sur plusieurs cellules.

### **The Gap It Fills**
Sans mécanisme intégré, les développeurs seraient obligés de prétraiter les données en Python — en concaténant les tableaux dans des chaînes délimitées avant de les lier au classeur de conception. Cela duplique la logique, complique les modèles de données et augmente les risques d’erreur. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative au sein même du Smart Marker.

## **Feature Benefits**
L’utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans une seule cellule, ce qui permet de conserver des mises en page compactes et prévisibles.
- **Contrôle du délimiteur** : spécifiez la chaîne de séparation de votre choix — une virgule, un point-virgule, un trait d’union, une barre verticale, un saut de ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme sont définies dans la balise Smart Marker.
- **Rapports plus propres** : les données du tableau ne repoussent plus le contenu voisin du modèle vers d’autres lignes ou colonnes.
- **Types de données polyvalents** : la fonctionnalité fonctionne avec des chaînes, des nombres, des dates et tout autre type de données pouvant être concaténé à l’aide d’un délimiteur.
- **Compatibilité ascendante** : lorsque les attributs sont omis, le comportement initial de répartition est conservé et les modèles existants continuent à fonctionner sans modification.

## **How to Use This Feature**

### **Smart Marker Syntax**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont transmis sous forme de paires clé-valeur dans les parenthèses d’un Smart Marker standard. La syntaxe générale est la suivante :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le Smart Marker standard qui référence la propriété de tableau de la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre l’ensemble du tableau dans une seule cellule. Seule la valeur `true` déclenche le comportement dans une cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, comporter un seul caractère ou plusieurs caractères.

{{% alert color="primary" %}}
L’attribut `extraDelimiter` accepte tout littéral de chaîne, notamment des délimiteurs composés de plusieurs caractères, du texte personnalisé ou des séquences d’échappement telles que `\n` pour produire une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante est laissée vide.
{{% /alert %}}

### **Step-by-Step Workflow**
Le processus suivant explique comment rendre un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparer la source de données** : créez une classe ou une structure de données qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `list[str]`, `list[int]` ou tout autre type de tableau pris en charge.
2. **Créer un classeur de conception** : créez un nouveau `Workbook`, ajoutez une ligne d’en-tête et placez dans une cellule un Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancer le WorkbookDesigner** : créez un objet `WorkbookDesigner`, associez-lui le classeur de conception et liez votre source de données à l’aide de la méthode `set_data_source`.
4. **Traiter les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Code Example 1 — Basic String Array Rendering**

```python
import aspose.cells as ac
class Product:
    def __init__(self):
        self.Tags = []
product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")
designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()
workbook.save("output_arraySingle.xlsx")
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```python
import aspose.cells as ac
class Student:
    def __init__(self):
        self.scores = []
student = Student()
student.scores = [95, 88, 76, 100, 67]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
worksheet.cells.get("A2").put_value(" - ".join(str(s) for s in student.scores))
workbook.save("output_numericArray.xlsx")
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```python
import aspose.cells as ac
class Order:
    def __init__(self, items):
        self._items = items
    @property
    def Items(self):
        return self._items
    @Items.setter
    def Items(self, value):
        self._items = value
order = Order(["Apple", "Banana", "Cherry", "Date"])
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Section 1: Default Smart Marker - values spread horizontally across cells
cells.get("A1").put_value("Default Spreading Behavior:")
cells.get("A2").put_value("&=Order.Items")
# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").put_value("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')
# Bind the data source and process Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()
# Save the resulting workbook
workbook.save("output_comparison.xlsx")
```

### **Notes & Best Practices**
Gardez les points suivants à l’esprit lorsque vous utilisez les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez les caractères spéciaux susceptibles d’être interprétés par le processeur de votre modèle.
- L’attribut `arrayasSingle` accepte une valeur booléenne (`True` / `False`). Seule la valeur `True` déclenche le comportement dans une cellule unique ; toute autre valeur entraîne le retour au comportement de répartition par défaut.
- Si le tableau est vide ou nul, la cellule reste vide ou contient une chaîne vide, selon le type de données.
- La fonctionnalité fonctionne avec les sources de données constituées d’objets, ainsi qu’avec les sources `DataSet` et `DataTable` dans lesquelles une colonne peut être scindée en tableaux.
- Pour produire une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou `os.linesep` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut déborder visuellement dans les cellules adjacentes selon le format.

## Related Articles
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Python via .NET](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/python-net/change-page-field-layout/)
- [Convertir une Sparkline en image et HTML dans Aspose.Cells for Python via .NET](/cells/fr/python-net/convert-sparkline-to-image-and-html/)
- [Convertir Excel au format OFD](/cells/fr/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}