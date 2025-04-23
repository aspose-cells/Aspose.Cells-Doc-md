---
title: Définir l ombre des effets de texte de la forme ou de la zone de texte
type: docs
weight: 250
url: /fr/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Vous pouvez définir l'**Ombre** des **Effets de Texte** de n'importe quelle Forme ou Zone de Texte. Veuillez utiliser la propriété [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Elle présente le paramétrage du texte de la forme et renvoie [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objets. Après y avoir accédé, veuillez définir l'**Ombre** via la propriété [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). Cette propriété est de type [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) qui a plusieurs valeurs. Certaines de celles-ci sont

- DécalageDiagonaleInférieureDroite
- DécalageBas
- DécalageDiagonaleSupérieureDroite
- ÀL'intérieurGauche
- ÀL'IntérieurCentre
- DiagonalePerspectiveSupérieureGauche
- DiagonalePerspectiveInférieureDroite

{{% /alert %}}

Le fragment de code suivant illustre l'utilisation de la propriété [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) pour définir l'ombre des effets de texte de la Forme ou de la Zone de Texte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
