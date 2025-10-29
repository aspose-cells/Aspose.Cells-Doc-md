---
title: Mise en forme des cellules Excel
linktitle: Mise en forme des cellules
type: docs
weight: 40
url: /fr/nodejs-cpp/mcp/cell-formatting
keywords: "Mise en forme des cellules Excel, styles de cellules Excel, bordures Excel, alignement Excel, couleurs de fond Excel, mise en forme Excel par IA"
description: "Mise en forme des cellules Excel  appliquer fonds, bordures, alignement, formats numériques et styles de cellules avec automatisation par IA"
---

# Mise en forme des cellules Excel

Appliquez une **mise en forme professionnelle des cellules Excel** avec une automatisation alimentée par l'IA. Mettez en style **les cellules Excel** avec fonds, bordures, alignement, formats numériques et propriétés avancées des cellules.

## Outils disponibles

- `cell_format` - **Mise en forme des cellules Excel** (fond, bordures, alignement, format numérique) via **Excel MCP**
- `cell_format_batch` - Appliquez une **mise en forme des cellules Excel** à plusieurs plages en batch avec **automatisation IA**

## Mise en forme d'une seule cellule

### Style de base des cellules
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/formatted-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "background_color": "#4472C4",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "text_wrap": true
  }
}
```

### Mise en forme professionnelle des en-têtes
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "range": "A1:F1",
    "background_color": "#2E5984",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "border_color": "#000000",
    "text_wrap": true
  }
}
```

### Mise en forme des nombres
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/financial.xlsx",
    "sheet_name": "Budget",
    "range": "C2:C10",
    "number_format": "$#,##0.00",
    "horizontal_align": "right"
  }
}
```

## Mise en forme en batch des cellules

### Style de rapport complet
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A1:F1",
        "background_color": "#2E5984",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "border_style": "thick",
        "border_color": "#000000"
      },
      {
        "range": "B2:B4",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "C2:C4",
        "number_format": "0",
        "horizontal_align": "center"
      },
      {
        "range": "D2:F5",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "A5:F5",
        "border_style": "thick",
        "border_sides": ["top"]
      }
    ]
  }
}
```

### Styles avancés de bordure
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/border-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A5:A7",
        "border_style": "thin",
        "border_color": "#000000",
        "border_sides": ["all"]
      },
      {
        "range": "B5:B7",
        "border_style": "medium",
        "border_color": "#FF0000",
        "border_sides": ["outline"]
      },
      {
        "range": "C5:C7",
        "border_style": "dashed",
        "border_color": "#0000FF",
        "border_sides": ["top", "bottom"]
      },
      {
        "range": "D5:D7",
        "border_style": "dotted",
        "border_color": "#00FF00",
        "border_sides": ["left", "right"]
      },
      {
        "range": "E5:E7",
        "border_style": "double",
        "border_color": "#FF00FF",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Présentation de l'alignement du texte
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/alignment-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A10",
        "horizontal_align": "left",
        "vertical_align": "top",
        "background_color": "#FFE6E6"
      },
      {
        "range": "B10",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "background_color": "#E6FFE6"
      },
      {
        "range": "C10",
        "horizontal_align": "right",
        "vertical_align": "bottom",
        "background_color": "#E6E6FF"
      },
      {
        "range": "D10",
        "horizontal_align": "justify",
        "vertical_align": "justify",
        "text_wrap": true,
        "background_color": "#FFFFE6"
      },
      {
        "range": "E10",
        "horizontal_align": "fill",
        "indent": 2,
        "background_color": "#FFE6FF"
      }
    ]
  }
}
```

### Effets de rotation du texte
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/rotation-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D1",
        "text_rotation": 45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "E1",
        "text_rotation": -45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "F1",
        "text_rotation": 90,
        "horizontal_align": "center",
        "vertical_align": "middle"
      }
    ]
  }
}
```

## Référence des paramètres de mise en forme

### Couleurs d'arrière-plan
- `"#FFFFFF"` - Blanc
- `"#4472C4"` - Bleu professionnel
- `"#E6F3FF"` - Bleu clair
- `"#FFFF00"` - Jaune
- `"#FFE6E6"` - Rouge clair
- `"#E6FFE6"` - Vert clair
- `"#F0F8FF"` - Bleu Alice

