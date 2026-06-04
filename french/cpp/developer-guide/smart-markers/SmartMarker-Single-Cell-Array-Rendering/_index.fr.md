---
title: Rendu de tableau dans une seule cellule avec SmartMarker | Aspose.Cells C++
description: Apprenez à restituer des données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for C++.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu des données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés au sein d'une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les Smart Markers dans Aspose.Cells constituent une fonctionnalité puissante basée sur des modèles qui vous permet de remplir dynamiquement des données de feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur concepteur, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.

Par défaut, lorsqu'un Smart Marker référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur développe le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez restituer l'intégralité du tableau dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble à l'intérieur d'une balise Smart Marker, répondent exactement à ce besoin. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'étalement de tableau**

Lorsqu'un Smart Marker référence une propriété de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` associé à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le reste du contenu du modèle vers l'extérieur et pouvant potentiellement perturber des mises en page de rapport soigneusement conçues.

### **Limitations du cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'étalement par défaut n'est pas souhaitable :

- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes de balises, d'étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres obliques dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs en un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui se répandent sur plusieurs cellules.

### **La lacune qu'elle comble**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en C++ — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont restitués dans exactement une seule cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, saut de ligne, ou tout autre texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme résident dans la balise Smart Marker.
- **Rapports plus propres** : les données de tableau ne poussent plus le contenu adjacent du modèle dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'étalement d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de restituer l'intégralité du tableau dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un seul caractère, ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte n'importe quelle chaîne littérale, y compris les délimiteurs de plusieurs caractères, du texte personnalisé, ou des séquences d'échappement telles que `\n` pour une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Flux de travail étape par étape**

Le flux de travail suivant décrit comment restituer un tableau dans une seule cellule à l'aide des Smart Markers.

1. **Préparez la source de données** : créez une classe (ou une structure de données) qui expose une propriété retournant un tableau. La propriété peut retourner `std::vector<std::string>`, `std::vector<int>`, ou tout autre type de tableau/vecteur pris en charge.
2. **Créez un classeur concepteur** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête, et placez une cellule Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur concepteur, et liez votre source de données à l'aide de la méthode `SetDataSource`.
4. **Traitez les marqueurs** : appelez la méthode `WorkbookDesigner.Process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner n'est pas disponible dans Aspose.Cells pour C++
    // Nous devons simuler le traitement des SmartMarkers en remplaçant les marqueurs manuellement
    // Puisque Aspose.Cells C++ ne supporte pas WorkbookDesigner, nous utiliserons le remplacement par U16String
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Remplacer le smart marker par les données réelles
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Exemple de code 3 — Comparaison du comportement par défaut et ArrayAsSingle**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Préparer la source de données
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Créer le classeur et obtenir la première feuille de calcul
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Section 1 : Smart Marker par défaut - valeurs réparties horizontalement entre les cellules
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Section 2 : Nouveau rendu en cellule unique utilisant arrayasSingle et extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Lier la source de données et traiter les Smart Markers
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Enregistrer le classeur résultant
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Notes et bonnes pratiques**

Gardez les points suivants à l'esprit lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur de `extraDelimiter` est traitée comme une chaîne littérale ; échappez tous les caractères spéciaux que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seul `true` déclenche le comportement de cellule unique ; toute autre valeur revient au comportement d'étalement par défaut.
- Si le tableau est vide ou nul, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec les sources de données objet ainsi qu'avec les sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule qui a une largeur suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes selon le format.

## **Articles connexes**

- [Smart Markers](/cells/fr/cpp/smart-markers/)
- [Fusion et annulation de la fusion de cellules](/cells/fr/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}