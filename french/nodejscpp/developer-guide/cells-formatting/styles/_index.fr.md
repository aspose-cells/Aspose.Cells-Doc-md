---
title: Obtenir et définir le style pour les cellules
description: Découvrez comment effectuer le formatage et la mise en style des données dans Aspose.Cells for Node.js via C++, notamment le formatage du texte, le formatage des nombres, le formatage des dates et d autres options de style. Notre guide vous aidera à créer des feuilles de calcul d apparence professionnelle avec un formatage attrayant.
keywords: Aspose.Cells for Node.js via C++, formatage des données, style, formatage du texte, formatage des nombres, formatage des dates, options de style, feuilles de calcul, attrayant, professionnel.
linktitle: Styles
type: docs
weight: 50
url: /fr/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ a introduit deux nouvelles méthodes pour le formatage des cellules : Cell.getStyle et Cell.setStyle. Cet article examine l'approche Cell.getStyle/setStyle pour vous aider à juger quelle technique vous convient le mieux.

{{% /alert %}} 
## **Mise en forme des cellules**
Il y a deux façons de formater une cellule, illustrées ci-dessous.
### **Utilisation de getStyle()**
Avec le code suivant, un objet Style est initié pour chaque cellule lors du formatage. Si de nombreuses cellules sont formatées, une grande quantité de mémoire est consommée car l'objet Style est volumineux. Ces objets Style ne seront pas libérés tant que la méthode Workbook.save n'aura pas été appelée.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **Utilisation de setStyle()**
La première approche est facile et directe, alors pourquoi avons-nous ajouté la deuxième approche ?

Nous avons ajouté la deuxième approche pour optimiser l'utilisation de la mémoire. Après avoir utilisé la méthode Cell.getStyle pour récupérer un objet Style, modifiez-le et utilisez la méthode Cell.setStyle pour le réassigner à cette cellule. Cet objet Style ne sera pas conservé et le ramasse-miettes de JavaScript le collectera lorsqu'il ne sera plus référencé.

Lors de l'appel de la méthode Cell.setStyle, l'objet Style n'est pas enregistré pour chaque cellule. À la place, nous comparons cet objet Style à une réserve interne d'objets Style pour voir s'il peut être réutilisé. Seuls les objets Style qui diffèrent de ceux existants sont conservés pour chaque objet Workbook. Cela signifie qu'il n'y a que quelques centaines d'objets Style pour chaque fichier Excel au lieu de milliers. Pour chaque cellule, seul un indice vers la réserve d'objets Style est conservé.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Sujets avancés**
- [Créer un objet Style en utilisant la classe CellsFactory](/cells/fr/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Modifier un style existant](/cells/fr/nodejs-cpp/modify-an-existing-style/)
- [Réutilisation des objets Style](/cells/fr/nodejs-cpp/reusing-style-objects/)
- [Utilisation des Styles Intégrés](/cells/fr/nodejs-cpp/using-built-in-styles/)

