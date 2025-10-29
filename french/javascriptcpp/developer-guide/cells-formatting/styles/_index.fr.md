---
title: Obtenir et définir le style pour les cellules
description: Découvrez comment effectuer le formatage et la stylisation des données dans Aspose.Cells for JavaScript via C++, y compris le formatage du texte, des nombres, des dates, et d autres options de style. Notre guide vous aidera à créer des tableurs d apparence professionnelle avec un formatage attrayant.
keywords: Aspose.Cells for JavaScript via C++, formatage de données, stylisation, formatage de texte, formatage de nombres, formatage de dates, options de stylisation, tableurs, formatage attrayant, apparence professionnelle.
linktitle: Styles
type: docs
weight: 50
url: /fr/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript via C++ a introduit deux nouvelles méthodes pour le formatage des cellules : Cell.style et Cell.style. Cet article examine l'approche Cell.style/style pour vous aider à juger quelle technique vous conviendrait le mieux.

{{% /alert %}} 
## **Mise en forme des cellules**
Il y a deux façons de formater une cellule, illustrées ci-dessous.
### **Utiliser le style**
Avec le code suivant, un objet Style est initié pour chaque cellule lors du formatage. Si de nombreuses cellules sont formatées, une grande quantité de mémoire est consommée car l'objet Style est volumineux. Ces objets Style ne seront pas libérés tant que la méthode Workbook.save n'aura pas été appelée.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Utiliser le style**
La première approche est facile et directe, alors pourquoi avons-nous ajouté la deuxième approche ?

Nous avons ajouté une seconde approche pour optimiser l'utilisation de la mémoire. Après avoir utilisé la propriété Cell.style pour récupérer un objet Style, modifiez-le et réaffectez-le en utilisant la même propriété à cette cellule. Cet objet Style ne sera pas conservé et le ramasse-miettes de JavaScript le récupérera lorsqu'il ne sera plus référencé.

Lors de l'affectation de la propriété Cell.style, l'objet Style n'est pas sauvegardé pour chaque cellule. Au lieu de cela, nous comparons cet objet Style à un pool interne d'objets Style pour voir s'il peut être réutilisé. Seuls les objets Style différents des existants sont conservés pour chaque objet Workbook. Cela signifie qu'il n'y a que quelques centaines d'objets Style pour chaque fichier Excel au lieu de milliers. Pour chaque cellule, seul un index vers le pool d'objets Style est conservé.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Sujets avancés**
- [Créer un objet Style en utilisant la classe CellsFactory](/cells/fr/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Modifier un style existant](/cells/fr/javascript-cpp/modify-an-existing-style/)
- [Réutilisation des objets Style](/cells/fr/javascript-cpp/reusing-style-objects/)
- [Utilisation des Styles Intégrés](/cells/fr/javascript-cpp/using-built-in-styles/)
