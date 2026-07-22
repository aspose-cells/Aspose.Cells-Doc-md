---
title: Rendu de tableau à cellule unique SmartMarker | Aspose.Cells for Python via .NET
linktitle: Rendu de tableau
description: Apprenez à rendre les données de tableau dans une seule cellule en utilisant les attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /fr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu de données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la façon dont les éléments du tableau sont séparés dans une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les Smart Markers dans Aspose.Cells sont une fonctionnalité puissante, basée sur des modèles, qui vous permet de remplir dynamiquement les données d'une feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.

Par défaut, lorsqu'un Smart Marker fait référence à une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur développe le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble dans une balise Smart Marker, répondent précisément à ce besoin. Ils vous permettent de conserver des mises en page de rapports compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'expansion du tableau**

Lorsqu'un Smart Marker fait référence à une propriété de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant les autres contenus du modèle vers l'extérieur et pouvant potentiellement rompre des mises en page de rapports soigneusement conçues.

### **Limites du cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'expansion par défaut n'est pas souhaitable :

- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes de balises, d'étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs à un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui se propagent sur plusieurs cellules.

### **Le manque qu'elle comble**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en Python — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une seule cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation souhaitée — virgule, point-virgule, trait d'union, barre verticale, retour à la ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme se trouvent dans la balise Smart Marker.
- **Rapports plus propres** : les données de tableau ne poussent plus le contenu voisin du modèle dans des lignes ou colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'expansion d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur entre les parenthèses d'un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche le comportement en cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, un caractère unique ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte tout littéral de chaîne, y compris des délimiteurs à plusieurs caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des retours à la ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Flux de travail étape par étape**

Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.

1. **Préparer la source de données** : créez une classe (ou structure de données) qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `list[str]`, `list[int]` ou tout autre type de tableau pris en charge.
2. **Créer un classeur de conception** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancier le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur de conception et liez votre source de données à l'aide de la méthode `set_data_source`.
4. **Traiter les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et peupler le classeur avec des données réelles.
5. **Enregistrer le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de base d'un tableau de chaînes**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **Exemple de code 3 — Comparaison du comportement par défaut et ArrayAsSingle**

```python
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

# Section 1 : Smart Marker par défaut - valeurs réparties horizontalement sur les cellules
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Section 2 : Nouveau rendu en cellule unique utilisant arrayasSingle et extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Lier la source de données et traiter les Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Enregistrer le classeur résultant
workbook.save("output_comparison.xlsx")
```

### **Notes et bonnes pratiques**

Gardez les points suivants à l'esprit lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez tous les caractères spéciaux que votre processeur de modèles pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`True` / `False`). Seul `True` déclenche le comportement en cellule unique ; toute autre valeur revient au comportement d'expansion par défaut.
- Si le tableau est vide ou null, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne aussi bien avec des sources de données objet qu'avec des sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des retours à la ligne, vous pouvez utiliser `\n` ou `os.linesep` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes en fonction du format.

## **Articles connexes**

- [Smart Markers](/cells/fr/python-net/smart-markers/)
- [Fusion et annulation de la fusion de cellules](/cells/fr/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}