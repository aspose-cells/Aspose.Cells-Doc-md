---
title: Utiliser le pinceau de mise en forme
type: docs
weight: 80
url: /fr/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Cet article présente le pinceau de mise en forme dans GridDesktop.
---

{{% alert color="primary" %}} 

Le pinceau de mise en forme est une fonctionnalité de MS Excel qui a été adaptée dans Aspose.Cells.GridDesktop. C'est une très belle fonctionnalité. Pour les personnes qui n'ont pas encore utilisé cette fonctionnalité, le pinceau de mise en forme permet aux utilisateurs d'appliquer les paramètres de mise en forme de n'importe quelle cellule ciblée à une autre cellule. La mise en œuvre de cette fonctionnalité est très simple. Dans ce sujet, nous couvrirons cela aussi.

{{% /alert %}} 
## **Utilisation du pinceau de mise en forme**
La fonctionnalité du **Pinceau de mise en forme** nécessite que les utilisateurs sélectionnent une cellule dont les paramètres de mise en forme doivent être appliqués sur d'autres cellules, puis appellent la méthode **StartFormatPainter** de **GridDesktop**. Il existe deux modes de pinceau de mise en forme comme suit:

- **Utiliser le pinceau de mise en forme une fois**
- **Utiliser toujours le copieur de mise en forme**
### **Utiliser le copieur de mise en forme une fois**
Si les développeurs veulent utiliser la fonctionnalité du copieur de format une seule fois pour appliquer les paramètres de formatage d'une cellule ciblée à une seule cellule, ils peuvent le faire en appelant la méthode **StartFormatPainter** et en lui passant une valeur **false**. Cette valeur **false** empêchera le copieur de format de peindre à jamais.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Utiliser toujours le copieur de mise en forme**
Utiliser toujours le copieur de mise en forme est une fonctionnalité utile lorsque nous devons appliquer les paramètres de formatage à plus d'une cellule. Les développeurs peuvent obtenir cette fonctionnalité en appelant simplement la méthode **StartFormatPainter** et en lui passant une valeur **true**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Ce type de copieur de format peint toujours à moins que nous ne l'arrêtions. Ainsi, pour arrêter le copieur de format de peindre toujours, nous pouvons simplement appeler la méthode **EndFormatPainter** de **GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
