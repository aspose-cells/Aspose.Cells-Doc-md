---
title: Rendu de tableau dans une cellule unique avec SmartMarker | Aspose.Cells Python via Java
description: Découvrez comment rendre des données de tableau dans une cellule unique à l’aide des attributs `arrayassingle` et `arraydelimiter` de Smart Marker dans Aspose.Cells for Python via Java.
linktitle: Rendu SmartMarker dans une cellule unique | Aspose.Cells
url: /fr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, bibliothèque Python via Java, tableur, Smart Markers, arrayassingle, arraydelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells peut rendre une source de données sous forme de tableau dans une cellule unique grâce aux Smart Markers. L’attribut `arrayassingle` désactive la propagation par défaut élément par élément, et l’attribut `arraydelimiter` choisit le séparateur inséré entre les éléments concaténés — une virgule par défaut, ou n’importe quel caractère unique ou chaîne multicaractère guillemetée que vous spécifiez.
{{% /alert %}}

## **Présentation**

Les Smart Markers d’Aspose.Cells constituent une fonctionnalité fondée sur des modèles qui remplit dynamiquement les données du tableur à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un Smart Marker référence un champ de tableau (par exemple, `&=Product.Tags` associé à une liste de quatre valeurs), le moteur développe le tableau et place chaque élément dans sa propre cellule, en répartissant les valeurs verticalement dans la colonne située sous le marqueur. Bien que ce comportement soit pratique dans de nombreux scénarios, certaines situations nécessitent de rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un séparateur de votre choix.
Les attributs `arrayassingle` et `arraydelimiter`, écrits dans les parenthèses d’un Smart Marker sous la forme `name:value`, répondent précisément à ce besoin. Ils permettent de conserver des mises en page de rapport compactes et prévisibles tout en exploitant nativement des sources de données sous forme de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut de propagation des tableaux**

Lorsqu’un Smart Marker référence un champ de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags`, associé à une liste de quatre valeurs, place chaque valeur dans sa propre cellule sous le marqueur, décalant les autres éléments du modèle et risquant de perturber des mises en page de rapport soigneusement conçues.

### **Limites des cas d’utilisation**

De nombreux scénarios pratiques rendent le comportement de propagation par défaut undesirable :
- **Rapports de synthèse** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** devant être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d’état** regroupant plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, publipostage) attendant une valeur consolidée unique par cellule plutôt qu’une plage étendue.
- **Compatibilité multiplateforme**, dans laquelle certains consommateurs ne peuvent pas gérer des tableaux qui débordent sur plusieurs cellules.

### **Le manque comblé**

Sans mécanisme intégré, les développeurs seraient obligés de prétraiter les données en Python, en convertissant les listes en chaînes délimitées avant de les associer au `WorkbookDesigner`. Cette approche duplique la logique, complique les modèles de données et augmente le risque d’erreurs. Les attributs `arrayassingle` et `arraydelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative au sein même du Smart Marker.

## **Avantages de la fonctionnalité**

