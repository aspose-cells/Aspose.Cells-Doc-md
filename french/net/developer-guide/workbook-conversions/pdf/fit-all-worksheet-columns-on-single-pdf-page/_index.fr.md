---
title: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Parfois, vous voulez générer un fichier PDF qui adapte toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) offre cette fonctionnalité de manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur du PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) s'assure que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données dans la feuille de calcul.

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) pour afficher une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
