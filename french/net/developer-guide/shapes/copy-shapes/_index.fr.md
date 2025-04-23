---
title: Copier les formes entre les feuilles de calcul
linktitle: Copier les formes
type: docs
weight: 200
url: /fr/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de copier des éléments sur une feuille de calcul, par exemple des images, des graphiques et d'autres objets de dessin, entre des feuilles de calcul. Aspose.Cells prend en charge cette fonctionnalité. Les graphiques, les images et d'autres objets peuvent être copiés avec le plus haut degré de précision.

Cet article vous donne une compréhension détaillée de comment copier des formes entre les feuilles de calcul.

{{% /alert %}}

## **Copier une image d'une feuille de calcul à une autre**

Pour copier une image d'une feuille de calcul à une autre, utilisez la méthode [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) comme indiqué dans le code exemple ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Copier un graphique d'une feuille de calcul à une autre**

Le code suivant démontre l'utilisation de la méthode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) pour copier un graphique d'une feuille de calcul à une autre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Copier les contrôles et autres objets de dessin d'une feuille de calcul à une autre**

Pour copier les contrôles et autres objets de dessin, utilisez la méthode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) comme indiqué dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
{{< app/cells/assistant language="csharp" >}}
