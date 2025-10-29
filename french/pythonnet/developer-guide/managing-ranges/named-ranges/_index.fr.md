---
title: Créez des plages nommées étendues pour le classeur et la feuille de calcul
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: Cet article montre comment créer des plages nommées étendues pour le classeur et la feuille de calcul avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Créer des plages nommées étendues pour le classeur et la feuille de calcul Python, Ajouter une plage nommée avec étendue de classeur Python, Ajouter une plage nommée avec étendue de feuille de calcul Python.
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells pour Python via .NET offre la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées avec une portée de classeur et de feuille de calcul. Lors de la création d'une plage nommée avec une portée de feuille de calcul, la référence de la feuille de calcul doit être utilisée dans la plage nommée pour la spécifier comme une plage nommée avec une portée de feuille de calcul.


{{% /alert %}} 
## **Comment ajouter une plage nommée avec une portée de classeur**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **Comment ajouter une plage nommée avec une portée de feuille de calcul**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/python-net/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/python-net/format-and-modify-named-ranges/)
- [Obtenir une plage avec des liens externes](/cells/fr/python-net/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/python-net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="python-net" >}}
