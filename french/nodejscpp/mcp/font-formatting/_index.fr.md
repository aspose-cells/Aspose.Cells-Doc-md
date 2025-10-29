---
title: Formatage de police et de texte Excel
linktitle: Formatage de police et de texte
type: docs
weight: 30
url: /fr/nodejs-cpp/mcp/font-formatting
keywords: "Mise en forme de la police Excel, Mise en forme du texte Excel, Réglages de police Excel, Style de police AI Excel, Automatisation de la police Excel"
description: "Mise en forme de la police et du texte Excel  appliquer styles de police, couleurs, tailles et effets de texte avec l’automatisation AI"
---

# Mise en forme de la police et du texte Excel

Appliquez une **mise en forme professionnelle de la police Excel** avec une automatisation alimentée par AI. Mettez en style le **texte Excel** avec des polices, couleurs, tailles et effets spéciaux pour des feuilles de calcul soignées.

## Outils disponibles

- `font_settings` - **Personnalisation de la police Excel** (famille, taille, gras, italique, couleur, etc.) avec **précision AI Excel**
- `font_settings_batch` - Appliquer **paramètres de police Excel** à plusieurs plages en batch via **spreadsheet MCP**

## Opérations sur une seule police

### Style de police de base
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### Effets de texte
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### Caractères spéciaux
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## Opérations de police par lots

### Style complet de l’en-tête
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### Vitrine d’effets de texte spéciaux
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### Style pour rapports professionnels
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## Référence des paramètres de police

### Familles de police
- `"Arial"` - Sans-serif propre et moderne
- `"Calibri"` - Par défaut dans Microsoft Office
- `"Times New Roman"` - Sérif classique
- `"Arial Black"` - Police d'affichage en gras
- `"Courier New"` - Police monospaced

### Tailles de police
- `8` - texte très petit
- `10` - texte petit
- `11` - Taille par défaut
- `12` - Texte de corps standard
- `14` - Texte large
- `16` - Taille du titre
- `18` - Grand titre

### Couleurs de police (Codes Hexadécimaux)
- `"#000000"` - Noir
- `"#FFFFFF"` - Blanc
- `"#FF0000"` - Rouge
- `"#0066CC"` - Bleu
- `"#006600"` - Vert
- `"#FF6600"` - Orange
- `"#800080"` - Violet

### Effets de texte
- `bold: true` - Texte en gras
- `italic: true` - Texte en italique
- `underline: true` - Texte souligné
- `strikethrough: true` - Texte barré
- `subscript: true` - Texte en indice (H₂O)
- `superscript: true` - Texte en exposant (x²)

## Styles avancés de la police

### Exemple de notation scientifique
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### Données codées par couleur
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## Bonnes pratiques

1. **Cohérence** : Utilisez des familles de polices cohérentes dans tous les rapports
2. **Hiérarchie** : Utilisez les tailles de police pour créer une hiérarchie visuelle
3. **Lisibilité** : Assurez-vous d'un contraste adéquat entre le texte et l'arrière-plan
4. **Effets** : Utilisez modérément les effets de texte pour mettre en valeur
5. **Professionnel** : Respectez les polices standards pour les rapports

## Cas d'utilisation courants

### En-têtes de rapport
- Gras, taille de police plus grande
- Couleurs contrastées
- Familles de polices professionnelles

### Mise en valeur des données
- Gras ou italique pour les valeurs importantes
- Codage couleur pour les indicateurs d'état
- Barré pour les données obsolètes

### Documents scientifiques
- Indices pour les formules chimiques
- Exposant pour les expressions mathématiques
- Monospace pour le code ou les données

## Gestion des erreurs

### Police de caractères invalide
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**Résultat** : Reviens à la police système par défaut

### Code couleur invalide
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**Résultat** : Utilise la couleur noire par défaut 
{{< app/cells/assistant language="nodejs-cpp" >}}
