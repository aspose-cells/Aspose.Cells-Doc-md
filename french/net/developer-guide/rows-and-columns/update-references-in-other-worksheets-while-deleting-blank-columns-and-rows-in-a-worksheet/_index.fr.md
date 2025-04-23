---
title: Mettre à jour les références dans d autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul
type: docs
weight: 5000
url: /fr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Lorsque vous supprimez les colonnes et les rangées vides dans une feuille de calcul, les références dans d'autres feuilles de calcul deviennent invalides. Si vous souhaitez éviter ce comportement et que ces références de la feuille de calcul actuelle dans d'autres feuilles de calcul soient également mises à jour, veuillez utiliser la propriété [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) et la définir sur **true**.

{{% /alert %}}

## **Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul**

Veuillez consulter le code d'exemple suivant et sa sortie console. La cellule E3 dans la deuxième feuille de calcul a une formule =Sheet1!C3 qui fait référence à la cellule C3 dans la première feuille de calcul. Si vous définissez la propriété [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) sur **true**, cette formule sera mise à jour et deviendra =Sheet1!A1 en supprimant les colonnes et les rangées vides dans la première feuille de calcul. Cependant, si vous définissez la propriété [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) sur **false**, la formule de la cellule E3 de la deuxième feuille de calcul restera =Sheet1!C3 et deviendra invalide.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) a été définie sur **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Il s'agit de la sortie console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) a été définie sur **false**. Comme vous pouvez le voir, la formule de la cellule E3 de la deuxième feuille de calcul n'est pas mise à jour et sa valeur est maintenant 0 au lieu de 4, ce qui est invalide.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
