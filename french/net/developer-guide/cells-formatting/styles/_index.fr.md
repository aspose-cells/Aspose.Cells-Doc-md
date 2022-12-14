---
title: Obtenir et définir le style des cellules
linktitle: modes
type: docs
weight: 50
url: /fr/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 introduit deux nouvelles méthodes de formatage des cellules : Cell.GetStyle et Cell.SetStyle. Cet article examine l'approche Cell.GetStyle/SetStyle pour vous aider à déterminer la technique qui vous convient le mieux.

{{% /alert %}} 
## **Formatage Cells**
Il existe deux manières de formater une cellule, illustrées ci-dessous.
### **Utilisation de GetStyle()**
Avec le morceau de code suivant, un objet Style est lancé pour chaque cellule lors du formatage. Si un grand nombre de cellules sont formatées, une grande quantité de mémoire est consommée car l'objet Style est un objet volumineux. Ces objets Style ne seront pas libérés tant que la méthode Workbook.Save n'aura pas été appelée.



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Utilisation de SetStyle()**
La première approche est simple et directe, alors pourquoi avons-nous ajouté la seconde approche ?

Nous avons ajouté la deuxième approche pour optimiser l'utilisation de la mémoire. Après avoir utilisé la méthode Cell.GetStyle pour récupérer un objet Style, modifiez-le et utilisez la méthode Cell.SetStyle pour le redéfinir sur cette cellule. Cet objet Style ne sera pas conservé et .NET GC le collecte lorsqu'il n'est pas référencé.

Lors de l'appel de la méthode Cell.SetStyle, l'objet Style n'est pas enregistré pour chaque cellule. Au lieu de cela, nous comparons cet objet Style à un pool d'objets Style interne pour voir s'il peut être réutilisé. Seuls les objets Style qui diffèrent des objets existants sont conservés pour chaque objet Workbook. Cela signifie qu'il n'y a que plusieurs centaines d'objets Style pour chaque fichier Excel au lieu de milliers. Pour chaque cellule, seul un index vers le pool d'objets Style est conservé.



**C#**

{{< highlight "csharp" >}}

 Style style = cellule.GetStyle();

style.Font.IsBold = true;

cellule.SetStyle(style);


## **Sujets avancés**
- [Créer un objet Style à l'aide de la classe CellsFactory](/cells/fr/net/create-style-object-using-cellsfactory-class/)
- [Modifier un style existant](/cells/fr/net/modify-an-existing-style/)
- [Réutilisation des objets de style](/cells/fr/net/reusing-style-objects/)
- [Utilisation des styles intégrés](/cells/fr/net/using-built-in-styles/)


