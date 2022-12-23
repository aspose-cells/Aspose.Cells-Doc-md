---
title: Rechercher si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 610
url: /fr/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit désormais le[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) propriété pour déterminer si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de faire la distinction entre des chaînes comme sample et 'sample etc.

{{% /alert %}} 
## **Rechercher si la valeur de la cellule commence par un guillemet simple**
L'exemple de code suivant explique que les chaînes telles que sample et 'sample ne peuvent pas être différenciées avec[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) la propriété. Nous devons donc utiliser[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)propriété de les distinguer.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
