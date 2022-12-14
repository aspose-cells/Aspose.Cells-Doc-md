---
title: Utilisation du peintre de format
type: docs
weight: 80
url: /fr/net/using-format-painter/
---
{{% alert color="primary" %}} 

Le peintre de format est la fonctionnalité de MS Excel qui a été adaptée dans Aspose.Cells.GridDesktop. C'est une très belle fonctionnalité. Pour les personnes qui n'ont pas encore utilisé cette fonctionnalité, le peintre de format permet aux utilisateurs d'appliquer les paramètres de formatage de n'importe quelle cellule ciblée à une autre cellule. La mise en œuvre de cette fonctionnalité est très simple. Dans ce sujet, nous couvrirons cela aussi.

{{% /alert %}} 
## **Utilisation du peintre de format**
 La caractéristique de**Peintre de format** demande aux utilisateurs de sélectionner une cellule dont vous souhaitez appliquer les paramètres de mise en forme à d'autres cellules, puis d'appeler**StartFormatPainter** méthode**GrilleDesktop**. Il existe deux modes de peintre de format comme suit :

- **Utiliser Format Painter une fois**
- **Toujours utiliser Format Painter**
### **Utiliser Format Painter une fois**
 Si les développeurs souhaitent utiliser la fonctionnalité de peintre de format une seule fois pour appliquer les paramètres de formatage d'une cellule ciblée à une seule cellule, ils peuvent le faire en appelant**StartFormatPainter** méthode et en passant un**faux** valeur à elle. Cette**faux** valeur empêchera format painter de peindre pour toujours.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Toujours utiliser Format Painter**
Utiliser le peintre de format est toujours une fonctionnalité utile lorsque nous devons appliquer les paramètres de formatage sur plusieurs cellules. Les développeurs peuvent obtenir cette fonctionnalité en appelant simplement**StartFormatPainter** méthode et en passant un**vrai** valeur à elle.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Ce genre de peintre de format continue de peindre pour toujours à moins que nous l'arrêtions. Donc, pour empêcher le peintre de format de toujours peindre, nous pouvons simplement appeler**EndFormatPainter** méthode de**GrilleDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
