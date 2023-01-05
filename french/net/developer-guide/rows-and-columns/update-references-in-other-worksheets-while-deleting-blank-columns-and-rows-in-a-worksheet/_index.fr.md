---
title: Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant des colonnes et des lignes vides dans une feuille de calcul
type: docs
weight: 5000
url: /fr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

Lorsque vous supprimez des colonnes et des lignes vides dans une feuille de calcul, ses références dans d'autres feuilles de calcul deviennent invalides. Si vous souhaitez éviter ce comportement et souhaitez que les références de la feuille de calcul actuelle dans d'autres feuilles de calcul soient également mises à jour, veuillez utiliser le[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) propriété et définissez-la sur**vrai**.

{{% /alert %}}

## **Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant des colonnes et des lignes vides dans une feuille de calcul**

 Veuillez consulter l'exemple de code suivant et sa sortie de console. La cellule E3 dans la deuxième feuille de calcul a une formule = Sheet1! C3 qui fait référence à la cellule C3 dans la première feuille de calcul. Si vous définissez[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) propriété comme**vrai** , cette formule sera mise à jour et deviendra =Sheet1!A1 lors de la suppression des colonnes et des lignes vides dans la première feuille de calcul. Cependant, si vous définissez[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) propriété comme**faux**, la formule dans la cellule E3 de la deuxième feuille de calcul restera =Feuille1!C3 et deviendra invalide.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Sortie console**

 Il s'agit de la sortie console de l'exemple de code ci-dessus lorsque[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) la propriété a été définie comme**vrai**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

 Il s'agit de la sortie console de l'exemple de code ci-dessus lorsque[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) la propriété a été définie comme**faux**. Comme vous pouvez le voir, la formule dans la cellule E3 de la deuxième feuille de calcul n'est pas mise à jour et sa valeur de cellule est maintenant 0 au lieu de 4, ce qui n'est pas valide.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
