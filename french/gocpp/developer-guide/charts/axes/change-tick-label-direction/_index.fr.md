---
title: Changer la direction de l étiquette de graduation avec Golang via C++
linktitle: Modifier la direction des étiquettes de graduation
description: Apprenez comment changer la direction des étiquettes des graduations dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment ajuster l’orientation des étiquettes des graduations sur les axes, y compris horizontal, vertical et inclinée.
keywords: Aspose.Cells for C++, étiquettes de graduation, direction, orientation, axes, horizontal, vertical, inclinée.
type: docs
weight: 170
url: /fr/go-cpp/change-tick-label-direction/
---

## **Changer la direction des étiquettes des graduations**

Aspose.Cells vous offre la possibilité de changer la direction des étiquettes de graduation du graphique en utilisant la propriété [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/). La propriété [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/) accepte la valeur d'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). L'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) fournit les membres suivants :

- Horizontale
- Verticale
- Rotation90
- Rotation270
- Empilée

L’image suivante compare le fichier source et le fichier de sortie :

### **Image du fichier source**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Image du fichier de sortie**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Le snippet de code suivant change la direction des étiquettes de graduation de Rotation90 à Horizontale.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTickLabelDirection.go" >}}
Les fichiers source et de sortie peuvent être téléchargés à partir des liens suivants.

[Fichier source](105480221.xlsx)

[Fichier de sortie](105480223.xlsx)
