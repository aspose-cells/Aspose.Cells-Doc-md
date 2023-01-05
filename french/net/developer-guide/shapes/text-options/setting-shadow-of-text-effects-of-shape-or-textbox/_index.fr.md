---
title: Définition de l'ombre des effets de texte de Shape ou TextBox
type: docs
weight: 250
url: /fr/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Vous pouvez régler le**Ombre** de**Effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser le[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) la propriété. Il présente le réglage du texte de la forme et renvoie[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objets. Après y avoir accédé, veuillez définir le**Ombre** via[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) la propriété. Cette propriété est du type[**Type d'ombre prédéfini**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)qui a plusieurs valeurs. Certains d'entre eux sont

- DécalageDiagonalBasDroite
- DécalageBas
- DécalageDiagonaleHautDroite
- IntérieurGauche
- À l'intérieur du centre
- PerspectiveDiagonaleSupérieurGauche
- PerspectiveDiagonaleInférieureDroite

{{% /alert %}}

L'extrait de code suivant illustre l'utilisation de[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)propriété pour définir l'ombre des effets de texte de Shape ou TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
