---
title: Obtenir et définir le style des cellules avec C++
linktitle: Styles
type: docs
weight: 50
url: /fr/cpp/styling-and-data-formatting/
description: Découvrez comment effectuer la mise en forme et la stylisation des données dans Aspose.Cells for C++, notamment la mise en forme du texte, la mise en forme numérique, la mise en forme des dates, et d autres options de stylisation. Notre guide vous aidera à créer des feuilles de calcul professionnelles avec une mise en forme attrayante.
keywords: Aspose.Cells for C++, mise en forme des données, stylisation, mise en forme du texte, mise en forme numérique, mise en forme des dates, options de stylisation, feuilles de calcul, mise en forme attrayante, aspect professionnel.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ a introduit deux nouvelles méthodes pour formater les cellules : `Cell.GetStyle` et `Cell.SetStyle`. Cet article examine l'approche `Cell.GetStyle`/`SetStyle` pour vous aider à juger quelle technique vous convient le mieux.

{{% /alert %}}

## **Mise en forme des cellules**
Il y a deux façons de formater une cellule, illustrées ci-dessous.

### **Utilisation de GetStyle()**
Avec le code suivant, un objet `Style` est initialisé pour chaque cellule lors du formatage. Si un grand nombre de cellules sont formatées, une grande quantité de mémoire est consommée car l'objet `Style` est volumineux. Ces objets `Style` ne seront libérés que lorsque la méthode `Workbook.Save` sera appelée.

**C++**

```cpp
cell.GetStyle()->GetFont()->SetIsBold(true);
```

### **Utilisation de SetStyle()**
La première approche est simple et directe, alors pourquoi avons-nous ajouté la deuxième approche ?

Nous avons ajouté la deuxième approche pour optimiser l'utilisation de la mémoire. Après avoir utilisé la méthode `Cell.GetStyle` pour récupérer un objet `Style`, le modifier et utiliser la méthode `Cell.SetStyle` pour le réaffecter à cette cellule. Cet objet `Style` ne sera pas conservé, et le runtime C++ le collectera lorsqu'il ne sera plus référencé.

Lors de l'appel à la méthode `Cell.SetStyle`, l'objet `Style` n'est pas enregistré pour chaque cellule. Au lieu de cela, nous comparons cet objet `Style` à un pool interne d'objets `Style` pour voir s'il peut être réutilisé. Seuls les objets `Style` qui diffèrent de ceux existants sont conservés pour chaque objet `Workbook`. Cela signifie qu'il n'y a que quelques centaines d'objets `Style` par fichier Excel au lieu de milliers. Pour chaque cellule, seul un index vers le pool d'objets `Style` est conservé.

**C++**

```cpp
auto style = cell.GetStyle();
style->GetFont()->SetIsBold(true);
cell.SetStyle(style);
```

## **Sujets avancés**
- [Créer un objet Style en utilisant la classe CellsFactory](/cells/fr/cpp/create-style-object-using-cellsfactory-class/)
- [Modifier un style existant](/cells/fr/cpp/modify-an-existing-style/)
- [Réutilisation des objets Style](/cells/fr/cpp/reusing-style-objects/)
- [Utilisation des Styles Intégrés](/cells/fr/cpp/using-built-in-styles/)
{{< app/cells/assistant language="cpp" >}}
