---
title: Verrouiller le filigrane WordArt avec Golang via C++
linktitle: Verrouiller le filigrane WordArt
type: docs
weight: 170
url: /fr/go-cpp/locking-wordart-watermark/
description: Découvrez comment verrouiller les filigranes WordArt dans les feuilles de calcul Excel en utilisant Aspose.Cells for C++. Empêchez la modification, le déplacement et la sélection des filigranes de manière programmatique.
---

{{% alert color="primary" %}}

 Les API Aspose.Cells permettent d'ajouter des filigranes WordArt sur la feuille de calcul de manière à ce que le WordArt devienne un objet que vous pouvez déplacer et positionner sur la feuille. Il est également possible de verrouiller l'objet WordArt pour toute interaction comme la modification, le déplacement et la sélection. Cet article explique l'utilisation de la méthode [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/go-cpp/shape/setlockedproperty/) pour verrouiller certains aspects du filigrane.

{{% /alert %}}

 Les API Aspose.Cells permettent de verrouiller certains aspects du filigrane afin que l'interaction de l'utilisateur puisse être limitée ou complètement bloquée. Le code suivant démontre l'utilisation de l'API Aspose.Cells for C++ pour verrouiller la sélection, le déplacement, la modification et le redimensionnement du filigrane en créant une feuille de calcul à partir de zéro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LockingWordartWatermark.go" >}}
