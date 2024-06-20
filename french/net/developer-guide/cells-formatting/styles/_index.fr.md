---
title: Obtenir et définir le style pour les cellules
description: Découvrez comment effectuer la mise en forme des données et le style dans Aspose.Cells for .NET, y compris la mise en forme du texte, la mise en forme des nombres, la mise en forme des dates et d autres options de style. Notre guide vous aidera à créer des feuilles de calcul au look professionnel avec une mise en forme attrayante.
keywords: Aspose.Cells for .NET, mise en forme des données, style, mise en forme du texte, mise en forme des nombres, mise en forme des dates, options de style, feuilles de calcul, mise en forme attrayante, aspect professionnel.
linktitle: Styles
type: docs
weight: 50
url: /fr/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 a introduit deux nouvelles méthodes pour formater les cellules : Cell.GetStyle et Cell.SetStyle. Cet article examine l'approche Cell.GetStyle/SetStyle pour vous aider à juger quelle technique vous convient le mieux.

{{% /alert %}} 
## **Mise en forme des cellules**
Il y a deux façons de formater une cellule, illustrées ci-dessous.
### **Utilisation de GetStyle()**
Avec le morceau de code suivant, un objet Style est initié pour chaque cellule lors de sa mise en forme. Si beaucoup de cellules sont formatées, une grande quantité de mémoire est consommée car l'objet Style est un objet volumineux. Ces objets Style ne seront pas libérés tant que la méthode Workbook.Save n'est pas appelée.



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Utilisation de SetStyle()**
La première approche est facile et directe, alors pourquoi avons-nous ajouté la deuxième approche ?

Nous avons ajouté la deuxième approche pour optimiser l'utilisation de la mémoire. Après avoir utilisé la méthode Cell.GetStyle pour récupérer un objet Style, le modifier et utiliser la méthode Cell.SetStyle pour le réintégrer dans cette cellule. Cet objet Style ne sera pas préservé et .NET GC le collectera lorsqu'il ne sera pas référencé.

Lors de l'appel de la méthode Cell.SetStyle, l'objet Style n'est pas enregistré pour chaque cellule. Au lieu de cela, nous comparons cet objet Style à un pool interne d'objets Style pour voir s'il peut être réutilisé. Seuls les objets Style qui diffèrent des existants sont conservés pour chaque objet Workbook. Cela signifie qu'il n'y a que plusieurs centaines d'objets Style pour chaque fichier Excel au lieu de milliers. Pour chaque cellule, seul un index vers le pool d'objets Style est conservé.



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **Sujets avancés**
- [Créer un objet Style en utilisant la classe CellsFactory](/cells/fr/net/create-style-object-using-cellsfactory-class/)
- [Modifier un style existant](/cells/fr/net/modify-an-existing-style/)
- [Réutilisation des objets Style](/cells/fr/net/reusing-style-objects/)
- [Utilisation des Styles Intégrés](/cells/fr/net/using-built-in-styles/)


