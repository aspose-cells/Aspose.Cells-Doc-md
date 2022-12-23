---
title: Mettre en œuvre des étiquettes de sous-total ou de total général dans d'autres langues
type: docs
weight: 50
url: /fr/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez afficher des étiquettes de sous-total et de total général dans des langues autres que l'anglais comme le chinois, le japonais, l'arabe, l'hindi, etc. Aspose.Cells vous permet de le faire en utilisant le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classe et[**Workbook.GlobalizationSettingsWorkbook.GlobalizationSettingsWorkbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) la propriété. Veuillez consulter cet article pour savoir comment utiliser[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classe

- [Utilisation de la classe GlobalizationSettings pour les étiquettes de sous-total personnalisées et une autre étiquette de graphique à secteurs](/cells/fr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Mettre en œuvre des étiquettes de sous-total ou de total général dans d'autres langues**

 L'exemple de code suivant charge le[exemple de fichier excel](5115151.xlsx) et implémente les noms de sous-total et de total général en chinois. S'il vous plaît, vérifiez le[fichier Excel de sortie](5115152.xlsx) généré par ce code pour votre référence. Nous créons d'abord une classe de[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)puis l'utiliser dans notre code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Utilisez maintenant la classe créée ci-dessus dans le code comme ci-dessous :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
