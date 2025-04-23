---
title: Définir l ombre des effets de texte de la forme ou de la zone de texte
type: docs
weight: 250
url: /fr/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Vous pouvez définir l'**Ombre** des **Effets de Texte** de n'importe quelle Forme ou Zone de Texte. Veuillez utiliser la propriété [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Elle présente le paramétrage du texte de la forme et renvoie [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objets. Après y avoir accédé, veuillez définir l'**Ombre** via la propriété [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). Cette propriété est de type [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) qui a plusieurs valeurs. Certaines de celles-ci sont

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INTÉRIEUR_GAUCHE
- CENTRE_INTERNE
- PERSPECTIVE_DIAGONAL_SUPÉRIEUR_GAUCHE
- PERSPECTIVE_DIAGONAL_SUPÉRIEUR_DROIT

{{% /alert %}}

Le fragment de code suivant illustre l'utilisation de la propriété [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) pour définir l'ombre des effets de texte de la Forme ou de la Zone de Texte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