L’utilisation des attributs `arrayassingle` et `arraydelimiter` dans vos Smart Markers présente plusieurs avantages :
- **Confinement dans une seule cellule** : Tous les éléments du tableau sont rendus dans exactement une cellule, ce qui permet de conserver des mises en page compactes et prévisibles.
- **Contrôle personnalisé du séparateur** : Spécifiez le séparateur de votre choix — la virgule par défaut, un point-virgule, un trait d’union, une barre verticale ou une chaîne multicaractère entre guillemets telle que `" | "`.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme sont définies dans la balise Smart Marker.
- **Rapports plus propres** : Les données sous forme de tableau ne déplacent plus les éléments voisins du modèle vers d’autres lignes ou colonnes.
- **Types de données polyvalents** : Fonctionne avec des tableaux de chaînes fournis sous forme de lignes JSON, y compris des valeurs numériques représentées sous forme de chaînes.
- **Compatibilité ascendante** : Lorsque les attributs sont omis, le comportement de propagation d’origine est conservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `arrayassingle` et `arraydelimiter` utilisent la syntaxe d’attributs `name:value` d’Aspose.Cells entre les parenthèses d’un Smart Marker standard. La syntaxe générale est la suivante :

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayField` — le Smart Marker standard qui référence le champ de tableau de la source de données associée.
- `arrayassingle:true` — demande au moteur de rendre l’ensemble du tableau dans une seule cellule au lieu d’en répartir les éléments.
- `arraydelimiter:;` — facultatif ; définit le séparateur placé entre les éléments du tableau. Si cet attribut est omis, une virgule est utilisée.

{{% alert color="warning" %}}
Rédigez les attributs sous la forme `name:value` (avec deux-points et non signe égal) et séparez plusieurs attributs par une virgole **sans espaces**. Un espace après la virgule décale la valeur analysée d’un caractère — `(arrayassingle:true, arraydelimiter:;)` produirait une concaténation avec le séparateur erroné `:;` au lieu de `;`.
{{% /alert %}}

### **Formes possibles du séparateur**

- Un caractère unique est placé directement après le deux-points : `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un séparateur multicaractère est écrit entre guillemets doubles : `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flux de travail 단계 par étape**

Le flux de travail suivant explique comment rendre un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparez la source de données** : Organisez chaque enregistrement sous forme d’objet JSON dans lequel un champ contient un tableau, par exemple `{"Tags": ["C#", "Aspose"]}`. Les instances de classes Python et les dictionnaires ordinaires transmis à `setDataSource` ne sont pas liés sur cette plateforme — les lignes JSON constituent la forme tabulaire prise en charge.
2. **Créez le classeur de conception** : Créez un nouveau `Workbook`, ajoutez une ligne d’en-tête et placez dans une cellule un Smart Marker qui référence le champ de tableau avec l’attribut `arrayassingle` (et `arraydelimiter` lorsqu’un séparateur personnalisé est nécessaire).
3. **Instanciez le WorkbookDesigner** : Créez un `WorkbookDesigner` autour du classeur et associez vos lignes JSON à l’aide de `setJsonDataSource`.
4. **Traitez les marqueurs** : Appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrez le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de base d’un tableau de chaînes**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

L’exemple affiche la valeur concaténée de l’ensemble du tableau. Les quatre étiquettes sont regroupées dans une seule cellule et séparées par la virgule par défaut :

```
C#,Aspose,SmartMarker,Excel
```

### **Exemple de code 2 — Valeurs numériques avec un séparateur personnalisé**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

Avec les scores fournis sous forme de chaînes JSON, la sortie concaténée conserve les nombres bruts :

```
95-88-76-100-67
```

{{% alert color="note" %}}
Les nombres JSON transmis par le moteur Java arrivent sous forme de valeurs à virgule flottante, de sorte que `[95, 88]` donnerait `95.0-88.0` après concaténation. Placez les nombres entre guillemets dans les lignes JSON lorsque vous souhaitez obtenir le texte exact des entiers dans la cellule concaténée.
{{% /alert %}}

### **Exemple de code 3 — Comparaison du rendu par défaut et du rendu dans une seule cellule**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Le marqueur par défaut remplit une cellule par élément, verticalement dans la colonne B, tandis que le marqueur `arrayassingle` condense le même tableau dans une seule cellule de la colonne C :

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes et bonnes pratiques**

Gardez les points suivants à l’esprit lorsque vous utilisez les attributs `arrayassingle` et `arraydelimiter` :
- Les valeurs d’attribut utilisent la forme `name:value`. Une forme avec signe égal, telle que `arrayassingle=true`, n’est pas reconnue et entraîne en silence un retour au comportement de propagation par défaut.
- Séparez les attributs par une virgole et sans espaces ; un espace après la virgule décale la valeur du séparateur d’un caractère (voir l’avertissement ci-dessus).
- La valeur de `arraydelimiter` peut être un caractère unique écrit directement après le deux-points ou une chaîne multicaractère entourée de guillemets doubles.
- Lorsque `arraydelimiter` est omis, les éléments sont concaténés avec une virgule.
- Fournissez les champs de tableau au moyen des objets de ligne de `setJsonDataSource` ; les objets Python ordinaires et les dictionnaires transmis à `setDataSource` ne sont pas liés sur cette plateforme.
- Par l’intermédiaire du moteur Java, les nombres JSON arrivent sous forme de valeurs à virgule flottante (`95` devient `95.0` après concaténation) ; placez les valeurs numériques entre guillemets dans les lignes JSON lorsque le texte exact des entiers est important.
- Placez le Smart Marker dans une cellule assez large pour afficher la chaîne concaténée obtenue ; sinon, selon le format, le contenu peut déborder visuellement sur les cellules adjacentes.

## **Articles connexes**
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Python via Java](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via Java](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/python-java/change-page-field-layout/)
- [Convertir Sparkline en image et HTML dans Aspose.Cells for Python via Java](/cells/fr/python-java/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}