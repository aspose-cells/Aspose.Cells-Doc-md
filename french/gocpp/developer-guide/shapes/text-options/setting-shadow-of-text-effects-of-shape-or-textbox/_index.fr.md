---
title: Configuration de l ombre des effets de texte de la forme ou de la zone de texte avec Golang via C++
linktitle: Définir l ombre des effets de texte
type: docs
weight: 250
url: /fr/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Apprenez comment définir l ombre des effets de texte pour les formes ou les zones de texte en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez définir la **Ombre** des **Effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser la propriété [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/). Elle présente le réglage du texte de la forme et retourne des objets [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Après y avoir accédé, veuillez définir la **Ombre** via la propriété [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Cette propriété est de type [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) qui a plusieurs valeurs. Certaines sont :

- DécalageDiagonaleInférieureDroite
- DécalageBas
- DécalageDiagonaleSupérieureDroite
- ÀL'intérieurGauche
- ÀL'IntérieurCentre
- DiagonalePerspectiveSupérieureGauche
- DiagonalePerspectiveInférieureDroite

{{% /alert %}}

Le snippet de code suivant démontre l'utilisation de la propriété [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) pour définir l'ombre des effets de texte de la forme ou zone de texte.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
