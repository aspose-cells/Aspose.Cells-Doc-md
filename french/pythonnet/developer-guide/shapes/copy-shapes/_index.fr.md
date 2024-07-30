---
title: Copier les formes entre les feuilles de calcul
linktitle: Copier les formes
type: docs
weight: 200
url: /fr/python-net/copy-shapes-between-worksheets/
description: Cet article montre comment copier des formes entre des feuilles de calcul via l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Copier des formes entre des feuilles de calcul en Python, Comment copier une image d une feuille de calcul à une autre en Python, Comment copier un graphique d une feuille de calcul à une autre en Python, Comment copier des contrôles et autres objets de dessin d une feuille de calcul à une autre en Python.
---

{{% alert color="primary" %}}

Parfois, vous devez copier des éléments sur une feuille de calcul, par exemple des images, des graphiques et d'autres objets de dessin, entre les feuilles de calcul. Aspose.Cells pour Python via .NET prend en charge cette fonctionnalité. Les graphiques, images et autres objets peuvent être copiés avec le plus grand degré de précision.

Cet article vous donne une compréhension détaillée de comment copier des formes entre les feuilles de calcul.

{{% /alert %}}

## **Copier une image d'une feuille de calcul à une autre**

Pour copier une image d'une feuille de calcul à une autre, utilisez la méthode [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) comme indiqué dans le code exemple ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Copier un graphique d'une feuille de calcul à une autre**

Le code suivant démontre l'utilisation de la méthode [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) pour copier un graphique d'une feuille de calcul à une autre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Copier les contrôles et autres objets de dessin d'une feuille de calcul à une autre**

Pour copier les contrôles et autres objets de dessin, utilisez la méthode [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) comme indiqué dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
