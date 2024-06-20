---
title: Implémenter des étiquettes de sous total ou de grand total dans d autres langues
type: docs
weight: 50
url: /fr/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez afficher des étiquettes de sous-total et de grand total dans des langues autres que l'anglais, comme le chinois, le japonais, l'arabe, l'hindi, etc. Aspose.Cells vous permet de le faire en utilisant la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) et la propriété [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Veuillez consulter cet article sur comment utiliser la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [Utilisation de la classe GlobalizationSettings pour des étiquettes de sous-total personnalisées et d'autres étiquettes du graphique circulaire](/cells/fr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implémenter des étiquettes de sous-total ou de grand total dans d'autres langues**

Le code d'exemple suivant charge le [fichier Excel exemple](5115151.xlsx) et implémente les noms de sous-total et de grand total en chinois. Veuillez consulter le [fichier Excel de sortie](5115152.xlsx) généré par ce code pour votre référence. Nous créons d'abord une classe de [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) et l'utilisons ensuite dans notre code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Utilisez maintenant la classe créée ci-dessus dans le code comme ci-dessous :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
