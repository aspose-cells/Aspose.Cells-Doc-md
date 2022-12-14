---
title: Créer des plages nommées d'étendue de classeur et de feuille de calcul
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/net/create-workbook-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux étendues différentes : classeur (également appelé étendue globale) et feuille de calcul.

- Les plages nommées avec une étendue de classeur sont accessibles à partir de n'importe quelle feuille de calcul de ce classeur en utilisant simplement son nom.
- Les plages nommées étendues à la feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elles ont été créées.

Aspose.Cells fournit la même fonctionnalité que Microsoft Excel pour l'ajout de plages nommées de classeur et de feuille de calcul. Lors de la création d'une plage nommée de portée de feuille de calcul, la référence de feuille de calcul doit être utilisée dans la plage nommée pour la spécifier en tant que plage nommée de portée de feuille de calcul.

{{% /alert %}} 
## **Ajout d'une plage nommée avec un classeur délimité**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Ajout d'une plage nommée avec l'étendue de la feuille de calcul**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/net/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/net/format-and-modify-named-ranges/)
- [Obtenir la portée avec des liens externes](/cells/fr/net/get-range-with-external-links/)
- [Implémentation de plages non séquentielles](/cells/fr/net/implementing-non-sequential-ranges/)
