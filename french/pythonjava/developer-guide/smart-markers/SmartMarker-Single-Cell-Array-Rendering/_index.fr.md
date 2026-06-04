---
title: Rendu de tableau dans une cellule unique avec SmartMarker | Aspose.Cells Python via Java
description: Apprenez à rendre les données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for Python via Java.
keywords: Aspose.Cells, bibliothèque Python via Java, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu des données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés au sein d'une même cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les Smart Markers dans Aspose.Cells sont une fonctionnalité puissante basée sur des modèles qui vous permet de remplir dynamiquement les données de la feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.

Par défaut, lorsqu'un Smart Marker référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur étend le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble à l'intérieur d'une balise Smart Marker, répondent précisément à ce besoin. Ils vous permettent de garder des mises en page de rapports compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'extension du tableau**

Lorsqu'un Smart Marker référence une propriété de tableau, Aspose.Cells étend le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs, placera chaque valeur dans sa propre cellule, repoussant le reste du contenu du modèle et pouvant potentiellement perturber des mises en page de rapports soigneusement conçues.

### **Limitations du cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'extension par défaut n'est pas souhaitable :

- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes de balises, d'étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales au sein d'une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs au même endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une seule valeur consolidée par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui s'étendent sur plusieurs cellules.

### **Le besoin qu'elle comble**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en Python — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une seule cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, saut de ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme se trouvent dans la balise Smart Marker.
- **Rapports plus propres** : les données de tableau ne poussent plus le contenu du modèle voisin dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec des chaînes, des nombres, des dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'extension d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche le comportement en cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un seul caractère ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte n'importe quelle chaîne littérale, y compris des délimiteurs à plusieurs caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Workflow étape par étape**

Le workflow suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.

1. **Préparez la source de données** : créez une classe (ou une structure de données) qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `string[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créez un classeur de conception** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule de Smart Marker qui référence la propriété du tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur de conception et liez votre source de données à l'aide de la méthode `set_data_source`.
4. **Traitez les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Définir la classe Student
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Exemple de code 3 — Comparaison du comportement par défaut et du comportement ArrayAsSingle**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Définir la source de données comme un dictionnaire (équivalent à la classe Order)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Section 1 : Smart Marker par défaut - valeurs réparties horizontalement sur les cellules
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Section 2 : Nouveau rendu en cellule unique utilisant arrayasSingle et extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Lier la source de données et traiter les Smart Markers
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Enregistrer le classeur résultant
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Notes et bonnes pratiques**

Gardez les points suivants à l'esprit lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur de `extraDelimiter` est traitée comme une chaîne littérale ; échappez tous les caractères spéciaux que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seul `true` déclenche le comportement en cellule unique ; toute autre valeur revient au comportement d'extension par défaut.
- Si le tableau est vide ou nul, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec les sources de données d'objets ainsi qu'avec les sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou la constante de saut de ligne de la plateforme comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes selon le format.

## **Articles connexes**

- [Smart Markers](/cells/fr/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}