### Alignement horizontal
- `"left"` - Aligné à gauche
- `"center"` - Centré
- `"right"` - Aligné à droite
- `"justify"` - Justifié
- `"fill"` - Remplir la cellule

### Alignement vertical
- `"top"` - Aligné en haut
- `"middle"` - Aligné au centre
- `"bottom"` - Aligné en bas
- `"justify"` - Justifié verticalement

### Styles de Bordure
- `"none"` - Pas de bordure
- `"thin"` - Ligne fine
- `"medium"` - Ligne moyenne
- `"thick"` - Ligne épaisse
- `"dashed"` - Ligne pointillée
- `"dotted"` - Ligne ponctuée
- `"double"` - Ligne double

### Côtés de la Bordure
- `["all"]` - Tous les côtés
- `["top", "bottom"]` - Haut et bas
- `["left", "right"]` - Gauche et droite
- `["outline"]` - Bords extérieurs uniquement
- `["inside"]` - Bords intérieurs uniquement

### Formats de Nombre
- `"General"` - Format par défaut
- `"0"` - Entier
- `"0.00"` - Deux décimales
- `"0%"` - Pourcentage
- `"$#,##0.00"` - Monnaie avec séparateur de milliers
- `"yyyy-mm-dd"` - Format de date
- `"h:mm AM/PM"` - Format de l'heure

### Propriétés du texte
- `text_wrap: true` - Retour à la ligne dans la cellule
- `text_rotation: 45` - Rotation du texte (degrés)
- `indent: 2` - Niveau d'indentation du texte
- `locked: true` - Verrouiller la cellule pour la protection
- `hidden: true` - Cacher la formule de la cellule

## Exemples de mise en forme avancée

### Mise en forme des rapports financiers
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-complete.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D2:D5",
        "background_color": "#F0F8FF"
      },
      {
        "range": "E2:E5",
        "background_color": "#FFF0F0"
      },
      {
        "range": "F2:F5",
        "background_color": "#F0FFF0",
        "border_style": "double",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Mise en évidence de la validation des données
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/data-validation.xlsx",
    "sheet_name": "Data",
    "format_ranges": [
      {
        "range": "A2:A10",
        "background_color": "#90EE90"
      },
      {
        "range": "B2:B10",
        "background_color": "#FFB6C1"
      },
      {
        "range": "C2:C10",
        "background_color": "#87CEEB",
        "border_style": "thin",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Paramètres de protection
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/protected.xlsx",
    "sheet_name": "Sheet1",
    "range": "B1:B5",
    "locked": false,
    "hidden": true
  }
}
```

## Bonnes pratiques

1. **Harmonie des couleurs** : Utilisez des couleurs complémentaires pour une apparence professionnelle
2. **Contraste** : Assurez-vous que le texte est lisible sur les couleurs de fond
3. **Cohérence** : Appliquez une mise en forme cohérente pour des données similaires
4. **Borders** : Utilisez des bordures pour séparer les sections et mettre en valeur les données importantes
5. **Formats numériques** : Appliquez des formats numériques appropriés selon le type de données

## Cas d'utilisation courants

### En-têtes de rapport
- Fond sombre avec texte blanc
- Alignement au centre
- Bordures épaisses
- Retour à la ligne activé

### Données financières
- Mise en forme monétaire
- Alignement à droite pour les chiffres
- Mise en évidence des valeurs négatives
- Séparateurs de milliers

### Indicateurs de statut
- Arrière-plans codés par couleur
- Alignement au centre
- Bordures en gras
- Distinction visuelle claire

### Tableaux de données
- Couleurs de lignes alternées
- Largeurs de colonnes cohérentes
- Formats de nombre appropriés
- Style clair pour l'en-tête

## Gestion des erreurs

### Code couleur invalide
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "background_color": "invalid-color"
  }
}
```
**Résultat** : Utilise la couleur de fond par défaut

### Format de nombre invalide
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "number_format": "invalid-format"
  }
}
```
**Résultat** : Utilise le format général en tant que fallback 
{{< app/cells/assistant language="nodejs-cpp" >}}
