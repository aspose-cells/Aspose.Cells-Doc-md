---
title: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 610
url: /fr/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells offre maintenant la propriété [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) pour trouver si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de distinguer entre les chaînes comme échantillon et 'échantillon etc.

{{% /alert %}} 
## **Trouver si la valeur de la cellule commence par un guillemet simple**
Le code d'exemple suivant explique que les chaînes comme échantillon et 'échantillon ne peuvent pas être différenciées avec la propriété [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). Par conséquent nous devons utiliser la propriété [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) pour les distinguer.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
