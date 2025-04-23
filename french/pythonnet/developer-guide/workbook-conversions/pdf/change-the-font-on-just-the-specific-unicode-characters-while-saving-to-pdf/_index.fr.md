---
title: Modifier la police sur des caractères Unicode spécifiques lors de l’enregistrement en PDF avec Python.NET
linktitle: Modifier la police sur certains caractères Unicode
type: docs
weight: 260
url: /fr/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Apprenez comment modifier les polices pour des caractères Unicode spécifiques lors de la conversion PDF avec Aspose.Cells for Python via .NET. Assurez un rendu précis du texte avec la substitution de police au niveau du caractère.
---

{{% alert color="primary" %}}

Certains caractères Unicode ne peuvent pas être affichés par les polices spécifiées par l'utilisateur. Un tel caractère Unicode est le **tiret non sécable** (U+2011) avec le numéro Unicode 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais peut l'être avec des polices comme **Arial Unicode MS**.

Lorsque de tels caractères apparaissent dans un texte formaté avec une police spécifique (par exemple, Times New Roman), Aspose.Cells change par défaut la police du mot/de la phrase entière vers une police compatible (par exemple, Arial Unicode MS). Pour les utilisateurs qui veulent uniquement changer la police du caractère non affichable, nous offrons un contrôle granulaire via la propriété **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **Exemple de comparaison**

Les captures d'écran ci-dessous illustrent les résultats avec des réglages différents. Le premier PDF montre une substitution totale de police, tandis que le second modifie uniquement la police du caractère spécifique.

|**Substitution Complète de Texte**|**Substitution au Niveau du Caractère**|
| :- | :- |
|![Changement Complet de Police](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Changement Sélectif de Police](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Étapes de Mise en Œuvre**

Pour activer la substitution de police au niveau du caractère :

1. Créer un objet [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Accéder aux cellules de la feuille de calcul via la propriété [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)
3. Définir les valeurs des cellules contenant des caractères Unicode spéciaux
4. Configurer [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) avec :
   - `is_font_substitution_char_granularity = True`
5. Enregistrer le classeur au format PDF

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **Configuration Clé**

Utilisez ces composants API essentiels :

- La classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) pour les paramètres de rendu PDF
- La propriété **is_font_substitution_char_granularity** pour la substitution de police au niveau du caractère
- La méthode [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) pour la génération de sortie

{{% alert color="note" %}} 
**Note de Différence de l'API** : Dans Python.NET, les propriétés booléennes utilisent la notation snake_case (`is_font_substitution_char_granularity`) au lieu de PascalCase utilisée dans .NET.
{{% /alert %}}
