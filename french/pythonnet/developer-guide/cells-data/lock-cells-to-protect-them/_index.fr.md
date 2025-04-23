---
title: Verrouiller les cellules pour les protéger avec Python.NET
linktitle: Verrouiller les cellules pour les protéger
type: docs
weight: 130
url: /fr/python-net/how-to-lock-cells-to-protect-them/
description: Apprenez à verrouiller des cellules spécifiques et à protéger des feuilles de calcul dans des fichiers Excel en utilisant Aspose.Cells pour Python via .NET.
keywords: Verrouillage de cellules en Python, protection de feuilles de calcul, protection des cellules dans Excel avec Python, tutoriel Aspose.Cells en Python
---

## **Scénarios d'utilisation possibles**
Verrouiller les cellules pour les protéger est une pratique courante dans les applications de feuille de calcul, telles que Microsoft Excel ou Google Sheets, pour plusieurs raisons importantes :

1. Prévenir les modifications accidentelles : Verrouiller les cellules peut empêcher les utilisateurs de modifier accidentellement des données ou des formules importantes.
2. Maintenir l'intégrité des données : assurer que les données critiques restent cohérentes et précises.
3. Accès contrôlé : gérer les permissions d'édition dans des environnements collaboratifs.
4. Protéger les formules : sauvegarder les calculs cruciaux contre toute modification.
5. Appliquer des règles métier : respecter les exigences de protection des données.
6. Guider les utilisateurs : fournir des zones éditables claires dans des feuilles de calcul complexes.

## **Comment verrouiller les cellules pour les protéger dans Excel**
Voici comment verrouiller des cellules dans Microsoft Excel :

1. Sélectionnez les cellules à verrouiller : choisissez des cellules ou passez cette étape pour verrouiller la feuille entière.
1. Ouvrir la boîte de dialogue "Format de cellule" : clic droit > "Format de cellule" ou Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Verrouiller les cellules : allez dans l'onglet "Protection" > cocher "Verrouillé" > cliquer sur "OK".
1. Protéger la feuille : onglet "Révision" > "Protéger la feuille" > définir un mot de passe/des permissions > cliquer sur "OK".
<br>
<img src="2.png" width=60% />

## **Comment verrouiller des cellules pour les protéger en utilisant Python**

Aspose.Cells pour Python via .NET permet la protection des cellules de manière programmatique. Suivez ces étapes :
1. Charger le [fichier d'exemple](sample.xlsx)
2. Déverrouiller toutes les cellules (l'état verrouillé par défaut n'est pas appliqué jusqu'à la protection)
3. Verrouiller des cellules spécifiques
4. Protéger la feuille pour appliquer le verrouillage

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **Résultat de sortie**
Cette implémentation verrouille les cellules spécifiées (A1 et B2) tout en laissant les autres modifiables. La protection de la feuille de calcul impose ces paramètres.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
